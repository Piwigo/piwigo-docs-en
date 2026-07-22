---
title: FAQ - Most common questions about Piwigo
description: On this page, we have summarized all the answers to questions we are frequently asked about using Piwigo. If you have a problem, start by looking here!
---

# FAQ - The most common questions about Piwigo

**On this page, we have summarized all the answers to questions we are frequently asked about using Piwigo. If you have a problem, start by looking here!**

Click on the arrow to show the answer to a question.

---

- Help, I don't see my photos / my albums!
    
    You created an album and you don’t see it in your gallery?
    
    No need to panic! It is probably an issue regarding permissions. 
    
    If your album is private and you didn't grant yourself the rights to it, it makes sense why you don't see it in your gallery. 
    
    In order to check, go in the administration, then Albums > Manage. Search for your album and edit it. Go in the "Permissions" tab. If your album is private, make sure you have permission to view it. 
    
    [Learn more about album permissions](organizing-albums/permissions-and-album-visibility.md)
    
    If you do have permission to view this album, make sure it isn't empty (without any photos). Empty albums aren't visible in the gallery.
    
    If you see an album but another user doesn't, even though they do have permissions on this album: make sure the album isn't locked!
    
- The emails sent from my Piwigo don't land (or land in the spam folder)
    
    The notification emails sent by Piwigo are sent using the main administrator's email (webmaster), i.e. the first user to be created. 
    
    Sometimes, your Piwigo's host server isn't allowed to send emails with this address, so they land as spam or don't land at all.
    
    To solve this problem, there are multiple solutions:
    
    - Changing the webmaster's email address: in order for the emails to reach their destination, your Piwigo gallery must be allowed to send emails with the address of your site's webmaster. Sending emails from Piwigo might not work with an address like Gmail, Yahoo, etc. Ideally, the webmaster's email address should have the same domain name as your gallery. For example, if your gallery's address is photos.mysite.com, the webmaster's email address would ideally be something such as *@mysite.com.
    - Installing the Protect Notification plugin: the Protect Notification plugin replaces the emails' sender with an address such as no-reply@mysite.com (mysite.com being replaced with your gallery's domain name). Generally, installing this plugin solves the email issues. Since February 2024, Protect Notification is activated by default on new Piwigo accounts.
    - ⚠️ These solutions do not solve the issues with receiving emails sent by the Contact Form plugin, since those are sent using the email address entered in the form. To solve issues with the Contact Form plugin, [visit this page](customizing-your-gallery/add-pages-to-piwigo-gallery.md).
- How do I delete my Piwigo cloud account?
    
    Contact support at support@piwigo.com.
    
- How do I associate my Piwigo cloud gallery with a custom domain name?
    
    By default, all Piwigo cloud accounts have a web address in the form of *.piwigo.com. You can add your own domain name, or a simple subdomain. 
    
    Given that Piwigo cloud does not sell domain names, you will need to purchase it from a domain name provider, such as OVH. 
    Send us an email at support@piwigo.com and tell us what your domain name (or subdomain name) is. 
    We will set up the Piwigo cloud servers and explain to you how to set up your domain name. 
    Once the DNS configuration is propagated, we will add a layer of security with HTTPS.
    
- How do I rename my Piwigo cloud account?
    
    Contact support at support@piwigo.com.
    
- How do I change the title of my Piwigo gallery?
    
    To modify the title of your gallery, go to your Piwigo's administration, in the Configuration > Options menu. On the first tab, you can change the name of your gallery in the first field, "Gallery title". 
    
- How do I make my gallery visible on search engines?
    
    Once your gallery has been created, it should be visible on search engines. However, if your domain name is new, or if you don't have much traffic, this can take some time. 
    
    Here are some tips to notify search engines that your Piwigo gallery exists:
    
    - Add links to your gallery on websites that already have visitors
    - Share your gallery on social media
    - Add your gallery to the [Google Search Console](https://search.google.com/search-console/welcome) tool (for Google) or [Bing Webmaster Tools](https://www.bing.com/webmasters/about) (for Bing).
- How do I make it so that my gallery is NOT visible on search engines?
    
    If you want your gallery to not be visible on search engines, you can create a robots.txt file in the root folder of your website (if you are using a self-hosted gallery) and add the following lines in this file:
    
    ```html
    User-agent: *
    Disallow: /
    ```
    
    You can also adjust your gallery's exposure on search engines by installing the Meta plugin. This plugin allows you to set up your site's metadata for search engines, on the whole site as well as page by page.
    
    To completely disable the indexing of your Piwigo gallery on search engines with the Meta plugin, go to the plugin's settings, and select the "robots" metadata on the first tab. Edit the metadata and enter the `noindex` value, then click on "Insert metadata".
    
    [Learn more about plugins for your gallery's indexing](administration-piwigo/plugins-for-administrators.md)
    
- How do I set the title and description of my gallery on search engines?
    
    To customize the way the pages of your gallery are displayed on search engines, install the Title and Meta plugins.
    
    The Title plugin allows you to modify the title displayed for each page on search engines. 
    
    The Meta plugin allows you to modify the description displayed for each page on search engines.
    
    ![Titre et description.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-cc312049.jpg)
    
    [Learn more about plugins for your gallery's indexing](administration-piwigo/plugins-for-administrators.md)
    
- How do I modify the look of my gallery when sharing it on social media?
    
    To customize the appearance (title, description, image...) of your gallery's pages when sharing them on social media, you can install the **Meta Open Graph** plugin. [Learn more](administration-piwigo/plugins-for-administrators.md)
    
- How do I modify my gallery's footer?
    
    By default, your gallery displays a text at the bottom of the page with a link to Piwigo cloud or piwigo.org (depending on whether your gallery is hosted on Piwigo cloud or your own hosting). 
    
    If you want to customize your gallery's footer, you can install the **Perso Footer** plugin ([learn more](customizing-your-gallery/customizing-piwigo-gallery-plugins.md)).
    
    If you want to hide the footer completely (and not advertise Piwigo 😢), you can add the following code in the website's CSS file through the LocalFiles Editor plugin ([learn more about LocalFiles Editor](self-hosting-piwigo/editing-configuration-localfiles-editor-plugin.md)). However, it would be a shame to do so.
    
    ```css
    #copyright{display: none;}
    ```
    
    Finally, in addition to the default footer, you can also create a custom footer by creating a custom block using the [PWG Stuffs](browsing-your-piwigo-gallery/tags-in-your-gallery/pwg-stuffs-plugin-piwigo.md) plugin. 
    
- How do I add a custom banner / photo to my Piwigo website?
    
    There are multiple ways to customize your Piwigo by adding a background image on the home page or a banner on your website's pages. 
    
    Read this article to find out how:
    
    [Adding a custom banner to your gallery](customizing-your-gallery/adding-a-custom-banner-to-your-gallery.md)
    
- How do I get an invoice on Piwigo cloud?
    
    Do you need an invoice for your Piwigo cloud subscription?
    
    - If you need an invoice before making a payment: ask support. Be careful: requesting an invoice requires you to pay it.
    - If you need an invoice after payment: no worries, it is automatically available in your Piwigo administration, in the My Account > Manage menu, in the billing tab.
