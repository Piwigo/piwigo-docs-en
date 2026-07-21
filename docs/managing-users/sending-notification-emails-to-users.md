# Sending notification emails to users

You might need to send emails to some Piwigo users, in order to notify them that new photos or new albums have been created.

To do this, you have two main options.

## Notifications on an album

In the administration, you can send an email to users or user groups about a particular album.

This lets them know when a new album is created, or when changes have been made.

To do this, you need to go to Albums > Manage, edit the album in question, and go to the "Notification" tab.

This tab lets you set the users or user groups to be notified, and the content of the additional message if needed.

![Notification sur album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7f0dc72d.jpg)

The people involved will receive an email containing a link to the album, along with your message.

![Email de notification.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-fed62f4c.jpg)

!!! warning "Warning :"
    Before sending a notification, remember to make sure users have access to this album in the Permissions tab.

## Global notifications

You can also set up emails to inform users of all the new content in the gallery since their last login.

!!! warning "Warning : only users who have the "Webmaster" status can access this feature."

To do this, go into Users > Notification.

### Email settings

The first "Settings" tab lets you define the settings of the emails sent:

![Paramètres email.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7419dacb.jpg)

- Send mail in HTML format: if you select "Yes", the email will be formatted with links, images, and colors. If you select "No", the email will be sent as raw text.
- Send mail as: this is the name of the sender that will be displayed in the email. By default, it is the name of your Piwigo gallery.
- Add some detailed content: if you select "Yes", the email will contain details about the changes performed (number of new photos, of albums updated, of new users).
- Complementary mail content: lets you set a custom message that will be added by default to the emails sent.
- Include display of recent photos grouped by dates: if you select "Yes", the email will contain all new photos added, by upload date.

### Setting which users to notify

The "Subscribe" tab lets you decide which users will receive notification emails.

To subscribe or unsubscribe users, move them to the left column by clicking on the orange arrows.

![Abonnement notifications.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-3f0dd524.jpg)

When a user is subscribed, they get a confirmation email. If they want, they can unsubscribe.

![Notification abonnement.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8f0f2f3c.jpg)

### Sending a notification email

The "Send" tab lets you trigger the sending of an email.

![Envoi de mail.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b08ba16a.jpg)

The "Select recipients" tab shows the users that are subscribed to the notifications, and are involved (meaning there have been new content on Piwigo since the last notification they received). You can select or deselect which users you want to send an email to.

The "Complementary mail content" section shows the default message specified in the settings and lets you customize it.

Click on "Send" to trigger the sending of the email.

![Nouvelles photos.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-db8a2c92.jpg)

## Protect Notification: Editing the sender of notification emails

Sometimes, notification emails sent by Piwigo may land in the spam folder. This comes from the fact that they are sent using the main administrator's (webmaster's) email address. Since the piwigo.com server isn't allowed to send emails from this email address, the emails are considered to be unsafe.

To solve this problem, you can install the **Protect Notif** plugin.

Once this plugin has been activated, all notification emails sent by Piwigo will be sent from a fake email address such as "no-reply@photolibrary.piwigo.com".

Therefore, the notification emails will be delivered properly.

!!! info "Since February 2024, Protect Notif is activated by default on all new accounts created on Piwigo Cloud."
