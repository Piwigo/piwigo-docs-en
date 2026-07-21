# Editing an album

## Editing an album from the administration

To edit an album in Piwigo's administration, go to the album list from the Albums > Manage menu.

From the album list, click on the "Edit album" icon in the list. A new page opens: the album editor page.

![Modifier album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5ee23170.jpg)

## Editing an album from your gallery

You can also edit an album from your gallery if you are an administrator.

To do this, go to the album's page and click on the "Edit album" icon.

Depending on your theme, this icon could take the form of a wrench or even a pen. You will be redirected to the album editing window in the administration.

## Viewing and editing an album's properties

The editing screen of an album gives you many possibilities.

!!! abstract "The screenshots below show the new version of the album editor, available from Piwigo version 14"

Let's start by looking into the first "Properties" tab.

![Edition album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e958fd3f.jpg)

### Viewing the album’s information

The screen shows information about your album.

In the page's header, you can find the album's name and, on the left, its place in the tree, as well as the album's ID (unique identifier) on the right.

Next, you can view information about the album: date of creation, of latest edit, number of photos, number of sub-albums.

### Editing the album's properties

The Properties tab lets you modify various details about your album.

- Editing your album’s name
- Editing your album’s description

If you add a description to your album, it will appear above your album's photos in your gallery, like in the example below.

![Description album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5dc7059e.jpg)

- Adding or editing a parent album for your album

This way, you can move an album inside of another album, thus making it a sub-album or, conversely, move an album "to the root" of your gallery.

- Editing the album's thumbnail (album representative)

When you edit an album in the administration, you can edit the thumbnail associated with an album in your gallery, by hovering the mouse over the image and clicking on "change thumbnail". Piwigo will go through the list of photos in this album, until you find the one that's right for you.

If you want a particular photo to represent your album, you need to edit this photo in the administration, and choose the album it represents using the "Album thumbnail" field. [Learn more](../import-and-manage-photos/properties-metadata-photos-piwigo.md)

You can also, from your gallery, choose a photo and click on the “set as album thumbnail” icon on the photo page.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a52d2e09.png)

### Allowing or blocking comments

At the bottom of the album editing screen, you can allow or block comments for the photos located in this album.

To manage comments in sub-albums, click on the icon which represents 3 dots in the top right corner.

![Commentaires sous albums.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-15baa234.jpg)

[Learn more about comments](../comments-and-ratings/managing-comments.md)

### Other actions available in the album

From the tool bar on the right, you have access to multiple options.

![Gérer photos album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e301da89.jpg)

- Manage album photos: this icon lets you edit photos from your album in batches. [Learn more about batch management](../import-and-manage-photos/batch-manager-piwigo.md)
- Add photos: this icon lets you add new files in your album
- Manage sub-albums: this icon brings you to the album list, if you need to edit the sub-albums located in your album
- Delete album: this icon allows you, as you wish, to delete the album and its content, or to only delete the album (the photos it contains will then be considered "orphans" in Piwigo).

Lastly, to open your album directly in the gallery, click on the "Open in gallery" button in the bottom right corner.

### Locking an album

At the bottom of the album editor screen, you have the option to lock an album.

!!! info "Info :"
    A locked album is inaccessible from the gallery, except for administrators. Most often, the locked status is used when an album is not yet ready to be made public in the gallery, because an administrator is working on it (preparation before publishing, maintenance...). This is therefore a "working", temporary status.

You can also lock / unlock a list of albums from the Albums > Properties > Lock menu.

## Changing the order of photos in an album

When you edit an album, the second tab, "Photos sort order", lets you edit the order of photos as they are displayed in your album.

!!! info "Info :"
    By default, Piwigo sorts photos in the following way: by upload date (from newest to oldest), THEN by file name (from A to Z), THEN by ID (from smallest to biggest). You can edit this setting in Piwigo's configuration options. [Learn more](../customizing-your-gallery/customization-options-for-your-gallery.md)

### Manually editing the order of photos

The first "Manual order" section lets you reorganize the order of photos as you wish, through drag-and-drop. Click on a photo and keep clicking: by moving the mouse, you can move the photo wherever you want. Release the click when your photo is in the right spot.

![Ordre des photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-31b42ab6.jpg)

### Automatically editing the order of photos

The second "Sort order" section lets you edit the photos' sort order automatically.

![Ordre de tri.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e2301eb2.jpg)

You have 3 options:

- Use the default photo sort order: this is the sort order that is applied when nothing has been modified. In this case, the photos are displayed by the date and hour they were uploaded to Piwigo.
- Manual order: if you have already edited the order of photos in your album manually, this option is automatically selected.
- Automatic order: if you choose this option, you will be able to choose to apply an automatic sort order among many options, as shown by the image below.
    
    ![Liste ordres.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2e36ecbd.jpg)
    
    If you want to, you can combine multiple options, for example: sorting photos by upload date (from oldest to newest), THEN by file name (from A to Z).
    

![Ordres combinés.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-fc9057f9.jpg)

Don't forget to click on Save Settings to save your choices!

The chosen sort order can be applied to sub-albums (if your album has any) by checking the box next to the save button.

### Reset Manual Order

Do you want to sort photos within an album by choosing an automatic sort order, but apply changes to it? To do this, you can activate the **Reset Manual Order** plugin.

This plugin adds an option to "Reset manual order with current automatic order". This applies an automatic sort order to your album, which you can then perform changes on manually.

## Editing permissions on an album

The third tab in the album editor is, without a doubt, the most important: indeed, it lets you decide who is allowed to view this album and its content in your gallery!

![Permissions.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-37a2ed66.jpg)

To learn everything about managing permissions on albums, read the following article:

[Permissions and album visibility](permissions-and-album-visibility.md)

## Sending a notification on an album

The Notification tab lets you send an email containing a link to the album to one or more users, or even all users of a group.

![Notif album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6dafd56c.jpg)

The people involved will receive an email containing a link to the album, along with your message.

![Mail album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f7bfa0ea.jpg)

!!! warning "Warning :"
    Before sending a notification, remember to make sure that the users have access to this album in the Permissions tab.

Article summary

---

← Previous

[Managing your albums](managing-your-albums.md)

Next →
