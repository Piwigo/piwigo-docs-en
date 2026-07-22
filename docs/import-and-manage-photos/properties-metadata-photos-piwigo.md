---
title: Photo properties and metadata - Piwigo Documentation
description: This article introduces all of the possibilities offered by Piwigo to describe, organize, present and index your files with the properties and metadata.
---

# Managing your files’ properties and metadata

**This article introduces all of the possibilities offered by Piwigo to describe, organize, present and index your files with the properties and metadata.**

## Glossary

Here are some clarifications to start off with!

### What are metadata?

The metadata are details from the original file. They are read and integrated by Piwigo during import.

The metadata are mainly relevant for photos. They are directly saved by the device upon shooting, or by a photo management software used by the photographer.

Piwigo handles two types of metadata:

- **EXIF**: these tags are typically used to describe how a photo was captured. For example, tags can contain information about the model of camera/smartphone used, lens, aperature size, focal length, exposure duration, date/time, GPS coordinates, etc.
- **IPTC:** IPTC headers describes the content of the image. Some cameras will allow you to record your name, and other copyright information to a digital photo, using this header. Sometimes, editing software is used to later add information like titles, headlines, captions, descriptions, keywords etc.

The basic metadata are the following:

- file name
- file size
- file dimensions
- author
- creation date

Many additional metadata can be available, such as the camera brand, the model, the details about the shooting, the keywords…

If you import your files into Piwigo from an external software such as Lightroom, Digikam, Shotwell, or Aperture, the metadata are imported to Piwigo from these softwares.

By default, Piwigo displays some **basic** metadata on the photo page (dimensions, filesize etc.). When the “Show metadata” icon is clicked, some additional **EXIF** metadata will be shown: Camera Make+Model, image capture date+time, and aperature F-number. Piwigo does not display IPTC metadata by default.

![The metadata displayed with the Modus theme](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5b2fae89.jpg)

The metadata displayed with the Modus theme

![The metadata displayed with the Bootstrap Darkroom theme](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e87db559.jpg)

The metadata displayed with the Bootstrap Darkroom theme

### What are properties?

Properties are Piwigo's in-house fields, allowing you to describe and sort your files.

Some properties are created by Piwigo, such as the import date; others are imported from the metadata, such as the creation date (date when the photo was taken); lastly, others can be chosen by you.

Some properties can be added with plugins. The **Manage Properties Photos** plugin even allows you to create custom properties (we will cover this topic later in this article).

In any case, these properties can be modified. They can be displayed in the gallery.

![The properties displayed with the Modus theme](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ce5c160e.jpg)

The properties displayed with the Modus theme

![The properties displayed with the Bootstrap Darkroom theme](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-78d870bc.jpg)

The properties displayed with the Bootstrap Darkroom theme

## Managing your photos’ metadata on Piwigo

As we said, metadata are automatically integrated into Piwigo when you import photos.

But there are some options to learn about in order to display and manage these metadata.

### Display metadata in the Piwigo gallery

**Displaying the metadata with Modus**

When using the [Modus](../piwigo-themes/modus-theme-piwigo.md) theme, a camera-shaped icon on a photo's page will allow you to display the metadata.

![afficher-metadonnees.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-03424eb2.png)

When clicking on this icon, some metadata will be added to the properties in the section on the right.

![EXIF metadata.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5b2fae89.jpg)

If you want to hide the metadata display icon in your gallery, go in the administration: in the Configuration > Options menu, in the "Display" tab, then the "Photo page" section: you are then able to select or deselect the "Activate icon "Show file metadata"" option.

If you want the metadata to always be displayed in your gallery without needing to click on this icon, then download the **AlwaysShowMetadata** plugin.

**Displaying the metadata with Bootstrap Darkroom**

When using the [Bootstrap Darkroom](../piwigo-themes/bootstrap-darkroom-theme-piwigo.md) theme, the metadata, when available, will be displayed below the photo by default, in the column on the right.

They can also be displayed in a tab, or in a side bar, depending on the option you chose when setting up your theme.

![Darkroom theme.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-423ae635.jpg)

If you want to hide the metadata with the Bootstrap Darkroom theme, the only solution is to also hide the properties through the theme's configuration, by selecting the "Picture info display position = disabled" option.

![Picture page display.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7d14f38d.jpg)

### Synchronizing metadata

On the editing page of a photo in the administration, a button allows you to synchronize a file's metadata. This action imports your files’ metadata to your Piwigo database. Normally, it should be automatically done when you imported the files to Piwigo.

But it might be useful if photos have been imported through FTP and the synchronization step has been skipped. 

It can also be useful after a change in configuration, to apply the metadata's new import configurations.

If you are a self hosted user and use FTP synchronization to import your files, you can also synchronize metadata in batch through the “Synchronize” menu of your administration panel. [Learn more about FTP Synchronization](../self-hosting-piwigo/importing-and-synchronizing-ftp-photos.md)

### Read Metadata: Display all the metadata of a file

If you want the ability to display all the metadata of a file from your gallery in the administration, you need to install the **Read Metadata** plugin.

This plugin's Configuration screen allows you to extract a file's metadata, either from its ID or by selecting it in a drop-down list.

![Read metadata.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b8adfb2b.jpg)

### Show more EXIF Metadata

As we said, Piwigo show some EXIF Metadata by default. But you can display more EXIF fields if your want to. 

If you are a Piwigo cloud customer, you need to contact support.

If you manage a self hosted Piwigo gallery, you just have to edit the configuration file using [LocalFiles Editor](../self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md).

- Click here to show how to add new EXIF fields to your Piwigo gallery
    
    By default, here are the EXIF fields displayed.
    
    ```php
    $conf['show_exif_fields'] = array(
      'Make',
      'Model',
      'DateTimeOriginal',
      'COMPUTED;ApertureFNumber'
      );
    ```
    
    To display *more* Exif fields, all you have to do is add their keys in your config file with LocalFiles Editor. Inserting the example code below into your config plugin, will add a few more camera settings:
    
    ```php
    $conf['show_exif_fields'] = array(
      'DateTimeOriginal',
      'Make',
      'Model',
      'ExposureProgram',
      'FocalLengthIn35mmFilm',
      'FNumber',
      'ExposureTime',
      'ISOSpeedRatings',
      'Flash',
      'WhiteBalance',
      'UserComment'
      );
    ```
    
    To see all available EXIF metadata, just use the Read Metadata plugin presented in the previous chapter.
    
    If you don’t want to show EXIF metadata at all on your gallery, just add the following code to your config file:
    
    ```php
    $conf['show_exif'] = false;
    ```
    

### Show IPTC Metadata

As we said, Piwigo does not show IPTC metadata by default. But it is possible !

 If you are a Piwigo cloud customer, you need to contact support.

If you manage a self hosted Piwigo gallery, you just have to edit the configuration files using [LocalFiles Editor](../self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md).

- Click here to show how to display IPTC fields to your Piwigo gallery
    
    Add this parameter to your config file with LocalFiles Editor.
    
    ```php
    $conf['show_iptc'] = true;
    ```
    
    Then you must choose which fields to display. Here is an example:
    
    ```php
    $conf['show_iptc_mapping'] = array(
      'iptc_creator'         => '2#080',
      'iptc_title'           => '2#005',
      'iptc_headline'        => '2#105',
      'iptc_description'     => '2#120',
      'iptc_keywords'        => '2#025',
      );
    ```
    
    To see all available IPTC metadata, just use the Read Metadata plugin presented earlier in this page.
    

### Mapping metadata with properties

By default, EXIF and IPTC metadata can be shown on the photo page, but but they are not searchable.

If you want, you can map some metadata with Piwigo properties, so they can be used to search and sort photos on your gallery. For example, the “Model” EXIF field can be added in tags, if you want to filter photo by camera model.

 If you are a Piwigo cloud customer, you need to contact support to do so.

If you manage a self hosted Piwigo gallery, you just have to edit the configuration files using [LocalFiles Editor](../self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md).

- Click here to show how to map EXIF metadata with properties
    
    By default, the EXIF “DateTimeOriginal” metadata is imported as creation date in Piwigo thanks to the following config parameter.
    
    ```php
     $conf['use_exif_mapping'] = array('date_creation' => 'DateTimeOriginal' ); 
    ```
    
    You can add more mapping option by adding new lines to this parameter. 
    
    This example imports comments to the description property:
    
    ```php
    $conf['use_exif_mapping'] = array(
      'date_creation'        => 'DateTimeOriginal',
      'comment'              => 'UserComment',
      );
    ```
    
    This example imports camera models as tags:
    
    ```php
    $conf['use_exif_mapping'] = array(
      'date_creation'        => 'DateTimeOriginal',
      'tags'                 => 'Model',
      );
    ```
    
- Click here to show how to map IPTC metadata with properties
    
    Example of extended mapping which imports IPTC metadata (often added using Adobe Lightroom) into corresponding Piwigo fields.
    
    ```php
    $conf['use_iptc_mapping'] = array(
      'author'          => '2#080',
      'name'            => '2#005',
      'comment'         => '2#120',
      'keywords'        => '2#025',
      );
    ```
    

### Write Metadata: Replace metadata with the properties

If you want to replace some IPTC metadata in the files imported to your gallery with information written in the Piwigo properties (title, description, authors, tags), you need to install the **Write Metadata** plugin.

!!! info "If you are a Piwigo Cloud plan customer, this plugin is only available from the Team plan and higher"

### Exif View: Translate your photos' EXIF values

If you want the ability to translate EXIF values in the gallery's language, you need to install the **Exif View** plugin.

### IPTC from Mac: Solve issues with special characters in your metadata

If you see strange characters in your photos' IPTC metadata, you can install the IPTC from Mac plugin, which converts IPTC data written in MacRoman to a UFT-8 encryption.

## Managing properties in Piwigo

### Editing a file’s properties

Unlike the metadata, it's up to you to set your files' properties in Piwigo. You can edit them when editing a photo in the administration.

![File properties.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1c3748d1.jpg)

!!! info "To learn more about photo editing, read the following articles :"
    
    - [Modifying or deleting photos](modifying-or-deleting-photos.md)
    
    - [Batch management: Modifying and managing a selection of photos](batch-manager-piwigo.md)

Here are the properties and informations Piwigo offers by default to label a file.

### Title

This is the name of the photo that will be displayed in the gallery. Depending on your theme and the chosen settings, the title will be displayed in multiple places in your gallery.

By default, the name is created from the file's name, but you can change it.

A photo's name allows you to find it easily using the search engine: this is therefore an important setting.

### Author

This property allows you to mention the author, such as the photographer who took the photo, for example. It's an unrestricted, text-based field that can later be displayed in the gallery.

### Creation date

By default, the creation date is imported from the file's *metadata*.

For a photo, this will usually be the date it was taken. For another file type, it will be the file's creation date.

When editing a photo, you can click on "Unset" to leave this property empty, or edit the date if you don't like the date displayed by default.

### Linked albums

Strictly speaking, linked albums aren't a property, even though they appear in the list of a photo’s properties.

It is the album or albums in which this photo is located.

Quick reminder, in Piwigo, a file can be located in multiple albums.

When editing a photo, click on the cross where the album's name is in order to remove it from this album.

To add the photo to another album, click on the "Add" button.

![Linked albums.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6d2c744f.jpg)

A window opens listing existing albums. It lists existing albums and allows you to search for the album of your choice. Click on + to add the photo to the chosen album. You can also create a new album by clicking on “Creation mode”.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-fc0d4b05.png)

Once you've made your album selection, you'll be taken back to the photo editing page. Don't forget to click on the “Save settings” button to save your changes!

To learn more about albums, [read this set of articles](../organizing-albums/index.md).

### Album thumbnail (album representative)

When editing a photo, this property shows the list of albums for which the current photo has been chosen as the main thumbnail.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-625b5c29.png)

If a photo is chosen to represent an album, it will be displayed in your gallery in the album list.

By default, the photo that Piwigo chooses to represent an album in the list is the first photo uploaded to the album, but you can very well change it if you want to.

Note that a photo doesn't need to be linked to an album in order to represent it.

To learn more about albums, [read this set of articles](../organizing-albums/index.md).

### Tags

To organize and describe your photos, you can link them to tags (which you can also call keywords, or labels).

Tags are displayed on the page of a photo in your gallery, the same way as properties, and they can be used to search for a photo that fits one or more criteria.

When editing a photo in the administration, the Tags field works the same way as the Album field, with one difference: if you enter the name of a tag that doesn't exist yet, you can create it on the fly by pressing the Enter key.

![Adding tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d58bf57c.jpg)

To learn more about tags, [read this set of articles](../tags-in-piwigo/index.md).

### Description

The Description property allows you to display a presentation text for your photo in your gallery.

Usually, the description is displayed below your photo in your gallery.

By default, the description is also displayed as a tooltip when you hover the mouse over the photo.

![Photo description.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-cd17604c.jpg)

If you are using the [Bootstrap Darkroom](../piwigo-themes/bootstrap-darkroom-theme-piwigo.md) theme, you can choose to display the photos' description instead of their title on an album's page.

To format your description's text (putting text in bold, adding a link...), you have two options.

- If you know the HTML language, you can insert HTML tags in your descriptions.
- You can also install the **FCKEditor** plugin, which adds a visual HTML editor to the Description field of the photo editor.

![FCKEditor.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b482ad9d.jpg)

To learn more about FCKEditor, [read this article](../administration-piwigo/plugins-for-administrators.md).

To be able to translate descriptions into multiple languages, use the **Extended Description** plugin. To learn more about content translation with Extended Description, [read this article](../customizing-your-gallery/managing-languages-available-gallery-piwigo.md).

### Who can see this photo (privacy level)

This property allows you to set a file's Privacy level.

By default, the privacy level is set to "Everybody": if the album is private, the photo will be shown to all users who are logged in and authorized to view the album.

![Privacy level.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0e6c29d2.jpg)

But you can set a more refined privacy level by selecting another option in the drop-down menu.

![Other privacy levels.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2737cf4d.png)

!!! warning "Warning :"
    This feature should not be mistaken for the permissions by album! This is an advanced feature of Piwigo that might be somewhat hard to understand.

To learn more about privacy levels, [read this article](../managing-users/privacy-levels.md).

### Displaying properties in your gallery

**Displaying properties with the Modus theme**

If you are using the [Modus](../piwigo-themes/modus-theme-piwigo.md) theme, the properties will be displayed in the section on the right of the photo.

![Description.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-151d7151.jpg)

**Displaying properties with the Bootstrap Darkroom theme**

If you are using the [Bootstrap Darkroom](../piwigo-themes/bootstrap-darkroom-theme-piwigo.md) theme, by default, the properties will be displayed under the photo, in the column on the right.

They can also be displayed in a tab or a side bar, depending on the option you chose in the theme's configuration.

![Darkroom theme.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-423ae635.jpg)

If you want to hide the properties with the Bootstrap Darkroom theme, you can do so via the theme's configuration, by choosing the "Picture info display position = Disabled" option.

**Showing / hiding the properties in the gallery**

If you want to choose which properties will be displayed and which ones won't next to each file in your gallery, go in the administration, in the Configuration > Options menu, then the "Display" tab, and the "Photo properties" section.

![Photo properties.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ec28a274.jpg)

To get access to further properties display options, you can use the **Manage Properties Photos** plugin (see next chapter).

## Customizing properties with plugins

### Manage Properties Photos: Customizing the properties

Do you want to add custom properties to your gallery, or even edit the display order of the existing properties?

To do this, you need to install the **Manage Properties Photos** plugin.

!!! info "If you are a Piwigo Cloud plan customer, this plugin is only available from the Enterprise plan and higher"

Once Manage Properties Photos is activated in your gallery, go in the plugin's configuration.

The Properties tab lists the existing properties and allows you to create a new one.

![Manage photo properties.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a47105d7.jpg)

This tab allows you to hide existing properties: you simply need to hover the mouse over a property to display the "Hide" option.

It is also possible to edit the display order of the properties on your gallery's Photo page, through drag-and-drop.

**Creating a new custom property**

To create a custom property, click on "Create new photo property".

![New photo property.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6ae92c9a.jpg)

The Label field allows you to choose the new property's name.

You also need to choose the type of property. Multiple types are available:

**Text:**

Choose the text type if your property's value is a free text (example: a noun, a city...).

**Select:**

Choose the select type if your property's value is a list of restrained options.

The Add field button allows you to add the available options for your property. In the example below, we have created a School property with 4 available values.

![Select property.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5c728505.jpg)

In a photo's editing page, administrators can choose the value of this property using a drop-down menu.

![School property.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-52cb3141.jpg)

**Radio:**

The Radio type works the same way as the Select type. It also allows you to choose the property's value from a predefined list, but the input is presented using a radio button rather than a drop-down list.

In the example below, we created an "Image rights" property with two options: yes and no.

![Radio property.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-206e119f.jpg)

**Date:**

The Date type is meant to be used for date type properties. It allows you to set the property's value from a calendar.

![Due date.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c13aa5be.jpg)

**EXIF and IPTC types:**

EXIF- and IPTC-type properties allow you to create a custom property that will retrieve the value of an EXIF or IPTC metadata.

To use this type of property, you first need to go into the plugin's Configuration tab. You need to choose a reference photo in your gallery that has EXIF or IPTC metadata, by entering its digital ID.

![EXIF IPTC.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f1ee4b64.jpg)

This will allow the plugin to load the list of EXIF and IPTC metadata available on your gallery.

![EXIF example.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-23c439de.jpg)

For example, you can create a Height property that will automatically retrieve the "Height" metadata's value that is saved within your photo; the height will be displayed on your gallery's photo page in pixels.

![Height value.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-52f485f1.jpg)

**Viewing the custom properties**

Once you have created a custom property, you can set its value for each photo in the "Additional properties" tab of the photo editor.

![Image rights.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-442b52a2.jpg)

Custom properties are also accessible from the batch manager, when you select a set of photos and you choose the "Change photo properties" option.

![Batch manager properties.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-97bdf9a6.jpg)

If you chose to display custom properties, they will be displayed among other properties in the gallery. Don't forget that the first tab of the Custom Properties' configuration allows you to edit the properties' display order and hide the ones you want to hide.

![Image rights yes.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-47514661.jpg)

**Manage Properties options**

The Manage Properties' Configuration tab offers multiple options that we are listing below.

![Manage properties configuration.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b5559618.jpg)

- **Adding a field to automatically delete photos at a certain date**

Click on this option to create a "Date"-type field, which, for each photo, will allow you to choose a date at which it will automatically be deleted

![Delete photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-fcd8f683.jpg)

- **Move description into info table**

Click on this option to display the photo's description among your gallery's properties. You will find the Description field in the property list of the plugin's configuration, and you will then be able to choose its display order.

![Description property.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-905437ee.jpg)

- **Showing the image’s ID**

Click on this option to display the digital ID of each file among properties in the gallery. This feature is also available with the **Show Photo Identifier** plugin.

- **Maximum number of fields for the "select" tags and the "radio" buttons**

Set the maximum number of values possible for the "drop-down list"- and "radio button"-type properties here.

- **The reference photo for the EXIF and IPTC metadata**

See previous chapter.

### Properties Mass Update: Updating the properties in bulk from a .csv file

Do you wish to update the properties of a set of photos from an existing table (an Excel file, for example)?

To do this, you need to install the **Properties Mass Update** plugin.

!!! info "If you are a Piwigo Cloud plan customer, this plugin is only available from the Enterprise plan and higher"

### Show Photo Identifier: Displaying the photo's identifier among properties

The **Show Photo Identifier** plugin allows you to display a photo's digital identifier on the photo's page, among its metadata and properties.

![Image ID.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2ca0d794.jpg)

### Download Counter: Displaying the number of downloads among properties

The **Download Counter** plugin allows you to count the number of downloads of a photo and to display it on the photo's page, among the photo's metadata and properties.

![Download counter.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-294cb0db.jpg)

### Expiry Date: Adding an expiry date to a file

Adding an expiring date to a file can be necessary, to manage a license's validity date, or even the validity of the image rights associated with a photo.

To do this, you need to install the **Expiry Date** plugin.

!!! info "If you are a Piwigo Cloud plan customer, this plugin is only available from the Enterprise plan and higher"

Once the plugin has been activated, a new "Expiry date" field appears on each photo, as well as in the batch manager.

![Expiry date empty.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-722d1d17.jpg)

The expiry date is displayed next to the other properties of your gallery.

![Expiry date.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-46807707.jpg)

If you want to hide the expiry date in the gallery, you need to use the **Manage Properties Photo** plugin (see above on this page).

But what happens when the expiry date is coming?

To set this, go in the Expiry Date plugin configuration.

![Expiry date configuration.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d7d99c2a.jpg)

You have multiple options:

- **Choosing what Piwigo needs to do when the photos are about to expire**

The Expiry Date plugin allows you to choose what happens when the expiry date is coming: do nothing, automatically delete the photos, automatically archive the photos.

Archiving the photos allows you to automatically move them to the album of your choice, which you will have created beforehand. This allows you to make the expired photos inaccessible without deleting them from your gallery.

![Archived photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2903a3ff.jpg)

- **Notifying users who have downloaded the photo**

Select this option to send an email notifying the users who downloaded a photo when it is expiring.

If you select this option, other choices appear.

![User notifications.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0c5881a2.jpg)

This way, you can send an email before the expiry date or only at the exact date, and add a custom message in the email sent.

- **Notifying the administrators when a photo has expired**

You can send an email to the administrators as soon as a photo's expiry date has come.

Just like the notifications to users, you can send an email before the expiry date or only at the exact date, and add a custom message in the email sent.

### Copyrights: Managing a file's copyrights

You may need to link a copyright to an image or a video, in order to specify the rights related to this file (usage, reproduction, distribution...).

To do this, you need to install the **Copyrights** plugin.

Once the plugin has been activated, a new "Copyright" property appears when editing a photo in the administration.

![Copyrights.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8a90932e.jpg)

If a value is chosen among the list of available copyrights, it will be displayed in your gallery with the other properties.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b486b74b.png)

By default, the plugin is installed with a predefined copyright list, but you can delete them, edit them, or create new ones in the Copyrights plugin's configuration.

![Create copyright.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b41d9515.jpg)

The description of a copyright is displayed when hovering the mouse over it in the gallery, and the link opens in a new tab when clicking on the copyright.

![CC BY.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ce81eb1d.jpg)

### Edit Filename: Editing a file's name

By default, in Piwigo's photo editor, you can edit the title of the medium when displayed in your gallery, but not the name of the source file.

If you need to do so, you must install the **Edit Filename** plugin.

Once this plugin is activated, the name of the source file can be edited through the photo's editing page.

![Edit Filename.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-632b69a5.jpg)
