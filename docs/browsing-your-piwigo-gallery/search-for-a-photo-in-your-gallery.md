# Search for a photo in your gallery

Several options are available to you in order to conduct a search in your Piwigo gallery, be it a simple quick search by keyword, or a multi-criteria search that combines several filters.

We cover it all in this article!

## The quick search

### Using the quick search field

If this feature is active in your gallery (this is the case by default for most themes), you have access to a search field.

![Recherche.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-93100bee.jpg)

On some themes, the search will be accessible by clicking on a menu item (example below with the default configuration for the Bootstrap Darkroom theme).

![Recherche BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-09d801d5.jpg)

Enter a word in the quick search and press the Enter key: the results show the photos that correspond to your search.

![Résultats recherche.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5675caaa.jpg)

By default, to filter the results, Piwigo searches for the word you entered:

- in the photo's name (title) in Piwigo
- in the file’s name
- in the file's description
- in the tags associated with your photos
- in the photos' ID

Furthermore, if the keyword entered corresponds to a tag or the name of an album in your gallery, they will also appear in the results. Click on the "Tags found" or "Albums found" button to see the list of tags / albums that correspond to your search.

![Trouvailles.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-99ff55de.jpg)

### Editing / refining a quick search

Since Piwigo version 14, every time you make a quick search, a filter bar appears above the search results. We will talk about it again in the next chapter. This filter bar allows you to refine your search by applying additional criteria (tag, album, author...).

This filter bar also lets you edit the current search. To do this, simply click on the area that shows the word you searched for, which will open a window.

![Recherche mots.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-899a93ba.jpg)

In this window, you will be able to:

- edit the content of your search;
- perform a search on multiple words by filtering on all words or one of the words;
- choose where Piwigo performs the search (for example, by deactivating the search in photo descriptions).

### RV autocomplete: Activate autocompletion on the quick search engine

Do you want to save even more time when searching for a tag or an album in your gallery?

We recommend you use the **RV Autocomplete** plugin.

Once the plugin has been activated, when entering a search term, the albums and tags that fit your search will automatically be recommended.

![RV Autocomplète.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8b1e3150.jpg)

## The multi-criteria search filters

### Starting a multi-criteria search

Since Piwigo version 14, the old advanced search has been replaced with a filter bar.

![Recherche début.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4cb2eef4.jpg)

There are multiple ways to start a search:

- Using the quick search form (explained in the previous chapter): you will then be able to refine or reset your search using the filters.
- Going into the Explore > Search menu (Modus theme) or Discover > Search (Bootstrap Darkroom theme) to display the search page.
- Starting from an album or tag page and clicking on the button or the icon titled "Search in this set" (if this button has been activated in your gallery).

### Choosing the filters shown

The filter bar shows 4 filters available by default:

- search by word (works the same way as the quick search)
- filter by Tag
- filter by Album
- filter by Author

![Filtres.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-09c3a22e.jpg)

You can click on "Choose filters" to add other criteria:

- Post date (date when the file was uploaded to Piwigo)
- Creation date  (date when the file was created)
- Added by (user who uploaded the file)
- File type (file extension: JPG, PNG...)
- Ratio (portrait, square, landscape...)
- Filesize (in bytes)
- Height (in pixels)
- Width (in pixels)

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5c14739d.png)

Simply click on a criteria to add or remove it from the filter bar, and save. The chosen criteria have been added. Your choice of visible filters is saved, but only applied for your user.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0c0eebd1.png)

### Using filters to find photos

**Search by word**

This filter works just like the quick search. 

You can enter one or more words, decide whether you want to show the results that contain all words or only one of them, and choose where to search the word you entered (in the photo's title, the file name, the description...).

![Recherche de mots.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d982afdb.jpg)

One click on "Delete" deactivates the filter; one click on "Clear" resets the filter.

**Search by tag**

The "tag" filter lets you show the photos associated with one or more tags.

You can decide whether the search should retrieve photos associated with all selected tags or at least one of them.

By clicking in the search field, you will show a drop-down list of all the tags, in which you can search for the desired tag by typing the first few letters.

![Recherche tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8e5721b0.jpg)

One click on "Delete" deactivates the filter; one click on "Clear" resets the filter.

**Search by post date and creation date**

The “post date” filter allows you to filter photos according to the date they were imported into Piwigo, and the “creation date” filter by the date the file was created.

Several ranges are available: last 7 days, last 30 days, last 3 months... The number of photos corresponding to each date range is also displayed. Irrelevant filters are grayed out.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5e047136.png)

You can also click on “Custom dates” to filter on one or more date ranges of your choice. These ranges can be a year, a month, a day... or a combination of all these.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-16beb8ca.png)

One click on "Delete" deactivates the filter; one click on "Clear" resets the filter.

**Search by album**

The album filter lets you search for photos within one or more albums, with or without including sub-albums.

![filters-album.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-800f9b4f.gif)

One click on "Delete" deactivates the filter; one click on "Clear" resets the filter.

**Search by author**

The author filter lets you search for a photo by author, by searching in the drop-down list of existing authors.

![Auteurs.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c1cb3753.jpg)

One click on "Delete" deactivates the filter; one click on "Clear" resets the filter.

**Search by "Added by" (user who imported the file)**

The "Added by" filter allows you to list users who imported files to your Piwigo gallery and filter the search results. The number of photos for each user is shown.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-611a803e.png)

One click on "Delete" deactivates the filter; one click on "Clear" resets the filter.

**Search by file type (format)**

The "File type" filter lets you filter the results by format (or file extension).

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e0b760d0.png)

**Search by ratio**

The “Ratio” filter lets you filter files by aspect ratio. Several ratios are detected by Piwigo: portrait, square, landscape, panorama.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0eb533ad.png)

**Search by filesize**

The “filesize” filter lets you filter files by minimum and/or maximum filesize in MB. Click on the scale to move the cursor.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e57b0a39.png)

**Search by height / width**

Filters by height/width allow you to filter files according to a minimum and/or maximum height/width, in pixels. Click on the scale to move the cursor.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ec54877f.png)

### Combining multiple filters

The strength of this search engine lies in its ability to combine multiple filters and see the results be instantly updated.

You can add or remove a filter at any moment, edit the criteria and refine your search, as seen in the animation below.

![filters.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-81aec1aa.gif)

### Searching for a photo in a set (album or tag)

On a album or tag page, you can display a button or an icon allowing you to start a search within this set of photos.

The "Search in this set" button:

![Recherche lot.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-12c769f9.jpg)

The "Search in this set" icon in the Album page's tool bar:

![icone-lot.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9d25876d.png)

Click this button to display the search filters on the current page.

To activate or deactivate the display of this button and this icon in your gallery, go in the administration, in the Configuration > Options menu, then the "Display" tab.

![Configuration.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bc617af1.jpg)

## Making a search using related tags

If your photos are correctly indexed using tags, the search by tag could be very powerful when it comes to finding a photo. You can search for a photo by tag by using the search engine, but also by browsing through tags using the "Related tags" feature or a tag cloud.

Read this article to learn more: [Using tags in your gallery](tags-in-your-gallery.md)
