---
author: 111qqz
date: 2018-11-06 13:33:00+00:00
draft: false
title: How to use Scrapy with Django Application（转自medium）
type: post
url: /2018/11/how-to-use-scrapy-with-django-application/
categories:
- 其他
tags:
- react
- 爬虫
---

在meidum上看到一篇很赞的文章...无奈关键部分一律无法加载出来...挂了梯子也不行，很心塞...刚刚突然发现加载出来了...以防之后再次无法访问，所以搬运过来．

There are couple of articles on how to integrate Scrapy into a Django Application (or vice versa?). But most of them don’t cover a full complete example that includes triggering spiders from Django views. Since this is a web application, that must be our main goal.


### What do we need ?




Before we start, it is better to specify what we want and how we want it. Check this diagram:


![](https://cdn-images-1.medium.com/max/1000/1*ZzTm-J_UgiuSoQtRmUoE9g.png)


It shows how our app should work



 	  * Client sends a request with a URL to crawl it. (1)
 	  * Django triggets scrapy to run  a spider to crawl that URL. (2)
 	  * Django returns a response to tell Client that crawling just started. (3)
 	  * scrapy  completes crawling and saves extracted data into database. (4)
 	  * django fetches that data from database and return it to Client. (5)

Looks great and simple so far.


### A note on that 5th statement


**`Django`** fetches that data from database and return it to **`Client`**. (5)

`Neither Django nor client` don’t know when `Scrapy` completes crawling. There is a callback method named `pipeline_closed,` but it belongs to Scrapy project. We can’t return a response from Scrapy `pipelines`. We use that method only to save extracted data into database.




Well eventually, in somewhere, we have to tell the client :





<blockquote>Hey! Crawling completed and i am sending you crawled data here.</blockquote>




There are two possible ways of this (_Please comment if you discover more_):




We can either use `web sockets` to inform client when crawling completed.




Or,




We can start sending requests on every 2 seconds (more? or less ?) from client to check crawling status after we get the `"crawling started"` response.




Web Socket solution sounds more stable and robust. But it requires a second service running separately and means more configuration. I will skip this option for now. But i would choose web sockets for my production-level applications.





### Let’s write some code




It’s time to do some real job. Let’s start by preparing our environment.





#### Installing Dependencies




Create a virtual environment and activate it:




    
    $ python3.5 -m venv venv
    $ source venv/bin/activate
    $ pip install django scrapy scrapyd python-scrapyd-api




[Scrapyd](https://github.com/scrapy/scrapyd) is a daemon service for running [Scrapy](https://github.com/scrapy/scrapy) spiders. You can discover its details from [here](http://scrapyd.readthedocs.io/en/stable/).




[python-scrapyd-api](https://github.com/djm/python-scrapyd-api) is a wrapper allows us to talk `scrapyd` from our Python progam.


**Note: I am going to use Python 3.5 for this project**


#### Creating Django Project


Create a django project with an app named `main` :

    
    $ django-admin startproject iCrawler
    $ cd iCrawler && python manage.py startapp main


We also need a model to save our scraped data. Let’s keep it simple:

    
    import json
    from django.db import models
    from django.utils import timezone
    
    class ScrapyItem(models.Model):
        unique_id = models.CharField(max_length=100, null=True)
        data = models.TextField() # this stands for our crawled data
        date = models.DateTimeField(default=timezone.now)
        
        # This is for basic and custom serialisation to return it to client as a JSON.
        @property
        def to_dict(self):
            data = {
                'data': json.loads(self.data),
                'date': self.date
            }
            return data
    
        def __str__(self):
            return self.unique_id


Add `main` app into `INSTALLED_APPS` in `settings.py` And as a final step, migrations:

    
    $ python manage.py makemigrations
    $ python manage.py migrate


Let’s add a view and url to our `main` app:

    
    from uuid import uuid4
    from urllib.parse import urlparse
    from django.core.validators import URLValidator
    from django.core.exceptions import ValidationError
    from django.views.decorators.http import require_POST, require_http_methods
    from django.shortcuts import render
    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from scrapyd_api import ScrapydAPI
    from main.utils import URLUtil
    from main.models import ScrapyItem
    
    # connect scrapyd service
    scrapyd = ScrapydAPI('http://localhost:6800')
    
    
    def is_valid_url(url):
        validate = URLValidator()
        try:
            validate(url) # check if url format is valid
        except ValidationError:
            return False
    
        return True
    
    
    @csrf_exempt
    @require_http_methods(['POST', 'GET']) # only get and post
    def crawl(request):
        # Post requests are for new crawling tasks
        if request.method == 'POST':
    
            url = request.POST.get('url', None) # take url comes from client. (From an input may be?)
    
            if not url:
                return JsonResponse({'error': 'Missing  args'})
            
            if not is_valid_url(url):
                return JsonResponse({'error': 'URL is invalid'})
            
            domain = urlparse(url).netloc # parse the url and extract the domain
            unique_id = str(uuid4()) # create a unique ID. 
            
            # This is the custom settings for scrapy spider. 
            # We can send anything we want to use it inside spiders and pipelines. 
            # I mean, anything
            settings = {
                'unique_id': unique_id, # unique ID for each record for DB
                'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
            }
    
            # Here we schedule a new crawling task from scrapyd. 
            # Notice that settings is a special argument name. 
            # But we can pass other arguments, though.
            # This returns a ID which belongs and will be belong to this task
            # We are goint to use that to check task's status.
            task = scrapyd.schedule('default', 'icrawler', 
                settings=settings, url=url, domain=domain)
    
            return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started' })
    
        # Get requests are for getting result of a specific crawling task
        elif request.method == 'GET':
            # We were passed these from past request above. Remember ?
            # They were trying to survive in client side.
            # Now they are here again, thankfully. <3
            # We passed them back to here to check the status of crawling
            # And if crawling is completed, we respond back with a crawled data.
            task_id = request.GET.get('task_id', None)
            unique_id = request.GET.get('unique_id', None)
    
            if not task_id or not unique_id:
                return JsonResponse({'error': 'Missing args'})
    
            # Here we check status of crawling that just started a few seconds ago.
            # If it is finished, we can query from database and get results
            # If it is not finished we can return active status
            # Possible results are -> pending, running, finished
            status = scrapyd.job_status('default', task_id)
            if status == 'finished':
                try:
                    # this is the unique_id that we created even before crawling started.
                    item = ScrapyItem.objects.get(unique_id=unique_id) 
                    return JsonResponse({'data': item.to_dict['data']})
                except Exception as e:
                    return JsonResponse({'error': str(e)})
            else:
                return JsonResponse({'status': status})


I tried to document the code as much as i can.

But the main trick is, `unique_id.` Normally, we save an object to database, then we get its `ID`. In our case, we are specifying its `unique_id` before creating it. Once crawling completed and client asks for the crawled data; we can create a query with that `unique_id` and fetch results.

And an url for this view:

    
    from django.conf import settings
    from django.conf.urls import url,static
    from django.views.generic import TemplateView
    from main import views
    
    urlpatterns = [
        url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
        url(r'^api/crawl/', views.crawl, name='crawl'),
    ]
    
    # This is required for static files while in development mode. (DEBUG=TRUE)
    # No, not relevant to scrapy or crawling :)
    if settings.DEBUG:
        urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#### Creating Scrapy Project\


It is better if we create Scrapy project under (or next to) our Django project. This makes easier to connect them together. So let’s create it under Django project folder:

    
    $ cd iCrawler
    $ scrapy startproject scrapy_app


Now we need to create our first spider from inside `scrapy_app` folder:

    
    $ cd scrapy_app
    $ scrapy genspider -t crawl icrawler https://google.com


i name spider as `icrawler`. You can name it as anything. Look `-t crawl` part. We specify a base template for our spider. You can see all available templates with:

    
    $ scrapy genspider -l
    Available templates:
    basic
    crawl
    csvfeed
    xmlfeed


Now we should have a folder structure like this:

![](https://cdn-images-1.medium.com/max/1000/1*CYNVpLHx8H6gMSkXkD91BQ.png)



#### Connecting Scrapy to Django




In order to have access Django models from Scrapy, we need to connect them together. Go to `settings.py` file under `scrapy_app/scrapy_app/` and put:




    
    import os
    import sys
    
    # DJANGO INTEGRATION
    
    sys.path.append(os.path.dirname(os.path.abspath('.')))
    # Do not forget the change iCrawler part based on your project name
    os.environ['DJANGO_SETTINGS_MODULE'] = 'iCrawler.settings'
    
    # This is required only if Django Version > 1.8
    import django
    django.setup()
    
    # DJANGO INTEGRATION
    
    ## Rest of settings are below ..


That’s it. Now let’s start `scrapyd` to make sure everything installed and configured properly. Inside `scrapy_app/` folder run:

$ scrapyd

This will start scrapyd and generate some outputs. Scrapyd also has a very minimal and simple web console. We don’t need it on production but we can use it to watch active jobs while developing. Once you start the scrapyd go to [http://127.0.0.1:6800](http://127.0.0.1:6800/) and see if it is working.


#### Configuring Our Scrapy Project




Since this post is not about fundamentals of scrapy, i will skip the part about modifying spiders. You can create your spider with official documentation. I will put my example spider here, though:




    
    class IcrawlerSpider(CrawlSpider):
        name = 'icrawler'
    
        def __init__(self, *args, **kwargs):
            # We are going to pass these args from our django view.
            # To make everything dynamic, we need to override them inside __init__ method
            self.url = kwargs.get('url')
            self.domain = kwargs.get('domain')
            self.start_urls = [self.url]
            self.allowed_domains = [self.domain]
    
            IcrawlerSpider.rules = [
               Rule(LinkExtractor(unique=True), callback='parse_item'),
            ]
            super(IcrawlerSpider, self).__init__(*args, **kwargs)
    
        def parse_item(self, response):
            # You can tweak each crawled page here
            # Don't forget to return an object.
            i = {}
            i['url'] = response.url
            return i


Above is `icrawler.py` file from `scrapy_app/scrapy_app/spiders`. Attention to `__init__` method. It is important. If we want to make a method or property dynamic, we need to define it under `__init__` method, so we can pass arguments from Django and use them here.

We also need to create a `Item Pipeline` for our scrapy project. Pipeline is a class for making actions over scraped items. From [documentation](https://doc.scrapy.org/en/latest/topics/item-pipeline.html):


<blockquote>Typical uses of item pipelines are:</blockquote>





 	  * cleansing HTML data
 	  * validating scraped data (checking that the items contain certain fields)
 	  * checking for duplicates (and dropping them)
 	  * **storing the scraped item in a database**

Yay! `Storing the scraped item in a database`. Now let’s create one. Actually there is already a file named `pipelines.py` inside `scrapy_project` folder. And also that file contains an empty-but-ready pipeline. We just need to modify it a little bit:

    
    from main.models import ScrapyItem
    import json
    
    class ScrapyAppPipeline(object):
        def __init__(self, unique_id, *args, **kwargs):
            self.unique_id = unique_id
            self.items = []
    
        @classmethod
        def from_crawler(cls, crawler):
            return cls(
                unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
            )
    
        def close_spider(self, spider):
            # And here we are saving our crawled data with django models.
            item = ScrapyItem()
            item.unique_id = self.unique_id
            item.data = json.dumps(self.items)
            item.save()
    
        def process_item(self, item, spider):
            self.items.append(item['url'])
            return item




And as a final step, we need to enable (uncomment) this pipeline in scrapy `settings.py` file:




    
    # Configure item pipelines
    # See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
    ITEM_PIPELINES = {
        'scrapy_app.pipelines.ScrapyAppPipeline': 300,
    }




<blockquote>Don’t forget to restart `scraypd` if it is working.</blockquote>




This scrapy project basically,






 	  * Crawls a website (comes from Django view)
 	  * Extract all URLs from website
 	  * Put them into a list
 	  * Save the list to database over Django models.



And that’s all for the back-end part. Django and Scrapy are both integrated and should be working fine.





### Notes on Front-End Part




Well, this part is so subjective. We have tons of options. Personally I have build my front-end with `React` . The only part that is not subjective is `usage of setInterval` . Yes, let’s remember our options: `web sockets` and `to send requests to server every X seconds`.




To clarify base logic, this is simplified version of my React Component:








    
    class Home extends React.Component {
      constructor(props) {
          super(props)
          this.state = {
              url: '',
              crawlingStatus: null,
              data: null,
              taskID: null,
              uniqueID: null
          }
          this.statusInterval = 1
      }
    
      handleStartButton = (event) => {
        if (!this.state.url) return false;
    
        // send a post request to client when form button clicked
        // django response back with task_id and unique_id.
        // We have created them in views.py file, remember?
        $.post('/api/crawl/', { url: this.state.url }, resp => {
            if (resp.error) {
                alert(resp.error)
                return
            }
            // Update the state with new task and unique id
            this.setState({
                taskID: resp.task_id,
                uniqueID: resp.unique_id,
                crawlingStatus: resp.status
            }, () => {
                // ####################### HERE ########################
                // After updating state, 
                // i start to execute checkCrawlStatus method for every 2 seconds
                // Check method's body for more details
                // ####################### HERE ########################
                this.statusInterval = setInterval(this.checkCrawlStatus, 2000)
            });
        });
      }
    
      componentWillUnmount() {
          // i create this.statusInterval inside constructor method
          // So clear it anyway on page reloads or 
          clearInterval(this.statusInterval)
      }
    
      checkCrawlStatus = () => {
          // this method do only one thing.
          // Making a request to server to ask status of crawling job
          $.get('/api/crawl/',
                { task_id: this.state.taskID, unique_id: this.state.uniqueID }, resp => {
              if (resp.data) {
                  // If response contains a data array
                  // That means crawling completed and we have results here
                  // No need to make more requests.
                  // Just clear interval
                  clearInterval(this.statusInterval)
                  this.setState({
                      data: resp.data
                  })
              } else if (resp.error) {
                  // If there is an error
                  // also no need to keep requesting
                  // just show it to user
                  // and clear interval
                  clearInterval(this.statusInterval)
                  alert(resp.error)
              } else if (resp.status) {
                  // but response contains a `status` key and no data or error
                  // that means crawling process is still active and running (or pending)
                  // don't clear the interval.
                  this.setState({
                      crawlingStatus: resp.status
                  });
              }
          })
      }
      
      render () {
        // render componenet
        return (<div></div>)
      }
    }










You can discover the details by comments i added. It is quite simple actually.




Oh, that’s it. It took longer than i expected. Please leave a comment for any kind of feedback.









