---
title: Modifying or deleting photos - Piwigo Documentation
description: How to edit a photo in Piwigo? How can administrators modify or delete an existing file?
---

# Modifying or deleting photos

As a Piwigo administrator, you may need to modify an image or any other file type at any time.

If you are trying to modify a specific file, the easiest way is through your gallery!

Once you are on your photo's page, click on the pen-shaped button in the tool bar.

![edit-photo.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c6929531.png)

!!! info "Info :"
    Depending on your theme, the button will not always appear in the same place. If you are the administrator and you don't see the edit button in your gallery, it means that this button was hidden. To display it, go in Piwigo's administration, into Configuration > Options, in the "Display" tab, then the "Photo page" section, and select "Activate icon "Edit photo"". [Learn more about Piwigo's configuration](../customizing-your-gallery/customization-options-for-your-gallery.md)

The photo editing page will then open, which will allow you to edit its properties.

!!! info "You can also modify a photo from the administration, namely from the [batch management](batch-manager-piwigo.md) screen."

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ee638764.png)

## Preview, download, delete, synchronize the metadata

When you are in administration, on the photo editing page, a thumbnail of your file appears on the left.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-985955e0.png)

Several actions can be performed from this section:

- Enlarge photo: click on the “enlarge” icon.
- Display the photo in your gallery: to do this, move the mouse over the image and click on the “open in gallery” button; the page for this photo in your gallery will be displayed in a new tab.
- Download photo: click on the 2nd icon with the arrow; the original file will be downloaded to your computer
- View the history of visits to this photo: click on the graph icon;
- Synchronize the metadata: to do this, 4th on the third icon, with two arrows; this is only useful if changes have been made in the metadata's configuration. [Learn more about metadata](properties-metadata-photos-piwigo.md)
- Delete photo: click on the 5th icon representing a trash can.

## Your file’s metadata

In the top right corner of the photo editor, some of your file's metadata are displayed (file name, file size and weight, file format), as well as details that can't be edited from this screen (upload date, upload user, number of views...).

![File metadata.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b873a50a.jpg)

Metadata is information associated with your photos and automatically retrieved from the source file's metadata (to find out more, read the article about [properties and metadata](properties-metadata-photos-piwigo.md)).

## Modifying your file’s properties

On the right part of the screen, your file's properties are shown, which you can edit: title, description, author, creation date…

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4c7c49b8.png)

!!! warning "Don't forget to click on the "Save Settings" button to save your changes!"

To learn more about your files' properties, their role, understand why and how to edit them, and discover advanced options, read the [Managing your files' properties and metadata](properties-metadata-photos-piwigo.md) article.

## Changing a photo’s center of interest

A photo's editing page contains a second tab: **Center of interest**.

This tab allows you to determine the most important part of your photo, which will be showcased when the photo is resized, in square format, for example.

At the top of the page, you can see what your photo looks like once resized in square format, and the original below.

Sometimes, the square format is not suitable because Piwigo automatically crops an important part of your image. In the example below, we don't want the photo to be cropped at the bottom.

![Center of interest.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-492ee557.jpg)

To edit the center of interest, on the photo shown below the thumbnail, select the most interesting part of your photo using your mouse, then click on Submit.

![Crop.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-eda08564.jpg)

The square format is updated according to your changes.

This is especially useful if your gallery displays photo thumbnails in a different format than usual, for example in landscape format when the original photo is in portrait format. For example, this is the case with the [Bootstrap Darkroom](../piwigo-themes/bootstrap-darkroom-theme-piwigo.md) theme.

## Photo Update: replacing a file without modifying its properties

From the photo editing screen, you can re-upload a file to replace the original file, all while maintaining the photo's properties.

To do this, you need to install the **Photo Update** plugin.

Once the plugin is activated, a new "Update" tab is added to the photo editing screen. This tab allows you to import a new file to replace the existing file.

![Plugin Photo Update.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b1a77acc.jpg)

It can also be used to update the image representing a non-image file (video, audio, document, etc.).

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-adb35d74.png)

## Rotate Image: Rotating an image

From the photo editing screen, you can rotate an image if it's not facing the right way.

To do this, you need to install the **Rotate Image** plugin.

Once this plugin is activated, a new "Rotate" tab is added to the photo editing screen.

![Plugin Rotate Image.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e216d6fb.jpg)
