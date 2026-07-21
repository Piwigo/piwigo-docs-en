# Permissions and album visibility

In this chapter, we will see how to manage and edit permissions on albums in Piwigo, meaning the albums' status (private / public), and the management of user rights on the albums.

We will also see how we can easily view and edit the albums' properties:

- locked / unlocked albums
- activating comments on albums
- albums which can and cannot be downloaded

## How do permissions work on albums?

When you create an album in Piwigo, who is allowed to view its content? How do you change it? What rules apply to sub-albums?

There are multiple things to know.

### Private albums and public albums

To get started, one must understand that an album can be private or public in Piwigo.

**Public albums** will be visible for all visitors of your photo library who are not logged in (who don't have an account: this corresponds to the special "guest" user).

As soon as a person visits your gallery's website on the Internet without logging in, they can view public albums, and only those albums.

**Private albums**, on the other hand, can only be accessed by identified users, who are connected with their login and password.

For each private album, you will be able to decide who, among users and user groups, is allowed to view it.

!!! info "Info :"
    When creating a new root album in Piwigo, it is always public by default. If you want to change this behavior, contact support if you are a piwigo.com customer. If not, add the following setting to your configuration using [LocalFiles Editor](../self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md): `$conf['newcat_default_status'] = 'private';`

### Editing permissions on an album

To edit permissions on an album, you need to edit this album:

- Either from your gallery, by visiting this album's page and clicking on the edit icon;
- Or from the administration, by going to the album list (Albums > Manage menu) and clicking on the edit icon.

[Learn more about editing albums](editing-an-album.md)

From the album editor, click on the "Permissions" tab. This tab lets you set your album's status (public or private).

![Permissions.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-37a2ed66.jpg)

If you choose to make an album private, you will be able to set who, among the users, is allowed to view its content.

You have the option to grant access rights:

- to one or more user groups
- to one or more specific users

![Accès privé.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-84a5d6f8.jpg)

To learn more about user groups, [read this article](../managing-users/user-groups.md).

!!! warning "Warning!"
    If an album is private, no one will see it in the gallery, not even administrators! Therefore, make sure to grant yourself the rights on any private albums you create.

The "Apply to sub-albums" checkbox lets you edit an album's permissions all at once, and apply these changes to all of its existing sub-albums.

!!! warning "Warning: this change doesn't apply to sub-albums that will be created in the future."

### Rules for permissions in the album hierarchy

When you create a sub-album from a public album, it will be public by default.

When you create a sub-album from a private album, it will be private; furthermore, it will be made accessible to all administrators by default, as for all of its parent albums.

If you make an album public when its parent albums are private, this will automatically make the parent albums public.

If you make an album private when its sub-albums are public, this will automatically make its sub-albums private.

Apart from the status (private / public), sub-albums don't automatically inherit their parent albums' permissions.

Let's take an example: you have a private album, accessible to users X and Y. If you create a sub-album of this private album, it will not be accessible to users X and Y by default (only to administrators).

!!! info "Info :"
    If you want sub-albums to automatically inherit their parent albums' permissions, contact support if you are a piwigo.com customer. Otherwise, add the following setting to your configuration using [LocalFiles Editor](../self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md): `$conf['inheritance_by_default'];`

## Managing album access in bulk (public / private)

To view and modify your albums's access types (public / private) at a glance, go in the administration, in the Albums > Properties menu.

The first tab lets you easily switch an album from public status to private status, and vice-versa.

![Propriétés albums.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-37a751a9.jpg)

On this screen, you can see the list of all albums and sub-albums in your photo library in the column that corresponds to their status (Public and Private).

!!! info "Sub-albums are easily recognizable since their name appears as follows: Root album / Sub-album 1 / Sub-album 2"

To switch an album from public status to private status, you simply need to click on this album and click on the arrow below the first column: it is then moved to the "Private" column. To switch a private album to public, it's the opposite!

You can select several albums, the same way you would in a file on your computer:

- Editing a list of albums that follow each other: Click on the first desired album, then press the Shift key on your keyboard, then click on the last desired album: all the albums in the list are selected
- Editing several albums that don't follow each other in the list: Click on the first desired album, then click on the Ctrl or Cmd key on your keyboard, click on another album, and keep doing so until all the desired albums have been selected.

### Particular case of albums with sub-albums

If you switch an album that has sub-albums to private mode, then all of its sub-albums will also switch to private.

But if you switch a sub-album to public status, then its parent album will also switch to public status automatically, since it is necessary to have access to an album in order to have access to one of its sub-albums.

You can see a concrete example below.

![Propriétés.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9e8786bc.gif)

## Managing album visibility in bulk (locked / unlocked)

To lock or unlock a list of albums in your gallery, go in the administration, in the Albums > Properties menu.

The second tab works exactly the same way as the first one (see previous paragraph), except it allows you to lock / unlock albums.

!!! info "Info :"
    A locked album is inaccessible from the gallery, except for administrators. Most often, the locked status is used when an album is not yet ready to be made public in the gallery, because an administrator is working on it (preparation before publishing, maintenance...). This is therefore a "working", temporary status.

To lock or unlock a single album, you can also simply edit this album.

## Managing comments on albums in bulk

If you have activated comments in your gallery, you can view at a glance which albums are open to comments or not. To do this, go in the administration, in the Albums > Properties menu.

The third tab works the exact same way as the two others (see previous chapters).

To learn more about comments, [read this article](../comments-and-ratings/managing-comments.md).

## Download Permissions: Managing the download rights for each album

By default, in Piwigo, users who are authorized to download photos can download all photos in the gallery.

If you need to manage the rights for each album, you can install the **Download Permissions** plugin.

!!! info "If you are a Piwigo Cloud customer, this plugin is only available from the Enterprise plan and higher."

It will add a new tab to the Albums > Properties page, allowing you to set which albums users are allowed to download photos in, in the same way as the other tabs.

![Téléchargement.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1fd60f62.jpg)

Article summary

---

← Previous

[Editing an album](editing-an-album.md)

Next →

[SmartAlbums](smart-albums-plugin-piwigo.md)
