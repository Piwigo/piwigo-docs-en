# Log in to Piwigo

## How to log in to Piwigo ?

To log in to your Piwigo account, you need to go to your gallery's URL (web address). 

If you are using Modus, the default theme installed with Piwigo, a "Login" link is available in the top right corner of your screen. This link opens the window that allows you to log into Piwigo.

![Ecran connection.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-546099ea.jpg)

If you are using the Bootstrap Darkroom theme, the login button opens a modal window but doesn't open a new page.

![Login BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-263eca8d.jpg)

!!! tip "Depending on the theme and your gallery's customization, the login screen might be different from what is shown in the previous images."

The URL of your Piwigo log in page is [`mygallery.com`](http://mygallery.com)/identification.php, `mygallery.com` representing the root URL of your gallery. 

If your gallery is hosted on piwigo.com and you have not customize your gallery’s domain name, your log in URL looks like `mygallery`.piwigo.com/identification.php, `mygallery` representing the username you have chosen when you first created your account.

To log into Piwigo, you can use your username OR your email address in the "Username" field.

You also need to enter your password.

Once logged in, you are redirected to your gallery.

## How to display a login form on the home page?

If you want the home page to display a login form directly, it is possible using the **PWG Stuffs** plugin.

[Learn more](../browsing-your-piwigo-gallery/tags-in-your-gallery/pwg-stuffs-plugin-piwigo.md)

## How to log in to Piwigo's administration?

If you are logged in to your Piwigo gallery as an administrator, you simply need to click on the Admin menu from your web gallery in order to switch to the administration.

By default, if you are using the Modus theme, the Admin menu is located in the top right corner of your screen.

![Admin Modus.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5b6e4744.jpg)

If you are using the Bootstrap Darkroom theme, the administration access menu can be reached by clicking on your username in the top right corner.

![Admin BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f4e53a6c.jpg)

## How to recover your Piwigo password?

If you lost your password, it cannot possibly be retrieved, whether you are a piwigo.com customer, or using a self-hosted Piwigo gallery. For this reason, you need to reset your password.

To reset your password, you need to go to your Piwigo's login window and click on "Forgot your password?".

Upon entering your username or your email address, you will receive a link via email to reset your password.

You can also ask an administrator to send you an email with a link to reset your password, or to set a new password for you and send it to you.

## How to recover your Piwigo username or connexion email address?

So you forgot your username and / or the email address you use to log into Piwigo?

No need to panic: there are multiple ways to retrieve your account.

### Ask an administrator

If you work within a team, get in touch with the main administrator of your Piwigo gallery: they will be able to retrieve your account.

You can also search in your inbox for the email that was sent when creating your account.

### Recover the login credentials received by email when creating the account

If you are the only user of your Piwigo gallery, or if you are the main administrator (the webmaster), you should have received your login credentials by email.

- If your Piwigo gallery is hosted on [piwigo.com](http://piwigo.com/): you have received an email when creating your Piwigo account.
- If you are using a self-hosted Piwigo gallery: when installing Piwigo for the first time, if you went through the install form, you may have selected the option to "receive my credentials by email".

### Are you really struggling to log in to Piwigo?

If you have an account on piwigo.com, reach out to support: we will find a way to retrieve it.

If you are using a self-hosted Piwigo gallery, sadly, we can't help you. However, if you have access to Piwigo's database, you can retrieve your username in the Users table.

## How to create a new account on a Piwigo gallery?

There are two options in order to create a new user on Piwigo.

### Case n°1 : an administrator is creating user accounts

In some cases, the option to "Allow user registration" has been deactivated (this option is available in the Configuration > Options menu, General tab, Permissions section).

In this case, it is impossible for a visitor of the gallery to create their account on their own: only an administrator can create new users. 

To learn how to create a user in the administration, [read this article](creating-and-managing-users.md).

### Case n°2 : the gallery's visitors can create their account

If the option to "Allow user registration" has been activated, any visitor of the gallery will be able to create their account.

!!! info "To learn more about allowing or disallowing account creation for gallery visitors, [read this article](creating-and-managing-users.md)."


To create a new account on a Piwigo gallery, you need to click on Login.

A "Register" button lets you create a new account.

To create a new account, you need to give a username, an email and a password.

!!! info "If you want to add custom fields to the account creation form, you need to activate the User Custom Fields plugin. [Learn more](creating-and-managing-users.md)"


!!! info "If you want to avoid the creation of fake users by robots, you can monitor account creation using a Captcha input. To do this, you need to activate the **Crypto Captcha** plugin. [Learn more](creating-and-managing-users.md)"


User accounts created independently bu users on the gallery are not administrators but simple Users. To learn more about user statuses, [read this article](user-statuses.md).

## How to enable two-factor authentication (2FA) on Piwigo?

Since version 16 of Piwigo, it has been possible to enable two-factor authentication (2FA) for users. This is a strong authentication method that is increasingly used today. When two-factor authentication is enabled, users will have to go through two steps to access Piwigo:

- Step 1: standard identification (login + password)
- Step 2: verification of their identity, either by sending an email or using an application that generates a one-time code (TOTP)

To set up this two-factor authentication system, you must install and activate the **Two Factor Authentication** plugin.

Click below to read the documentation for this plugin:

[Two Factor Authentication: enable 2FA on Piwigo](user-groups.md)

## How to turn on single sign on (SSO) in Piwigo?

If you are working within an organization, you may already be using a user and password management system. For this reason, you want users to be able to log into Piwigo automatically.

There are two ways to do this: with the **LDAP Login** plugin and with the **Microsoft 365 Connect** plugin.

### LDAP Login: using an LDAP directory

This plugin lets you connect Piwigo to an LDAP directory.

!!! info "If you are a Piwigo Cloud customer, this plugin is only available from the VIP plan and higher."

### Microsoft 365 connect: connecting Piwigo to an Azure Active Directory

This plugin lets you connect Piwigo to an Azure Active Directory.

!!! info "If you are a Piwigo Cloud customer, this plugin is only available from the VIP plan and higher."

This way, users can user their Microsoft 365 account to log into Piwigo.

- The Piwigo user's email address must correspond to the Microsoft 365 account's email address.
- You first need to register your Piwigo App in the Azure portal (explanation on the plugin's configuration page).

## **Password Policy: Setting security rules for passwords**

The **Password Policy** plugin lets you set up security rules on passwords: strength score, renewal policy, management of failed login attempts…

!!! info "If you are a Piwigo Cloud customer, this plugin is only available from the VIP plan and higher."

Once the Password Policy plugin has been activated in your Piwigo gallery, go to its configuration.

The plugin's **Configuration** tab lets you define security rules.

![Password Policy.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-69207d70.jpg)

Therefore, on this page, you can:

- Activate the reinforcement of password security
- Set the minimum score to reach for a password to be approved

A score below 100 is considered to be weak. A score between 100 and 500 is within the average. A score over 500 is excellent. The score depends on various settings (length, type of character used).

- Test a password and obtain its score
    
!!! info "For example, the password `piwigo12` gets a weak score (48) while the password `Xhj89^h5M%` gets an average score (286)."
    
- Set whether or not the password reinforcement rule is activated for administrators
- Activate the password renewal rule (in this case, the administrator will be able to force users to renew their password)
- Activate the management of failed attempts: after a customizable number of attempts, the access to the gallery will be locked. The message shown can be customized.
    
    ![Message d'information.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-25072184.jpg)
    

The Management tab lets you manage password renewal requests and unlock locked accounts.

![Gestion utilisateurs PP.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c5454ae0.jpg)

Article summary

---

← Previous

[Users: introduction](users-introduction.md)

Next →

[User statuses](user-statuses.md)
