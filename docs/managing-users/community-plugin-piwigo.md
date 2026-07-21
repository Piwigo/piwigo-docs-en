# Managing contributors (Community plugin)

## Why use the Community plugin?

By default, in Piwigo, only administrators are allowed to upload content to your photo library.

However, sometimes, you want to allow some users to import files, without giving them the administrator status. Some examples within an organization:

- You are working with a photographer, and, in order to save time, you want them to send their latest photoshoot straight to Piwigo to sort it, rather than going through a CD or a file transfer;
- Some members of your team are tasked with creating files (edited photos, graphic creations, brochures...); you don't want them to be forced to ask an administrator to import their content to Piwigo, but you also don't want to give them access to the administration.
- Users in the field need to send photos taken on site (service agents, construction site managers, worksite supervisors...). Allowing them to add photos straight to Piwigo saves time for everybody (especially if they are using [the Piwigo mobile app](../mobile-apps/index.md) for iOS or Android!).

If you are using Piwigo in a family, friend or club setting, you can also give other people the possibility to send their photos to your Piwigo gallery.

All of these users who aren't administrators but are allowed to import content into Piwigo are what we call **contributors** here.

To activate this feature, you need to install the **Community** plugin.

!!! info "If you are a piwigo.com customer, this plugin is only available from the Team plan and higher."

## Setting which users are authorized to send photos and their permissions

Once the Community plugin has been activated, you need to go to the plugin's settings by clicking on "Settings".

![Plugin Community.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-09c97702.jpg)

The first tab lets you set Community's permissions and options.

By default, a permission has been created, which allows all registered users to be contributors.

You can edit this permission by clicking on the edition icon, or delete it by clicking on the deletion icon (the cross).

![Page Community.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e7d5db8b.jpg)

You can also add a new permission by clicking on "Add a permission".

When clicking on "Add a permission", we get access to the various available options.

![Ajout de permission.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c2139294.jpg)

**Who?**

Here, set who is allowed to add photos from the gallery:

- Any visitor (even anonymous)
- Any registered user
- A specific user: you can then choose said user
- A group: you can create a Contributors group, which is the most practical. [Learn more about user groups](user-groups.md)

**Where?**

Here, choose which space in the gallery contributors can add photos in:

- In the whole gallery (any album)
- In a specific album

!!! info "Info"
    By default, activating the Community plugin creates a new "Community" album. You can opt for contributors' photos to go first into this album, for an administrator to sort and approve them.

If you select "Apply to sub-albums", users will be allowed to add photos in the chosen album AND its sub-albums.

If you select "Ability to create sub-albums", users will be allowed to create a new album when uploading photos.

**Which level of trust?**

You have the choice between two options:

- Low trust: uploaded photos will need to be approved by an administrator before being visible on the gallery.
- High trust: photos uploaded by contributors will be directly visible on the gallery.

**Other options**

Lastly, you can:

- restrict the number of photos that contributors will be allowed to add (limit per user)
- restrict the storage space used by photos uploaded by contributors (limit per user)

These values are unrestricted by default.

Click on Add: the permission has been created.

If you want to manage different types of contributors with different rights, you need to create multiple permissions.

**Automatic creation of an album by contributor**

If you want, Piwigo can automatically create a new album for every contributor upon their first login.

To do this, go to the Configuration tab in the Community plugin's settings.

![Configuration de Community.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-654efc11.jpg)

If you select this option, you can choose which album the albums specific to each contributor will be created in.

## For contributors: how to add photos on Piwigo with Community?

Users who are authorized to add photos to the gallery have access to a new menu item called "Upload photos" under the "Explore" menu.

![Ajout photos Community.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ba709fad.jpg)

!!! note "Note :"
    The "Upload photos" menu can be displayed on the home page, to the right of the "Explore" menu. To do this, install the Upload 1 Menu plugin. If you are a piwigo.com customer, this plugin is only available from the Team plan and higher.


The Upload photos menu lets you access the photo upload page.

![Ecran ajout photos Community.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1c98b145.jpg)

The user has the option:

- to choose the album in which to add the photos (only authorized albums are accessible)
- to create a new album (if they are allowed to)
- to add photos from their computer (by clicking on Add photos or through drag-and-drop)
- to set the photos' properties (Title, Author, Description) by clicking on "Set photo properties”

The "Start transfer" button sends the photos to Piwigo.

Depending on the level of trust selected during the creation of the user permission, the photos will either:

- Be visible in the gallery instantly
- Or be subjected to approval from an administrator

### Viewing and editing added photos as a contributor

As a contributor, you have access to an "Edit photos" menu under the main "Explore" menu.

This page lets you see the photos you have added. Those that are awaiting approval show the "Waiting" label.

![Menu Edit Photos Community.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a5ba48be.jpg)

This page lets you delete added photos, and add tags to them.

To edit photos, click on the desired photos to add them to the selection, or use the All / None / Invert buttons for selection mode.

Next, click on the "Action" drop-down list to choose which action to perform:

- Deleting selected photos
- Adding tags

![Choisir une action.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a2c8d348.jpg)

## For administrators: how to approve the photos added by contributors through Community?

If you selected the "low trust" option in the Community plugin's settings (see first chapter on this page), the photos added by users need to be approved by an administrator before being posted on the gallery.

There are multiple ways to view the photos that need approval from an administrator.

### Notification by email

The administrators receive an email each time photos are added. This email contains a link allowing them to verify and approve photos directly.

![Notification nouveaux ajouts.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ab56a7a6.jpg)

### Piwigo dashboard

When photos are waiting for approval, the administrators are notified of it through a banner visible from the homepage of Piwigo's administration (the dashboard).

### Approving pending photos

From the link sent via email or accessible from the administration's homepage, you are redirected to Community's settings, in the "Pending Photos" tab.

This tab lists the photos that are waiting for approval.

![Décision photos Community.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-969920ba.jpg)

For each photo, you can see its settings, expand it by clicking on "Zoom", and edit it by clicking on "Edit". This way, you can adjust the image's properties (title, description, album, tags...) before finally uploading it online.

Lastly, you can adjust the photos' privacy level using the drop-down list below the "Who can see this photo?" text (learn more about [privacy levels](privacy-levels.md)). If you are not using privacy levels, juste leave the drop down list on “Everybody”.

Then, simply select the photos and click on "Validate" (upload the photos) or "Reject" (reject the photos' upload).

## Complementary plugins to the Community plugin

Some plugins are useful for Piwigo galleries who use the Community plugin: here is the list.

!!! info "If you are a piwigo.com, this plugins are only available from the Team plan and higher."

### **Upload 1 Menu**

This plugin lets you show the "Upload photos" menu on the gallery's home page, next to the "Explore" menu.

![Upload 1 Menu.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-78529d2b.jpg)

### **See My Photos**

This plugin lets you show a "My photos" menu in the gallery. This way, each user can easily view the photos they have added to the gallery, all albums included.

[Learn more](../customizing-your-gallery/customizing-piwigo-gallery-menu-navbar.md)

### **See photos by user**

This plugin lets the gallery's visitors easily filter photos based on the user who added them.

[Learn more](../customizing-your-gallery/customizing-piwigo-gallery-menu-navbar.md)

### **Photo added by**

This plugin allows you to show the ID of the user who added the photo on its page, under the "Photo added by" field.

![Photo ajoutée par.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0785b63f.jpg)

The plugin's settings let you decide where you want this information to be displayed (right before "Albums" by default).

If the "See photos by user" plugin is activated, you can make the username clickable, to allow access to the page that lists all photos added by this user.

Article summary

---

← Previous

[User groups](user-groups.md)
