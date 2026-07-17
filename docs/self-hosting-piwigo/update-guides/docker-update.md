

!!! info "Ce guide concerne uniquement les utilisateurs de l'image Docker officielle."
    This guide only apply to the official Piwigo image, if you are using a Linux server container please use their documentation instead.    
     If you want to switch to the official image you can [follow this guide](https://github.com/Piwigo/piwigo-docker/wiki/Migration-Guide-from-the-LinuxServer)

## Step 1 - Checking for updates

Container's version numbers will always match the Piwigo version, starting from 16.3.0 they will have an extra letter after to allow container specific updates

=== "Container version 16.3 and higher"

    You should already be able to see if any update is available in the update interface :
    
    <figure markdown="span">
      ![](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629172514-64cac366-la.webp)
      <figcaption>Update list example</figcaption>
    </figure>
    
=== "Container version 16.2 and lower"

    Go to the taglist on [dockerhub](https://hub.docker.com/r/piwigo/piwigo/tags) or on [GitHub](https://github.com/Piwigo/piwigo-docker/pkgs/container/piwigo) and find the tag you want

## Step 2 - Create a backup

To make sure updating is risk free, you should make a backup of both the database and the files of your Piwigo instance.
Go to the folder where your `compose.yaml` is

### Backup your database

You can create a backup of your database using the following command (replace `piwigo-db-1` by your database container name):

```bash
docker exec -it piwigo-db-1 mariadb-dump -u piwigodb_user -p "piwigodb" | tee db_dump.sql 
```

### Backup your gallery and config files

To backup any image/photo uploaded and your current configuration to your Piwigo, copy the following folders : `galleries`, `upload` and `local` fromt the `./piwigo-data/piwigo/` folder.

!!! Warning "Depending on the amount of photos you have the `galleries` and `upload` can take a lot of space" 

### Backup your `compose.yaml` and `.env` files

Rename your `compose.yaml` and make a copy of your `.env` (par exemple rajoutant `.bak` à la fin)

???+ tip "You can use the following commands to create a backup with a timestamp"

    ```bash
    mv compose.yaml "compose.yaml_$(date '+%F-%H-%M-%S').bak" 
    cp .env "env$(date '+%F-%H-%M-%S').bak"
    ```

## Step 3 - Pulling the new compose file and updating `.env`

- Download the version of the `compose.yaml` that correspond to the tag choosen during [step 1](#step-1-checking-for-updates)

!!! tip ""

    You can use the following command to fetch it, just swap `<TAG>` by the tag you choose (eg: `16.4a`)

    ```bash
    PWG_DOCKER_VERSION="<TAG>"; curl -O "https://raw.githubusercontent.com/Piwigo/piwigo-docker/refs/tags/v$PWG_DOCKER_VERSION/compose.yaml" 
    ```
    
- Check the [Github Wiki](https://github.com/Piwigo/piwigo-docker/wiki/Environment-file-updates) page and update your `.env` file accordingly.

??? example "Example of an update from version 15.6 to version 16.3c"

    `.env` before the update :

    ```
    piwigo_port=8080
    db_user_password=4JKQplDWaePjjwqiuAmcWWrwY3oqxWtxRs2XCEObf1wRdD2boDa6VA804kzQm2kj
    ```
    
    We add the timezone field because it was introduced in `15.7.0` and the UID/GID fields that was introduced in `16.3.0c` 

    ```
    piwigo_port=8080
    db_user_password=4JKQplDWaePjjwqiuAmcWWrwY3oqxWtxRs2XCEObf1wRdD2boDa6VA804kzQm2kj
    timezone=Europe/Paris
    PIWIGO_UID=1004
    PIWIGO_GID=1001
    ```

## Step 4 - Updating and restarting the container

Pull the image with `docker compose pull` and restart your containers with `docker compose up  -d`.  
You can check the logs with `docker compose logs` to check that everyhting is working fine.
