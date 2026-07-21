# Editing the local configuration with LocalFiles Editor

## Introduction

The local configuration consists of editing specific settings of your Piwigo gallery, which can't be edited through a visual interface in the administration.

These settings are stored in a configuration file: `config_default.inc.php`

This file must **NEVER** be edited: however, you can *overload it by using the* **LocalFiles Editor** *plugin*.

!!! tip "Tip :"
    We very strongly recommend you don't edit Piwigo's files directly through FTP. Using the **LocalFiles Editor** plugin has many benefits, as you will see.

## Activating the LocalFiles Editor plugin

The first step when editing the local configuration is to activate the LocalFiles Editor plugin.

![Plugin LFE.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-2f3c60d6.jpg)

Once the plugin has been activated, click on "Configuration".

You then have access to the screen below, with an empty file.

![LFE auto hébergement.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-4b38d1fb.jpg)

## Default configuration

From this screen, you have access to the default configuration file, which lists all available configuration options in this file: to do this, click on the *Display reference file: "config_default.inc.php"* link in the top right corner of the screen.

Each line that starts with `$conf` represents an option.

Options are grouped into logical sections (urls, tags, related albums…).

Above each option, a section of comments (starting with `//` ) explains the role of the option.

Let's take an example with the `'enable_formats'` option: this options lets you activate or not activate the handling of multiple formats in your gallery. It is deactivated by default  (`false`).

```php
// enable_formats: should Piwigo search for multiple formats?
$conf['enable_formats'] = false;
```

## Editing the local configuration

As we said, you should not edit the configuration file provided with your Piwigo gallery.

LocalFiles Editor will allow you to overload the settings for this file, meaning to specify which settings need to be edited compared to the original file.

Let's take the previous example again: let's imagine that you want to activate the handling of [multiple formats](../import-and-manage-photos/multiple-formats-piwigo.md).

You only need to copy the section that corresponds to the `'enable_formats'` setting and paste it in the Local Config tab of LocalFiles Editor. You can now replace the `false` value with `true` just like the example below.

!!! warning "Warning! The file must always start with `<?php` and end with `?>`."

![LFE Code.jpg](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8/2026/07/03/20260703190344-cf33c6f7.jpg)

Save the file: the setting is updated and the management of multiple formats is activated.

!!! info "Info :"
    We recommend you also copy the explanation in the comments above the line that contains the configuration setting. This way, it will be easier for you to remember the role of each setting.

Article summary
