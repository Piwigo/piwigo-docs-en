# Importing photos into Piwigo

There are many ways to import files into Piwigo.

!!! tip "Tip"
    Most of the time, we are talking about photos, but what applies to photos also applies to every other image, video and document type in general (see article: [The different file formats in Piwigo](file-formats-compatible-piwigo.md)).

This article allows you to discover how to add files:

- from Piwigo’s administration
- from your gallery (for users that aren’t administrators)
- from other sources

!!! warning "Some options, such as FTP upload, are only available to users who are using a self-hosted gallery."

## Importing photos from Piwigo's administration

Go to the administration to import photos (or any other type of file) from Piwigo's administration.

On the left menu, select Photos > Add. You will land on the Photo Upload page.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b175687b.png)

### Choose the destination album for your photos

To import files into Piwigo, you must first choose an album by clicking on the icon next to “Choose an album”. This opens a window listing all existing albums. Albums with sub-albums appear with an arrow on the left, and you can scroll down the tree by clicking on the arrow. You can search for the album of your choice by name.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b4272d6b.png)

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-cd92b583.png)

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bafc87cd.png)

Click on the + next to an album to select it.

You can also create a new album by clicking on “Creation mode”. Choose the parent album from the list to create a sub-album, or click on “Create a root album” to create an album on the first level of your Piwigo space. Give the album a name, choose whether to display it at the beginning or end of the album list, and click on “Create and select”.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d655458a.png)

### Importing files into Piwigo

Once the album has been selected, you have two choices to import files from your computer:

- Clicking on the Add Photos button, and selecting the desired files on your computer.
- Dragging and dropping the files directly from your computer's folder into the gray area, as seen in the example below.

![Glisser déposer.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8066d9b3.gif)

As you go along, the files are displayed on the screen. They are in a sort of queue. You can see their name and their size. If it turns out you don't want to import one of the files, simply click the cross on the right.

![Attente de transfert.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-43a211fc.jpg)

Once you are satisfied, click on the "Start Upload" button.

As Piwigo is importing your files, they disappear from the queue. Once the import is over, you can choose:

- to change the photos' properties in batches by clicking on "Manage this set of photos”
- or to add other files by clicking on "Add another set of photos”

![Importer des photos.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0f178ec0.gif)

## Detecting duplicates during import

When you import files into Piwigo, Piwigo can detect duplicates and avoid importing them.

When adding photos, if you import a file that is identical to another file from your Piwigo gallery, Piwigo will add the existing file to the import album, but will not duplicate the file.

You can turn this feature on or off from the administration, in the Configuration > Options menu, in the General tab, then the Miscellaneous section.

![Détecter doublons.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-87ce4644.jpg)

## Resizing photos during import

To adjust the size of files imported into your gallery, go in the administration, and, in the left menu, click on Configuration > Options. Next, click on the "Photo sizes" tab.

![Tailles de photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1a2a40a9.jpg)

By default, Piwigo imports the file in its original size.

If you wish, you can ask Piwigo to automatically resize files during the import.

**❓ Why resize photos during import?**

This can be useful if your original photos have a very high resolution and you don't need to display your photos in their optimal resolution in your photo library. The benefits are as follows:

- This reduces file size, and thus your needs in terms of storage space
- This reduces the server's needs in terms of resources

However, we don't recommend resizing your photos if Piwigo is the main space where you store your files. Quality is lost when resizing files. If you send a lower quality version of your images to Piwigo, make sure to keep the original ones in another safe space (a backup on a hard drive, for example).

To automate the resizing of your photos, tick the "Resize after upload" box in the menu Configuration > Options, then Photo sizes. You can choose:

- The maximum width of your photos (in pixels)
- The maximum height of your photos (in pixels)
- The image quality after resizing (in percentage points)

![Redimensionner photo.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7a39c4b3.jpg)

## Editing files after an import

When you just finished importing a set of photos into Piwigo, you are able to edit their properties in the process, by clicking on "Manage this set of photos".

![Gérer lot photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5f6e10f7.jpg)

This adds the selected photos into your caddie. You then land on the "Batch Manager" page, sorted with the photos you just uploaded.

You have the ability to apply changes to the files you imported:

- either by batch, by staying on the current tab (Global mode)
- or individually, file by file, by clicking on the "Single mode" tab.

![Sélection photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6d37ff62.jpg)

To better understand how to use the batch manager, [read this article](batch-manager-piwigo.md).

## Importing photos from your gallery

Do you want a user to be able to add photos to your Piwigo gallery without being an administrator? This is possible, thanks to the Community plugin. 

This plugin allows you to grant non-administrator users the right to add photos in Piwigo from a dedicated page in your gallery.

[Visit the Community plugin documentation](../managing-users/community-plugin-piwigo.md)

## Importing files from your mobile device

You can connect your phone or tablet to Piwigo in order to create albums and add photos and videos to your gallery. To do this, install one of the official Piwigo [mobile apps](../mobile-apps/index.md).

## Importing files from one of your computer's folders with Piwigo Remote Sync

It is possible to automatically synchronize one of your computer's folders with Piwigo, and even to add an entire tree of folders.

Each time you start the synchronization, only new photos will be added.

To do this, you need to install the [Piwigo Remote Sync](https://piwigo.org/ext/index.php?eid=851) app on your computer. This software is compatible with Mac, Windows and Linux.

To learn more, visit the dedicated documentation by clicking the link below:

[Documentation : Piwigo Remote Sync](../organizing-albums/how-to-create-an-album.md)

## Importing and synchronizing one of your computer's folder trees as FTP

If you are using a Piwigo that is hosted on your own server, and not on [piwigo.com](http://piwigo.com/), you can synchronize one of your computer's folders with your gallery.

To do so, you will need an FTP client software.

To learn more, read the article below.

[FTP import and synchronization](../self-hosting-piwigo/importing-and-synchronizing-ftp-photos.md)

## Importing files from Adobe Lightroom

If you are using the Adobe Lightroom photo manager, you can install a plugin that will allow you to transfer photos directly to your Piwigo gallery. This plugin is not developed by Piwigo. It is sold for $15 by its creator.

[Visit this page to learn more](https://alloyphoto.com/plugins/piwigo/)

## Importing files from Digikam

[Digikam](https://www.digikam.org/) is a free photo management software, compatible with Linux, Windows and Mac. It features an "export to Piwigo" plugin that allows you to transfer photos from Digikam to Piwigo.

[Visit this page to learn more](https://docs.digikam.org/en/export_tools/piwigo_export.html)

## Importing files from Shotwell

[Shotwell](https://wiki.gnome.org/Apps/Shotwell) is an open source photo manager for Linux. It is installed by default on Ubuntu and Fedora. A Shotwell plugin allows you to export photos to Piwigo.

[Download the connector on GitHub](https://github.com/guillaumev/piwigoshotwell)

## Importing files from your Flickr account

Do you have photos on a Flickr account and wish to upload them to Piwigo? That's possible!

To do this, install the Flickr2Piwigo plugin.

!!! warning "If you are using a self-hosted gallery, make sure to have the latest version of the plugin."

The plugin setup page explains the various steps to connect your Piwigo gallery to Flickr.

![Plugin Flickr.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-3c5ca4d4.jpg)

You first need to log in to your Flickr account and visit [this page](https://www.flickr.com/services/apps/create/apply/) to create your API key.

On the first page, choose the "Apply for a non-commercial key" option.

On the next page, fill in the Name and Description fields for your key, like below for example. Make sure to tick the two boxes to agree with the Terms of Use and click on "Submit".

![API key request.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-67d95267.jpg)

Flickr will then display two strings of characters: "Key" and "Secret".

Retournez dans la configuration du plugin Flickr2Piwigo, et coller ces deux chaînes de caractères dans les champs “Clé API” et “Secret API”. Enregistrez les paramètres.

Toujours dans la configuration du plugin, allez dans l’onglet “Importation et cliquez sur “Connexion”. Vous allez être redirigé vers une page Flickr. Cliquez sur ”OK, je l’autorise”.

![Page Flickr.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-03eecec1.jpg)

There you go, you're connected!

![Flickr fini.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0e6397d8.jpg)

You now have the ability to:

- List your Flickr albums and choose which photos you want to upload to Piwigo for each album ;
- Upload all the photos from your Flickr account.

### Listing your Flickr albums

If you choose this option, the list of albums on your Flickr account will be displayed. Click on an album to choose the photos to upload to Piwigo. You can select the photos to import and choose which album to import them into. You can also choose whether or not to import your photos' description data from Flickr to Piwigo (name of the photo, author, creation date, tags...).

![Import album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-272bf490.jpg)

### Importing all photos from your Flickr account

If you choose this option, you will be able to choose to recreate all of your Flickr albums in Piwigo, or to import all of your Flickr photos into the album of your choice. You can also choose whether or not to import your photos' description data from Flickr to Piwigo (name of the photo, author, creation date, tags...).

![Importer tout.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5408c32d.jpg)

And voilà!

As you can see, importing photos from your Flickr account and into Piwigo is very easy 🙂
