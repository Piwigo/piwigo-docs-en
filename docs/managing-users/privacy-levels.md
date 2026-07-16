# Privacy levels

## Privacy levels: what for?

In order to determine which users have access to what content in Piwigo, the most common and most practical solution is to use permissions on albums.

As a reminder, an album can be private or public, and the users and user groups either have or don't have access to each private album. [Learn more about album visibility](../organizing-albums/permissions-and-album-visibility.md)

This way, when a user is logged into your gallery, they are only viewing albums they have access to.

But in some cases, you might need to manage a finer level of rights, file-by-file, beyond albums. This is what "privacy levels" are useful for.

<aside>
⚠️ Warning! This is one of Piwigo's advanced features, which we don't recommend using if you are a beginner.

</aside>

## Privacy levels: how does it work?

In Piwigo, each file can be associated with a privacy level.

Therefore, when you are editing a photo, you can set its privacy level using the field titled "Who can see this photo?" (by default: Everybody).

![Niveau de confidentialité.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-abb3ba46.jpg)

When dropping the list down, you can choose the privacy level assigned to this photo.

![Niveaux de confidentialité.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e8767701.jpg)

When using privacy levels, each user will also need to be associated with a privacy level:

- Admins (warning: this doesn't have anything to do with the Administrator status)
- Family
- Friends
- Contacts
- None (by default)

The users with the highest level (Admins) will have access to everything.

The "Family" users will only have access to photos associated with the "Family", "Friends", and "Contacts" privacy levels.

The "Friends" users will only have access to the "Friends" and "Contacts" levels.

The "Contacts" users will only view files with the "Contacts" level.

And users with the "None" status will only have access to files accessible for "Everybody".

This is a "cascading" model of right management, somewhat hard to understand and relatively "rigid", which is why we tend to not recommend it to beginner-level users.

<aside>
ℹ️ If you don't like the Admin, Family, Friends, and Contacts labels, you should know that they can be customized by reaching out to support if you have a piwigo.com account, or by editing them in the database if your Piwigo is self-hosted. However, adding another privacy level is impossible.

</aside>

Article summary

---

← Previous

[Creating and managing users](creating-and-managing-users.md)

Next →

[Sending notification emails to users](sending-notification-emails-to-users.md)