# Move your Piwigo to another server

You want to move your Piwigo to a new web hoster,  move from piwigo.com to your own environment or move your gallery to a sub-directory? This is the right place!

Article summary

## Move Piwigo to a new server

To move your Piwigo to a new web hoster, you need to follow these steps in the right order.

1. Backup your database (DB)

Most of the time, you will use the default database manager **phpMyAdmin.**

1. Backup all your files through FTP

Using your FTP transfer software, select the folder where your gallery is installed. The default directory is: ./piwigo

1. Import your DB to the new web hoster

This involves performing the reverse operation of point #1, i.e. “importing” the backup previously created in the phpMyAdmin manager.  If your backup is too large, you'll need to delete the history on your gallery (first host). If that's not enough, perhaps some plugins are likely to be taking up a lot of space. Uninstall them and make a backup.

1. Move all the files to the new web hoster through FTP

This is the reverse of point #2, i.e. “send” your files to the new installation folder.

1. Edit the content of the file *./local/config/database.inc.php*

Here is an example of the file with comments.

```php
<?php
$conf['dblayer'] = 'mysql'; // DB type
$conf['db_base'] = 'piwigo'; // DB Name
$conf['db_user'] = 'gotcha'; // connexion ID to your DB
$conf['db_password'] = 'xxxxxx'; // connexion password to your DB
$conf['db_host'] = 'localhost'; // DB hostname 
$prefixeTable = 'piwigo_'; // table prefix
 
define('PHPWG_INSTALLED', true);
define('PWG_CHARSET', 'utf-8');
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');
 
?>
```

## **Move from Piwigo.com**

You already have a Piwigo hosted on piwigo.com and you want to move it to your own environment? Follow the guide.

- on your Piwigo.com account, page [Administration > My account > Manage > tab My data], ask to retrieve your data. They will be provided as a list of 500MB zip files. You can also request for an FTP access, if you contact Piwigo.com support for that.
- extract content of the zip files. In the first zip file, you will get the SQL database dump + the “local” directory. All zip files, including the first one, will include the “upload” directory.
- download the latest version of Piwigo (not the netInstall), extract files, transfer them on your hosting but do not start the installation.
- edit file local/config/database.inc.php so that it matches your database credentials on your new hosting server. Please note that tables have no prefix on Piwigo.com, so change `$prefixeTable = '';`
- transfer directories “local” and “upload” on your new hosting server
- import your database dump
- you're good to go, an you may certainly have to install/activate a few plugins you were using on Piwigo.com, but your Piwigo will tell you.

## Move a gallery from the root to a subdirectory

### I don't want to move my photos

!!! info "Info :"
    In the process below, we'll use the convention that the dot {.} corresponds to [http://www.exemple.com](http://www.exemple.com/)
    In your database (DB), we'll assume that your table prefix is `piwigo_`.

1. First, activate the maintenance mode (Administration, Tools, Maintenance, action “Lock gallery”).
2. Now go to your ./`my_gallery`/index.php address to check that the site is under maintenance.
3. Copy all your Piwigo directories and files from the root, into the directory ./`my_gallery`/ except ./galleries/ and except ./uploads/.
4. Let's move on to the first modification of your Database (DB) ⇒ In your DB, with the help of phpMyAdmin, “SQL” tab, enter the following code:

```sql
UPDATE `piwigo_sites` SET `galleries_url` = '../galleries/' WHERE `id` =1 AND  `galleries_url` = './galleries/';
UPDATE `piwigo_sites` SET `galleries_url` = '../uploads/' WHERE `id` =2 AND  `galleries_url` = './uploads/';
```

1. Let's log on to ./`my_gallery`/identification.php and check that ./galleries/ is working properly for album management. To do this: go to Administration > Tools > Synchronize, tab “Site manager” and you should see ./galleries/ If not, start again.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-30c509c5.png)

1. Now you need to rename (at the root) ./index.php to ./index.old.php.
2. The gallery can now be unlocked (Administration, Tools, Maintenance, action “Lock gallery”).
3. We're going to place the new index.php at the root of the site:
    1. Rename old index.php to index.php.old
    2. Your new index.php file will serve as a welcome page when you land at http://www.exemple.com.
4. Then, to finalize the process, it is necessary to update the information concerning the paths (among others): Administration > Tools > Maintenance and choose:
    1. Update albums’ information
    2. Update photo’s information
    3. Purge compiled templates
5. Last check: make sure the images are available on the site.

In a few days (while you check that everything has gone smoothly), you'll be able to delete all your old folders/files at root level, except : `./galleries/` `./uploads/` `./my_gallery/` `./index.php`

### I want to move everything (including photos)

It's even easier! :-)
Move all the files/folders and... that's it!
