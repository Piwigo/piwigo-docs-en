# Albums in your gallery

In a Piwigo gallery, it is most common to browse using albums. As a reminder, in Piwigo, a photo has to be located in an album, which can be considered as a directory or a category.

Albums are organized like trees and they can contain sub-albums, which can contain sub-albums themselves, etc.

As soon as you click on an album in your gallery, you will access the Album page.

In this article, we will discover how to browse the albums, how the Album page is structured, which features are available, and what customization options are available, as standard or with plugins.

!!! note "Note"
  Most of the screenshots presented in this article show a gallery that uses the Modus theme. The way the information and the icons are displayed might not be the same depending on the theme your gallery uses.

To learn more about the albums, read this set of articles:

[Organizing albums](../organizing-albums/index.md)

## Preamble

In your gallery, the different pages that are listing photos (search results, list of photos associated with a tag, "My photos" page or "Most visited" page...) are all displayed the same way as the Album page.

Overall, this means that the features on the Album page are the same as the other pages that list photos.

![Album page](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-49b0922b.jpg)

Album page

![Tag page](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-00ec7d64.jpg)

Tag page

![Search results page](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f44e9417.jpg)

Search results page

## The albums in your gallery

When landing on your gallery's home page, you can view the list of first-level albums (root albums).

![Albums.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5b1f1709.jpg)

The albums that appear are:

- All the public albums
- All the private albums you are allowed to view, if you are logged in. [Learn more about permissions](../organizing-albums/permissions-and-album-visibility.md)

!!! info "Info :"
    By default, the home page displays 12 albums per page. You can browse your albums using the page links at the bottom of the page. If you want to change the number of albums shown per page, go in the administration, then Configuration > Options, in the Display tab.


By clicking on an album, you enter the Album's page.

Its content is different depending on the album's content: it either contains photos directly (or other files), or sub-albums.

!!! info "Info :"
    To understand the concept of albums and sub-albums, [read this article](../organizing-albums/albums-and-sub-albums-piwigo.md). An album may contain both sub-albums and files, but we don't recommend this.

## Album with sub-albums

If the album contains sub-albums, then the root album's page displays the thumbnails of these sub-albums, and so on.

The browsing path (or breadcrumb trail) in the top left corner allows you to view where you are in the tree.

![Example: an album “Buildings” with two sub-albums “Churches” and “Houses”](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-fab9f046.jpg)

Example: an album “Buildings” with two sub-albums “Churches” and “Houses”

The tool bar offers several possible actions, depending on your user rights, your theme, and depending on your gallery's settings. 

Among other things, you can display all of the album's files (all sub-albums combined), by clicking on the appropriate icon (it is different depending on your theme). You can go back to the default display by clicking on the tree diagram-shaped icon.

## Photo display on the Album page

If the album doesn't contain sub-albums, but only photos, the album page displays the thumbnail for the album's photos.

If you have a lot of files in this album, page links will appear at the bottom, allowing you to browse within your album.

![Pagination.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-41c3c554.jpg)

If you want to display all the photos on the album page, you can activate the **RV Thumb Scroller** plugin. This plugin progressively loads the photos as the user scrolls through the page. 

!!! info "Info :"
    To change the number of photos displayed on an album page, go to your [user preferences](../managing-users/creating-and-managing-users.md); you can access them by clicking on the "Customize" menu in the gallery, or by editing your user profile in the administration.

## The Album page tool bar

The tool bar gives you access to multiple features.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6b027860.png)

!!! note "Note"
    The icons and features available on your gallery depend on the theme you have chosen, on Piwigo's configuration, on the plugins activated... The examples displayed on this page show the default possibilities of the [Modus](../piwigo-themes/modus-theme-piwigo.md) theme. If you are using the [Bootstrap Darkroom](../piwigo-themes/bootstrap-darkroom-theme-piwigo.md) theme, for example, the features available are generally the same, but the icons are slightly different.

### Changing the photos' sort order

You can change the default sort order by clicking on the "Sorting" icon: this way, you can sort your photos by date posted, by alphabetical order, by number of visits…

![Ordre de tru.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1e01d25d.jpg)

!!! info "Info :" To change the default sort order, go in the administration, in the Configuration > Options menu.

### Changing the size of the photos shown

To change the size of the thumbnails displayed on the screen, you can click on the "Size" icon.

![Tailles de photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-814fc23e.jpg)

Example of a display with the "Thumbnail" size:

![Taille miniature.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-000dc2e6.jpg)

### Add to caddie (administrators only)

If you are an administrator, the cart-shaped icon allows you to add all the photos in the album into your caddie. You will then find this caddie in the administration, and you will be able to perform actions on these photos, through the [batch manager](../import-and-manage-photos/batch-manager-piwigo.md).

### Edit album (administrators only)

If you are an administrator, the tool-shaped icon allows you to go to the administration to [edit the album](../organizing-albums/editing-an-album.md).

### Displaying the photos in Calendar mode

If you want to display the photos according to their upload date, click on the Calendar-shaped icon. You will then be able to filter your photos based on the year and month they were added to Piwigo.

![Date de publication.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-01c39b75.jpg)

If you click on the camera-shaped icon, you will be able to filter the photos based on their creation date (and not the date they were added to Piwigo).

![Date de création.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-56fff16b.jpg)

To go back to the normal view, click on the tree diagram-shaped icon.

### Starting a slideshow

Clicking on the "Play" icon in the tool bar allows you to start a full-screen slideshow.

![Diaporama.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a372817c.jpg)

### Album description

When you edit an album in the administration, you can choose to enter a description for said album.

It will be displayed on the album page and on the list of albums (depending on the themes and their configuration).

If you are using the Modus theme, the description will be displayed at the top of the Album page by default.

![Description album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5dc7059e.jpg)

## Options of the Album page

### Setting the actions available in the Album page

You can customize the way some features are displayed on the album page through the Configuration > Options menu in Piwigo's administration.

In the "Display" tab, you can customize the actions available via the tool bar on the Album page.

- Activate icon “Sort order”
- Activate icon “Display all photos in all sub-albums”
- Activate icon “Display a calendar by posted date”
- Activate icon “Display a calendar by creation date”
- Activate icon “Slideshow”
- Activate icon “Photo sizes”
- Activate icon “Edit album” (available for administrators only)
- Activate icon “Add to caddie” (available for administrators only)

![Affichage.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b38cee21.jpg)

### Options related to themes

Depending on the theme your gallery uses, you have access to other formatting options for your Album page.

Visit your theme's documentation to learn more:

- [Modus documentation](../piwigo-themes/modus-theme-piwigo.md)
- [Bootstrap Darkroom documentation](../piwigo-themes/bootstrap-darkroom-theme-piwigo.md)

### Changing the number of photos shown on the Album page

By default, Piwigo shows 15 thumbnails on an album's page, but you can show more (or fewer).

To change the number of photos shown on an album page, go to your user preferences; you can access them by clicking on the "Customize" menu in the gallery, or by editing your user profile in the administration.

[Learn more about preferences](../managing-users/creating-and-managing-users.md)

## Customizing the Album page with plugins

### Comments on albums: Displaying comments on the albums

By default, Piwigo lets users of your gallery post [comments](../comments-and-ratings/plugins-comments-management-piwigo.md) on photos, but not on albums.

If you want to activate this option, simply activate the **Comments on Albums** plugin.

[Learn more](../comments-and-ratings/plugins-comments-management-piwigo.md)

### Batch Downloader: Download all the files of an album (or a selection) in zip format

The **Batch Downloader** plugin allows authorized users to download a .zip file containing a batch of files in one click. It can be done from an album's page, among other methods.

Once the plugin has been activated, a new icon will appear in the tool bar of an album's page. This icon will allow you to download all files in the selection.

![Télécharger toutes les photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-766e8b93.jpg)

This icon will not only be available from an album's page, but on any page that lists photos:

- Search results
- List of photos linked to one or more tags
- "My favorites" page
- etc.

One click on the icon allows you to choose the size of the downloaded photos, based on the photo sizes available in your gallery.

![Téléchargement.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e568972c.jpg)

Once the size has been chosen, the download starts.

The user can find the history of downloaded files at any moment from the "Downloads" menu that appeared in the gallery.

This page summarizes the downloaded files, allows you to cancel the download, and to download the file on your computer by clicking on the "Archive (ready)" link.

![Archive prête.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-56875108.jpg)

The Batch Downloader plugin settings give you access to a page with two tabs:

**History**

This page shows the history of downloads via the Batch Downloader plugin. This way, you can see:

- the user who requested the download
- the downloaded batch
- the date
- the size
- the number of photos
- the status

![Téléchargement masse.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0f8b9a69.jpg)

**Configuration**

The configuration tab allows you to manage the options available in your gallery with precision.

![Config téléchargement masse.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-49bb67a4.jpg)

- Who can download photos in a batch
- What type of set of photo can be downloaded (albums only, or "Special" pages as well (Most Visited, Best rated...))
- The photo size allowed for downloads

You can also set rules for the amount of time that archives will be stored on the server, for the maximum number of photos per batch, for the maximum size of each archive…

The advanced features list the options that can be edited through Piwigo's configuration file.

You can edit them using [LocalFile Editor](../self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md) if you are working on a self-hosted Piwigo gallery; if you are a piwigo.com plan customer, reach out to support to edit one of these settings.

### ShareAlbum: Share a security link to an album

The **ShareAlbum** plugin allows authorized users to generate a share link to this album. What's really useful about this plugin, is that it allows you to share the content of a private album, even with people who don't have a Piwigo account.

Once this plugin has been activated, you will find a "Share" icon on each album in your Piwigo gallery.

![sharealbum.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8fb407d2.png)

If you click on this icon, a "Share this album" button appears.

![sharealbum.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-23bfb0b4.png)

Once the album has been shared, click on the icon again to view the share link.

![Sharealbum lien.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-46564762.jpg)

Once you don't need it anymore, you can cancel the share link: it will then not be accessible anymore.

You can also click on "Renew link" to generate a new link (the link generated previously will not be accessible anymore).

If you are using Piwigo as part of a company, this is very useful when you occasionally need to share an album's content with a person who is not part of your organization (a client, a partner, a journalist...).

The ShareAlbum plugin configuration gives you access to two tabs:

**Configuration tab**

This tab gives you access to the configuration options for ShareAlbum.

- Hide menus for album visitors: if this option is activated, the share link will only display the album's contents, without the browsing menu at the top of the screen. If you activate this option, you can choose whether or not to display a login menu on the shared page.
- Activate the auto-login
- Replace navigation breadcrumbs with album name: allows you to hide the album's tree
- Apply shares to sub-albums: allows you to set whether or not sharing an album also gives access to its sub-albums
- Enable non-admin power users to share albums: allows you to give permission to non-admin users to create share links

![Sharealbum.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d9f770d4.jpg)

**Shared Albums tab**

The second tab allows you to see the history of share links generated by the ShareAlbum plugin. You can see who created links, the number of times these links were visited, the associated album, renew and delete existing share links.

You can also create share links from this screen, without going through your gallery.

![Albums partagés.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7d51229c.jpg)

### GThumb+: Display a patchwork of thumbnails

By default, the thumbnails are displayed in a grid shape on the Album pages and the other pages that list photos in your gallery; all thumbnails have the same height.

The GThumb+ plugin allows you to display them in the form of a patchwork with varying heights.

![Default display](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-df0b6b3a.jpg)

Default display

![Gthumb+ display](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-712ffb35.jpg)

Gthumb+ display

The plugin's configuration allows you to customize the default options, such as:

- Maximum height of thumbnails
- Margin between thumbnails
- Number of thumbnails per page
- etc.

### Image Preview: Enlarge thumbnails on mousehover

The **Image Preview** plugin allows you to expand photos' thumbnails when hovering the mouse over them, from the Album page or any other listing page in the gallery.

![Miniature.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-dff2e378.jpg)

The plugin's configuration allows you to set the size of the image displayed (by default: maximum of 400px in width and 600 px in height).

You can also choose whether or not to display the image's name, to apply a transparency effect when hovering over it, and to preload the images (not recommended for performance reasons).

!!! warning "Warning :"
    If you are using the Modus theme, you first need to activate the **GThumb+** plugin in order to use the Image Preview plugin (see previous chapter).

### Lightbox: Display the photo in a pop-in window instead of the Photo page

By default, when you click on a photo in an album, you are redirected to the photo's page.

The Lightbox plugin changes Piwigo's behavior: once you have activated it, when clicking on a photo, it is displayed in a pop-in window (modal pop-up) over the Album page, as you can see in the example below.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0068cdc1.png)

Arrows allow you to browse within the album.

The plugin's configuration options allow you to customize some settings:

- Whether or not to display the image's title
- Allowing people to access the photo page by clicking on the image's title
- Whether or not to display the browsing arrows
- Customizing the lightbox's look (dark or light background...)
- Lightbox dimensions

### Permalink Generator: Customize an Album page's URL

By default, when you create a new album, called "Shooting", for example, its URL (web address) takes the following form: mypiwigo.com/index?/category/XX_shooting (XX being this album's ID in Piwigo's database)

If you edit the album's name, its URL will also change.

The **Permalinks Generator** plugin allows you to generate unique URLs for your albums, which will remain valid even if you edit their name.

Once the plugin has been activated, go into its configuration and click on "Generate missing permalinks". You will see that your albums' URLs have changed and now have the following format: mypiwigo.com/index?/category/shooting. 

If you edit the album's name, the URL will stay the same.

### Quick Fav: Add a photo to your favorites from the Album page

With Piwigo, it is possible for each user to add a photo to their favorites to find it again later. By default, this can only be done from a photo page.

The **Quick Fav** plugin allows you to add a photo with only one click from its thumbnail, on the Album page or another listing page.

!!! warning "Warning :"
    For now, this plugin is only compatible with the Bootstrap Darkroom theme. Furthermore, it is only accessible to [piwigo.com](http://piwigo.com/) customers (this will be fixed soon).

Once this plugin has been activated, a heart appears when hovering the mouse over a photo: a click on this heart adds the photo to the user's favorites.

![Quick fav 2.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-106deb84.jpg)

When hovering the mouse over a favorite, the heart appears as filled. Click on it again to remove the photo from your favorites.

![Favori.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-22b2178f.jpg)

**Add an entire album to your favorites with Quick Fav**

With the **Quick Fav** plugin, it is also possible to add an entire album to your favorites.

From an album-listing page, you will see the same icon appear as on a list of photos, which allows you to add the content of an album to your favorites in one click.

![Album fav.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7951755d.jpg)

### Thumbnail Tooltip: Customize the tooltip shown on a photo's thumbnail

When hovering the mouse over a photo on an album's page, some information about the photo is shown in a tooltip (title, number of visits...).

Customizing the content of this tooltip is possible using the **Thumbnail Tooltip** plugin.

!!! warning "Warning :"
  The Modus theme doesn't display a tooltip on the Album page. Due to this, the Thumbnail Tooltip plugin isn't compatible with Modus.

Once the plugin has been activated, go into its configuration to set what you want to display in the tooltip, and which order to display it in.

![TT.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6af3607c.jpg)

![TT example.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-531023f7.jpg)

### RV Thumb Scroller: Infinite scroll on the Album page

The **RV Thumb Scroller** plugin allows you to turn off page links on the Album page.

If you activate it, the photo's thumbnails will progressively load when scrolling on the page, no matter the number of photos in the album.
