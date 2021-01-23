---
author: 111qqz
date: 2018-10-19 08:18:53+00:00
draft: false
title: 爬虫学习笔记
type: post
url: /2018/10/web-crawler-notes/
categories:
- 其他
tags:
- python
- 爬虫
---

再次迫于生计。。。



参考了[面向新人的 Python 爬虫学习资料](https://www.v2ex.com/t/370455#reply9)

大致的学习路线为:


<blockquote>一： 简单的定向脚本爬虫（ request --- bs4 --- re ）

二： 大型框架式爬虫（ Scrapy 框架为主）

三：浏览器模拟爬虫 （ Mechanize 模拟 和 Selenium 模拟）</blockquote>


有Python基础和一点html基础的话。。。貌似上手是0难度的

年轻人的第一个爬虫(虽然代码是直接copy的...

    
    '''
    抓取百度贴吧---生活大爆炸吧的基本内容
    爬虫线路： requests - bs4
    Python版本： 3.6
    OS： mac os 12.12.4
    '''
    
    import requests
    import time
    from bs4 import BeautifulSoup
    
    # 首先我们写好抓取网页的函数
    
    
    def get_html(url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
            # r.endcodding = r.apparent_endconding
            r.encoding = 'utf-8'
            return r.text
        except:
            return " ERROR "
    
    
    def get_content(url):
        '''
        分析贴吧的网页文件，整理信息，保存在列表变量中
        '''
    
        # 初始化一个列表来保存所有的帖子信息：
        comments = []
        # 首先，我们把需要爬取信息的网页下载到本地
        html = get_html(url)
    
        # 我们来做一锅汤
        soup = BeautifulSoup(html, 'lxml')
    
        # 按照之前的分析，我们找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
        liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
    
        # 通过循环找到每个帖子里的我们需要的信息：
        for li in liTags:
            # 初始化一个字典来存储文章信息
            comment = {}
            # 这里使用一个try except 防止爬虫找不到信息从而停止运行
            try:
                # 开始筛选信息，并保存到字典中
                comment['title'] = li.find(
                    'a', attrs={'class': 'j_th_tit '}).text.strip()
                comment['link'] = "http://tieba.baidu.com/" + \
                    li.find('a', attrs={'class': 'j_th_tit '})['href']
                comment['name'] = li.find(
                    'span', attrs={'class': 'tb_icon_author '}).text.strip()
                comment['time'] = li.find(
                    'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
                comment['replyNum'] = li.find(
                    'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
                comments.append(comment)
            except:
                print('出了点小问题')
    
        return comments
    
    
    def Out2File(dict):
        '''
        将爬取到的文件写入到本地
        保存到当前目录的 TTBT.txt文件中。
    
        '''
        with open('TBBT.txt', 'a+') as f:
            for comment in dict:
                f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                    comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))
    
            print('当前页面爬取完成')
    
    
    def main(base_url, deep):
        url_list = []
        # 将所有需要爬去的url存入列表
        for i in range(0, deep):
            url_list.append(base_url + '&pn=' + str(50 * i))
        print('所有的网页已经下载到本地！ 开始筛选信息。。。。')
    
        #循环写入所有的数据
        for url in url_list:
            content = get_content(url)
            Out2File(content)
        print('所有的信息都已经保存完毕！')
    
    
    base_url = 'http://tieba.baidu.com/f?kw=&ie=utf-8'
    # 设置需要爬取的页码数量
    deep = 100
    
    if __name__ == '__main__':
        main(base_url, deep)




年轻人的第二个爬虫:https://github.com/111qqz/spider-demo，爬了我家一周的天气情况

爬虫能够work我觉得主要取决于两个因素

一个是，一个网站的网页源码，其实是在我们本地存储的

另一个是，网页的代码是有规律的...

所以初级的爬虫的难度就仅仅在于找规律。。。然后配合chrome 开发者工具的模拟点击功能和　xpath这种文本解析工具...　就可以搞定了。。。

关于反爬虫的处理办法，以及如何提高爬虫的速度，可能才是“爬虫工程师”的核心技能？

参考资料:

[BeautifulSoup官方文档，一个将html数据结构化的python库](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[Scrapy官方文档，一个爬虫框架](https://docs.scrapy.org/en/latest/intro/overview.html)












