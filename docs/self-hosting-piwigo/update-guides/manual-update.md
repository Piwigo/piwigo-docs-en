# Manual Update

This procedure is compatible with any version greater or equal to 1.4. For an older version, ask for help on the forum.

!!! warning "Check the new requirements"
    Please do check Piwigo current [Requirements](../install-guides/requirements.md). Especially if your **PHP** / **MySQL** configuration is NOT sufficient, do not go further as the upgrade process will fail.

## Step 1 - Package preparation

- [Download the latest Piwigo release archive](https://piwigo.org/get-piwigo)
- On your computer, extract the `piwigo` directory.
- Remove the default `piwigo/local` directory.

## Step 2 - Database preparation (Recommended)

Backup your current tables

If you are using a version from the PhpWebGallery 1.7 family or later, you can use the DB Backup plugin. Previous releases users should have to backup their tables by other means, for example with phpMyAdmin.

<figure markdown="span">
    ![](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172445-b7bbee28-me.webp)
    <figcaption>PhpMyAdmin recommended options.</figcaption>
</figure>

!!! info
    Our advice: unselect “Extended inserts” or reduce “Maximal length of created queries”.

In any case, be sure to check the backup is exhaustive and has successfully completed (the result is sometimes truncated due to server limits).

## Step 3 - File server preparation

!!! info "If you're running Piwigo 2.1 or higher, skip this step."

Backup your customized files only or all files

- Download the `Prepare 2.1 Upgrade` extension tool
- extract the `prep21up.php` script and transfer it at the root of your Piwigo installation
- open `prep21up.php` from your web browser `http://exemple.com/photos/prep21up.php` and you will receive an `upgrade21.zip` archive
On your computer, extract the `local` directory from `upgrade21.zip` into the `piwigo` directory (extracted during [step 1](#step-1-package-preparation)).

## Step 4 - Gallery preparation

**Lock the gallery**

With Piwigo 2.3 or earlier version: Configuration > General > Lock gallery. For Piwigo 2.4+: Tools > Maintenance.

From now on, non-administrator users of any gallery version should see something like: “The gallery is locked for maintenance. Please, come back later.”.

<figure markdown="span">
    ![](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172446-132e2d1c-me.webp)
    <figcaption>Lock gallery</figcaption>
</figure>

## Step 5 - Cleaning

Remove all files of your current Piwigo installation

!!! Danger "with the following exceptions, do NOT delete these directories :"
    - Galleries
    - Upload
    - Plugins
    - Themes
    - Template-extension
    - Local
    - _data

## Step 6 - FTP upload

Use your standard FTP client to upload the new release, ie the content of the `piwigo` (directory (extracted during [step 1](#step-1-package-preparation) and updated during [step 3](#step-3-file-server-preparation)), into the previous Piwigo installation directory.

Check that your FTP client did not encounter any error.

## Step 7 - Database upgrade

**Launching upgrade**

In your web browser, open the `upgrade.php` script and follow the guide, `http://example.com/photos/upgrade.php`

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172446-2bb8d9d9.webp)
    <figcaption>Starting upgrade page.</figcaption>
</figure>

To avoid any upgrade by another visitor you are invited to sign in

---

Your previous release is identified and you will get a summary of the upgrade operations.  

Plugins active before the upgrade will be switched off to inactive status, as they could fail to work with the new release and need their own specific upgrade.

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172446-82c85f1c.webp)
    <figcaption>Upgrade memo page.</figcaption>
</figure>

Plugins active before the upgrade will be switched off to inactive status, as they could fail to work with the new release and need their own specific upgrade.

## Step 8 - Check the upgrade result

Your first controls could take time because you are not aware of all the changes.

You will see a list of all your previous plugins; some of them have been fully integrated in the core (like Plugins Manager), others are now distributed (like LocalFiles Editor), but any desactivated plugin has been so for a good reason.

Try to find an upgrade first; the plugins tabsheets can help you.

For themes, keep an admin page opened in your browser in case you need to reverse any of your tests.

Don't forget that your members or visitors can have a specific selected theme which is not compatible with your new release. You'd probably better have to reset their theme in the Admin users page.

## Step 9 - Unlock your gallery

You begin to be confortable with our last release, do not forget to unlock your gallery to give access to visitors.

## Step 10 - Post upgrade cleaning

**Nothing**

Nothing has to be removed after any upgrade. The `upgrade.php` itself is not to be removed. Remember that the “No upgrade required” message and the sign-on process are protecting your gallery.
