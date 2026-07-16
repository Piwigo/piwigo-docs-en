# Maintenance of your Piwigo gallery

For Piwigo's "technical" administrators, a Maintenance menu is available to you, only accessible for users with the Webmaster status.

To access it, go to the administration, in the Tools > Maintenance menu.

## Maintenance actions available on Piwigo

The first "Actions" tab offers many actions in order to administrate your Piwigo gallery.

![Page de maintenance.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e890070e.jpg)

The most used action within a "normal" use of Piwigo is the "Lock gallery" action (see next chapter), which lets you make the gallery unavailable (for example, when you are working to reorganize it).

The other actions are mainly used to delete unused data or refresh the information displayed on Piwigo.

<aside>
💡 **Why may these actions be necessary?**

In order to optimize page loading times, Piwigo is using cached data. For example, instead of counting the number of photos in each album every time a page is reloaded, this information is stored in the database. In theory, this information is always correct, but a mistake can sometimes happen and the cached information becomes false. In this case, deleting and regenerating the cache can be useful.

Furthermore, some data become useless with time. Deleting them from the database frees up storage space.

</aside>

### Actions on the gallery

Here are the actions available in the "Global Gallery Actions" section.

- **Lock gallery**

This action lets you switch your gallery to "maintenance mode".

A locked gallery is only visible to administrators. As long as the gallery is locked, a warning message will be displayed on all pages in Piwigo's administration.

![Galerie verrouillée.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-826b8c70.jpg)

The gallery's visitors, on the other hand, will not be able to browse the website, which will display the following message: *The gallery is locked for maintenance. Please come back later.*

- **Update albums’ information**

This action can be useful if an error message ever appears on your gallery. It checks and potentially corrects some of the data saved on the albums in the database.

- **Update photos’ information**

This action can be useful if an error message ever appears on your gallery.

It checks and potentially corrects some of the data saved on the photos in the database.

- **Repair and optimize database**

This action can be useful if an error message ever appears on your gallery.

It performs a maintenance operation on your database: optimization (deleting the empty-tagged spaces that have contained data) and repair (checking and repairing table structures). It also allows the size of the database to be slightly compacted.

- **Reinitialize integrity check**

Usually, you shouldn't need to perform this action.

It allows you to reset the error counters possibly detected by integrity checks, including the results displayed on the home page of the administration panel.

### Purge actions

Here are the actions available in the "Purge Actions" section.

- **Purge user cache**

This action can be useful if a user sees elements they shouldn't see in the gallery (for example, if you witness a breach of user rights). Usually, you shouldn't need to perform this action.

- **Delete orphan tags**

This action lets you delete all tags that aren't associated with any photo.

- **Purge history details**

This action deletes the entire history of visits. The search screen in the history (accessible from the Tools > History > Search menu) will not show any data anymore.

<aside>
⚠️ Warning: all data will be lost, without any possibility of getting them back. However, the graphs available from the Statistics tab will still be displayed, except if you also delete the history summary (next paragraph).

</aside>

- **Purge history summary**

This action deletes the statistical graphs available from the Tools > History > Statistics menu.

<aside>
⚠️ If you don't delete the history details (previous paragraph) along with it, the graphs will be recalculated from the information located in the detailed history.

</aside>

- **Purge sessions**

Visitors of a gallery logging in generates a session with a unique identifier, memorized in a table in the database and in a cookie (its validity is 30 minutes for the cookie). This session identifier is used for various purposes, namely statistics, and purging sessions that haven't been used in a long time can be necessary.

Among other things, this can reduce the size of the database.

- **Purge never used notification feeds**

The RSS notification feed is customized for all visitors (new elements, new comments, etc). This feature lets you delete "customization" for visitors that aren't using the information feed.

- **Purge search history**

Piwigo remembers the criteria of searches performed by visitors in your gallery. This feature lets you purge this history.

Among other things, this can reduce the size of the database.

### Purge cache

Here are the actions available in the "Purge Cache" section.

**Calculate cache size**

You can click on "Refresh" to update this calculation.

**Purge compiled templates**

Use this feature to regenerate the gallery's display if it is not proper, generally following a manipulation on templates or a theme switch.

### Delete multiple size images

Every time a user requests for a version of a photo to be displayed on the gallery, this version is saved. At some point, this can take up space in your database. This section shows the space taken by these versions and lets you delete them. They will then be regenerated upon request.

## Environment: Information about your Piwigo gallery

The "Environment" tab shows information about your Piwigo gallery.

For customers hosted on piwigo.com, only the information below is available:

- Current version of Piwigo
- List of plugins activated

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-14cd61fc.png)

For self-hosted Piwigo, additional information is available:

- Installation date
- Operating system
- PHP version
- MySQL version
- Graphics library used and version
- Cache size

From this page, you can also check whether a Piwigo update is available.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-191f586d.png)

## System Activities

The third tab “System Activities” (introduced in Piwigo version 15) allows you to view a detailed, time-stamped history of all the following events:

- Modification of a Piwigo configuration parameter
- Installation / activation / deactivation of a plugin
- Theme installation / activation / deactivation
- Theme or plugin update
- Piwigo core update
- Default theme modification
- Maintenance actions

For each action, you can see the object concerned (core, plugin or theme), the type of action (configuration, update, activation...), the user who initiated the action, the date and time, as well as details (version, etc.).

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-46f517ca.png)

## **Delete Hit/Rate: Deleting views (hits) and photo ratings**

If you want to reset views and photo ratings, you can install the **Delete Hit/Rate** plugin.

- Hits: these are the photos' views. They are displayed in the gallery if you have activated this option. This is what is used to sort photos by number of views.
- Rates: these are the photos' ratings. They are displayed if you have activated the "Allow rating" option on the Configuration > Options page.

[Learn more about ratings](../comments-and-ratings/managing-ratings-votes.md)

Once the Delete Hit/Rate plugin is activated, two new purge actions are available on the Maintenance screen:

- Purge all hits on the gallery (delete all visits)
- Purge all ratings on the gallery

![Actions de purge.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-23ad9743.jpg)

Article summary

---

← Previous

[Viewing the statistics of your Piwigo gallery](viewing-statistics-piwigo-gallery.md)

Next →

[Plugins for administrators](plugins-for-administrators.md)
