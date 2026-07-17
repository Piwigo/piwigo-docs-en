# Manual installation

!!! abstract "Manual installation requirements"
    This guide only cover how to install piwigo, to see the required dependencies read the [requirements guide](requirements.md) 

## Step 1 - Download the full archive

[Download the full archive](https://piwigo.org/get-piwigo) and unzip it.

## Step 2 - Upload the archive content

Transfer the archive content to your web server with any FTP client.

!!! info
    The Piwigo team recommends FileZilla as an FTP client because, just like Piwigo, it is free and compatible with Windows and Linux.

Start FileZilla and fill the following connection settings with the information given by your web hosting provider :

- Host
- Username
- Password

Click the Quickconnect button. You are now connected to your web server.

![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155500-5ba173ff.webp)

1.  Create a directory `photos` on your web server.
2.  On you hard disk drive, open the `piwigo` extracted directory.
3.  Select all the files and transfer them on your server in the `photos` directory.

## Étape 3 - Paramétrages

!!! info
    You can also install Piwigo at the website root, the `piwigo` directory is not mandatory. Whatever directory name you choose, it is recommended to avoid showing Piwigo release number.

Once all files are transfered, go to the web address with a web browser, for example `http://example.com/photos` Piwigo will detect nothing is installed yet, and redirect you to the installation page.

<figure markdown="span">
    ![](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155501-48828109-me.webp)
    <figcaption>Installation side</figcaption>
</figure>

Now comes the MySQL database settings and the webmaster account to administer your gallery.

Fill in MySQL database connection settings, as given by your web hosting provider:

- Host 
- User (Warning, your web hosting provider may provide separate connection settings for FTP and MySQL).
- Password
- Database name
- A prefix for Piwigo table names

!!! note ""
    Most often, web hosting providers allow a single database per customer, but you can create as many tables as you want in the same database.  
    To avoid conflicts with other web applications, or allow several Piwigo installations on the same website, the table names have a prefix. By default, this prefix is `piwigo_`, but you can change it (only alphanumeric characters are allowed).

The following is required to create the webmaster account :

- An account identifier, chosen by you
- A password you have to enter twice, for checking
- Your email address, so that visitors can contact you

Run the “Start Install” action.  
You will be informed about either success or failure of the installation process.

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155501-7b2c5f28.webp)
    <figcaption>Successful installation</figcaption>
</figure>

## Step 4 - First connection

Once the installation is finished, you can go into your gallery. Login with your webmaster account, and you can reach the administration panel.

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155501-7cf8f4d0.webp)
    <figcaption>Piwigo is installed</figcaption>
</figure>
