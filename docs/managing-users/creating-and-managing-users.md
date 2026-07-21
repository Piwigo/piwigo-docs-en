# Creating and managing users

## Viewing and managing users

To create, edit, delete users in Piwigo's administration, you need to click on Users > Manage in the left menu.

![users.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b8726ada.png)

The first tab lists the users created in your Piwigo gallery and lets you perform a certain number of actions.

- Create a user
- Search a user
- Edit a user
- Edit multiple users in bulk
- Edit the guest user (anonymous)

!!! info "Piwigo 15, you can sort the list of users displayed by name or creation date by clicking on the column heading."

## How do I create a new user in the administration?

To create a new user in Piwigo's administration, click on "Add a user" in the list of users: a pop up opens.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-84899d98.png)

This pop up lets you set the following details for your user:

- username (login to Piwigo)
- email
- status (learn more about [user statuses](user-statuses.md))
- privacy level (learn more about [privacy levels](privacy-levels.md))
- group(s) (learn more about [user groups](user-groups.md))
- permission to upload files to gallery

By default, new users inherit the same preferences as the “Guest” user (discussed [later in this page](https://app.notion.com/p/Cr-er-et-g-rer-les-utilisateurs-3e044cd69819423e8160c30f1b1d03e2?pvs=21)).

Once you have created a new user, you can edit it to customize its profile.

Since Piwigo 15, when you create a new user in the administration, a link is automatically sent to the user's e-mail address so that he or she can choose a password.

## How to edit a user?

To edit a user from the user list, simply click on the pen-shaped icon to the left of the name in the user list. The selected user is highlighted using the orange color.

![Modifier utilisateur.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8503e72b.jpg)

The user editing screen then opens.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-47138217.png)

This screen allows you to modify many user parameters and view certain information.

This information is grouped into 3 parts:

- main information on the left
- properties tab on the right
- preferences tab on the right

Some plugins add new tabs to this screen.

## Change username and password

The left-hand section of the screen lets you change a user's login and password.

**Username**

The user name appears at the top left of the window.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-dffce812.png)

Click on the pencil icon to modify it; the user name then becomes editable in a window.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-69830722.png)

!!! warning "The username is also the identifier that allows users to login to Piwigo.  Do not change it without notifying users."

**Password**

Click on “password” to open the screen below.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ac1b797f.png)

This window allows you to :

- copy the password reset link for forwarding to a user (if e-mailing the link doesn't work)
- resend the password reset link by e-mail
- change a user's password

### Editing user permissions on albums

In Piwigo, you can set whether an album is private or public. If it is private, then only authorized users will be able to see it in the gallery.

To learn more about album permissions, [read this article](../organizing-albums/permissions-and-album-visibility.md).

From a user editing window, click on “Permissions” to view and edit the albums a user is allowed to view.

![permissions.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-05e4f72a.png)

The screen then opens as a window listing private albums:

- on the left, the ones the user is allowed to view
- on the right, the ones they aren't allowed to view.

To edit which albums the user has access to, simply move them from one column to the other by clicking on the arrows.

![Gérer les permissions.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c0ac9326.jpg)

!!! info "If the user is part of a group, individual permissions have priority over group permissions. [Learn more about user groups](user-groups.md)"

### Delete a user

The user modification screen lets you delete a user by clicking on the “trash” icon.

![delete-user.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1f997a1a.png)

An intermediate screen lets you confirm your choice.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bc6416fc.png)

### Change the main user of your Piwigo

The “main” Piwigo user is by default the first user:

- the one who installed Piwigo, if your gallery is self-hosted;
- the one who created the account, if you use an account on [piwigo.com](http://piwigo.com/).

This user has “webmaster” status.

It is represented by a crown in the user list.

![main.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bce6eb27.png)

Once a user has the status “webmaster”, he or she can be chosen as the main user, by clicking on the “crown” icon in the user modification window. If you confirm, he/she will replace the current main user (there can only be one main user in a Piwigo account).

![main2.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-035e918b.png)

### Edit user properties

The “properties” tab lets you modify the properties defined when the user was created.

![properties.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c727020f.png)

**Email address** 

You can edit a user's email address from this window. Don't forget to click on "Update" to save the changes.

**Status**

You can edit a user's status, namely after its creation, to change it to Administrator, Generic, Webmaster…

To learn more about the roles and the rights associated with each status, [read this article](user-statuses.md).

There are some limitations:

- The administrator that is logged in can't modify their own status
- If you want to change the status of the first Piwigo user (main user), you must first define a new main user (see below).

**Privacy level**

By default, privacy levels aren't used in Piwigo. You can therefore ignore this setting, except if you have a very specific need.

[Learn more about privacy levels](privacy-levels.md)

**Group**

You can associate a user with one or more existing groups from the user editing window.

[Learn more about user groups](user-groups.md)

**Allow download**

Check this box if you allow a user to download the original version of a photo in your gallery.

If you uncheck this option, the user will be able to view photos in the gallery, but the download icon will be hidden.

### Edit user preferences

Preferences change the Piwigo gallery's appearance depending on the users.

From the user modification screen in administration, the “Preferences” tab lets you modify these settings.

![preferences.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-af0c4e19.png)

Users can also modify them themselves when logged into the gallery, by clicking on the “Customize” menu.

!!! info "Info : "
    The editing of preferences by users through the gallery can be deactivated in Piwigo's options (by deselecting the "Allow user customization" option). In this case, the "Customize" menu is only used to edit one's email address and / or password.

To change the default preferences applied to new users, modify the “guest” profile (see later).

Lastly, you can edit the preferences of a list of users in bulk by using Selection mode (see chapter [Editing users in bulk](creating-and-managing-users.md)).

Here are a few details about preferences.

**Photos per page**

This is the number of photos shown on a page in the gallery (on an album's page for example). By default, this number is set to 15, which means that beyond 15 photos on a page, page links will be displayed. You can increase or decrease this number.

**Theme**

In most cases, Piwigo galleries only use one theme. This setting is therefore not to be edited. It is only useful if you have installed multiple themes in your gallery, and you want to display different themes depending on the user.

[Learn more about themes](../piwigo-themes/index.md)

**Language**

In each gallery, a default language is set, but you can install several of them.

This way, this setting lets you choose which language will be used for Piwigo's interface for a given user, among the languages activated in the gallery.

[Learn more about languages](../customizing-your-gallery/managing-languages-available-gallery-piwigo.md)

**Recent period**

This is the photos' display period when the user clicks on the "Recent photos" menu in your gallery. This period, set to 7 days by default, can be edited.

**Expand all albums**

By default, this option is deactivated, which makes the Albums menu in the gallery only list root albums (not sub-albums).

![Tous les albums.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c79788c4.jpg)

If you select this option, the menu will show the entire tree structure.

![Albums étendus.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-70e5457c.jpg)

**Show number of comments**

This option lets you display the number of comments of each photo under the thumbnail on listing pages in the web gallery.

!!! info "This option is compatible with some themes (Elegant, Bootstrap Darkroom) but not with the Modus theme."

![Nombre de commentaires.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4d3944cc.jpg)

**Show number of hits**

This option lets you display the number of visits of each photo under the thumbnail on listing pages in the web gallery.

!!! info "This option is compatible with some themes (Elegant, Bootstrap Darkroom) but not with the Modus theme."

![Nombre de visites.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2d39be8e.jpg)

## How to see a user's history?

The user modification screen displays a user's creation date and last login date. It also gives access to the user's visit history by clicking on the “Visit history” button.

![history.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-02660928.png)

### Visit history

The "Visit history" button lets you open this user's visit history. This lets you see which albums have been viewed, which photos have been viewed and downloaded.

[Learn more about the visit history](../administration-piwigo/viewing-statistics-piwigo-gallery.md)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-94c3e836.png)

### Administrator activity

To view the detailed history of all actions of a user in the administration, you need to go to the Activity tab in the Users page.

[Learn more about the activity history](../administration-piwigo/viewing-statistics-piwigo-gallery.md)

!!! info "If you are a Piwigo Cloud customer, this plugin is only available from the Enterprise plan and higher."

![Liste activité.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-49d3aeab.jpg)

## Searching for a user

The user list lets you perform a search to easily find a user if you have a lot of them.

A search engine lets you find a user through its username. Type a few letters in the search engine: the list is automatically updated.

![Recherche utilisateur.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e43e94df.jpg)

You can also click on the Filters button to show search criteria.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7d4e82c2.png)

You can filter the user list by:

- Status (Webmaster, Administrator, Visitor…)
- Privacy level
- Group
- Registration date (user creation)

## Edit users in bulk

Do you need to apply changes to a selection of users?

To do this, simply click on the "Selection mode" button from the user list, on the right of the screen.

![Mode sélection utilisateurs.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e6522118.jpg)

Once selection mode has been activated, you can select users you want to edit: they appear in a list on the right of the screen, one after the other. In the event of a mistake, you can remove a user from the selected list by clicking on the cross next to its name.

At the top of the screen, the buttons named The whole page / The whole set / None / Invert allow you to go faster with the selection if you have a lot of users to manage.

- Clicking on "The whole page" adds all users visible on screen to your selection list
- Clicking on "The whole set" adds all users of your Piwigo gallery to your selection list
- Clicking on "None" empties your selection list
- Clicking on "Invert" adds all users to the selection, except the ones currently selected.

![Choisir action utilisateurs.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-27a15512.jpg)

Once your user selection is done, click on the action of your choice:

- Delete selected users
- Associate to group / dissociate from group
- Allow download
- Privacy level
- Edit preferences (number of photos per page, theme, language, recent period, expand all albums, show number of hits)

## Edit “guest” settings

The user management page lets you edit the guest user.

The “guest” user corresponds to the profile of anonymous visitors to the gallery, who view it without being logged in to Piwigo. But that's not all: the settings for this user are also the default settings for all new users.

To modify this guest profile, click on “Edit guest user”.

![Modifier utilisateur invité.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-867edb0e.jpg)

This will open a window that resembles the user editing window.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-abd5d211.png)

## Allowing or disallowing account creation for gallery visitors

Depending on the way you use your Piwigo gallery, you can accept or refuse that users create an account themselves.

For example :

- Companies and organizations that manage a private photo library with Piwigo don't want a person from outside the company to be able to create an account: users are always created by an administrator.
- Some organizations (tourist offices, for example) allow authorized people (journalists, partners, schools...) to create an account on their photo library to access copyright-free images, but they want this account creation to be approved by an administrator.
- Other photo library managers make part of their content available to the public, but want users to create an account before accessing the gallery, to better understand how their content is used and collect data about the people who are interested.

This way, Piwigo lets you set the rules of your photo library in terms of account creation by visitors.

To do this, go to the administration, in the Configuration > Options menu, in the Permissions section.

![Permissions tous admins.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-837c1808.jpg)

One option is offered: **Allow user registration**.

Selecting this option will show a "Register" link in your gallery, allowing a user to fill out a form to create an account in your gallery.

The associated option to "Email admins when a new user registers" makes it so that every time a person creates an account on your gallery, the administrators will receive an email. This way, they will be able to verify that the person is authorized to register, and to grant them the desired permissions, add them to a group, etc.

You can choose to notify all administrators when creating a new account, or only the members of a group.

## User Mass Register: creating users in bulk

If you want to create multiple users at once, you need to activate the **User Mass Register** plugin.

This plugin lets you create users in bulk from a list of email addresses. The users are created with the User status by default.

You can then edit these users in bulk using selection mode (see chapter: [Editing users in bulk](creating-and-managing-users.md))**.**

!!! info "If you are a Piwigo Cloud customer, this plugin is only available from the Enterprise plan and higher."

## Add User Note: Adding a comment to a user

To add a note or a comment to a user, you can activate the **Add User Note** plugin.

!!! info "If you are a piwigo.com customer, this plugin is only available from the Team plan and higher"

This plugin adds a “Notes” tab to a user's edit window.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6a142b84.png)

When a note has been entered on a user, an icon appears next to its name in the list. By hovering the mouse over this icon, you will be able to read the note.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e1ff79d6.png)

## User Custom Fields: Adding custom fields to users

You can create custom fields associated with users.

!!! info "If you are a piwigo.com plan customer, this plugin is only available from the Team plan and higher."

To do this, you need to activate the User Custom Fields plugin.

The benefit of this plugin is that it allows you to request additional information from people who are registering on your gallery (when you have activated this feature). The additional fields can be mandatory or not.

In the example below, we have added the "City" field in the gallery's registration form.

![User Custom Fields.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-cc40ba03.jpg)

When this plugin is activated, a "Custom fields" tab appears on the user editing window.

Clicking on this button lets you view and edit the custom fields’ content.

## Crypto Captcha: Preventing the creation of fake users

To prevent robots from creating fake users in your gallery, you can install the **Crypto Captcha** plugin.

This plugin forces users to enter a Captcha before creating an account. This Captcha can also be added to the comment posting form.

Several options are available to set up your Captcha.

![Test Captcha.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ac638942.jpg)
