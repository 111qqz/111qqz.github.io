---
author: 111qqz
date: 2018-05-14 13:08:30+00:00
title: wordpress 开启全站https
type: post
url: /2018/05/enable-https-for-wordpress/
categories:
- 其他
tags:
- wordpress
- blog
---

**20190511更新:**

证书到期了,写一下更换证书的流程.

重新申请好证书之后,直接把Apache里面对应的123放到/data/cert文件夹.

其中1对应server-ca.crt,2对应server.crt,3对应server.key



由于从套路云转移到良心云，迫于国内某些蛋疼的政策，以及一些其他原因，决定全站上https.

首先是申请SSL证书，这个良心云就可以申请，也有其他地方。

这里要注意的是，有些证书是只能对应一个域名，腾讯云貌似就是这样，不过好像www.111qqz.com的证书也可以用于111qqz.com

得到证书中有Apache,Nginx,Tomcat和IIS四个文件夹，由于我们使用的是Apache，所以其他三个不用管。



 	  1. 将证书上传到服务器证书目录：/data/cert（没有cert目录可以自己新建）
 	  2. 在/etc/httpd/conf.d目录下新建一个https配置文件，假设命名为mydomain-ssl.conf。
 	  3. 拷贝下面的https配置文件模板到mydomain-ssl.conf文件中，并保存

    
    <VirtualHost *:443>
    ServerName www.111qqz.com
    ServerAlias 111qqz.com
    DocumentRoot "/data/wwwroot/default/wordpress"
    #ErrorLog "logs/www.mydomain.com-error_log"
    #CustomLog "logs/www.mydomain.com-access_log" common
    <Directory "/data/wwwroot/default/wordpress">
    Options Indexes FollowSymlinks
    AllowOverride All
    Require all granted
    </Directory>
    SSLEngine on
    SSLCertificateFile  /data/cert/server.crt
    SSLCertificateKeyFile  /data/cert/server.key
    SSLCertificateChainFile  /data/cert/server-ca.crt
    </VirtualHost>


需要注意的是，servername那里要写带www的域名，不带www的写在serveralias
 	  4. 修改配置文件中相关项，并保存
ServerName  #主域名，务必修改
ServerAlias   #副域名，可选项
DocumentRoot #网站路径，务必填写网站实际路径，例如:/data/wwwroot/default/wordpress
Directory #同上
SSLCertificateFile #证书，务必填写网站实际路径
SSLCertificateKeyFile #证书私钥，务必填写网站实际路径
SSLCertificateChainFile #证书链（CA文件），务必填写网站实际路径



然后由于我是迁移了服务器，很大可能是主页可以访问，但任何一个其他页面都会因报错500 internal error 之类，查看日志，位置在/var/log/httpd 里面，发现报错AH00124: Request exceeded the limit of 10 internal redirects due to probable configuration error. Use 'LimitInternalRecursion' to increase the limit if necessary. Use 'LogLevel debug' to get a backtrace., referer: [https://111qqz.com/](https://qq.111qqz.com/)


查了很多，最后发现问题是在wordpress的根目录下的.htaccess文件中




将Rewritebase的  /wordpress 改成/




将RewriteRule的 .  /wordpress/index.php  改成  .  /index.php




最后.htaccess文件如下：






    
    RewriteEngine On
    RewriteCond %{HTTPS} !=on
    RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R=301,L]
    
    # BEGIN WordPress
    <IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /wordpress/
    RewriteRule ^index\.php$ - [L]
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule . /index.php [L]
    </IfModule>
    
    # END WordPress
    







这个时候发现，虽然一般页面也是可以访问了，但是后台登录不进去，提示重定向次数过多。

查了下发现基本都在说由于原始链接是http://的问题，并给了几种解决方案。

我是用phpadmin直接改的，大概是wp_option里面有两项要修改。

然而修改之后仍然不可以。尝试了好多内容都不行。大概包括排查插件，修改权限之类

最后发现，http到https在数据库里修改是不行的，必须要在wp-config.php中修改才可以。主要是手动添加wp_home和wp_siteurl

修改后的wp-config.php如下:

    
    <?php
    /**
     * The base configuration for WordPress
     *
     * The wp-config.php creation script uses this file during the
     * installation. You don't have to use the web site, you can
     * copy this file to "wp-config.php" and fill in the values.
     *
     * This file contains the following configurations:
     *
     * * MySQL settings
     * * Secret keys
     * * Database table prefix
     * * ABSPATH
     *
     * @link https://codex.wordpress.org/Editing_wp-config.php
     *
     * @package WordPress
     */
    
    // ** MySQL settings - You can get this info from your web host ** //
    /** The name of the database for WordPress */
    define('DB_NAME', 'wordpress');
    
    /** MySQL database username */
    define('DB_USER', 'wordpress');
    
    /** MySQL database password */
    define('DB_PASSWORD', '-2254965');
    
    /** MySQL hostname */
    define('DB_HOST', 'localhost');
    
    /** Database Charset to use in creating database tables. */
    define('DB_CHARSET', 'utf8');
    
    /** The Database Collate type. Don't change this if in doubt. */
    define('DB_COLLATE', '');
    
    /**#@+
     * Authentication Unique Keys and Salts.
     *
     * Change these to different unique phrases!
     * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
     * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
     *
     * @since 2.6.0
     */
    define('AUTH_KEY',         'put your unique phrase here');
    define('SECURE_AUTH_KEY',  'put your unique phrase here');
    define('LOGGED_IN_KEY',    'put your unique phrase here');
    define('NONCE_KEY',        'put your unique phrase here');
    define('AUTH_SALT',        'put your unique phrase here');
    define('SECURE_AUTH_SALT', 'put your unique phrase here');
    define('LOGGED_IN_SALT',   'put your unique phrase here');
    define('NONCE_SALT',       'put your unique phrase here');
    
    /**#@-*/
    
    /**
     * WordPress Database Table prefix.
     *
     * You can have multiple installations in one database if you give each
     * a unique prefix. Only numbers, letters, and underscores please!
     */
    $table_prefix  = 'wp_';
    
    /**
     * For developers: WordPress debugging mode.
     *
     * Change this to true to enable the display of notices during development.
     * It is strongly recommended that plugin and theme developers use WP_DEBUG
     * in their development environments.
     *
     * For information on other constants that can be used for debugging,
     * visit the Codex.
     *
     * @link https://codex.wordpress.org/Debugging_in_WordPress
     */
    define('WP_DEBUG', false);
    
    define('WP_HOME','https://111qqz.com');
    define('WP_SITEURL','https://111qqz.com');
    
    define('FORCE_SSL_ADMIN',true);
    // in some setups HTTP_X_FORWARDED_PROTO might contain
    // // a comma-separated list e.g. http,https
    // // so check for https existence
     if (strpos($_SERVER['HTTP_X_FORWARDED_PROTO'], 'https') !== false)
     $_SERVER['HTTPS']='on';
    
    /* That's all, stop editing! Happy blogging. */
    
    /** Absolute path to the WordPress directory. */
    if ( !defined('ABSPATH') )
            define('ABSPATH', dirname(__FILE__) . '/');
    
    /** Sets up WordPress vars and included files. */
    require_once(ABSPATH . 'wp-settings.php');
    




至此，博客终于可以访问了...感动

然后用了个叫really simple ssl的插件，据说很好用。。。




