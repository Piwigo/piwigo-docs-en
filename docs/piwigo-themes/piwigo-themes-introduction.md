# Piwigo themes: introduction

## What is a theme in Piwigo?

As you probably already know, Piwigo is separated into two interfaces:

- the administration, which is only accessible to administrators;
- the gallery, which can be accessible to common users, and even to all visitors if your gallery is public.

Your Piwigo gallery is a website that can be customized: colors, fonts, page layout…

But in order to customize your gallery, you first need to choose a theme, or "template": this is your gallery's model.

To view various examples of customization, based on different themes, you can visit our [Demos page](https://piwigo.com/demo).

You can also discover a blog article, which showcases [8 examples of graphic customization for Piwigo](https://piwigo.com/blog/2022/02/03/8-examples-customized-piwigo-galleries/).

## Default themes

Piwigo always comes installed with two themes activated by default:

- Modus, in its black and white version, is the theme used by your gallery when accessing it from a computer;
    
    ![Page accueil Modus.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-041139c5.jpg)
    
- Smart Pocket, a theme that will only be displayed from a phone or a tablet.
    
    ![Screenshot_20240723_122220_Chrome.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2ec1e5de.jpg)
    

But naturally, you can choose:

- to edit the colors of the Modus theme
- to use another theme for your gallery
- to deactivate the Smart Pocket mobile theme (in this case, on a mobile screen, your gallery will use the same theme as with a computer. This is not a problem with the Modus and Bootstrap Darkroom themes, which are *responsive*, meaning they adapt to all screen sizes).

## Piwigo.com customers and self-hosting: the differences when adding a new theme

Do you want to add a new theme? First of all, you should know that things are slightly different depending on whether you have an account on [piwigo.com](http://piwigo.com/) or are using a self-hosted Piwigo gallery.

- I am using a self-hosted gallery
    
    If you are using a self-hosted gallery, you can add a new theme yourself from the administration, in the Configuration > Themes menu, then the "Add theme" tab.
    
    You can also download a theme on [piwigo.org](http://piwigo.org/) and add it to your Piwigo gallery via FTP.
    
    You also need to think about updating your installed themes when a new update is available.
    
- I have a Piwigo account hosted on piwigo.com
    
    If you created an account on piwigo.com, your Piwigo gallery is hosted on our servers.
    
    Your account was set up with a list of pre-installed themes. You can't install a new one. You don't need to update your themes.
    

## Managing themes in Piwigo

To view, edit and set up your theme in Piwigo, go to the administration and click on Configuration > Themes in the menu on the left.

At the top of the screen, under "Active themes", you can see the theme(s) activated in your gallery.

Further down, under "Inactive themes", you can see the themes that are installed but not activated.

![Tous les thèmes.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f34d0747.jpg)

When a theme is activated, this means it can be displayed in Piwigo.

If you set it as "default", it will be displayed by default for all new users.

But for each user, you can set which theme is displayed for them specifically: this is why it is possible to activate multiple themes at once.

!!! info "Info :"
    In the vast majority of cases, users only activate one theme, the same for all users (apart from the Smart Pocket theme, which, when activated, is automatically displayed when viewing the gallery from a mobile device).

## Changing the default theme

If you want to change the default theme in your gallery, it's really simple.

From the screen available from the Configuration > Themes menu, choose the theme you want to display in your gallery and click on the Activate button.

![Activation thème BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e54c19d8.jpg)

Once activated, this theme is available in your gallery, but it isn't displayed by default yet: to do this, you need to click on "Set as default".

![Activer thème BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1dcfd849.jpg)

Go to your gallery: the new theme is taken into account.

## Setting up your theme

Choosing a theme is only a first step in the customization of your gallery: indeed, most themes offer configuration options, allowing you to:

- edit your gallery's colors
- edit some display options
- add customization elements (logo, banner...)
- activate optional components

The most recent themes, [Modus](modus-theme-piwigo.md) and [Bootstrap Darkroom](bootstrap-darkroom-theme-piwigo.md), offer many color styles and configuration options. Other older ones are not customizable.

We recommend you explore the options of the main themes to make your choice. 

## Introduction to the main themes

### Modus

Modus is the theme that's activated by default in Piwigo. It is a modern, responsive theme, which offers a guaranteed compatibility with most plugins. Its browsing menu is horizontal.

![Page accueil Modus.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-041139c5.jpg)

It offers 18 different color sets, which you can choose in its configuration options.

![Liste thèmes Modus.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-80c0803e.jpg)

It also lets you:

- customize the size and format of your albums' thumbnails (square 250x250 pixel thumbnails by default)
- add a banner in your gallery

[Read the documentation for the Modus theme](modus-theme-piwigo.md)

### Bootstrap Darkroom

It's currently the second most popular theme after Modus.

Bootstrap Darkroom is a modern, responsive, and very customizable theme. It is based on the Bootstrap 4 framework, a very popular open source project in the world of web interface creation. Its browsing menu is horizontal.

![Page d'accueil BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e6a71abd.jpg)

Bootstrap Darkroom has over 30 extremely varied color styles.

![Couleurs BD.gif](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-41cb4d0e.gif)

In addition to these color styles, Bootstrap Darkroom offers many configuration options:

- Adding a logo
- Adding a banner (image, text)
- Editing many display options
- Adding custom CSS code
- Adding social media share icons
- …

[Read the documentation for the Bootstrap Darkroom theme](bootstrap-darkroom-theme-piwigo.md)

### Elegant

Elegant is a theme that was very popular for many years and is still used a lot. It features a vertical browsing menu, on the left side of the screen. The albums are displayed as large blocks instead of thumbnails, which allows for descriptive text for each album if you want.

![Thème Elegant.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-57c3ebf0.jpg)

Colors can't be edited directly from the Elegant theme configuration: [piwigo.com](http://piwigo.com/) customers need to contact support to request it or to get access to Piwigo's style sheet.

Elegant offers some configuration options:

- Showing or hiding the menu side panel
- Showing or hiding the photo description side panel
- Showing or hiding the comment panel

## How do I test a theme without making it visible for everyone?

As we saw, it is possible to activate multiple themes on Piwigo, but only the default theme is displayed for all users.

Therefore, if you want to test a theme without making it accessible to everyone, it's very simple.

Simply activate it from the administration, in the Configuration > Themes menu.

Next, go to your gallery and to the "Customize" menu. This menu lets you edit your preferences. This way, you can switch themes: this change will only be visible to you.

![Choix de thèmes.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c33f8f0d.jpg)

## Switching themes easily with Theme Switch

If you want to make switching themes in your gallery even easier, you can activate the Theme Switch plugin.

Once activated, this plugin adds a paintbrush-shaped icon in your gallery, which lets you switch themes in one click.

!!! warning "Warning : this icon is visible to all visitors, not only administrators."

![Theme Switch.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-1b953541.jpg)

## Switching themes easily with Admin Tools

The Admin Tools plugin offers many possibilities for accessing administration actions from your gallery.

Among others, it lets you switch themes easily.

When this plugin is activated, an additional menu is added when an administrator logs into the Piwigo gallery. The Option button, in the top right, lets you switch the active theme with one click. This is only visible to you.

![Admin Tools.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-110f8230.jpg)

!!! info "Info :"
    This plugin also lets you switch languages with one click or view your gallery as any other user: therefore, it is very useful for testing.

[Learn more about the Admin Tools plugin](../administration-piwigo/plugins-for-administrators.md)
