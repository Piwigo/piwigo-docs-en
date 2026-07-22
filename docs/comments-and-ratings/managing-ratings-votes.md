---
title: Managing ratings (votes)
description: This article explains how to allow visitors to your Piwigo gallery to rate your photos.
---

# Managing ratings (votes)

With Piwigo, you can allow visitors of your gallery to rate photos and other files by assigning them a number of stars. This allows you to set up a voting system to organize photo competitions, for example.

## Activating or deactivating ratings

To activate or deactivate ratings, go in the administration, in the Configuration > Options menu.

In the Permissions section, check or uncheck the option to "**Allow rating**".

If you check this box, a new option will appear: "Rating by guests". Select this option if you accept that all visitors (even anonymous) can rate a file, and deselect it if you want to keep this feature only for users logged in to your gallery.

## Displaying ratings in your gallery

When ratings are activated in your gallery, two new attributes appear next to a photo:

- Score: Here, the photo's score is displayed (meaning, the average rating, weighted by the number of ratings) as well as the number of votes.
- Rate this photo: allows visitors to rate the photo by clicking on the desired number of stars (1 star = 0, 6 stars = 5). A user can edit their rating at any moment.

![Score et note.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-91833265.jpg)

When ratings are activated, a "Best rated" tab is added to your gallery.

It lets you view all photos that have been rated, sorted by score (from highest to lowest).

![Mieux notées.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-3f36fdac.jpg)

!!! info "Why use a weighted score rather than an average rating?"
    
    If we use the average rating, a photo with one 5/5 rating will be considered as having a better rating than a photo with 500 ratings and an average of 4,8/5. In a competition setting, this is not relevant.


## Managing ratings in the administration

To manage ratings in the administration, go to the Photos > Rating menu.

This screen contains two tabs: Photos and Users.

### Ratings by photo

The Photos tab shows the list of photos that have been rated, and, for each of them, all the information related to the ratings (number of ratings, score, average rating, sum of the ratings, users who have voted, vote dates...).

You can sort this list based on various criteria. You can also filter ratings by user type (logged in users or anonymous guests). Lastly, you can filter the list by album.

You can delete all ratings on a photo and reset the score by clicking on the trash can on the right of each line.

To edit a photo, click on its thumbnail: you will be redirected towards the photo editing screen.

![Toutes les notes.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-ae35fb19.jpg)

### Ratings by user

The user tab shows the list of users who have rated photos, and, for each of them, all the information related to the ratings (date of the last rating, number of ratings, average rating, distribution of votes per rating...).

You can filter the list to only show users who have left more than a certain number of ratings.

You can delete all ratings left by a user by clicking on the trash can on the right of the line.

![Tous les noteurs.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-edd593fe.jpg)

## Resetting all ratings

The Delete Hit/Rate plugin lets you reset all ratings:

- Of a specific photo, straight from the photo editor
- Of all the photos in an album, straight from the album editor

It also allows you to reset all ratings of the gallery from the Tools > Maintenance page.
