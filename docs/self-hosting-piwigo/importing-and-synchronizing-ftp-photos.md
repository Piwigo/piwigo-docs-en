# FTP import and synchronization

!!! info "Read also: [Importing photos into Piwigo](../import-and-manage-photos/importing-photos-into-piwigo.md)"

## Introduction

If you are using a Piwigo gallery that is installed on your own server (or a server managed by your organization), you can transfer directories from your computer to your Piwigo gallery by using the FTP protocol.

This method, which is historically the oldest, is the longest to set up. It is meant for advanced users, who have a stable workflow.

If you have a large photo library, this photo upload method might be made for you.

If you prefer, there are other methods for uploading your photos: to learn more, visit the section about [uploading photos to Piwigo](../import-and-manage-photos/importing-photos-into-piwigo.md).

!!! warning "Warning :"
    This upload method is only available for self-hosted Piwigo galleries: therefore, it is not available for customers of a Piwigo Cloud plan.

## Pros and cons of this method

| Pros | Cons |
| --- | --- |
| ✅ Perfect for large galleries | ⚠️ Requires knowing how to prepare photos before publishing them online |
| ✅ Suitable for uploading files other than photos | ⚠️ No room for renaming / moving your photos and albums |
| ✅ Freedom with creating directories on your server | ⚠️ Use of an FTP transfer software |
|  | ⚠️ Required to synchronize Piwigo with your files |

## Transferring a first album

1. Create a directory on your computer.
2. Paste photos inside of this directory.
    
!!! warning "Warning :"
    The name of the directories and files must only contain letters, numbers, and the "-", "_", or "." symbols. No spaces or characters with accents.

3. With an FTP client, copy the directory in the `./galleries/` directory in your Piwigo setup.
4. Log into your Piwigo gallery, go to the administration, in the Tools > Synchronization menu. Select the Directories + files options, Synchronize metadata, and do not select "Simulation only".

Congratulations! An album has been created on your gallery.

## Understanding synchronization

Copying files on your server with your FTP software is not enough for your photos to be visible to everyone. Piwigo needs to *go over* the changes that happened. You just added photos, you now need to tell your gallery to display your photos: this is what **synchronization** is for.

Therefore, each time you want to transfer files in Piwigo with FTP, you will create a sub-directory of `./galleries/` and you will put your elements there (in a web-suited size). 

Optionally, you will need to place thumbnails in a sub-directory of the one you just created. 

Then, from the online administration, you need to ***synchronize*** the database in order to make it recognize your new elements.

## **Organization of directories and files**

The directories that represent albums are located in the `./galleries/` directory in your Piwigo setup.

Here is the directory tree of a very small gallery below.

```
galleries
|-- wedding
|   |-- ceremony
|   |   |-- entrance
|   |   |   |-- paul-arriving.jpg
|   |   |   +-- jane-arriving.jpg
|   |   +-- exit
|   |       |-- flower-children-exit.jpg
|   |       +-- paul-and-jane-exit.jpg
|   +-- cocktail
|       |-- speech001.jpg
|       |-- speech002.jpg
|       +-- speech003.jpg
+-- honeymoon
|   |-- hotel.png
|   |-- plane-takeoff-video.avi
|   +-- pwg_representative
|       +-- plane-takeoff-video.jpg
+-- photographer-session
    |-- img0001.jpg
    |-- img0002.jpg
    +-- pwg_format
        |-- img0001.cr2
        |-- img0001.cmyk.jpg
        |-- img0001.zip
        |-- img0002.cr2
        +-- img0002.cmyk.jpg
```

Some explanations to better understand this diagram:

- With the exception of "pwg_representative" and "pwg_format", each directory in `./galleries/` generates an album. The number of levels (depth) is not limited.
- Fundamentally, a photo is represented by a file. For Piwigo, a file can be a photo if its extension appears in the list of the `file_ext` configuration setting (see file include/config.inc.php). A file can be a photo if its extension appears in the list of the `picture_ext` configuration setting.
- By default, the elements other than photos (sounds, text files, anything you want...) are represented by a icon that corresponds to the extension of the file's name. As an option, a representative can be associated (see file plane-takeoff-video.avi in the example).
- Multiple formats: you can offer a photo in multiple formats. In this example, there are 3 additional formats for img0001.jpg. You can activate this feature by adding `$conf['enable_formats'] = true;` to your local configuration and by setting a list of formats, such as `$conf['format_ext'] = array('cmyk.jpg', 'cr2', 'zip');`. [Learn more about multiple formats](../import-and-manage-photos/multiple-formats-piwigo.md)

!!! warning "Warning :"
    The name of the directories and files must only contain letters, numbers, and the "-", "_", or "." symbols. No spaces or characters with accents.

!!! tip "Tip :"
    An album can contain both photos and sub-albums. Nevertheless, for each album, choosing between containing photos **or** sub-albums is strongly recommended.

- Once the files are correctly placed in directories, go to the Administration > Tools > Synchronize screen.

## File synchronization

As soon as you choose to transfer your files via FTP, synchronization is a necessary step whenever you *add* / *rename* / *move* / *delete* *any element* in your photos.

!!! warning "This feature is useless if you are transferring your files in another way."

Go to Tools > Synchronize in the administration.

You will then get access to the screen below.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-28b01f5b.png)

This page allows you to choose the synchronization settings and start a synchronization.

Here are the options available:

### Synchronize file structure with database

This is what allows you to tell Piwigo: "hey, there are new files, it's time to go see them and take them into account".

3 options are available:

- Nothing: in this case, nothing will be synchronized. This is what you will select if you only want to synchronize the metadata.
- Directories only: with this option, only directories will be synchronized. This is useful if you don't need to synchronize your entire gallery.
- Directories + files: with this option, not only will you synchronize the files but also the elements that make them up. If you select this option, new options appear.
    
    ![Option de synchronisation.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-62d9274c.jpg)
    
    Displaying maximal information will allow you to obtain statistics on the results of the synchronization.
    
    Adding the new photos to the Caddie will allow you to put all the added photos in the Caddie (to then manage them using the [batch manager](../import-and-manage-photos/batch-manager-piwigo.md), for example).
    
    "Who can see these photos?" lets you set the [privacy level](../managing-users/privacy-levels.md) for the added photos.
    

### Synchronize database photos with file metadata

This section offers one option and two sub-options:

- Synchronize metadata (filesize, width, height): lets you choose whether or not to synchronize the files' metadata.
    - Including already synchronized photos: if you select this option, you will even update the elements that are already located in your gallery. Useful when you modified the metadata of your photos.
    - Override existing values with empty ones: if you select this option, you will replace the old values with new ones, even if they are empty.

### **Simulation**

Piwigo allows you to not perform a change straight away in order for you to make sure the synchronization is running smooth.

As the name suggests, this feature will therefore simulate the result of the synchronization.

!!! warning "If you really want to synchronize your files, make sure this box is not ticked!"

### **Reduce to single existing album**

In this area, you are able to browse your albums and sub-albums in order to help Piwigo find elements to synchronize. Synchronizing an entire gallery when we know the right directory to synchronize is useless (and sometimes even dangerous).

A small option called "*Search in sub-albums*" is here to prevent you from refining your search too much for the folder that needs to be synchronized. Experience will tell you how to use it wisely.

## Common errors

In the event of a problem, Piwigo will inform you of the errors it encounters.

Let's go over these errors together.

- **PWG-UPDATE-1**: the name of directories and files must *only* be made up of letters, numbers, of "-", "_", and ".". This means no *fancy* characters and no characters with accents.
- **PWG-ERROR-NO-FS**: the file or directory can't be accessed (either it doesn't exist, or the access has been denied).
- **PWG-ERROR-VERSION**: the version of `create_listing_file.php` on the distant site and on Piwigo needs to be the same.
- **PWG-ERROR-NOLISTING**: the listing.xml file can't be found on the distant site. This file is generated by choosing the "generate listing" command in the site manager.

## **Additional information**

- **pwg_representative**: (optional use) for non-image elements. Example: a zip file: since the zip file isn't an image, the .jpg image with the same name will be displayed in the gallery, and the zip will be downloadable through the floppy disk icon.

## Tips

- Don't deselect *Search in sub-albums*.
- Keep simple names, there are restrictions (due to the web, see below).
- Typography rules, names of directories and images, meaning:
    - no spaces and no accents
    - so, only letters, numbers, or the characters "-", "_", and ".".
- Prepare your elements before placing them on the server.

## Single synchronization

From Piwigo's administration, you can re-synchronize a photo's metadata by clicking on the "synchronize metadata" icon from a photo's editing screen.

![Synchroniser unitaire.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ada63451.jpg)

Article summary
