# Batch management: Modifying and managing a selection of photos

**How do I edit, delete, update a selection of files in bulk in Piwigo?**

This is the goal of the Batch management feature.

The batch manager allows you to select a series of files according to various criteria to edit or delete them.

You also have the ability to create a selection of photos by adding them to your cart when you are browsing the gallery, and edit them afterwards in the administration with the Batch Manager.

The batch manager is one of Piwigo's most powerful features, which will spare you an endless amount of time, so take the time to get familiar with it!

## Batch management: introduction

To access the Batch Manager menu, go in the administration and, in the left menu, go into Photos > Batch Manager.

![Batch Manager.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5509dea2.jpg)

This screen contains two tabs:

- Global mode (by default)
- Single mode

The Global mode tab allows you to choose a selection of photos from many criteria and modify them in bulk.

This screen is designed with three parts:

- Filter: this section allows you to create a selection of files that you want to update, by combining files using the numerous criteria available.
- Selection: this section displays the selection resulting from your filter criteria, and allows you to refine it by ticking / unticking specific files.
- Action: this section allows you to choose the action to be carried out onto your selection.

## Batch Manager: Using the Filters

By default, the last used filter is applied. It is often the last import.

By clicking the cross, you can delete this filter.

![Animation.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1d015b12.gif)

By clicking on "Add a filter", you will be able to choose the filtering criteria for your selection, among the available criteria.

![Adding a filter.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9d29322d.jpg)

When you add a filter, the photos that fit this filter aren't automatically displayed: to view the result of your selection, you must click on "Refresh photo set".

### Filtering photos by album

The Album filter allows you to choose an album to display its files.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d4f8929c.png)

To select an album, click on the button: this opens the album search window.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-faf44dfe.png)

Use the search engine or browse the list and click on the + to choose the album.

Once you've chosen an album, you can choose to include photos from its child albums in your selection, by checking “include sub-albums”.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bbd4e67c.png)

### Filtering photos by tag

The Tag filter allows you to filter photos by Tag. You can enter multiple tags, and choose:

- to only display files associated with ALL selected tags (All tags)
- or to display files associated with at least one of the selected tags (Any tag)

![Filter by tag.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9de126af.jpg)

### Filtering photos by privacy level

The Privacy level filter allows you to only display files associated with a specified privacy level:

- Everybody
- Contacts
- Friends
- Family
- Admins

The option to "include photos with a lower privacy level" allows you to overlap several privacy levels.

![Filter by privacy level.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4572f8d4.jpg)

For example: if we choose the "Friends" privacy level and select this option, photos associated with the "Friends" AND "Contacts" privacy levels will be displayed.

To understand how privacy levels work, [read this article](../managing-users/privacy-levels.md).

### Filtering photos by dimensions

The Dimensions filter allows you to filter photos depending on their dimensions:

- width
- height
- width / height ratio (format)

![Filter by dimensions.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5355d5b9.jpg)

To select the range of your choice, simply move the sliders just like the example above.

If you want a specific file format (portrait, landscape, panorama), click on the corresponding label: the ratio will automatically be updated.

### Filtering photos by file size

The Filesize filter allows you to filter photos depending on their size in MB (Megabytes).

![Filter by size.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-34cb25ce.jpg)

### Searching for a photo with keywords

The "Search" filter allows you to show a text search engine.

![Search filter.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f12b73ba.jpg)

It works the same way as your gallery's search engine.

Click on “Search tips” to discover powerful searching features. 

### Filtering photos with predefined filters

By default, Piwigo offers many predefined filters that correspond to a frequent use of Piwigo. 

Here are the standard available filters:

- Last import: show the latest imported photos (you can also click on the Photos > Recent photos menu to show the last import)
- Duplicates  this allows you to find all duplicate photos (that have the same name) in your photo library in order to remove duplicates
- Your favorites: allows you to find the photos you added to your favorites in the gallery
- Caddie: allows you to find all photos added to your cart or "Caddie" (you can also click on the Photos > Caddie menu, see Caddie chapter)
- With no album (Orphans): this allows you to find photos in your gallery that haven't been added to any album, and therefore aren't visible
- With no tag
- All: shows all the photos in your library

![Predefined filter.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2767c70f.png)

### Combining multiple filters

Combining multiple filters is entirely possible.

Once the first filter has been selected, click again on "Add a filter": the filters combine.

![Combined filters.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-65282181.png)

### Batch Manager Prefilters: Adding new predefined filters to the Batch Manager

To add new predefined filters, install the **Batch Manager Prefilters** plugin.

It adds the following filters:

- associated to only one album
- associated to several albums
- with author
- without author
- with tags
- with no creation date
- with no title

You can also install the **Batch Manager, Description** plugin to add the "without description" prefilter.

This way, you will be able to view all photos without a description in the blink of an eye.

### Batch Manager Added By: Searching for a photo by user

To filter photos based on the user who uploaded them to Piwigo, you need to install the **Batch Manager, Added By** plugin.

!!! info "If you are a Piwigo Cloud plan customer, this plugin is only available from the Team plan and higher"

Once activated, this plugin adds a new "Added by" filter in the batch manager.

## Batch manager: Your selection

Once you have applied all your filters and clicked on "Refresh photo set", the photos relevant to your search will be displayed in the "Selection" area.

By default, 20 files are shown on screen. You can browse your selection using the page number links or the arrows in the bottom right corner ; you can also increase the amount of files displayed on screen by clicking on 50, 100 or All in the bottom left corner.

![Batch manager selection.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ee1d3fa6.jpg)

To select the files you want to modify, you can simply click on each file to edit. You can also click on:

- “The whole page” to select all the files visible on the screen
- “The whole set” to select all the files of your selection
- “Invert” to select all files except the ones you clicked on
- “None” to deselect all the selected files

The selected files are highlighted by an orange icon.

![Animation.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bf8ae1c3.gif)

You can also edit a single file on the global mode screen.

To do this, hover the mouse over the photo's thumbnail and click on the pen-shaped icon.

![Edit photo icon.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-3fe27552.jpg)

The photo editing page then opens in a new tab. You can now edit what you want, save your changes by clicking on "Save Settings", close the tab and go back to the Global mode page to carry on with your changes.

## Batch manager: Editing your selected files in bulk

Once you have chosen photos to edit, click on "Choose an action": the drop-down list shows all the changes you can make to your selection:

- Delete selected photos
- Associate to one or several album(s)
- Move to album(s)
- Dissociate from album
- Add tags
- Set author
- Set title
- Set creation date
- Who can see these photos! (Privacy level)
- Synchronize metadata
- Add to caddie (if your caddie is empty)
- Remove from caddie (when the “Caddie” filter is selected)
- Delete multiple size images
- Generate multiple size images
- Videos (specific actions for video files)

![Choose an action.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8ee09784.jpg)

### Example: changing the photos’ title

You have uploaded files to Piwigo with a name generated by the shooting device. The default file title is retrieved from the file's name (IMG_4545, IMG_4546…).

You want to add an explicit label in front of the current name.

Once the files have been added, select the "Set title" action.

In the entry field, enter the title you want to give to your files, here: "beach".

![Set title.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-feabe8d9.jpg)

Click on "Apply action": the files' title is now "beach(IMG_XXXX.JPG)”.

### Example: adding a tag to a selection

To add a tag to a selection, click on Choose an action > Add tags. Choose an existing tag in the list or enter text to add a new tag.

![Add tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d52c4ba4.jpg)

Click on Apply action: the tag has been added to your photos.

### Posted Date Changer: Edit the add date with the batch manager

Changing the add date of a selection of photos after the upload can be very useful, but this action is not available in Piwigo by default. To add it, you need to activate the **Posted Date Changer** plugin.

Once the plugin has been activated, the action to "Change Posted Date" becomes available in the batch manager.

## Batch manager: Single mode

The batch manager also allows you to edit your selected files one by one.

To do this, go into the Single mode tab.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ba1e1bbe.png)

This page shows all the files that correspond to the filters you applied in the first tab.

!!! warning "Warning :"
    If you edit these filters, make sure to click on "Refresh photo set": this will also update the selection shown in the "Single mode" tab.

This way, you can edit the title, the author, the creation date, the privacy level, edit tags, edit associated album(s) edit the description for each file.

Don't forget to click on the Submit button at the bottom of the screen to save your changes.

## Using the caddie in Piwigo

As explained in the previous chapter, Piwigo allows you to create a "Caddie" that contains a selection of files set aside for later.

From your gallery, you can add a photo to your caddie from this photo's page by clicking on the "Add to caddie" button.

Depending on your theme, the icon can take the shape of a shopping cart, a flag, or even a basket. On Modus, Piwigo's default theme, the icon is shaped like a shopping cart.

![Add to caddie.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4df4feba.jpg)

You can also add all of the photos of an album to your caddie by clicking on the "Add to caddie" icon in the Album page.

![Add to caddie icon.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-72835069.jpg)

Once you have made your selection, you need to go back to the administration to view your caddie.

To do this, click on the Photos > Caddie menu. This menu displays the number of files in your caddie at any given time.

![Left menu.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2a93dea6.jpg)

The Caddie menu simply displays the batch manager screen, filtered through the "Caddie" prefilter.

To empty the caddie, click on the "Empty caddie" button below the filter.

![Empty caddie.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-dc919217.jpg)
