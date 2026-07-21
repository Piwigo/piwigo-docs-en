# SmartAlbums

You can create "smart" albums, automatically fed by photos that fit certain criteria.

To do this, you need to install the **SmartAlbums** plugin.

!!! info "If you are a Piwigo Cloud customer, this plugin is only available from the Enterprise plan and higher."

Once the plugin has been activated, go to its configuration page.

## Creating a SmartAlbum

The first tab lists SmartAlbums and lets you create a new one. A SmartAlbum can be added at the root of your gallery or inside of a parent album.

![SmartAlbums.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4c6e0d44.jpg)

Once the SmartAlbum has been created, you can set the criteria that define its content.

To do this, choose a filter among the available criteria: tags, date, album, name, dimensions, author, number of views, etc.

For example, we will create an album filled by all photos associated with the "dog" tag. One click on the "Count" button lets you know the number of photos affected.

![SmartAlbum chien.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-009a18c7.jpg)

You can combine multiple filters and choose:

- Whether the photos need to fit all filters in order to join the Smart Album,
- Or if they need to fit at least one filter.

Once your filters have been set, click on "Save" to save your SmartAlbum.

## Managing the SmartAlbums

The albums created this way are visible in the list of albums just like any other album. You can edit the filters by editing the album and going in the "SmartAlbum" tab.

![Modifier album chien.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-80922515.jpg)

Let's go back to the configuration of the SmartAlbums plugin.

The SmartAlbums created can be seen in the list.

![SmartAlbum éclair.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-713522c7.jpg)

At any moment, you can regenerate the photos in the SmartAlbums, either in every album, or choose for each album. Regenerating the photos lets you update the content of a SmartAlbum.

## SmartAlbums configuration

The Configuration tab lets you choose some settings.

![SmartAlbum configuration.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6cde2b5a.jpg)

- **SmartAlbums update frequency**: SmartAlbums aren't updated in real time. If you just imported new photos, they will not come to fill a SmartAlbum immediately, except if you "force" the update by using the SmartAlbums' regeneration feature. By default, SmartAlbums are updated every 3 days but you can customize this setting.
- **Updating the albums after importing a file**: if you want SmartAlbums to be regenerated automatically after every new upload, select this option, but beware: this may slow your gallery down, especially if you have a lot of content.
- E**xcluding SmartAlbums from access rights management**: in this case, SmartAlbums are considered to be private for everyone, and a user can only see their content when it is available in another album they have access to.
