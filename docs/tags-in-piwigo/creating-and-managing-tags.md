# Creating and managing tags

Tags are an essential tool to organize your photo library and make searching for content easier. How can you create them and organize them in Piwigo?

## How do I create tags?

There are multiple ways to create tags. You can create them yourself in Piwigo's administration; they can also be imported from your computer if you are already using a keyword system to sort your photos, or from a third-party software such as Lightroom.

To learn more about photo import, [read this article](../import-and-manage-photos/importing-photos-into-piwigo.md).

### Creating a tag in the administration

To create a tag, go in the administration, and click on the Photos > Tags menu on the left.

You will end up in the tag manager, which lists the existing tags, lets you edit them, and create new ones.

![Liste des tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9178cf82.jpg)

To create a tag, click on "Add a tag", enter the tag's label and click on the + button or press the Enter key on your keyboard. The tag has been created.

![Nouveau tag.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-017399c2.jpg)

You can also create a tag directly each time you are able to assign a tag to a photo:

- from the photo editor
- from the batch manager

### **Add tags mass: Creating a tag list in bulk**

If you need to import a list of existing tags into your Piwigo gallery, or create several tags quickly, simply activate the "Add tags mass" plugin.

!!! info "If you are a piwigo.com customer, this plugin is only available from the Team plan and higher"

Once this plugin has been activated, go to the plugin's configuration to add tags in bulk.

![Ajouter tags en masse.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f99f9b8e.jpg)

Simply add tags one after the other, line by line, in the form, and click on Submit to save them.

!!! info "You can copy and paste a tag list into this form from a spreadsheet (Excel for example)."

### Importing tags from your IPTC keywords

Your photos may already be tagged with keywords added from a photo processing software such as Lightroom.

These keywords are part of your photos' IPTC metadata, and they can be imported to Piwigo in tag form.

This is the case by default: if you want to edit these settings, and you are a piwigo.com plan customer, you need to contact support.

!!! warning "Piwigo does not handle the import of tags you may assign to a photo from MacOS's Finder."

## How do I associate tags with my photos?

### Associating tags from the photo editor

To edit a photo's tags in single mode, simply edit this photo.

The photo editor lets you add one or more tags to a photo using the Tags field.

[Learn more about photo editing](../import-and-manage-photos/modifying-or-deleting-photos.md)

When clicking on the input area, the drop-down tag list appears. To search for a particular tag, simply enter a few characters: the list is immediately reloaded to only display tags that correspond to your input.

![Ajouter un tag.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b80f5e81.jpg)

Click on a tag to link it to your photo: it now appears in orange.

![Tag Espagne.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-87cd4f9d.jpg)

To remove a tag from the photo that's currently being edited, click on the cross next to the tag's name. This does not delete the tag from your photo library: it can still be used for other photos.

You can keep doing so and assign multiple tags to your photo.

If you want to create a new tag, simply enter its name in the input area. The "Create ..." option appears: click on it or press the Enter key on your keyboard to create a new tag.

![Création de tag.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4fae74ae.jpg)

!!! info "Remember to save your changes in order for them to be applied to your photo!"

### Associating tags with photos in bulk with the batch manager

In general, it is best to tag photos in bulk rather than doing it in single mode:

- Either after importing a batch of photos to Piwigo
- Or to update a list of photos that fit a criterion (photos of an album, selection of photos in your Caddie...)

You can do this easily through the [Batch Manager](../import-and-manage-photos/batch-manager-piwigo.md).

Once your selection has been made, you can choose the "Add tags" action. It lets you assign existing tags or a newly created tag to a batch of photos.

In global mode:

![Gestion lot créer tag.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f5389291.jpg)

In single mode:

![Créer tag gestion lot.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-13540705.jpg)

### Deleting tags from photos in bulk with the batch manager

The batch manager also allows you to remove tags from a list of photos.

To do this, select the "Remove tags" action and choose the tags you do not wish to assign to the selection of photos anymore.

This does not delete the tags from your photo library: it can still be used for other photos.

## Managing and editing tags

To manage, edit, and delete tags from your photo library, go to the tag management screen by clicking on the Photos > Tags menu.

![Nouvelle liste de tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ffa4fc28.jpg)

A search engine lets you find a tag easily: useful when you have a lot of them!

When you click on the 3 dots next to a tag, you will see the number of photos associated with this tag appear, as well as a list of actions available.

![Actions tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0dfe098a.jpg)

- View in gallery: shows all photos associated with this tag in your Piwigo gallery
- Manage photos: lets you manage / edit the photos associated with this tag using the batch manager
- Edit: lets you rename the tag
- Duplicate: creates a copy of the tag
- Delete: lets you delete the tag

### Editing tags in bulk: selection mode

To edit a list of tags in bulk, you need to switch to selection mode by clicking on the "Selection mode" button on the right of the screen.

This feature allows you:

- to delete a list of tags in bulk
- to merge tags (useful in case there are duplicates)

Click on the tags that need to be edited: they appear one after the other in a list on the right of the screen.

![Sélection de tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-126c5057.jpg)

In the event of a mistake, you can remove a tag from the selected list by clicking on the cross next to its name.

![Supprimer tag sélection.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ef71c1cd.jpg)

At the top of the screen, the All / None / Invert buttons allow you to go faster with the selection if you have many tags to deal with.

- Clicking on "All" adds all tags on the screen to your selection list
- Clicking on "None" empties your selection list
- Clicking on "Invert" adds all tags to the selection, apart from the ones that are currently selected.

Once you are done with selecting tags, click on the desired action:

- Merge: all tags selected will be merged into one (you will need to choose which tag name to keep)
- Delete: all selected tags will be deleted.

## Read also: The tags in your gallery

Read this article to discover how to use tags in your gallery, as well as options and plugins to dive deeper into using tags.

[Tags in your gallery](../browsing-your-piwigo-gallery/tags-in-your-gallery.md)

Article summary

---

← Previous

[Tags: introduction](tags-introduction.md)

Next →

[Tag Recognition: Tag your photos automatically with AI](tag-recognition-plugin-piwigo.md)
