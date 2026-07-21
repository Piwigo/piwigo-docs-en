# Plugins for administrators

In addition to Piwigo's standard administration features, some further options are available through plugins.

We are going over them on this page.

## Admin Tools: Administrating Piwigo from your gallery

The **Admin Tools** plugin allows administrators to perform some administration tasks directly from the gallery (photo editing, album editing...).

Once the Admin Tools plugin has been activated, you will see a new browsing bar appear in your gallery when you are logged in as an administrator. 

![Plugin admin tools.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6a2bdf6f.jpg)

This tool bar lets you access the main administration pages from your gallery.

From a photo's page, you have access to shortcuts to administration actions that will appear:

- edit the photo
- choose the photo as thumbnail for the album
- add to cart

![Admin tools barre.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-874eee94.jpg)

A quick edition window lets you edit the main details about the photo without going through the administration.

The same features are accessible from the albums' pages.

Lastly, other tools are accessible to the right of the Admin Tools bar:

![Outils supp.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-3f7e0949.jpg)

- View as: to view the gallery from the point of view of another user
- Quick theme switch
- Quick language switch
- The other options will only be used by developers.

## Admin Messages: Adding a welcome message in the administration

!!! info "If you are a Piwigo Cloud plan customer, this plugin is only available from the Enterprise plan and higher"

The **Admin Messages** plugin lets users add messages on the home page in Piwigo's administration (to communicate with the other administrators).

The messages are displayed on the dashboard, at the bottom of page.

For each message, we show the administrator's name, the date, and the message.

![Messages admin.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e0045482.jpg)

## Protect Notification: Changing the sender of notification emails

Sometimes, notification emails sent by Piwigo may land in the spam folder. This comes from the fact that they are sent using the main administrator's (webmaster's) email address. If your server (or the piwigo.com server if you are a customer) isn't allowed to send emails from this email address, the emails are considered to be unsafe.

To solve this problem, you can install the **Protect Notif** plugin.

Once this plugin has been activated, all notification emails sent by Piwigo will be sent from a fake email address such as "no-reply@[`mygallery.com`](http://mygallery.com)" (replace `mygallery.com` by your domain name).

Therefore, the notification emails will be delivered properly.

!!! info "Since February 2024, Protect Notif is activated by default on all new accounts created on Piwigo Cloud"


## Download Limits: Restricting the number of downloads per day

!!! info "If you are a Piwigo Cloud plan customer, this plugin is only available from the Enterprise plan and higher"

The **Download Limits** plugin lets administrators restrict the number of downloads per day on their gallery.

!!! warning "Warning :"
    The maximum number of downloads isn't customizable in Piwigo's interface but in a configuration file. If you are a Piwigo Cloud customer, contact support to set it up.


## Export Data: Exporting your Piwigo gallery's data

!!! info "If you are a piwigo.com plan customer, this plugin is only available from the Team plan and higher"


The **Export Data** plugin lets administrators export data from Piwigo to a spreadsheet.

The following data can be exported:

- Albums
- Photos
- Comments
- Downloads

The data are exported in a .CSV file.

## FCK Editor: Adding a WYSIWYG editor to Piwigo

The **FCK Editor** plugin lets you add an HTML editor with format options on most input fields in Piwigo's administration:

- “Description” fields on albums and photos
- Custom pages (available with the **Additional Pages** plugin)
- Custom blocks (available with the **PWG Stuffs** plugin)

You can see below how to format a photo's description with FCK Editor.

![Description avancée.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-06abbf51.jpg)

By default, the basic version of FCK Editor is displayed on most pages, so the available features are limited. However, it is possible to enable more features, as shown in the screenshot below.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-93cd3f42.png)

**How to enable all these features?**

- If your Piwigo is hosted on piwigo.com, contact support.
- If you are self-hosting Piwigo, follow the tutorial below.
- Click here to display the tutorial
    
    The configuration of FCK Editor can be found in the file `plugins/FCKEditor/fckeditor.tpl`.
    
    Edit this file and look for the following code:
    
    ```jsx
    CKEDITOR.config.toolbar_Basic =
    [
      ["Source"],["Bold","Italic","Underline"],
      ["JustifyLeft","JustifyCenter","JustifyRight","JustifyBlock"],
      ["Styles","Format","Font","FontSize"],
      ["Link","Unlink","ShowBlocks"]
    ];
    ```
    
    Replace this snippet of code with the following code:
    
    ```jsx
    CKEDITOR.config.toolbar_Basic =
    [
        ['Source','-','Save','NewPage','Preview','-','Templates'],
        ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print', 'SpellChecker', 'Scayt'],
        ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
        ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
        '/',
        ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'],
        ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
        ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
        ['Link','Unlink','Anchor'],
        ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'],
        '/',
        ['Styles','Format','Font','FontSize'],
        ['TextColor','BGColor'],
        ['Maximize', 'ShowBlocks','-','About']
    ];
    ```
    

## LocalFiles Editor: Adding custom code

The **LocalFiles Editor** plugin lets you edit Piwigo files directly from the administration.

!!! warning "this feature is for advanced users only!"


For piwigo.com customers, this plugin only lets you add custom CSS code.

For other users who are using a self-hosted Piwigo gallery, this plugin lets you edit other files (local configuration, language files, etc).

[Learn more about LocalFiles Editor](../self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md)

## Rightclick: Deactivating right click on photos

Do you want to stop your gallery's visitors from being able to download the photos in your gallery?

First, you can block downloads for guests users (anonymous) or for some users, in the user management, [as explained in this article](../managing-users/creating-and-managing-users.md). If you deactivate downloads, the download icon will not be displayed.

However, visitors will still be able to download photos by performing a right click > Save image as.

![Clic droit.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-eb7be9d9.jpg)

To deactivate this option, simply activate the **Rightclick** plugin.

Once this plugin has been activated, the right click on images will be deactivated in your gallery (except for administrators).

## Piwishack: Integrating a photo on a web page

Do you need to integrate your photos on other websites?

With the **Piwishack** plugin, you can generate a HTML code for each photo, which will allow you to bring your photo to a web page.

Once the Piwishack plugin has been activated, a new icon will appear on your gallery above the photos.

![Piwishack.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f4ea2792.jpg)

One click on this icon opens a window that will allow you to retrieve multiple codes.

The first tab generates multiple HTML codes that allow you to bring the photo to a web page.

![Fenêtre Piwishack.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-51d965e9.jpg)

Here are the different options available:

- Show the thumbnail without a link
- Show the thumbnail with a link to the photo in your gallery
- Show the thumbnail with a direct link to the photo
- Show the normal view (normal-sized photo) without a link
- Show the normal view (normal-sized photo) with a link to the photo in your gallery

The second tab generates multiple codes in BBCode format (used mainly on discussion forums), with the same options.

Lastly, it is possible to generate custom codes.

## Stop Spammers: Fighting against spam

The **Stop Spammers** plugin sets up an anti-spam check in your gallery. If it isn't activated, remember to do it.

## AntiAspi: Banning IP addresses from your gallery

The goal of the AntiAspi plugin is to protect your gallery from robots or malicious users who could attack your site, namely to "pump out" its content.

The plugin's settings allow you to set criteria that trigger the ban of the IP address that's visiting your site, such as:

- Banning the IP address if 20 different pages have been visited within 10 seconds
- Banning the IP address if the same page has been viewed 15 times within 30 seconds
- Etc.

These criteria are customizable.

![Plugin AntiAspi.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-593652db.jpg)

The IP addresses tab in the settings for the AntiAspi plugin lets you view the history of banned IP addresses, and add IP addresses that are always allowed (whitelist).

## Cookie Consent: Adding a consent banner

The **Cookie Consent** plugin lets you add a banner on your website, inviting users to confirm their consent to basic cookies your gallery might leave on their computer.

It can also be used to invite users to declare their consent to the terms and conditions of your gallery.

![Cookie Consent.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2796e715.jpg)

The text, the button's text, as well as the link are customizable.

The confirmation is saved in the form of a cookie for which you can choose the validity duration. 

![Cookie Consent Config.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d056bb42.jpg)

!!! warning "Warning :"
    If your gallery is using third-party cookies, such as those from Google Analytics, this banner is not enough to collect the consent of your visitors, since it is only informational (the user can't reject the cookies, nor take back their consent).


## Plugins for your gallery’s SEO

If your gallery is public, you most likely wish for its pages to be visible on Google and other search engines.

The plugins below are useful if you want to improve the natural referencing (SEO) of your Piwigo gallery.

### Title: Customizing the Title tag on the website's pages

This plugin lets you customize the "Title" meta tag for all pages of your gallery.

You can customize the Title tags for the main pages from the plugin's settings.

![Plugin Title.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b295d299.jpg)

Furthermore, you can edit the Title meta tag of each photo and each album on the editing page, with the other properties.

![Options de titre.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e6063dcd.jpg)

### Meta: Customizing the meta tags on the website's pages

Apart from the Title meta, customizable thanks to the **Title** plugin, other tags related to SEO (Search Engine Optimization) can be set up in Piwigo, using the **Meta** plugin.

The plugin handles the following meta:

- author
- description
- keywords
- robots

You can set some meta tags in a global manner on all pages of the website, in the first tab of the plugin's settings.

![Plugin meta.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-14761527.jpg)

Among others, the **robots** tag lets you specify whether or not you want your website to be indexed on search engines:

- if you don't want your gallery to be indexed, enter `noindex`
- if you want your gallery to be indexed, enter `index`

Regarding the **Description** meta, we recommend you set it up one page at a time. This is an important piece of information for SEO since it appears in the results on search engines.

![Titre et description.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-cc312049.jpg)

You can edit the description meta of each photo and each album on the editing page, with the other properties.

![Edition photo meta.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-61f178c7.jpg)

The "Custom metadata" tab in the plugin's settings lets you add custom meta tags.

![Ajouter une meta.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-cdf64f3a.jpg)

### Meta Open Graph: Customizing the open graph meta tags for social media

The Open Graph meta allow you to customize the content of the preview that is shown when sharing a website's page on social media.

These data are not shown on Piwigo by default. If you share the link to your gallery, the title shown will be the gallery's title, along with a randomly selected photo.

To customize these meta tags on your Piwigo gallery, you can install the **Meta Open Graph** plugin.

This plugin's settings allow you to customize the Open Graph meta for each page of your gallery.

![Open Graph.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6ff33e11.jpg)

Choose a page, the home page for example, and click on "Edit Open Graph metadata".

Enter a title, a description, and choose the photo that is meant to represent the page (through the drop-down list or by entering the ID of the chosen photo in the "Metadata Open Graph link image" field).

![Description plus longue.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-15c721c8.jpg)

Click on “Save”.

Now, if you share the page on social media (such as Facebook), the preview will take into account the tags you entered.

![Capture d’écran 2024-08-20 à 14.34.01.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a21553df.png)

For each photo and each album, you can provide custom meta tags in the administration, on the editing page of the photo or the album.

![Options Open Graph.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-86be356c.jpg)

The Configuration tab in the plugin's settings page lets you specify default settings.

![Config Open Graph.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7bae3079.jpg)

Among other things, this allows you: 

- to be able to set a specific image for the meta of your albums and photos (by default, we will display the photo and the album's thumbnail image)
- to set an album to choose a random photo from for the meta image tag when it is not specified
- to choose the size of the photo used
- to set the default language
- to specify the name of your website
- to enter a Facebook app ID
- to specify the type of card displayed when sharing with Twitter (Twitter Card)
- to enter your Twitter ID if you have one

[Learn more about Facebook open graph meta](https://developers.facebook.com/docs/sharing/opengraph/using-objects?locale=fr_FR)

[Learn more about Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/guides/getting-started)

## Plugins to add custom code in your gallery

There are two plugins that allow you to add custom code to your Piwigo gallery.

Knowing both of them is interesting since they can work side by side.

This way, for example, you can add code in the <head> tag with the first, and in the website's footer (before closing the <body> tag) with the second.

### Add < head > element: Adding code in the <head> tag

The **Add < head > element** plugin lets you add code (A Javascript script, for example) in your gallery's <head> tag. You can choose to activate this code in the gallery, the administration, or both.

### Statistics: Adding code in the <head> tag or the footer

The Statistics plugin, made for inserting tracking code for an external statistics tool (such as Matomo or Google Analytics) in your gallery, also allows you to add code for another use.

It allows you to enter the desired code and choose whether to insert it in the website's header, in the footer, or both.

The "Exclude administrators from statistics" option allows you to not activate the code you entered when an administrator is logged in.

The "Exclude guests from statistics" option allows you to not activate the code you entered when the gallery's guests aren't logged in.
