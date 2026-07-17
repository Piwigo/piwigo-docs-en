# Automatic Update

This is the recommended method to upgrade your Piwigo to the latest release. So simple you have no more excuse to forget or postpone your upgrades. It truly takes less than 1 minute to run the latest and most secure Piwigo release.

!!! info "Make Backups !"
    Always have a backup of your database and files. The best is to have them made automatically on a regular basis. If anything bad happens during the update, you would be able to retore a backup.

## One single step

Go to Administration > Tools > Updates and follow the guide

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172500-ab117913.gif)
    <figcaption>Yes, only 2 clickss</figcaption>
</figure>

??? note "If you are running a version older than Piwigo 2.3.0"
    === "Piwigo 2.1.x or 2.2.x"
    
        1. Go to Administration > Plugins > Manage > Other plugins available and install Piwigo Auto Upgrade. If the plugin is already installed, check you're running the latest revision on the Administration > Plugins > Manage > Check for updates screen.
        2.  Go to Administration > Plugins > Manage > Plugins list to install and activate this new plugin.
        3.  Go to Administration > Plugins > Piwigo AutoUpgrade and follow the guide.
    
    === "Piwigo 2.0.x"
    
        1.  Administration > Specials > Plugins > Other Plugins and perform an automatic installation of Piwigo Auto Upgrade. If the plugin is already installed, check you're running the latest revision.
        2.  Go to Administration > Specials > Plugins to install and activate this new plugin
        3.  Go to Administration > Specials > Plugins > Piwigo AutoUpgrade and follow the guide, you can either choose to upgrade to the last release of the same “branch” or to the very latest Piwigo release.
    
    === "Piwigo 1.7.x"
    
        1.  Download the Piwigo Auto Upgrade plugin and unzip it into your “plugins” directory
        2.  Go to Administration > Specials > Plugins > Administration and click on the “install” action in front of “Piwigo AutoUpgrade” plugin and then the “Activate” action.
        3.  Go to Administration > Specials > Plugins > Piwigo AutoUpgrade and follow the guide, you can either choose to upgrade to the last release of the same “branch” or to the very latest Piwigo release.
    
    
    === "Older than Piwigo 1.7.x"
    
        If you have an earlier release, please follow the [Manual Upgrade Guide](manual-update.md) instead.
