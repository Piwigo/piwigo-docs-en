# Issues with generating thumbnails and representatives

<aside>
💡 Read also: [Importing photos into Piwigo](../import-and-manage-photos/importing-photos-into-piwigo.md)

</aside>

When you upload files to Piwigo, there is a whole process at work. Files are uploaded to the server but also registered in the database, and some other files are generated on the go:

- sevaral files are created when Piwigo generates multiple sizes of your picture, including thumbnails that will be displayed on your gallery;
- for some file formats (videos, PDF,…) images are generated to be displayed instead of the source file on your gallery: that’s what we call representatives.

Thumbnails and representative generation can fail if something is not configured correctly on your server. Indeed, Piwigo uses external libraries to do this work.

If you manage your server by yourself, you might need to investigate to  make it work properly: that’s what we will explain in this article.

<aside>
⚠️ This article is only for webmasters of a self hosted Piwigo library. If you are a [piwigo.com](http://piwigo.com) customer, you are not concerned: the hosting environment on piwigo.com is optimized.

</aside>

## 1- Photo thumbnails generation issues

You have imported pictures in an album, but you don’t see images on your Piwigo gallery? It might be caused by a thumbnail generation problem.

To be sure, go to the batch manager in the administration and select your album. Once you have validated the filter, some thumbnails should appear. If you see “XX photos in current set” but just empty squares, there is a thumbnail issue.

### Check if an error is returned by the i.php url

<aside>
ℹ️ Piwigo calls i.php to generate the resized picture in ./_data/i/, then directly calls the resized picture from ./_data/i/. Many problem may appear: an overloading of the server, a picture that is too big or with a wrong extension, not enough permission on files/folders etc.

</aside>

In the Batch Manager, right-click on a failed picture then “Display the picture” or “copy the url to the picture”, from your browser. You can also try to display the source code of the page (Ctrl+U usually) and search (Ctrl+F) for an url with “i.php”. Then go to this url with your browser and note any error message displayed.

Here are the error message you could find:

1. “source not found” : check by Ftp, if the source picture exists and if the permissions of the file is enough (Chmod: 755 folders, 644 files). If it's still not solved, be sure the Php user/system has enough rights on your server
2. “dir create error” : check by Ftp, if the permissions of the folders are set right (Chmod : 755 folders, 644 files). If it's still not solved, be sure the Php user/system has enough rights on your server
3. “Empty array while parsing Sizing” “Sizing arr” “Invalid chars in request”… : a theme or plugin is not working, write a post on the forum with a list of the plugins used and your theme.
4. 404 error page : the file i.php is missing. Download the zip of your current version of Piwigo on piwigo.org, extract and upload the files by Ftp. Overwrite all the files : you will not lose any customization or pictures.
5. 403 error page: check the permissions on the file i.php (and the other files also). Chmod : 755 folders, 644 files.
6. “500 Internal error page” or “PHP Fatal Error: Allowed memory size of …”: many problems may cause this error. If some pictures are generated and others not, it might be due to an overload of your server (just wait a few hours) or a lack of memory for PHP (ask to your hoster to change the memory_limit option). If the graphical library is GD, install Imagemagick.

No error message?

1. With Localfiles Editor, put this local config variable: `$conf['enable_i_log'] = true;` Then try to generate some size with the Batch Manager. Once started, you can go to _data/tmp/i.log and open the file to see if there is any error message in it. Post on the forum the content of this file.
2. You can also read the instructions for “500 Internal error page” and use Imagemagick. Or post a url to your website on the forum with public visible pictures.

### **Install ImageMagick**

GD Graphics Library and ImageMagick are both open source libraries for dynamic images generation. You can experience issues with thumbnail generation (among other problems) if you server uses the GD Graphics Library. 

That is why we recommend to switch to Imagemagick. Imagemagick is available with most hosting packages. First, Imagemagick needs to be installed if it’s not already done. Then you can tell Piwigo where the files are.

To do so, add the following variables with [Localfiles Editor](editing-configuration-localfiles-editor-plugin.md). You first need to ask to your hoster for the path to the ImageMagick binaries.

```php
// Library used for image resizing. Value could be 'auto', 'imagick',
// 'ext_imagick' or 'gd'. If value is 'auto', library will be choosen in this
// order. If choosen library is not available, another one will be picked up.
$conf['graphics_library'] = 'ext_imagick';
// If library used is external installation of ImageMagick ('ext_imagick'),
// you can define imagemagick directory.
$conf['ext_imagick_dir'] = '/usr/local/bin/';//change with own path!
```

To check which Graphics Library is used on your environment, you can go to the administration, menu Tools > Maintenance, and go on the tab Environment.

![ext-image-magick.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7b656060.png)

<aside>
⚠️ Warning! Your server may not be using ImageMagick, but Imagick, a PHP feature that "encapsulates" ImageMagick, but does not generate previews for certain file formats. Be sure to use External Image Magick.

</aside>

## 2- Video thumbnails generation issues

You can upload videos to your Piwigo by using the VideoJS plugin and adding some code to your local configuration ([as explained here](../import-and-manage-photos/file-formats-compatible-piwigo.md)).

But this plugin needs the **ffmpeg** library to work properly. If it is no installed on your server, Piwigo won’t be able to execute the command that generate thumbnails.

In that case there can be two consequences:

- Either the video is added to your gallery but no image is generated, so it is represented by a default icon;
- Or the video is not added to your gallery at all.

So, if you want videos to work properly on your Piwigo, you need to check if **ffmpeg** is installed. If it is, good: you just have to tell Piwigo where the files are.

To do so, add the following variables with [Localfiles Editor](editing-configuration-localfiles-editor-plugin.md). You first need to ask to your hoster for the path to the **ffmpeg** binaries, and replace the code with the path on your own server.

```php
$conf['ffmpeg_dir'] = '../../apps/ffmpeg/';
```

If you need more technical support on this subject, check the [VideoJS documentation on GitHub](https://github.com/Piwigo/piwigo-videojs/wiki/How-to-add-videos#step-2-install): you will find detailed instruction about **ffmpeg** installation.

<aside>
⚠️ If ffmpeg is not available on your web hosting, you can not manage videos properly with your Piwigo. We recommend to switch to another web hoster.

</aside>

## 3- Preview issues with some files type (PDF, PSD, HEIC…)

You can upload PDF files to Piwigo, [as it is explained here](../import-and-manage-photos/file-formats-compatible-piwigo.md).

Piwigo will generate a thumbnail to represent your file, by extracting the first page of the file and converting it to an image.

But sometimes, after uploading a PDF file to Piwigo, you will see an icon instead of the thumbnail, like on the exemple below.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-24a21bc4.png)

On your gallery, your PDF will be also displayed with this default icon.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-90ba4ef5.png)

In this case, the file is correctly uploaded to Piwigo, and can be downloaded by clicking on the “Download file” icoon. But the thumbnails are not correctly generated.

To fix this issue, check if the **External** **ImageMagick** library is installed and if necessary, declare its path in the local configuration (as explained in a previous chapter on this page).

Article summary

This problem doesn't just affect PDFs: it also prevents thumbnails from being generated for PSD, AI, TIF, TIFF and HEIC files.