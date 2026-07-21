# The Photo page in your gallery

As soon as you access a file (image or other) in the Piwigo gallery, from an album, a search, or any other method, you access the Photo page.

This page allows you to view a photo and its details, and perform a certain number of actions on this file.

In this article, we will see how the Photo page is structured, which features are available, and how you can customize it, as standard or with plugins.

!!! note "Note"
    Most of the screenshots presented in this article show a gallery that uses the Modus theme. Depending on your gallery's theme, the way the information is presented and the icons used are not necessarily the same.

## Structure of the Photo page

No matter the theme of your gallery, the Photo page always contains the same elements, in addition to the menu and the page footer which are displayed on every page:

- A breadcrumb trail, which allows you to see where this photo is located in the album tree, and browse this tree;
- A tool bar, with icons that allow you to perform some actions on the photo;
- Browsing arrows, allowing you to browse from picture to picture within the album;
- The photo's information (properties, metadata);
- The photo itself (with its description if applicable);
- A comment area (if comments are activated in the gallery).

You can see below how the Photo page is structured with the default theme (Modus).

![Page photo fini.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-fe68b5d6.jpg)

If you are using another theme, such as Bootstrap Darkroom, for example, the page's structure will be different, but the same elements will be present.

![Jolie petite maison.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9f7d9c10.jpg)

### Browsing with the arrows

On the Photo page, you are able to browse within a selection of photos thanks to arrow-shaped icons.

With the Modus theme, these arrows are displayed in the top right corner of the page.

![Flèches.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8206f097.jpg)

The photo selection depends on the path you took to access the photo:

- If you are coming from the Album page, the arrows allow you to see all the photos of the album;
- If you clicked on a tag, the arrows allow you to see all photos associated with the same tag;
- If you are coming from a search, the arrows allow you to browse within the search results;
- etc.

The left and right arrows allow you to view the next photo and the previous photo.

The upwards arrow allows you to go back to the previous page (album, tag, search, etc.).

### Properties and metadata

The Photo page shows some of your file's properties and metadata.

With the Modus theme, this section is displayed to the right of the photo.

![Description.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-fd9b02f9.jpg)

To learn more about the properties and metadata, and to learn:

- how to choose which ones to show or not to show in your gallery
- how to set the properties' display order
- how to show or not to show the metadata
- how to create custom properties
- etc

Read [the article about properties and metadata](../import-and-manage-photos/properties-metadata-photos-piwigo.md).

### Comments

If you activated the comments in your gallery, a comment section is displayed on the Photo page.

To learn more, read [the article about comment management](../comments-and-ratings/managing-comments.md).

### Available actions on a photo

The tool bar gives you access to various features. 

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-036c3e5c.png)

**Changing the photo size displayed**

The first icon allows you to choose the size of the photo displayed, among the sizes available in the gallery.

![Tailles photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-48bf7fe5.jpg)

To learn how to set the photo sizes available in the gallery, read the chapter about [Managing the file sizes available in your gallery.](the-photo-page-in-your-gallery.md)

**Starting a slideshow**

The "Play"-shaped icon allows you to start a fullscreen slideshow, which browses through the photos in your selection.

![Diaporama.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a372817c.jpg)

**Showing the metadata**

The camera-shaped icon allows you to show or hide your photo's metadata in the side panel of properties. Learn more about [displaying the metadata](../import-and-manage-photos/properties-metadata-photos-piwigo.md)

**Downloading the photo**

The floppy disk-shaped icon allows you to download the photo onto your computer.

By default, the downloaded photo is the original.

If you have activated the **Download by Size** plugin, the user needs to choose the size of the photo they are downloading beforehand.

![Télécharger tailles.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-44796342.jpg)

If the "Download" user permission is deactivated on your profile, the original version of the photo is not available. You only see the sizes that were made available on your gallery. This way, if you wish, you can only display low definition versions of your photos in your gallery.

If you want to deactivate the "Download" button completely in your gallery, go in the administration, in the Configuration > Options menu, then the Display tab, and the "Photo page" section, and uncheck the *Activate icon "Download this file”*  box.

**Add the photo to your favorites**

The heart-shaped icon allows you to add the photo to your favorites. You can find your favorites again in the Your favorites page available through the Explore menu (or Discover if you are using the Bootstrap Darkroom theme). [Learn more about favorites](manage-your-favorites.md)

**Choose the photo as the album thumbnail (administrators only)**

The trophy-shaped icon is only visible for the administrators. It allows them to choose the current photo to become the thumbnail that represents the album.

**Edit the photo (administrators only)**

The pen-shaped icon is only visible for the administrators. It allows them to access the editing screen for the current photo in Piwigo's administration.

**Add the photo to the caddie (administrators only)**

The cart-shaped icon is only visible for the administrators. It allows them to add the photo to their caddie. After that, the caddie is accessible in the administration to perform actions in bulk through the [batch manager](../import-and-manage-photos/batch-manager-piwigo.md).

## Managing the file sizes available in your gallery

To set the file sizes available in your gallery, go to the administration, in the Configuration > Options menu, then the Photo sizes tab.

By default, Piwigo offers multiple file sizes. In reality, Piwigo only imports the original file, but it can generate other sizes upon request from the users, depending on the sizes you will have activated.

![Tailles multiples.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-cf92d23b.jpg)

### What is the purpose of the different file sizes?

- The Square, Thumbnail and Medium sizes are used by Piwigo to display the photos in the gallery. This is why you can't deselect them.
- The other sizes can be deactivated by deselecting them. In your Piwigo gallery, the users will be able to choose the file size displayed on their screen among the available formats.

To learn more about the various formats, and possibly customize them, click on "show details" (on the right of the page). After that, for each format, you will be able to:

- See the size generated by Piwigo, by default;
- Customize this size by clicking on "edit" next to each format;
- Customize the image quality (95% by default);
- Restore the default values: this allows you to cancel the changes you previously made and go back to Piwigo's default settings;

![Montrer détails.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7aad7329.jpg)

### Why customize the available image sizes?

This can be useful for various needs.

Example: for your website, you have a standard photo size used on all the pages, that is 700 pixels wide. The same photos need to be 400 pixels wide in your newsletter.

You can customize the XS size by choosing a width of 400 px, and the S size by setting a width of 700 px.

This way, users in your photo library know that they must download download the S version of a photo for your website, and the XS version for your newsletter.

If you have activated the **Download by size** plugin in your gallery, the download button in your gallery will allow the user to choose the file size when downloading.

To customize the size of one of the file formats, you need to click on "show details" beforehand in the Configuration > Photo sizes page.

Across from the format you want to edit, click on "edit". You can then edit the maximum width and height of the chosen format.

![Modifier détails.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bc2fe3f8.jpg)

If you select "Crop", your file will automatically be "cut" by Piwigo to fit the chosen sizes.

!!! danger "By making this choice, you risk losing a part of your image."

Once you are done customizing the file sizes, don't forget to click on "Save Settings" to save your configuration.

## Options of the Photo page

### Actions and properties displayed on the Photo page

In Piwigo's administration, you can set which actions are available via the tool bar, which properties are displayed on the Photo page, and other customization options of this page.

To learn more, read the article about [your gallery's customization options](../customizing-your-gallery/customization-options-for-your-gallery.md).

For more information about customizing the display of properties and metadata, read the article about [properties and metadata](../import-and-manage-photos/properties-metadata-photos-piwigo.md).

### Add a watermark to your photos

When you upload a photo to Piwigo, Piwigo can automatically add a watermark, meaning an image that will be displayed "over" your photo.

**Why add a watermark to my photos?**

Adding a watermark to the photos in the gallery is useful when you want to protect your copyrights.

With a watermark, your photos will be visible in your gallery, but the original will not be available. This option is often used by photographers who want to showcase their work in their Piwigo gallery but want to protect themselves from an infringement of their copyright.

**How do I add a watermark to my photos?**

Go in the administration, and, in the left menu, click on Configuration > Options.

Next, click on the "Watermark" tab. This screen allows you to choose an image file that will be added to all photos in your gallery, and to setup a certain number of display options for this watermark.

![Filigrane.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9cdf5a09.jpg)

To see what this looks like, you can do the test with one of the files provided by Piwigo.

Next to "Select a file", choose Owned.png, for example. You can change the placement of the watermark (in the center of the image or in one of the corners of the image). For example, let's choose "bottom right corner".

![Filigrane owned.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-533bc214.jpg)

Save the settings: in your gallery, all photos are displayed with this watermark in the bottom right corner.

![Filigrane test.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-34ba3a9c.jpg)

Of course, you can add your own watermark.

For this, we recommend a PNG file on a transparent background.

## Customize the Photo page with plugins

Here is a selection of plugins that allow you to add features to the Photo page.

### Custom Download Link: Add a big download button

The Custom Download Link plugin adds a big download button on the Photo page.

![Bouton télécharger.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5f35d7ea.jpg)

This button allows you to directly download the original version of the photo. It's not displayed if the logged in user doesn't have the "Download" permission activated on their profile.

### Download by size: Choose the size of the downloaded file

We have already talked about it earlier in this article: the **Download by Size** plugin allows you to give users the option to choose the size of the downloaded photo when clicking on the "Download" icon. 

![Télécharger tailles.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-44796342.jpg)

### Private Share: Share a photo with a secure link through email

The Private Share plugin allows authorized users to generate a share link for a photo and send it via email. What is really useful about this plugin, is that it allows you to share a photo located in a private album, even with people who don't have a Piwigo account.

Once this plugin has been activated, you first need to set which users are allowed to use it. To do this, go to the plugin's configuration. The first tab allows you to set which user groups are allowed to use it. [Learn more about user groups](../managing-users/user-groups.md)

![Partage privé.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7a18ccbb.jpg)

The authorized users will see a "Share" icon on each photo in your Piwigo gallery.

![private-share.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0613b9fa.png)

If you click on this icon, a window appears. It allows you to enter the email address you want the photo to be sent to, and how long the link is valid (1 week, 2 weeks, 1 month, or 3 months).

![Partager cette photo.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7e0d92f6.jpg)

The recipient receives a link allowing them to view the photo.

![Envoi de photo.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7ba56cdf.jpg)

The link generated is perfectly secure and only gives access to this photo: the recipient has no way to access the rest of the gallery.

![Partage photo.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e54ff42e.jpg)

At any moment, through the plugin's configuration (Activity tab), the administrators can check Private Share's usage history: they can see the links shared, the recipients, the share and expiry dates, and choose to make the share link expire if needed.

![Liens envoyés.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0028a962.jpg)

### Loupe: Being able to zoom on a photo

The **Loupe** plugin allows users to extend or zoom in on a detail of a photo by hovering the mouse over it.

Once this plugin has been activated, when the user hovers their mouse over a photo, the pointer turns into a magnifying glass. You can zoom in and out using the mouse's scroll wheel.

![Loupe.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bde6ce16.jpg)

### Social Buttons: Add social media sharing buttons

The Social Buttons plugin lets you display buttons on your Photo page to share it on social media. 

![Social buttons.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-507e15f1.jpg)

For an optimal display, here are the options we recommend you use in the Configuration page for the Social Buttons plugin.

- Buttons position on picture page: Top or Bottom
- Display buttons: only on photo
- Shared picture size: we recommend not to share the original but a smaller size format
- Light mode: On (if you turn off light mode, cookies will be installed on your users' computer to activate their tracking by the platforms. Moreover, light mode is more elegant).

![Social buttons paramètres.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0e95eaba.jpg)

!!! info "Info :"
    If you are using the Bootstrap Darkroom theme, you don't need to use this plugin, since the theme already includes buttons to share to social media.

### Back2Front: Handle double-sided images

On the Photo page, the **Back2Front** plugin lets you display an alternative version of the same photo; it is generally used for double-sided images.

For example, it has been used for postcard or trading card galleries.

When the plugin is activated, on a photo's editing page in the administration, you can set whether this image is the back of another image (the front) while specifying the ID of the front. You can choose whether the back needs to be hidden in the album.

![Recto verso.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f1c307b0.jpg)

When a back side has been selected for a photo, a "See back" button appears on the Photo page. When clicking this button, the image that corresponds to the back side is then displayed.

![Verso.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-692be821.jpg)

### AlwaysShowMetadata: Always show the files' metadata

By default, the metadata are hidden on your gallery's Photo page: you must click on an icon to show them.

If you want them to always be displayed, install the **AlwaysShowMetadata** plugin.

To learn more about metadata, [read this article](../import-and-manage-photos/properties-metadata-photos-piwigo.md).

### RightClick: Block the right click on the Photo page

If you want to prevent users from performing a right click on a photo to download it, you can install the **rightClick** plugin.

Once this plugin has been activated, the right click will be ineffective on the Photo page, but also on other pages, except for administrators.

!!! warning "Warning :"
    This plugin doesn't guarantee that your images are totally secure. Only setting your albums to private mode protects your photos.

### Hide title: Hide the photo's name in the breadcrumb trail

By default, the breadcrumb trail displayed on the Photo page shows the photo's name.

![Titre.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c8fa5581.jpg)

To hide it, simply activate the **Hide Title on Browse Path** plugin.

![Sans titre.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4f6f1c97.jpg)

### Automatic size: Automatic file size depending on the screen size

The Automatic Size plugin lets you adapt the default file size displayed based on the user's screen size. It was made for galleries that use the **Elegant** theme.

This plugin **isn't useful if your gallery is using the Modus theme**, since Modus already handles the automatic display of the size that fits your screen's resolution by default.

Furthermore, this plugin isn't compatible with the **Bootstrap Darkroom** theme.

### Color Palette: Extract the photo's colors

The Color Palette plugin lets you automatically extract a photo's colors and search photos by color.

Once this plugin has been activated, you will find the palette of colors found in the photo for each photo in your gallery.

![Palette écran complet.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b2cd7de3.jpg)

By clicking on one or more colors of the palette, you can search for all photos of your gallery that contain the same colors.

![Palette.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2222c058.jpg)

![Recherche palette.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d926b5ba.jpg)

The plugin's configuration page lets you set up some options, such as the number of colors extracted per palette.

![Palette config.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7830d4e6.jpg)

!!! warning "Warning :"
    Activating the plugin doesn't generate palettes on every image of your photo library. A photo's palette is generated when it is displayed for the first time after activating the plugin. At first, the search by color will then yield very few results since your photos' palettes will not have been generated yet.
