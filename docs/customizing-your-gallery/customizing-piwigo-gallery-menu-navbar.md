# Customizing your gallery’s menu

How can you customize your gallery's menu bar, modify the tree structure and add new menu items? We will explain everything in this article.

## Presentation of Piwigo's default menu

All galleries are created with the same browsing menu by default. What we call **the menu** means the links displayed in the strip at the top of all pages in the gallery.

![The browsing menu with the Modus theme](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-19542d3a.jpg)

The browsing menu with the Modus theme

![The browsing menu with Bootstrap Darkroom](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-edcd40fb.jpg)

The browsing menu with Bootstrap Darkroom

With the previous examples, you will notice: 

- that the menu items displayed are not the same depending on the theme used in your gallery;
- that the menu isn't the same depending on whether or not we are logged in as a user.

Some menu items open a list with sub-menus:

- The Albums link shows the list of albums with the number of photos it contains for each of them.
- The "Related tags" menu shows the tag list and lets you search for a photo by tag.
- The Explore menu (on Modus) or Discover (on Bootstrap Darkroom) lists many sub-menus.

![Menu additionnel.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4cf49a38.jpg)

## Customizing the menu: basic options

To customize the browsing menu in your gallery, go to the administration, in the Configuration > Menus menu.

This page lets you view the links in the menu, reorganize them, and hide some of them.

![Liste des menus.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-82955015.jpg)

It is important to understand what each line on this page corresponds to:

- The "Specials" line corresponds to a list of links available when clicking in the "Explore" menu item on Modus and "Discover" on Bootstrap Darkroom. The "special" pages are the following:
    - My favorites (for users who are logged in)
    - Most visited
    - Best rated
    - Recent photos
    - Recent albums
    - Random photos
    - Calendar

![The "Menu" and "Specials" blocks on a gallery with the Modus theme](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8461e87c.jpg)

The "Menu" and "Specials" blocks on a gallery with the Modus theme

- The "Menu" line corresponds to another list of links available when clicking on the "Explore" menu item on Modus and "Discover" on Bootstrap Darkroom. The "Menu" block contains the following links:
    - Tags
    - Search
    - Comments
    - Notifications
- The "Related albums" line is only displayed on a photo page
- The "Links" line corresponds to external links that can be added in Piwigo's configuration (with [LocalFile Editor](../self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md) if you are using a self-hosted Piwigo gallery, or with the [Advanced Menu Manager](customizing-piwigo-gallery-menu-navbar.md) plugin)

To edit the display order of menu items, simply perform a "drag-and-drop" and save the settings.

![Changer liste menus.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-47022628.gif)

You can also check "Hide" if you want to hide an element in the menu.

## Customizing the menu with plugins

Multiple plugins allow you to go further in the customization of your menu.

### Advanced Menu Manager: advanced menu customization

The Advanced Menu Manager plugin offers additional options for customizing your browsing menu. Once activated, go to the plugin's configuration page.

5 tabs are available to you.

**“Menu management” tab**

This tab, just like the menu configuration page in the administration, lets you reorganize menu items through "drag-and-drop". It also lets you edit the visibility of some menu items depending on the users:

- by [user status](../managing-users/user-statuses.md) in the left column (administrator, webmaster, visitor, guest...)
- by [user group](../managing-users/user-groups.md) in the right column

![Plugin AMM.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2e2eff09.jpg)

On this same tab, by clicking on "Content for 'Menu' & 'Specials' menus", you can customize the pages displayed in the "Menu" and "Specials" blocks (see previous paragraph).

![Plugin AMM autre menu.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-95b63dc2.jpg)

On this page, you can therefore reorganize links in these two menu blocks, but also click on the lock to set the visibility of these links by user status and by user group.

**“Links” tab**

This tab lets you add external links which will be inserted into the "Links" group (for example, if you want to integrate a link to your website on your gallery).

Here, you can:

- Add one or more external links
- Rename the "Links" menu item displayed in your gallery
- Edit other options

**“Random picture” tab**

The Advanced Menu Manager plugin adds a "A random picture" menu item to your gallery. This link lets you display a randomly chosen image when hovering the mouse over it.

![Image au hasard.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4997c09f.jpg)

In the "Random picture" tab, you can customize the title of this block in the menu, the data displayed, as well as the visibility of this block in some albums only.

**"Personalized menu" tab**

This tab lets you add the menu items you want in the menu.

**“Album ⇒ Menu” tab**

This tab lets you create menu items from an album.  

This is useful if you want to showcase a specific album in the browsing menu.

### RV Menu Tree: Browsing through the album tree

The RV Menu Tree plugin changes the way the "Albums" menu item works in your gallery.

It allows you to browse through the sub-album tree, which is not available by default.

![“Albums” menu with the default Modus theme](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bca5c267.jpg)

“Albums” menu with the default Modus theme

![“Albums” menu with the Modus theme AND RV Menu Tree](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-139dbda1.jpg)

“Albums” menu with the Modus theme AND RV Menu Tree

### See my photos: Adding a "My photos" menu

The **See My Photos** plugin lets you add a "My photos" menu item in the gallery, available inside the "Specials" block.

<aside>
⚠️ If you are a piwigo.com customer, this plugin is only available from the Team plan and higher.

</aside>

This link allows users to see all photos they imported into Piwigo themselves. This is particularly useful when using the [Community](../managing-users/community-plugin-piwigo.md) plugin.

### See photos by user: Adding a “Users” menu

The **See photos by user** lets users of the gallery easily filter photos based on the user who added them.

<aside>
⚠️ If you are a piwigo.com customer, this plugin is only available from the Team plan and higher.

</aside>

You can refine this plugin's settings from its configuration page in the administration:

- choosing a minimum number of photos required to start displaying a user in the gallery
- choosing the maximum number of users to display on the page
- choosing the display order for users on the page (alphabetical order, number of photos...)
- choosing the location of the page on the gallery:
    - "See photos by user" menu under the "Explore" menu
    - or adding a "Users" menu in the main menu, with a sub-menu corresponding to each user
- choosing the user filtering method in the gallery:
    - displaying a classic user cloud
    - displaying an animated and colored user cloud
    - displaying a drop-down user list

We can see an example of a "Users" page below with the "Users" menu and a classic user cloud display options.

![Voir photos par utilisateur.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-00e893c3.jpg)

<aside>
⚠️ This plugin is only partially compatible with the Bootstrap Darkroom theme.

</aside>

### Menu Random Photo: adding a random photo

The **Menu Random Photo** plugin lets you add a menu item that displays a randomly chosen image in Piwigo.

![Plugin MRP.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-500bc174.jpg)

This feature is also available in the Advanced Menu Manager plugin.

### Menu Tags

The **Menu Tags** plugin adds a "Tags" menu on all pages that have no related tags.

If you activate this plugin, the "Related Tags" menu will always be displayed on an album's page (it will only display tags related to this album's photos).

But on the home page, instead of the "Related Tags" menu, we will display a "Tags" menu, which shows all the tags in your gallery, with a size that's proportional to their use rate.

![Plugin MT.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0238d1ec.jpg)

[Learn more about tags in your gallery](../browsing-your-piwigo-gallery/tags-in-your-gallery.md)

### **Upload 1 Menu: adding an “Add photos” menu**

<aside>
⚠️ If you are a piwigo.com customer, this plugin is only available from the Team plan and higher.

</aside>

When the [Community](../managing-users/community-plugin-piwigo.md) is activated, the **Upload 1 Menu** plugin lets you display the "Add photos" menu in the gallery's main menu, next to the "Explore" menu.

![Plugin UP.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-55e5277b.jpg)

Article summary

---

← Previous

[Managing the languages available in your gallery](managing-languages-available-gallery-piwigo.md)

Next →

[Adding pages to your gallery](add-pages-to-piwigo-gallery.md)