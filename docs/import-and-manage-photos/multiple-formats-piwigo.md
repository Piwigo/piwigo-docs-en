# Multiple formats for one single photo

Multiple formats allow you to offer different versions when downloading a single photo or image. For example :

- a JPG version and a PNG version ;
- a JPG version, a PSD version and a PDF version
- etc.

<aside>
ℹ️ If you are a piwigo.com customer, this plugin is only available from the Enterprise plan and higher.

</aside>

## How do I activate multiple formats ?

The answer is different whether you are using a self-hosted Piwigo gallery or are a piwigo.com customer.

- I am hosting my gallery myself (or my organization is doing so)
    
    To activate this option, you need to use [LocalFile Editor](../self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md) and add the code below in your configuration file. If this is not possible, ask the webmaster who is managing your gallery.
    
    ```php
    // enable_formats: should Piwigo search for multiple formats?
    $conf['enable_formats'] = true;
    ```
    
    You can modify the default accepted formats with the following configuration setting.
    
    ```php
    // photo (or nay other file). Formats are in sub-directory pwg_format.
    $conf['format_ext'] = array('cr2', 'tif', 'tiff', 'nef', 'dng', 'ai', 'psd');
    ```
    
- I am a piwigo.com customer
    
    This feature is available for [piwigo.com](http://piwigo.com/) customers who have subscribed to an Enterprise or VIP plan. To activate it on your gallery, you need to make a request to the support.
    

## Adding multiple formats on a photo

Once the "multiple formats" option has been activated, a new "Formats" tab appears when editing a photo in Piwigo's administration.

![Edit photo formats.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ebaca22d.jpg)

Click on "Add formats" to add one or more versions of the current photo.

You will then land on the photo upload form. You are reminded of the photo to be associated with new formats. You can add as many formats as you wish among those accepted by your configuration.

![Formats Upload.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-59b21a2f.jpg)

Click on "Start transfer" to send files to the server.

Once the formats have been added, you can view them from the Formats tab of your photo in the administration.

![Edit photo TIFF.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-33a26685.jpg)

Note that once the "multiple formats" option has been activated, you can also add new formats from the photo upload page, by selecting the "Upload formats" option. In this case the files' names need to be the same as the file for which you want to add these new formats.

![Upload formats.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-50117a2b.jpg)

## Displaying multiple formats in my gallery

In order to display the different formats available for a photo in your gallery, you need to install the **Download Formats Buttons** plugin.

Once this plugin has been activated, a file's download button shows the different formats available as well as the file size. Click on the chosen format to download it.

![Download formats.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-867a63cf.jpg)

Article summary

---

← Previous

[Managing your files’ properties and metadata](properties-metadata-photos-piwigo.md)