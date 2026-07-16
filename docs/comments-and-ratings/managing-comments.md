# Managing comments

With Piwigo, you can allow users in your gallery to add comments on the content of your photo library.

## Turning comments on or off in your gallery

To turn comments on or off in your gallery, go in the administration, in the Configuration > Options menu, then the Comments tab.

To turn on comments, select the option "Activate comments" and save the settings. However, start by taking the time to look at the available options (see next chapter)!.

## Comment management options

Once the option to "Activate comments" has been selected, multiple sub-options appear: browse them attentively!

![Configuration commentaires.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c8c4a805.jpg)

Some further details about some of these options:

- **Comments for all**: if you select this option, even anonymous visitors (not logged in to your gallery) can leave a comment;
- **Validation**: if you select this option, comments will not be posted straight away; they will need to be approved by an administrator before becoming visible in your gallery.
- **Notify administrators**: if you select the option "Validation", we recommend you activate the administrator notification when a comment is **awaiting approval**. You can also ask administrators not to approve comments, but simply inform them when a comment is posted, by selecting the option "Notify administrators when a comment is **added**".

### Some tips to avoid spam in the comments:

A checking is set up by default to avoid misuse: if a user tries to post multiple comments on one photo from the same IP address within a very short time span, the system blocks the second comment from being sent.

But this doesn't solve all problems. 

If your gallery is public and you accept comments from anonymous users, you are taking a risk: your comments might get polluted by spam bots.

To avoid this, we recommend you follow some good practices:

- Don't select the option "Allow users to add a link to their website": when anyone can leave a comment on a website, this option is very popular among spammers;
- Force users to give information in order to leave a comment (email address, username)
- If necessary, add an anti-spam control on comments (to learn more, visit the [Customizing comment management with plugins](plugins-comments-management-piwigo.md) page)

## Appearance of comments in the gallery

In your gallery, comments are displayed at the bottom of the photo on a photo's page (in most themes).

If comments are only allowed for users who are logged in, anonymous visitors will be able to see the number of comments and read the comments posted, but they will not see the comment posting form displayed.

### Appearance of comments with the Modus theme

In galleries that use the Modus theme, the entry form for new comments is displayed on the left for each photo, and the list of comments that have already been posted is on the right.

![Espace commentaires.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-b84b8dea.jpg)

### Appearance of comments with the Bootstrap Darkroom theme

In galleries that use the Bootstrap Darkroom theme, the posted comments are displayed on the right under each photo.

![Espace commentaires BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-22f4823c.jpg)

The "Add a comment" button lets you open a new comment input tab.

![Ajouter commentaire BD.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-41ea19aa.jpg)

### Comment page in your gallery

In your gallery, you can see all comments thanks to the page under the Explore > Comments menu.

This page shows all comments posted on your gallery with the associated photo, the date, etc.

You can choose to sort comments by photo or by date, and use the search engine to filter comments (by album, by author, by searching for a specific word...).

![Voir commentaires.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-89e11245.jpg)

<aside>
💡 Note: from this page, administrators can approve, edit and delete comments.

</aside>

## Managing, editing, deleting comments

### Approving awaiting comments after an email

When a new comment is waiting to be approved and the administrators get notified (see chapter "Comment management options"), they receive an email as shown below with a mention saying "this comment requires validation".

![Validation commentaire.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-6c7cbb66.jpg)

The "Manage this user comment" link gives you direct access to the comment in the gallery, and provides you with the 3 options available: Validate, Delete (equals rejecting the comment), Edit.

![Valider commentaire.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e813e195.jpg)

### Approving pending comments in the administration

From Piwigo's administration, you can manage comments from the Tools > Comments menu.

From this screen, you can see all comments posted on your gallery by clicking on "All". If you have activated the "Validation" option, you will find the comments waiting for approval using the red "Pending" label.

![Liste commentaires.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-a609a283.jpg)

To only see comments waiting for approval, click on the "Pending" button.

To approve or reject a comment, simply select it and click on "Validate" or "Reject".

![Commentaire en attente.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-de9d13a7.jpg)

Once a comment has been rejected, it is not visible in the list anymore.

Note: when a comment is awaiting approval, a banner is displayed on the administrators' dashboard. A button gives them direct access to the pending comment management page.

![Attente validation.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-734bc3b2.jpg)

### Editing or deleting a comment

Administrators can delete or edit users' comments from the gallery.

When an administrator is viewing a photo's comments in the gallery, they have access to two actions for each comment: "Edit" and "Delete". If the comment is waiting for approval, the "Validate" action is also available.

![Modifier ou supprimer.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-65f2ade6.jpg)

<aside>
ℹ️ If you selected the options that allow users to delete / edit their own comments, they will also have access to these actions on their comments (except for anonymous users who are not logged in).

</aside>

Of course, these actions are also available from the gallery's comment page.

When administrators are notified by email after every comment upload (without approval), they receive an email which contains a link to read, and potentially edit or delete the comment.

Article summary

---

Next →

[Customizing comment management with plugins](plugins-comments-management-piwigo.md)