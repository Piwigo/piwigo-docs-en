# PWG Stuffs: adding blocks in your gallery

The **PWG Stuffs** plugin offers various options for adding blocks to your gallery. These blocks enhance the existing pages. This is therefore a very complete plugin to customize your gallery.

It is mainly used for:

- Adding a tag cloud on the home page
- Adding a login area on the home page

---

## Adding a login area on the home page with PWG Stuffs

If your gallery is 100% private, you probably want users who land on the home page to be able to login directly.

This is possible thanks to the **PWG Stuffs** plugin.

In the settings for the PWG Stuffs plugin, go to the "Add a block" tab. Choose "Login" in the list and click on "Add a block".

![Plugin PWG.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-889c76a3.jpg)

You now have access to your block's configuration options. Here, you can customize the title of your login block, specify whether or not this title is displayed on the home page, and set which pages this block is displayed on.

![Nouveau bloc.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c04f30b6.jpg)

Submit. You now land on the block management page.

In front of "Main block", select "Hide on home page".

![Gérer les blocs.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-30d37c64.jpg)

And you're done! Your home page now shows a login form.

![Formulaire connexion.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0bf39463.jpg)

Let's go back to the block management. You can delete an added block by clicking on the red cross, and edit its settings by clicking on the tool-shaped icon.

## Adding a tag cloud on the home page with PWG Stuffs

To add a tag (or keyword) cloud on your home page or another page in your gallery, you also go through the PWG Stuffs plugin.

In the settings for the PWG Stuffs plugin, go to the "Add a block" tab. Choose "Tags" in the list then click on "Add a block".

![Bloc tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-d714fa7c.jpg)

You now have access to your block's configuration options. Here, you can customize the title of your tag cloud block, specify whether or not this title is displayed on the home page, and set which pages this block is displayed on.

You can also choose between 3 display options:

- Tag cloud
- Group by letters
- Use Cumulus mode (the Cumulus Tag Clouds plugin needs to be activated. This plugin is not available for piwigo.com customers)

![Bloc tags config.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-5d29b359.jpg)

Choose the “Tag cloud” option and submit.

And you're done! Your home page now shows a tag cloud.

![Nuage tags accueil.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4e9e6494.jpg)

Let's go back to the block management, edit the block created by clicking on the tool-shaped icon and let's now choose the "Group by letters" option.

Tags are now grouped by letter and in alphabetical order.

![Tags par lettre.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-8abb5e4c.jpg)

## Other features

Apart from the login form and the tag cloud, the PWG Stuffs plugin lets you add other blocks in your gallery: 

- Personal block: adds text or HTML content of your choice, such as a welcome message.
- Last comments: shows the latest comments posted on the gallery
- Random pictures: shows X number of random images in the gallery or in the current album
- Featured photos: shows the favorite images of the user with webmaster status
- Recent pictures: shows recent images of the gallery or the current album (if there are any)
- Best rated: shows X number of best rated images in the gallery or the current album
- Most visited: shows X number of most visited images in the gallery or the current album

## Access authorizations on blocks

You can set up user rights management in order to customize the display of blocks based on the users who are logged in.

To do this, go to the Configuration tab in the settings for PWG Stuffs.

You can manage authorizations:

- By [user status (or type)](../../managing-users/user-statuses.md)
- By [privacy level](../../managing-users/privacy-levels.md)
- By [user group](../../managing-users/user-groups.md)

Let's say that we only want to display a block for anonymous users (not logged into the gallery). In this case, we will activate the rights by user type.

![Config blocs PWG.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0a7a7157.jpg)

In the settings for a block, we will now be able to select the users who are allowed to see this block. In our case, we will only select "Guest". This way, only users who are not logged in will see this block.

![Modifier bloc tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-88811045.jpg)

## Alternating modules

With this plugin, you can go quite far into the customization of your gallery's content based on the users.

Indeed, for each module, you can choose the type of page it will be displayed on, the type of user that will see it, the line where it will be displayed and its width. By playing with these elements, you can alternate two modules in one location.

For example:

- Module 1 *EDITORIAL*, (display settings: line A, 60%, displayed on main page only, visible for all), could contain an introduction to your gallery.
- Next to it, Module 2 *NEWS*, (display settings: line A, 40%, displayed on main page only, only visible for logged in users), could make new visitors want to create an account if that's possible.
- Module 3 *WELCOME*, (display settings: line A, 40%, displayed on main page only, only visible for logged in users), could contain their username and a welcome message.

Upon arrival, the user sees the *EDITORIAL* in the top left, with the *NEWS* to the right. When logging in, NEWS is replaced with *WELCOME*. Then, when they start visiting the albums, these modules disappear to make more room for your gallery's content.
