# Tags in your gallery

**How can you use tags in your Piwigo gallery? Which display options are available to you? Here is where we explain everything!**

To learn more about tags, read these articles as well:

[Tags: introduction](../tags-in-piwigo/tags-introduction.md)

[Creating and managing tags](../tags-in-piwigo/creating-and-managing-tags.md)

[Tag Recognition: Tag your photos automatically with AI](../tags-in-piwigo/tag-recognition-plugin-piwigo.md)

## Using tags in your gallery

By default, Piwigo galleries come installed with two menu items for your tags: Tags and Related tags.

### Related tags

![Tags.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-80528e77.png)

On the home page, the menu shows the list of your gallery's main tags. Clicking on a tag lets you see all photos associated with this tag.

![Tag espagne.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-fca9d8a7.jpg)

If you then click on the "Related tags" menu once again, it only shows the tags associated with the photos shown; you can then click on a new tag: both tags are combined to refine the search.

![Combinaison tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6106a105.jpg)

To remove a tag from the search filters, you simply need to click on the cross next to its label.

When you click on "Related tags" from an album's page, only the list of tags that are in this album is shown.

**This way, the Related tags menu is a very useful tool to explore your photo library and refine a search as you go along.**

### Tags (tag clouds)

The "Tags" submenu under "Explore" shows the number of tags that are in your gallery and lets you open a page that lists all your tags.

![Explorer tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-03cc8243.jpg)

The opened Tags page shows tags in the form of a word cloud, with the size of each tag being proportional to the number of photos it appears on.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-36106dc5.png)

Clicking on a tag shows all photos associated with this tag.

### Search by tag

When you type a word into the gallery search engine, if that word corresponds to a tag, you will see "1 tag found". You can then click on the tag to display the associated photos.

![Recherche tag.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-15bf076b.jpg)

If the **RV Autocomplete** plugin is activated in your gallery, the tag list is even displayed using autocomplete when making a search.

![RV autocomplete.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f694e0c1.jpg)

Finally, you can combine tags with other search criteria using the search filters. Filters can be accessed once you have started a search, or by clicking from the Explore > Search menu.

Click on the "Tag" filter to add one or more tags to your search.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-91b1e4f4.png)

[Learn more about search filters](search-for-a-photo-in-your-gallery.md)

## Customizing tag management with plugins

### PWG Stuffs: Display a tag cloud on your home page

Do you want to display a tag cloud on your gallery's home page, just like [this example](https://demo3.piwigo.com/)?

You can do this by activating the **PWG Stuffs** plugin.

[Learn more](tags-in-your-gallery/pwg-stuffs-plugin-piwigo.md)

### Menu Tags: Listing all the tags in the menu

As explained earlier on this page, by default, in your gallery, the Tags menu dynamically displays the Tags related to the content you are currently watching.

This way, if you are on the page of an album where the photos aren't linked to any tags, the Related tags menu doesn't appear.

If you want to display a Tags menu listing all the tags available in your gallery when you are on a page without any related tags, you can activate the **Menu Tags** plugin.

As a result, instead of displaying a "Related tags" menu on the home page, the menu will display a "Tags" menu showing all tags in your gallery, with a size that is proportional to their use.

### Birthdate: Displaying the age of an element in a photo

The Birthdate plugin lets you associate a birth date with a tag, to display the age of an element of a photo at the time it was taken.

This feature is often used for photos of people, especially children. Let's imagine that I have a series of photos of a child named John. With the Birthdate plugin, I associate the tag "John" with his birth date.

This way, in the gallery, next to each photo of John, we will show how old he was when the photo was taken (down to the hour!).

This feature can also be useful for other specific cases:

- Following the growth of a plant from its planting date
- Following the evolution of a building from its construction date
- …

### Tag Groups: Creating tag groups

By default, tags are all at the same level, unlike albums: they follow a tree structure.

However, you can create a tag tree structure with one level using the **Tag Groups** plugin.

!!! info "Info :" If you are a piwigo.com customer, this plugin is only available from the Enterprise plan and higher.

This plugin lets you create tag groups: for example, a "Color" group, in which you will find one tag per color; or a "City" group in which you will find one tag per city.

Instead of being displayed in the form of a tag cloud on your gallery's Tags page, they can be sorted by group.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-87aed4ac.png)

This plugin also lets you set up filters by tag group in your gallery.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8b84279a.png)

**How do I create a tag group?**

To create a "color" tag group, you only need to create a "color:blue" tag, a "color:red" tag, etc.

In the same way, you can create a "city" group by creating a "city:paris" tag, a "city:london" tag, etc.

**How do I display tags by group?**

The display of tags by group replaces the tag cloud display on your gallery's Tags page.

To display tags by group, on the Tags page, click on the "Show tag groups" button in the top right corner.

![Montrer groupes de tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-49e461c0.jpg)

If you want the Tags page to display tags in groups by default, it is possible.

If you are a piwigo.com plan customer, you must reach out to support to activate this option.

If you are using a self-hosted Piwigo gallery, you can activate it by editing the local configuration with LocalFiles Editor, using the configuration setting below.

```php
$conf['tags_default_display_mode'] = 'groups';
```

**How do I activate multi-criteria filters by tag group?**

If you are a piwigo.com plan customer, you must reach out to support to activate this option.

If you are using a self-hosted Piwigo gallery, you can activate it by editing the local configuration with LocalFiles Editor, using the configuration setting below.

```php
$conf['tag_groups_index_filters'] = true;
$conf['tag_groups_dynamic_filters'] = true;
```

To learn more about tag groups, you can:

- [Read this blog article](https://piwigo.com/blog/2020/06/09/add-a-filter-bar-to-your-photo-gallery/)
- [View this demo sample](https://hannah.piwigo.com/)

### Add colors to tags with Colored Tags

You can assign a color to tags by activating the Colored Tags plugin.

Once the plugin has been activated, you will be able to set a list of colors in the plugin's configuration, through a hex code or by picking on the color wheel.

![Couleurs de tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-57357e72.jpg)

To edit the color associated with a tag, you must go in the administration, in the Photos > Tags menu, and switch to Selection mode. From there, you will be able to assign a color to one or more tags.

![Tags avec couleurs.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-3eb03a55.jpg)

The tag colors are visible in your gallery, in the Related tags menu and the Tags page.

![Tags colorés.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a95d65d5.jpg)

![Affichage tags couleur.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-38ee7cfb.jpg)

### Tag To Keyword: Renaming "tag" to "keyword”

Some users don't like the term "tag" and prefer "keyword".

This is why there is a "Tag To Keyword" plugin, which replaces the word "tag" with "keyword" once activated.

Article summary

---

← Previous

[The Photo page in your gallery](the-photo-page-in-your-gallery.md)

Next →

[Search for a photo in your gallery](search-for-a-photo-in-your-gallery.md)
