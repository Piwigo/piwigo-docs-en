---
title: Languages and translation - Piwigo documentation
description: You can create a multilingual photo library with Piwigo and let visitors browse your photo library in the language of their choice. In this article we explain how.
---

# Managing the languages available in your gallery

Piwigo's interface is available in over 70 languages.

You can therefore create a multilingual photo library with Piwigo and offer visitors the ability to browse your photo library in the language of their choice.

We'll explain how in this article.

## Managing the languages available in Piwigo

To edit the languages available in your Piwigo gallery, go to the administration, in the Configuration > Languages menu.

The screen shows the languages activated in your Piwigo gallery, lets you activate new languages and choose the language available by default.

![Liste langues.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-40c57bcb.jpg)

If you created your account from the piwigo.com website, the configuration is as follows:

- The language activated is English
- The default language is English.

To deactivate a language, simply click on "Deactivate".

To activate another language, simply choose a language in the list and click on "Activate".

To switch the default language, simply click on "Default" on the chosen language.

Next, go to the gallery.

By clicking on "Customize", you can change the display language: this choice will only apply to you alone (it is a preference saved for every user).

[Learn more about preferences](../managing-users/creating-and-managing-users.md)

![Options customisation.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6e2d7d1f.jpg)

The language switch is immediately applied: it applies to all the text in your gallery (menus, action buttons...), but beware: dynamic content from database (album names, photo names, descriptions...) aren't translated.

![A Piwigo gallery in Spanish.](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f241a9d8.png)

A Piwigo gallery in Spanish.

## Switching languages in your gallery

If you want to make switching languages easier and faster in your gallery, it can be done using the **Language Switch** plugin.

Once this plugin has been activated, a flag appears in your gallery, which corresponds to the current language.

If you click on this flag, you can switch languages in one click by choosing another flag.

![Switching languages with Language Switch and the Modus theme](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b7adfd03.jpg)

Switching languages with Language Switch and the Modus theme

![Switching languages with Language Switch and the Bootstrap Darkroom theme](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a348cdfc.jpg)

Switching languages with Language Switch and the Bootstrap Darkroom theme

## Exif View: Translating the names of EXIF metadata

If you want to translate EXIF metadata values into the gallery's language, you need to install the **Exif View** plugin.

## Extended Descriptions: Translating the names and descriptions of photos and albums

If you want to translate the names and descriptions of photos or albums, you need to install the **Extended Descriptions** plugin.

This plugin adds many features to Piwigo, including the ability to display a different title and description for a photo or an album, depending on the user's language.

The way this plugin works is documented in the plugin's "Configuration" page.

In Piwigo's administration, for each field you wish to translate, you need to surround each value with two tags that allow you to specify the language, just like the example below.

```html
[lang=en]Default description[/lang]
[lang=fr]Description en français[/lang]
[lang=de]Deutsche Beschreibung[/lang]
```

You can specify the default language by using the "default" tag like the example below.

The default description (or name) will be used if the description is not specified for the user's language.

If [lang=default] doesn't exist, everything located outside of the language tags will be considered as the default description.

```html
[lang=default]Default description[/lang]
[lang=fr]Description en français[/lang]

// OR

Default description
[lang=fr]Description en français[/lang]
```

The "all" tag lets you set a text that will always be displayed, no matter the user's language.

Everything located between the [lang=all] and [/lang] tags will be included, no matter the user's language.

This is particularly useful for including HTML or Javascript code in a description.

```html
[lang=all]<p>[/lang]
  [lang=default]Default description[/lang]
  [lang=fr]Description en français[/lang]
  [lang=de]Deutsche Beschreibung[/lang]
[lang=all]</p>[/lang]
```

Note that the Extended Descriptions plugin gives you access to other features to customize your gallery.

[Learn more about Extended Descriptions](customizing-piwigo-gallery-plugins.md)
