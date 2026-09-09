---
title: "Two Factor Authentication: enable 2FA on Piwigo"
description: "How do you log in to your Piwigo account? What are the options for creating an account and logging in? Everything is explained in this article."
---

# Two Factor Authentication: enable 2FA on Piwigo

Table of content:

Since Piwigo version 16, users can enable two-factor authentication (*2FA*). This is a strong authentication method, increasingly used today. When 2FA is enabled, users must go through two steps to access Piwigo:

- Step 1: standard login (username + password)
- Step 2: identity verification, either via an email code or an authentication app generating a one-time code (TOTP)

To enable two-factor authentication, you need to install and activate the **Two Factor Authentication** plugin.

## Configuring the **Two Factor Authentication** plugin

Go to the plugin settings to configure two-factor authentication.

![image.png](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-29507eb1-sm.png)

Several options are available:

- **Maximum number of failed attempts before lockout:** if a user tries to log in unsuccessfully several times, their account will be locked. Set the maximum number of attempts here.
- **Lockout duration (in seconds):** the period during which the account remains locked once the limit of failed attempts is reached.

Two methods can be used for two-factor authentication:

- **2FA by application:** users must use an authentication app that generates a one-time code (TOTP)
- **2FA by email:** users receive a one-time code via email

You can enable both methods if you wish: users will then be able to choose the one they prefer.

## User activation of two-factor authentication

Once 2FA is enabled through the plugin, it is **not** activated by default for Piwigo users.

Each user must activate 2FA from their own profile.

To do this, users must go to their Piwigo gallery, then open the Profile page.

![image.png](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9310ab1e-la.png)

Click the arrow next to “Two-factor authentication” to show the available options. You can then choose the preferred authentication method.

Note: if only one method was enabled in the plugin settings, only that one will appear here.

![image.png](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f5e7bfae-me.png)

## Using two-factor authentication with an authentication app

If you choose this method, you will need an authentication app such as 1Password, Authy, Microsoft Authenticator, TOTP, or any other app capable of generating one-time login codes.

First install the app of your choice on your phone if you haven’t already. This documentation illustrates the process using the free TOTP app (available for iOS and Android).

Go to your profile and select “Setup using an authentication app”. Instructions will appear.

![Capture d’écran 2025-11-17 à 17.18.35.png](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5eb07cca-me.png)

Open your authentication app on your phone and add your Piwigo account by scanning the QR code displayed on your screen.

![IMG_4248.jpg](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-241841b6-la.jpg)

Once added, the app generates a one-time code.

![IMG_4249.jpg](https://ressources.piwigo.com/picture?/1863/category/172-two_factor_authentication_enable_2fa_on_piwigo)

Enter this code in the dedicated field on your Piwigo profile.

A confirmation message then appears.

![Capture d’écran 2025-11-17 à 17.28.03.png](https://ressources.piwigo.com/_datas/c/v/7/cv7jpz6hf8/i/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1c48becb-sm.png)

Copy your recovery codes and store them in a secure place that you will remember (a note, a document, an email, etc.).


!!! warning "**Warning**"

    Once two-factor authentication is enabled, third-party apps connecting to your Piwigo account (Piwigo mobile apps, Lightroom plugin, Piwigo Remote Sync) will no longer be able to log in using your usual username and password. [Read the last chapter of this page to remedy this.](#connecting-third-party-applications-when-2fa-is-enabled)

## Using two-factor authentication by email

!!! warning "**Warning**"

    This method is less secure. Emails can end up in spam, or fail to send if your server is not properly configured. If you enable this method, make sure emails sent from your Piwigo installation reach their destination.

Once email-based 2FA is enabled in the plugin settings, go to your profile and select “Setup using email”. Verify that the email address linked to your account is correct, enter it again in the “Confirm your email” field, and click **“**Send email**”**.

![Capture d’écran 2025-11-17 à 17.49.36.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f744751a.png)

Check your inbox, and when you receive the code, enter it in the appropriate field.

![Capture d’écran 2025-11-17 à 17.51.08.png](Two%20Factor%20Authentication%20enable%202FA%20on%20Piwigo/Capture_decran_2025-11-17_a_17.51.08.png)


!!! warning "**Warning**"

    Once two-factor authentication is enabled, third-party apps connecting to your Piwigo account (Piwigo mobile apps, Lightroom plugin, Piwigo Remote Sync) will no longer be able to log in using your usual username and password. [Read the last chapter of this page to remedy this.](#connecting-a-third-party-application-with-your-api-key)

## Connecting third-party applications when 2FA is enabled

When 2FA is active, third-party applications cannot log in using only your username and password.

Until they implement API-key authentication or native 2FA, Piwigo provides a workaround allowing these apps to continue working without updates.

**If a user enables 2FA and wants to keep using the Piwigo mobile app, Piwigo Remote Sync, or the Lightroom export plugin, they must follow the instructions below.**

### Creating an API key in your profile

Go to your Piwigo gallery and open your Profile page.

![image.png](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9310ab1e-la.png)

Click the arrow to expand the API keys section.

Create a new API key and name it after the application you want to connect—for example *“Piwigo mobile iOS”*.

Choose the validity period for this key. Once expired, you will need to generate a new one and repeat the process.

![Capture d’écran 2025-11-17 à 17.54.07.png](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4c54c8e2-sm.png)

Click **“**Generate key**”**. Piwigo will display an **ID** and a **secret**, which you **must copy and store securely** (a note, document, email, etc.).

![Capture d’écran 2025-11-17 à 17.55.23.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-fb3ad674.png)

### Connecting a third-party application with your API key

Open the third-party application you want to use (for example, the Piwigo mobile app).

Instead of your username, enter the API key **ID** (starting with “pkid-…”), and instead of your password, enter the **secret** of the API key.

You will then be logged in and recognized as the user associated with that key.

!!! note "**Note**"
    API keys have an expiration date. Make sure to renew them regularly. Piwigo will notify you by email when one of your keys is about to expire.
