# Tag Recognition: Tag your photos automatically with AI

Do you have an important number of photos and you want to tag them quickly and automatically? This is possible using the Tag Recognition plugin.

!!! info "If you are a Piwigo Cloud customer, this plugin is only available from the Enterprise plan and higher."

## Choosing which API to use

Once the Tag Recognition plugin has been installed and activated, go to the plugin's settings.

You first need to choose which solution you will use to generate tags automatically. 

Indeed, the plugin uses a third-party image recognition API, which handles photo analysis and tag generation. You can choose between two solutions:

- [Imagga](https://imagga.com/)
- [Microsoft Azure AI Vision](https://azure.microsoft.com/en-us/products/ai-services/ai-vision/)

The choice depends on your preferences and the amount of photos that need to be analyzed. Indeed, these two solutions offer a free plan, and fee-based offers above a certain amount. All the details are available on the providers' websites.

!!! info "Since this plugin uses an external API, we cannot ensure that your data won't be used or sold. We recommend checking the data policy for each external API that you use with this plugin."

## Setting up Tag Recognition with Imagga

If you choose Imagga, here are the steps to follow.

First of all, you need to create an account on the [https://imagga.com/](https://imagga.com/) website.

In your account's dashboard, you will find two pieces of information that you need: your API key and your secret key (*API Secret*).

![Imagga.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-f988b6ea.jpg)

Copy these two keys and paste them in the Tag Recognition plugin's configuration screen. Click on Save settings.

![Reconnaissance des tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2f92ec50.jpg)

[Imagga Documentation](https://docs.imagga.com/)

## Setting up Tag Recognition with Azure AI Vision

If you choose Azure AI Vision, here are the steps to follow.

First of all, you need to create an account on the [https://azure.microsoft.com/en-us/free/](https://azure.microsoft.com/en-us/free/) website.

Once you are logged into your account, you need to go to the Computer Vision service. If you don't have a subscription, choose the trial period to begin. You will then be able to claim your API Endpoint and your API Key to enter them in the Tag Recognition plugin's configuration.

![Untitled](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-3c10df32.png)

[Azure AI Vision Documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview?wt.mc_id=searchAPI_azureportal_inproduct_rmskilling&sessionId=8acf0be16fd54e18a988e52fa4dc2edd)

## Using Tag Recognition to suggest tags on a photo

Once the plugin has been set up correctly, you will be able to use it to automatically generate tags.

To do this, choose a photo you want to tag, and edit it.

In the input field for the tags related to this photo, click on the robot-shaped icon.

![Tag robot.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-adc3fc23.jpg)

You can now choose how many tags you want to generate, and which language to generate them in.

![Générer des tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-3c189468.jpg)

Let's try to generate 10 tags for this photo of a dog, in English.

![pauline-loroy-U3aF7hgUSrk-unsplash.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-61bd9029.jpg)

The API suggests the following tags:

![Tags suggérés.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-991aa7b8.jpg)

Click on the tags you like, and click on "Apply tags": the tags are added to your photo. Don't forget to click on "Save settings".

## Using Tag Recognition to apply tags to a selection in bulk

If you want to go fast, you can generate tags in bulk with the [Batch Manager](../import-and-manage-photos/batch-manager-piwigo.md).

Indeed, a new action is made possible in the batch manager: "Tag Recognition".

Make your selection of photos, select the "Tag Recognition" action. Choose the number of tags to generate and the language.

![Gestion lot générer tag.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-06c13dd0.jpg)

Click on "Apply action": the process begins. The photos are processed one by one.

![Chargement des tags.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-c58d2705.jpg)

Once the batch has been processed, the photos are tagged! You can go to the "Single mode" tab in the batch manager to make sure you like the chosen tags.

![Tags générés en masse.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-e3fc3d90.jpg)
