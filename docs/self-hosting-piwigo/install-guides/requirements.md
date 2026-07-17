# Requirements

Piwigo requires a web hosting to run. For a photo gallery solution with all included (installation, hosting, backups), or if you simply want to try Piwigo with no installation, you may consider [opening a free trial account on
Piwigo Cloud](https://piwigo.org/inscription).

### Minimum Requirements

- A web server like Nginx or Apache
- MySQL 5.6+ or MariaDB 10.1+. MySQL 5.0 works but is no longer maintained.
- PHP 8.2+. Piwigo can run with PHP 7.4+ but these end-of-life versions are no longer maintained and may expose your site to security vulnerabilities. See [officially PHP supported versions.](https://www.php.net/supported-versions.php)
- A graphic library: ImageMagick is recommended for its performances and image quality but GD, often bundled with PHP, can also do the job.
- an FTP client software will be required to upload the files (netinstall or full package): Piwigo team recommends FileZilla as FTP client software, because it is free as Piwigo is, and compatible with Windows, Mac and Linux.
- Enough disk space for your pictures: in addition to the photos you upload, Piwigo will store the "multiple sizes" in a cache directory of your server.

### Optional Requirements

- `exiftool` is required for plugin Write Metadata or any other plugin dealing with EXIF/IPTC metadata
- `ffmpeg` is required for plugin VideoJS to create video poster
