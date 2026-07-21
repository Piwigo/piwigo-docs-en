# Customizing your gallery with plugins

On this page, you will find some plugins that allow you to customize your gallery's appearance and features.

You will find other customization plugins for your gallery by reading the following articles:

[Albums in your gallery](../browsing-your-piwigo-gallery/albums-in-your-gallery.md)

[The Photo page in your gallery](../browsing-your-piwigo-gallery/the-photo-page-in-your-gallery.md)

[Tags in your gallery](../browsing-your-piwigo-gallery/tags-in-your-gallery.md)

## PWG Stuffs: adding customizable blocks to your gallery

The **PWG Stuffs** plugin offers various options for adding customizable blocks to your gallery.

These blocks enhance the existing pages. Therefore, this is a very complete plugin for customizing your gallery, which allows you, among other things, to customize the display depending on the user.

It is used namely for:

- Adding a keyword cloud on the home page
- Adding a login area on the home page
- Etc.

Click below to read the complete documentation for PWG Stuffs.

[PWG Stuffs: adding blocks in your gallery](../browsing-your-piwigo-gallery/tags-in-your-gallery/pwg-stuffs-plugin-piwigo.md)

## Fotorama: another slideshow for your gallery

The **Fotorama** plugin lets you replace the slideshow player used by default in your Piwigo gallery with another slideshow.

There are various customization options in the plugin's settings.

![Full screen slideshow with Fotorama](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-14cf1f90.jpg)

Full screen slideshow with Fotorama

## Extended Description: many options for customizing your gallery

The Extended Description plugin offers many possibilities. Among other things, it is used to translate the titles and descriptions of albums and photos in multiple languages, [as explained in this article.](managing-languages-available-gallery-piwigo.md)

But it has many other possibilities to offer.

Indeed, it allows you to manage tags that you can insert wherever you want in your gallery.

This may allow you:

- To manage two different descriptions for an album (a short one displayed in the album list and a long one on the album page)
- To insert an album or a photo in any text field in your gallery
- To insert a carousel (or slideshow) in any text field in your gallery
- To hide an album on the parent album's page or in the menu
- To hide a photo on an album page
- To redirect an album to any URL
- To redirect an element to an image, an album, or a search page
- To insert a login link to the gallery wherever you want.

Once you have installed Extended Description, you will see a question mark-shaped icon appear next to the input fields: click on it to display all of the plugin's options.

We have listed them all below.

- **View the complete documentation for the Extended Descriptions plugin**
    
    **Multilingual descriptions**
    
    Multilingual descriptions are made between the `[lang=xx]` and `[/lang]` tags, whereby xx is the language code (for example: en, fr, es...).
    
    ```html
    [lang=en]Default description[/lang]
    [lang=fr]Description en français[/lang]
    [lang=de]Deutsche Beschreibung[/lang]
    ```
    
    ***Default* tag**
    
    If the description is not specified in the user's language, the default description will be used.
    If `[lang=default]` doesn't exist, everything that's located outside of the language tags will be considered as the default description.
    
    ```html
    [lang=default]Default description[/lang]
    [lang=fr]Description en français[/lang]
    
    // OR
    
    Default description
    [lang=fr]Description en français[/lang]
    ```
    
    ***All* tag**
    
    Everything that's located between the `[lang=all]` and `[/lang]` tags will be included in the description, no matter the user's language.
    This is especially useful for including HTML or Javascript code in a description.
    
    ```html
    [lang=all]<p>[/lang]
      [lang=default]Default description[/lang]
      [lang=fr]Description en français[/lang]
      [lang=de]Deutsche Beschreibung[/lang]
    [lang=all]</p>[/lang]
    ```
    
    **Extended descriptions**
    
    The extended description tags allow you to have a shortened description for an album's presentation, a lengthened description for the description that's displayed on the album's page, or two different description on the album's page.
    
    **<!--more-->**
    
    Only the shortened description will be displayed for the album's presentation. On the album itself, the description will consist of the shortened description + the detailed description.
    
    ```html
    shortened description <!--more--> detailed description
    ```
    
    **<!--complete-->**
    
    Only the shortened description will be displayed for the album's presentation. However, on the album itself, the description will only consist of the detailed description, meaning 2 different descriptions.
    
    ```html
    shortened description <!--complete--> detailed description
    ```
    
    **<!--up-down-->**
    
    Only the upper description will be displayed for the album's presentation. On the album itself, the upper description will be displayed above the thumbnails, whereas the lower description will be displayed below (where the description is usually located).
    
    ```html
    upper description <!--up-down--> lower description
    ```
    
    **Inserting an album or a photo
    [photo id=xx]**
    
    This tag lets you insert a photo of any size.
    
    **Options:**
    • `id` the photo’s number
    • `album` (optional) the parent album’s number
    • `size` (optional) the photo’s size, among *SQ, TH, XXS, XS, S, M, L, XL, XXL*
    • `html` (optional) if `false`, the tag only retrieves the photo's URL, without HTML
    • `link` (optional) if `true`, the photo can be clicked, bringing you to its page
    
    ```html
    [photo id=46]
    
    [photo id=46 album=22 size=M html=true link=true]
    ```
    
    **[random album=xx]**
    The options are the same, except that the photo(s) are randomly picked either from the whole gallery or from `album`.
    To display several images, use the option:
    • `nb_images` (optional) the number of images to display
    
    ```html
    [random]
    
    [random album=123 size=M html=yes link=yes]
    
    [random album=123 size=M html=yes link=yes nb_images=8]
    ```
    
    **[cat=xx]**
    
    This tag lets you insert an album in the description, with `xx` being the album’s number.
    
    **Inserting a carousel
    [slider album=xx]**
    Lets you insert a slideshow.
    
    **Options:** (you need to specify `album` OR `list`)
    • `album` (optional) source album
    • `nb_images` (optional) maximum number of photos in the slideshow
    • `random` (optional) choose the photos randomly in the album
    • `list` (optional) a list of photos separated by a comma
    • `size` (optional) the photo sizes, among *SQ, TH, XXS, XS, S, M, L, XL, XXL*
    • `speed` (optional) the slideshow speed (in seconds)
    • `title` (optional) display the photo’s name
    • `effect` (optional) transition effect (see [the NivoSlider documentation](http://docs.dev7studios.com/jquery-plugins/nivo-slider#jumpNav-5))
    • `arrows` (optional) displaying browsing arrows
    • `elastic` (optional) adapting the slideshow’s size to each photo
    • `control` (optional) displaying the browsing bar, can also equal `thumb`
    • `thumbs_size` (optional) thumbnail size in pixels if `control=thumb`
    
    ```html
    [slider album=123]
    
    [slider list=46,47,52]
    
    [slider album=123 nb_images=10 random=false size=M speed=3 title=false effect=fade arrows=true elastic=false control=true thumbs_size=80]
    ```
    
    **Hiding an element**
    
    **Hiding an album**
    
    Use the `<!--hidden-->` tag in the album’s name:
    • it will not be displayed on the parent album's page anymore
    • it remains visible in the album menu
    
    **Hiding an album in the menu**
    
    Use the `<!--mb-hidden-->` tag in the album’s name:
    • it will not be displayed in the album menu anymore
    • it remains visible on the parent album's page
    
    **Hiding a photo**
    
    Use the `<!--hidden-->` tag in the photo’s name:
    • it will not be displayed on the thumbnail page anymore
    • however, it remains visible within the album
    
    **Redirecting an element**
    
    **[redirect http://piwigo.org]**
    Insert this tag in an album's description in order to redirect it to the URL of your choice.
    
    **[redirect img=xx]**
    Redirects to a photo of your gallery where `xx` is its ID; you can also specify the album's ID after the photo's number: `xx.ccc`.
    
    **[redirect cat=xx]**
    Redirects to an album of your gallery where `xx` is its ID.
    
    **[redirect search=xx]**
    Redirects to a search page in your gallery where `xx` is the ID of the search page.
    
    **Login link & logged block
    [login-link]**
    This tag lets you add a login link anywhere with automatic redirection to the current page.
    
    **Options:**
    • `html` (optional) if `false`, the tag only returns the link's URL, without HTML
    • `text` (optional) texte du lien, link's text, can contain `[lang]` tags
    
    ```html
    [login-link]
    
    [login-link html=true text="log in[lang=en]log-in[/lang]"]
    ```
    
    **[logged]**
    Displays a text block depending on whether the user is logged in or not.
    
    ```html
    [logged=true] Welcome back [/logged]
    [logged=false] Please log in [/logged]
    ```
    

## Perso Footer: Customizing your gallery’s footer

By default, your gallery's footer shows a presentation text for Piwigo, as well as a login / logout link and a link for sending an email to the gallery's webmaster (piwigo.com subscribers only).

![Pied de page basique.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-02bf4b28.jpg)

You can add content to this footer using the **Perso Footer** plugin.

The settings for this plugin give you access to an text input block where you can insert simple text or HTML code.

If you install the FCKEditor plugin on top of that, adding a visual editor to text input fields to format text, you will be able to easily create a custom footer.

![Plugin PF config.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-cefaec71.jpg)

## Personal Favicon: Customizing your gallery's icon in the browser

By default, your Piwigo gallery's Favicon, meaning the icon that is displayed in the browser, is the Piwigo.com icon.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8435a237.png)

You can customize this icon by activating the **Perso Favicon** plugin.

Once this plugin is activated, go to its configuration page.

On Piwigo, you can upload a file (.ico extension, 5ko max), which will replace the default icon.

![Plugin PF.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7ab12eea.jpg)

## OpenStreetMap: Geolocating you photos on an interactive map

The OpenStreetMap plugin, which is based on the free [OpenStreetMap](https://www.openstreetmap.fr/) mapping project, allows you to display your photos on a map based on their GPS coordinates.

Here, you can see an example of a gallery that integrates geolocation with OpenStreetMap: [https://laseineavelo.piwigo.com/](https://laseineavelo.piwigo.com/)

The map can be displayed:

- On Piwigo’s homepage
    
    ![Plugin OSM.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5d071890.jpg)
    
- On an album page
    
    ![OSM page album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-90f3d987.jpg)
    
- On a photo page
    
    ![Carte sur page image.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0dd4baba.jpg)
    

Furthermore, the plugin can add a page available from the gallery's menu, which opens a full-screen map.

![Carte plein écran.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-034adaee.jpg)

When clicking on a point of interest on the map, it displays the associated photo as well as the available information, such as the photo's title or its author. One click on the image opens the photo's page.

![Focus sur image.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6389439b.jpg)

When you edit a photo in the administration, an OpenStreetMap tab lets you view the geographical coordinates of the image and edit them if necessary.

![Edition photo OSM.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b5a3a44e.jpg)

Editing the GPS coordinates for a batch of photos is also possible in the batch manager.

![OSM GeoTag BM.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b775355d.jpg)

Many configuration options are available in the plugin's settings. Namely, you can edit the map's appearance, its size, choose whether or not to activate its location…

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8d4fc096.png)

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f72fd449.png)

You can even create your own custom style for your map's colors as well as the pins that represent the photos.

## Header Manager: Easily managing your gallery's banner

There are multiple ways to add a banner to your Piwigo gallery.

The most basic is available from the administration, in the Configuration > Options menu, General tab, Basic settings section. In this spot, you can enter HTML code for your banner.

The **Header Manager** plugin gives you more options to set up your banner.

![Bannière photo.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-495987f6.jpg)

This plugin lets you:

- upload one or more images or choose one among your gallery's photos
- resize your image online to create your banner
- customize your banner:
    - Only display one image
    - Display your gallery’s title above the image (in transparent text)
    - Display the image and text of your choice
    - Choose whether or not the banner is displayed on photo pages
    - Rotate between multiple banners randomly
    - Set up specific banners for each album

To learn more about banner creation, with or without this plugin, read this article:

[Adding a custom banner to your gallery](adding-a-custom-banner-to-your-gallery.md)

## Paypal Shopping Cart: Selling photos in your gallery with Paypal

Do you want to sell photo prints on your gallery, for example?

This is made possible by the **Paypal Shopping Cart** plugin.

To use this plugin, you need to create a PayPal account beforehand.

**This account must use the same email address as your gallery's webmaster.**

The PayPal Shopping Cart plugin configuration lets you set:

- The currency used on your website
- The activation of the PayPal cart for the whole gallery or only for some albums
- The management of different rates depending on the photo sizes
- The amount for shipping costs (flat)

Once these elements have been set up, an "Add to cart" button will be added to the photo's pages in the albums involved.

![PayPal Images.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-91f408b3.png)

Adding a photo to the cart automatically opens a PayPal payment page; but the visitor can go back to your gallery, and add other photos to their cart.

Once they are done with their shopping, they can go through with their order on PayPal.

![Panier achats.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ae87289b.jpg)

---
