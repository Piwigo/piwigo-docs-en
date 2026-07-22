---
title: Create a custom banner - Piwigo documentation
description: How do you create a customized banner for your Piwigo gallery? We take a look in this article.
---

# Adding a custom banner to your gallery

**Many users want to add a custom banner to their gallery, in the form of an image, a text, or a mix of both.**

There are two main ways to do so, which we list in this article:

## Using the “Page banner” field

By default, you can set up a banner in your gallery through the Configuration > Options menu, in the Page banner field.

![Paramètres de base bannière.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bc1edea8.jpg)

In this field, you can enter raw text content but also HTML code. You can visually edit the HTML code if you activated the FCKEditor plugin.

![Changer galerie FCK.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2c07f8bf.jpg)

You can easily insert an image, which can be located on your Piwigo gallery, on your server, or on another website. Simply retrieve this image's URL and add the HTML code below in the "Page banner" field, replacing the URL with your image's URL.

```html
<img src="https://piwigo.mysite.com/uploads/myimage.png">
```

The banners set up in the "Page banner" field are displayed in slightly different ways depending on your gallery's theme.

Let's see the result for each theme.

### Displaying a page banner with Modus

If you are using the Modus theme, the banner is displayed at the top of all pages like the example below.

![Bannière de base.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b6aab97e.jpg)

If the banner isn't displayed, go to the Configuration > Themes menu, then to the settings for the Modus theme. Make sure the "Display page banner" option is selected.

![Afficher bannière.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-30eced1f.jpg)

### Displaying a page banner with Bootstrap Darkroom

By default, page banners aren't displayed with the Bootstrap Darkroom theme. To display them, you need to go to the Configuration > Themes menu, then to the settings for the Bootstrap Darkroom theme.

The "Page header" field lets you choose between three display options for your banner.

![Afficher bannière BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ea627ac3.jpg)

- Disabled: No banner.
- Jumbotron: The content set in the "Page banner" field appears at the top of all pages.

![Exemple bannière BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6878bfe5.jpg)

- Hero image: This option lets you use an image located in your Piwigo gallery as a banner background. If you want, you can display this image in full height. The content set in the "Page banner" field appears in the center as an overlay.
    
    ![Exemple bannière image.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a55748ff.jpg)
    

### Displaying a page banner with the other themes

Most themes handle the banner set in the "Page banner" area.

Here are some preview examples.

- Displaying the banner with the Elegant theme
    
    ![Bannière Elegant.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-508d8fec.jpg)
    
- Displaying the banner with the Simple White theme
    
    ![Bannière SW.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-584f14e9.jpg)
    
- Displaying the banner with the Clear theme
    
    ![Bannière Clear.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-9e42995b.jpg)
    

## Using the Header Manager plugin.

If you are searching for a more complete way to create your banner, you can install the **Header Manager** plugin.

In the plugin's settings, the "Add a banner" tab lets you download an image that will act as a banner on your website, or enter the image's ID if it is located on your gallery.

![Plugin HM ajout.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f0a9ecd7.jpg)

Once the photo has been chosen, you can easily resize it so that it has the desired height and width.

![Recadrer image bannière.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-bb39679c.jpg)

The Configuration tab lets you customize your banner:

- Only displaying one image
- Displaying your gallery's title over the image (as transparent text)
- Displaying the image and text of your choice

![Bannière photo.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-495987f6.jpg)

The Header Manager plugin lets you have multiple different images for your banner and switch them randomly.

You can even set up specific banners for each album.

Indeed, on an album's editing page, the plugin adds a "Banner" tab, allowing you, for a given album, to choose which banner to display among the existing banners.
