# Customizing comment management with plugins

In the article about [Managing comments](managing-comments.md), we introduced the basic options for managing comments in Piwigo. But there are several plugins that allow you to go further: in this article, we are going over these options.

## Comment formatting options

### BBCode Bar: Adding a tool bar to format comments

If you want users to be able to format their comments (bold text, italic text, bullet points...), simply install the **BBCode Bar** plugin.

This plugin lets you display a formatting bar in the comment window. You can choose whether or not to activate the options.

![BBCode Bar.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ff9b017e.jpg)

### Smilies Support: Adding emotes in comments

If you want users to be able to add emotes in comments, simply install the **Smilies Support** plugin.

This plugin lets you choose a set of emotes to add to your gallery. When entering their comment, the user can choose an emote in the list.

![Smilies.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f370aea2.jpg)

!!! note "Note"
    These emotes are the same kind of emotes you would find on discussion forums. They are not to be mistaken for emojis, which we use far more nowadays. Piwigo doesn't have an emoji keyboard.

## Subscribe to Comments: Enable notifications for anyone when new comments are posted

If you want a user (other than an administrator) to be able to get notified when a new comment is posted, simply install the **Subscribe to Comments** plugin.

Once this plugin has been activated, when typing a comment, a user will be able to choose to get notified:

- When a new comment will be posted on this photo (this equals subscribing to this photo's comments);
- When a new comment will be posted on a photo from the same album
- When a new comment will be posted on the site

![Zone de commentaires.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-0f344f4b.jpg)

A user can totally subscribe to comments without typing any comment themselves: to do this, simply click on "Subscribe without commenting".

When a person is subscribed to comments, they receive an email as shown below for every new comment. From this email, it is possible to click on the image to see the photo, to unsubscribe from this photo's comments, and to manage all comment subscriptions.

![image.png](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-7e1f590a.png)

## Avoiding spam in the comments

Sadly, comment input areas are often popular among spam robots. Sometimes, it is therefore necessary to set up preventive actions to avoid spam.

Several plugins allow you to control comment input in Piwigo.

### Comments Blacklist: Banning certain words from comments

To set a list of banned words in the comments, you can install the **Comments Blacklist** plugin.

This plugin lets you enter a list of banned words. If a comment containing these words is written, its publishing will either be blocked or subjected to moderation (depending on your choice).

This allows you to ban words that are often used in "spam" comments, but also to avoid rude, offensive or inappropriate comments.

### Crypto Captcha: Adding a Captcha in the comment area

To add a Captcha to the comment input form, you can install the **Crypto Captcha** plugin.

This plugin forces users to enter a Captcha before approving a comment. This Captcha can also be added to the new user creation form, in order to avoid creating "fake accounts".

Several options are available to set up your Captcha.

![Captcha.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-216bec65.jpg)

### RV Akismet: Monitoring comments with Akismet

You can use the [Askimet](https://akismet.com/) online service, a reference in the field, to make sure comments that are entered in your gallery aren't spam.

To do this, simply install the **RV Akismet** plugin.

Once the plugin has been activated, you need to create an Akismet account: this will give you access to an API key that you will need to enter in the plugin's configuration.

!!! info "Info :"
    You can create a free Akismet account, but some options require paying for a subscription. Free accounts are only for personal, non-commercial use.

The plugin gives you a choice between two options:

- Rejecting all comments flagged as spam by Akismet
- Moderating comments flagged as spam by Akismet (meaning, subjecting them to approval before posting).

## Comments on Albums: Allowing comments on Album pages

By default, Piwigo manages comments on photo pages.

However, if you want, you can also activate a comment area on Album pages.

To do this, simply activate the **Comments on Albums** plugin.

Once this plugin has been activated, it adds a comment input window on the album pages in your gallery.

The comments on album pages are subjected to the same rules and the same settings as photo comments.

![Commentaire album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ded72f82.jpg)

Once this plugin has been activated, an Albums tab is added:

- on the comment management page in the administration
    
    ![Commentaire sur album.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-16c3f423.jpg)
    
- on the listing page that lists comments in the gallery
    
    ![Commentaire utilisateur.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b2691fa8.jpg)
