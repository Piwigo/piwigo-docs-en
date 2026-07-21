# Plugins on Piwigo: Presentation

If you are already using Piwigo, and you have already gone through this documentation, you surely understand that plugins are a major part of Piwigo.

However, we thought it would be useful to go over the subject again in this article.

## What is a plugin for Piwigo ?

A plugin is an extension that adds or changes Piwigo's base features.

When installing Piwigo for the first time, you have access to Piwigo’s core system, the technical and functional foundation on which the whole software stands:

- Piwigo’s administration
- The gallery with the default Modus theme

By default, some plugins are already installed on your Piwigo, depending on whether it is a self hosted gallery or a piwigo.com account.

- Self-hosted galleries
    
    If you install the last version of Piwigo on your environment, the following plugins will be installed by default, but not activated:
    
    - Admin Tools (allows admins to perform some administration actions from the gallery)
    - Language Switch (allows to change the gallery’s language easily)
    - LocalFiles Editor (allows to edit local configuration files from the administration)
    - Take A Tour of Your Piwigo (adds an interactive guided tour of Piwigo’s administration for new users)
- Galleries hosted on piwigo.com
    
    If you create an account on piwigo.com, the following plugins will be activated by default:
    
    - Stop Spammer (a plugin to avoid spam, not to be deactivated)
    - VideoJS (the video management plugin, activated by default for piwigo.com customers since March 2023).

**But you shouldn't stop with the pre-installed plugins.** 

Piwigo is a modular tool to which you can choose whether or not to add features: this is what plugins are for.

If you know WordPress, this is the exact same principle. By the way, you will notice that very few websites created using WordPress work without any plugins. Similarly, it would really be a shame to use Piwigo without enhancing it with the plugins that correspond to your needs.

## Plugin management: difference between piwigo.com customers and self-hosting

The way plugins work is different whether you have an account on piwigo.com or are using a self-hosted Piwigo gallery.

### You are a piwigo.com customer

If you are a customer for a hosting plan on piwigo.com, you don't need to install or update plugins.

You have access to a limited list of plugins, depending on the subscription plan you chose. They are already installed on your Piwigo gallery, and you can activate or deactivate them as you wish.

**Plugin list**

To find your plugins, go to the administration of your Piwigo gallery, in the Plugins menu.

The List tab lets you view the plugins that are already activated in your Piwigo gallery, and search among all the plugins.

![Liste des plugins.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-97a78cd9.jpg)

To activate a new plugin, simply click on the activation button: the plugin is activated instantly. You then have access to its configuration.

**Plugins by pricing plan**

The second tab lists the plugins available for each pricing plan. You can only activated plugins that are within your plan.

![Plugins par prix.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0ab1b3f6.jpg)

On this page, the plugins are sorted by plan; the icons on the right let you know which plans a plugin is available on at all times.

If you are searching for a specific plugin, combine the Ctrl+F keys on your keyboard to search for the plugin's name or a specific feature in the page.

**Example**: for the User Custom Fields plugin, the first icon is shaded, since it is only accessible from the Team plan.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f455e07d.png)

### You are using a self-hosted Piwigo gallery

If you are using a Piwigo gallery that is installed on your own hosting platform, and not on piwigo.com, things are a little bit different.

In order to use a new plugin, you first need to install it on your server, then activate it.

**List of plugins installed**

To find the plugins installed on your Piwigo gallery, go to Piwigo's administration, in the Plugins menu.

The List tab lets you view the plugins that are already activated in your Piwigo gallery, and search among the plugins that are installed but deactivated.

![Plugins auto hébergement.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-44e31d6d.jpg)

**Updating the plugins**

Unlike piwigo.com customers, you need to update your plugins yourself when a new version is available. The Search for updates tab is available to you for this purpose, allowing you to see if updates are available and install them.

![Plugins mise à jour.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-efa434ef.jpg)

If an update is available for a plugin, you can install it right away by clicking on "Install". You can also download the plugin file, or choose to ignore the update.

**Installing a plugin**

If you want to install a plugin, you need to go to the third "Add a plugin" tab.

This page lets you browse all of the plugins published on piwigo.org, which you can also find on [the website's Extensions page](https://piwigo.org/ext/).

You can search for a plugin by keyword or filter the plugins (by date, author, tag, rating...).

![Ajouter un plugin.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-163c6615.jpg)

In this list are some plugins that aren't available on piwigo.com. These are community-made plugins, which the Piwigo developer team hasn't always tested or approved: therefore, we can't guarantee that they work correctly, nor that they are compatible!

!!! info "Info :"
    The plugins we are showcasing in the current documentation are the ones available on Piwigo Cloud, which our team has tested and approved. However, of course, this does not mean that the other plugins available aren't interesting.

To install a new plugin, click on Add.

![Bouton ajouter plugin.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7ee02561.jpg)

You can activate a plugin right after installing it by clicking on the "Activate now" link in the banner.

![Activation plugin special.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-908e71ca.jpg)

If you don't, the plugin is now available in the List tab, in the "Deactivated" category. Simply click on the activation button in order to activate it.

![Plugins désactivés.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f846d4d2.jpg)

## Plugin configuration

Most of the time, plugins have their own configuration page. You have access to them from the list of plugins activated in your Piwigo gallery, by clicking on the Configuration button when it is orange-colored.

![Exemple plugin activé.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7d6d22ae.jpg)

Sometimes, this configuration page only contains a few settings, and you will very rarely need to visit it..

But in some cases, the plugin's configuration gives access to a whole set of important features brought by this plugin. Visiting the configuration page is therefore crucial. Besides, within this documentation, we show a preview of the settings page each time we introduce a plugin.

On the other hand, some plugins don't offer a settings page: in this case, the Configuration button is shaded.

This is the case when the plugin doesn't need a user interface in order to work and offers no settings.

For example, the **Stop Spammers** plugin works on its own as a background task: therefore, it doesn't need a configuration page.

![Stop spammers.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-95090bc0.jpg)

This is also the case when the plugin adds a feature available from another screen in Piwigo.

For example, the **Rotate Image** plugin adds an image rotation feature on a photo's editing page: therefore, it doesn't require a settings page.

![Rotate Image.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5d1afa3a.jpg)

Article summary

---

## Plugins for all your needs

All throughout this documentation, we are introducing plugins every time it is relevant.

You will find some plugin selections in the articles below to answer your needs.

- [Customizing your gallery with plugins](../customizing-your-gallery/customizing-piwigo-gallery-plugins.md)
- [Customizing the Album page with plugins](../browsing-your-piwigo-gallery/albums-in-your-gallery.md)
- [Customizing the Photo page with plugins](../browsing-your-piwigo-gallery/the-photo-page-in-your-gallery.md)
- [Customizing tag management with plugins](../browsing-your-piwigo-gallery/tags-in-your-gallery.md)
- [Customizing comment management with plugins](../comments-and-ratings/plugins-comments-management-piwigo.md)
- [Plugins for administrators](../administration-piwigo/plugins-for-administrators.md)
- [Creating collections with the User Collections plugin](../browsing-your-piwigo-gallery/user-collections-plugin-piwigo.md)
- [Creating smart albums with the SmartAlbums plugin](../organizing-albums/smart-albums-plugin-piwigo.md)
- [Managing contributors with the Community plugin](../managing-users/community-plugin-piwigo.md)
