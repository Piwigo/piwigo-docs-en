# Viewing the statistics of your Piwigo gallery

Piwigo provides administrators with multiple ways, as standard or with plugins, to monitor the use of their photo library and to track how it performs.

## Dashboard

The home page of Piwigo's administration is called Dashboard.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-99beacea.png)

The dashboard lets you view the usage of your gallery at a glance:

- Number of photos
- Number of albums
- Number of tags
- Number of users
- Number of groups
- Comments
- Notes
- Pages seen (from the beginning)
- Plugins installed
- Storage used
- Only for piwigo.com: Number of days remaining on the current period (trial period, subscription...)

Each icon is also a shortcut to the management screen for each topic.

Furthermore, the dashboard gives you an overview of the peaks in activity in the last 4 weeks.

A colored bubble represents the activity for each day of the week. When hovering the mouse over this bubble, you will be able to see the actions performed.

![en-activity-dashboard.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-79b0b62b.png)

Since the version 14 of Piwigo, you can also view the storage used for each file type and format on the dashboard.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-27638894.png)

## Statistics for the history of visits

To access the visit statistics for your Piwigo gallery, go to the administration, in the Tools > History menu.

This page shows the graph of visits on your Piwigo gallery.

![fr-historique-stats.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6cae9134.png)

You can view these statistics:

- everyday for the last 3 months
- every hour for the last 3 days
- every month for the last 5 years
- every year since the creation of your Piwigo gallery

When hovering the mouse over the graph, you can view the number of pages seen for each period.

When clicking on "Compare mode" in the top right, you get access to another view of the statistics.

- The Year view shows one curve per year, with a color code for each one; each curve shows the number of monthly visits for the year. For example, this lets you see whether the visits in your gallery correspond to a seasonal phenomenon which is repeated every year.
    
    ![en-history-compare-month.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bd711ced.png)
    
- The Month view shows one curve per month for the last 3 months, as well as an average for the last 12 months, with one color code per curve; each curve shows the number of visits per day. For example, this lets you see whether the visits in your gallery have evolved in the last few months.
    
    ![en-history-compare-month.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-68fea989.png)
    

### Options for statistics

You can customize the tracking of visits in the Configuration > Options page in the administration, General tab, Miscellaneous section.

The option to "Save visits in history for..." lets you set which visits are saved in the statistics:

- Visits from "simple visitors" (anonymous)
- Visits from registered users
- Visits from administrators

Of course, you can select all of these options or only some of them.

For example, if you want these statistics to reflect your gallery's popularity and not the work of the administrators, deactivating the statistics for the administrators might be relevant.

### Browsing the history

How can you know what users are doing in your gallery? Who downloaded this file or that file?

This is a recurring need, in order to know which photos are popular, but also to know who downloaded files that are under copyright, for example.

This is possible thanks to the **search in history** tool.

From the Tools > History menu, the Search tab lets you view a detailed history of the actions performed on your Piwigo gallery, and perform a search.

![Historique par utilisateur.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-923e5b0d.jpg)

This page lists the actions performed in your gallery on a certain period, in chronological order. You can choose the period using the filters by date.

Two types of action are shown here:

- Page visits
- File downloads

Thanks to the "Action" filter, you can choose to only show visits, or downloads.

The table shows:

- Date: The date and time of the action
- User: The user behind the action (if it is an anonymous user, they're shown as "guest”) and their IP address
- Object: The album or the file involved. The home page visits are tagged with the "Root" label.
- Details: For simple visits, the album involved is displayed here; for downloads, the "Downloaded" label is shown.

![Activités différentes.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1c9e8597.jpg)

It's possible to filter the list on a specific user by clicking on their name in the bar above the table.

The chosen user then appears in the additional filters. You can reset the filters by clicking on the cross next to the user.

![Dernière capture.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-70e4047b.jpg)

Lastly, it is possible to filter the actions on a specific photo: to do this, click on the 3 dots next to a thumbnail and click on "Add as filter".

![Ajouter comme filtre.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-31f8b368.jpg)

This way, you will be able to view all downloads for one photo for the period of your choice.

## Viewing the activity of Piwigo administrators

To view the detailed history of all the user's actions in Piwigo's administration, you simply need to go to the Activity tab on the Users page.

!!! info "If you are a Piwigo Cloud customer, this feature is only available from the Team plan and higher"

This page shows all activities performed by users in your Piwigo gallery:

- Login / logout
- Photo import / edition / deletion (and other files)
- Album creation / edition / deletion / relocation
- User and user group creation / edition / deletion
- Tag creation / edition / deletion

You can filter this list by user.

![Activité utilisateur.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4d5075b2.jpg)

## AStat.2: Detailed statistics

To get access to more advanced statistics, you can download the **AStat.2** plugin.

Once this plugin has been installed, it lets you view the number of pages seen, of images seen, of albums seen, according to many criteria. It gives access to:

- statistics by period
- statistics by IP address
- statistics by album
- statistics by file

Options allow you to customize the way the data is presented.

Lastly, this plugin lets you "clean" the statistics so that they are more complete when users, files or albums have been deleted.

It also lets you purge your history if needed.

![Statistics by album](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f82a2632.jpg)

Statistics by album

![Statistics by photo](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5919e257.jpg)

Statistics by photo

![Statistics by month](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e3bc16dc.jpg)

Statistics by month

## **Statistics: Integrating an external statistics tool in Piwigo**

Do you want to follow your gallery's statistics with a Web Analytics tool you are already using such as Google Analytics, Matomo, Piwik, or many others?

This is possible: to do this, simply activate the **Statistics** plugin.

Once this plugin has been activated, it allows you to connect Piwigo to your external statistics tool. You will need to retrieve your tool's tracking code (or script) and paste it in the plugin's settings.

You can choose the code's location (header or footer); you can also choose to exclude administrators or users who are not logged in from the statistics.

!!! warning "Warning"
    When using statistics tools such as Google Analytics, you must obtain the consent of visitors in your gallery. We suggest you follow the recommendations from the authorities of your visitors' countries in terms of data tracking and user consent collection

## **No Stats for Robots:** Excluding robots from the statistics

Statistics in Piwigo may sometimes be "polluted" by visits from robots (search engines, etc).

To exclude them, simply activate the **No Stats for Robots** plugin.

This plugin excludes visits from known robots from your visit statistics.

Article summary

---

Next →

[Maintenance of your Piwigo gallery](maintenance-piwigo-gallery.md)
