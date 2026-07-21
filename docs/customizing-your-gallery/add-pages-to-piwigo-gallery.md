# Adding pages to your gallery

Do you want to add custom pages to your Piwigo gallery? This is possible with the help of a few plugins.

## Additional Pages: Adding HTML pages

The Additional Pages plugin lets you add new pages in your gallery and make them accessible through the [browsing menu](customizing-piwigo-gallery-menu-navbar.md).

Once this plugin has been activated, go to its configuration page.

### Adding a new page

The first tab lets you add a new page on your gallery.

You can start fresh or load an existing page template provided with the plugin.

You can set the attributes and options of this page:

- Choosing a page template (by default, only the "Standalone Homepage" template is available)
- Page name
- Permalink (URL)
- Choosing whether this page replaces your home page or not
- Choosing whether this page is autonomous or not (if it is autonomous, it is not linked to the style of your Piwigo gallery and thus doesn't retrieve the defined CSS styles).

The "Content" field lets you enter your page's HTML code.

![Plugin AP.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bcded356.jpg)

If you installed the FCKEditor plugin, we will display an HTML editor by default, which will allow you to view the result, but you can display the HTML code by deactivating FCKEditor in the bottom right corner of the window.

![Plugin AP avec FCK.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5e930604.jpg)

### Creating a home page for your Piwigo gallery

The Additional Pages plugin is often used to create a dedicated home page for a Piwigo gallery.

The page offered by default with the *Standalone Homepage* template is made for creating a home page that displays a chosen photo in your gallery, just like this example: [https://endangeredarts.com/](https://endangeredarts.com/) 

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f3d57b74.png)

If you want to do the same, you need to install the Extended Description plugin, which will allow you to display content from your gallery on the page.

[Learn more about Extended Description](customizing-piwigo-gallery-plugins.md)

Next, in the HTML code found by default when creating the page, you need to edit the content of the tag (`[photo id=12345 size=L link=no]`) to adapt it to what you want:

- Replacing 12345 with the numeric ID of the photo you want to display on the home page
- Edit the size of the image displayed (SQ, TH, XXS, XS, S, M, L, XL, or XXL)
- Do not edit “link=no”

You can also replace this tag with `[random album=xx]`, by replacing xx with the ID of the album of your choice: this will automatically display a random photo on your home page, picked from the selected album.

You can also replace this tag with `[slider album=xx]`, by replacing xx with the ID of the album you chose: this will show a slideshow of photos from the selected album on your home page. You can manage all of the options for the slideshow by using the features from the Extended Descriptions plugin.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4ee672eb.png)

Lastly, as soon as you reach a certain level with HTML, the possibilities are endless! For example, you can create a bespoke browsing menu at the top or the bottom of the page.

### Managing the existing pages

Once you created a first page, you can view and edit it in the "Manage" tab. You can also reorganize the pages created.

### Configuration of additional pages

The Configuration tab offers several options.

![Config AP.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8c4cc10f.jpg)

**Activate authorization management**

You can activate the management of access rights to additional pages: by privacy level, by user type (status), by user group, by language. If you activate one of these options, you will be able to set the access rights to each page by editing it.

![Niveaux confidentialité AP.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-14758bcb.jpg)

**Displaying additional pages in your gallery**

These options are available for all of your additional pages.

You can set:

- Whether or not the additional pages contain a button to return to the home page
- Whether or not the additional pages are accessible via a menu item, and the name of this menu item in each of your gallery's languages.

## Contact Form: adding a contact form in your gallery

The Contact Form plugin lets you add a page containing a contact form in your gallery.

Every time a visitor of your gallery will fill out this form, a notification email will be sent to you by your Piwigo gallery.

Once this plugin has been activated, visit its Configuration page.

### Contact form configuration

The Configuration tab lets you set up your form and its visibility.

![Plugin CF.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bd10c103.jpg)

This page lets you choose:

- Whether or not to add a Contact link in the menu
- Whether or not to allow guests (anonymous visitors of your gallery) to view the form
- Whether or not to redirect the user to a specific URL after submitting the form
- The format of the email sent to the administrator after form submission
- The text (optional) displayed above and below the form on the page.

### Choosing the email recipients

The E-mails tab lets you set who the recipient for the notification emails will be when a person fills out the contact form.

![CF emails.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2ac5d66a.jpg)

By default, all administrators and webmasters are recipients, but you can delete some by clicking on the cross.

You can add new recipients by clicking on the drop-down list named "Select a new user".

Lastly, you can add new recipients on the right, even if they aren't users of your Piwigo gallery.

### Displaying the form in your gallery

If you selected this option, the form is accessible from a "Contact" menu item available from the Specials menu block ([learn more about menus](customizing-piwigo-gallery-menu-navbar.md)).

![Formulaire contacty.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c28415ff.jpg)

If you want to display the link to the form directly from the main menu in your gallery, that's possible thanks to the **Contact 1 Menu** plugin.

This plugin moves the "Contact" menu directly to the main browsing bar.

![Plugin C1M.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7317d208.jpg)

### Crypto Captcha: Protecting your form against SPAM

Sadly, forms on the Internet often generate spam because they are filled out by robots.

To avoid this issue, you can install the **Crypto Captcha** plugin.

This plugin forces users to enter a Captcha before sending the form. Several options are available to set up your Captcha.

![Plugin CC.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5c63613e.jpg)

!!! info "This plugin also allows you to add a Captcha for entering a comment or creating a new user."

### ⚠️ Frequent problems with the Contact Form plugin

When a contact sends you a message via the Contact form, the email address of the sender of the notification email is the address that was entered in the form.

However, your Piwigo website is not allowed to send emails from a Gmail, Yahoo or Orange address. Some email providers will therefore block these emails.

As a result, emails sent through this form might not reach their destination: this is especially the case when the sender writes from a Gmail address, and the recipient's email is also a Gmail address.

If you encounter this type of issue, you can attempt to solve it by changing the email address of the recipients (avoid Gmail or Yahoo addresses).

If you don't manage to solve the issue, we recommend you uninstall Contact Form.

Article summary

---

← Previous

[Customizing your gallery’s menu](customizing-piwigo-gallery-menu-navbar.md)

Next →

[Customizing your gallery with plugins](customizing-piwigo-gallery-plugins.md)
