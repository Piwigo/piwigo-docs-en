---
title: Users - Piwigo Documentation
description: Introduction to the user concept in Piwigo and user configuration options.
---

# Users: introduction

## Users in Piwigo

Understanding the concept of user is essential in order to use Piwigo correctly.

In Piwigo, a user is any person who visits your web gallery.

As such, a user can be:

- Anonymous: if your gallery contains public albums, a user will be able to view their content without being registered. They will not need to create an account nor log in. They will have **Guest** status. [Learn more](user-statuses.md)
- Registered: a registered user has a user account on Piwigo. Once logged into Piwigo, they are viewing custom content, potentially different from what another user will see. What a user sees on Piwigo depends on multiple criteria:
    - Their status (visitor, administrator, webmaster): [learn more](user-statuses.md)
    - The albums they are allowed to view: [learn more](creating-and-managing-users.md)
    - The group(s) they are a part of: [learn more](user-groups.md)
    - Their privacy level: [learn more](privacy-levels.md)
    - Their preferences: [learn more](creating-and-managing-users.md)

## Users: configuration options

From the Options > Configuration menu, some general options have an impact on user management.

![Permissions utilisateur.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-18d71862.jpg)

- Allow user registration

If you select this option, users will be able to create their account themselves from your gallery. You can subject their registration to approval by an administrator.

If you deselect this option, users will need to be created by an administrator in Piwigo's administration.

- Allow user customization

If you select this option, users will be able to edit their preferences themselves from their account in the gallery, by clicking on the "Customize" menu.

Preferences are visualization options: theme, language, number of photos per page... [Learn more about preferences](creating-and-managing-users.md)

If you deselect this option, users will not be able to edit their preferences.
