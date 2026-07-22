---
title: User statuses - Piwigo Documentation
description: Administrator, User, Webmaster... What are the different user statuses in Piwigo and what are they for?
---

# User statuses

To understand user management in Piwigo, the first thing to know is how **Statuses** work.

In Piwigo, there are 5 statuses, which grant different rights. A user always has one of these 5 statuses.

Here is the list of statuses.

## 1- Administrator

An administrator has access to all data located in Piwigo, and, above all, has access to the administration space:

- adding, editing and deleting albums,
- adding, editing and deleting photos,
- adding, editing and deleting users,
- managing tags,
- viewing statistics and history of actions in the gallery,
- managing comments.

However, they don't have access to the gallery's theme configuration, nor the addition of plugins.

In most organizations, administrators are the photo library's managers: documentalist, communication manager, photographer…

!!! info "Info : "
    An administrator has access to all albums and all photos in the administration. However, once logged into the web gallery, permissions are applied: they only see public albums or private albums they have access to.

## 2- User

A User can log into your Piwigo gallery, but not the administration. By default, when you create a user, or when a user registers on their own, they have “User” status.

A User can view and download the files in your photo library they are entitled to, but they cannot add photos to Piwigo (except with the [Community](community-plugin-piwigo.md) plugin).

Within an organization, in most cases, the majority of users have this status: they are the ones who log into the photo library to search for and download files they need.

## 3- Webmaster

By default, the first user created when creating a Piwigo account or installing a Piwigo (main user) has webmaster status.

Webmasters have the same rights as the administrator, but also other rights: activating or deactivating plugins, changing the theme, accessing the gallery's configuration options…

## 4- Generic

This status can be useful when multiple people share the same user account.

Generic profiles have access to your gallery but not the administration, just like Users, but with some specific features (no ability to edit the password or the display language, for example).

## 5- Guest (deactivated)

Users with this status can't log into Piwigo.  

This status is useful to deactivate a user's account without deleting their history.

!!! warning "Not to be mistaken for the "guest account" or "guest", which is the generic name given to the profile of anonymous visitors (not logged into the gallery): see below"


## Special case: the “Guest” user

The Guest user is a "ghost" user in Piwigo. This corresponds to users who are visiting your gallery and are not logged in.

In the administration, you can determine the permissions and settings applied to these users. They will be applied by default to all new users created afterwards: therefore, these are Piwigo's "default" settings.

To learn how to edit the "Guest" account, [read this article](creating-and-managing-users.md).

## Contributor status (Community plugin)

In our [pricing plans](https://piwigo.com/pricing), we refer to the “Contributor” status.

This status is not a user type in the strict sense: it refers to non-administrator users who are authorised to import files into Piwigo when the Community plugin is enabled.

For more information, read this article: [Managing contributors (Community plugin)](community-plugin-piwigo.md)
