# Installation Docker

!!! abstract "Docker install requirements"
     This guide assume you can connect to your server via ssh and already have installed docker, if that's not the case follow the [official docker documentation](https://docs.docker.com/engine/install/)

## Step 1 - Installing the container

Connect to your server and create a folder named `Piwigo` then download the `compose.yaml` from the [Piwigo/piwigo-docker](https://github.com/Piwigo/piwigo-docker) repository inside it.

!!! tip "You can use curl to download `compose.yaml` without leaving the terminal :"
    ```
    curl -O "https://raw.githubusercontent.com/Piwigo/piwigo-docker/refs/heads/main/compose.yaml"
    ```

Create a file named `.env` with the following :

=== "Required fields"

    ```bash
    piwigo_port=8080
    db_user_password=
    timezone=
    ```

=== "Field explanation"

    ```bash
    piwigo_port= # the exposed port by docker
    db_user_password= # Database password
    timezone= # Container timezone
    PIWIGO_UID= # the UID of the user who will own the Piwigo folder
    PIWIGO_GID= # the GID of the group who will own the Piwigo folder
    ```
    
=== "Default values"
    ```bash
    piwigo_port=8080
    db_user_password=
    timezone=UTC
    PIWIGO_UID=1000
    PIWIGO_GID=1000
    ```

=== "Sample config"

    ```bash
    piwigo_port=10004
    db_user_password=Nkhcfnfk5GmpnLGIFoIDJqRFPW22C7PlyEUYVaB1lkte5Dn0wOQs3TI4wom1E4A6
    timezone=Europe/Paris
    PIWIGO_UID=1001
    PIWIGO_GID=1004
    ```

!!! tip "Tip" 
    You can use the following command to generate a valid password : 
    ```bash
    printf $(tr -dc '[:alnum:]' </dev/urandom | head -c64)"\n" 
    ```
    
Start your container with : `docker compose up -d`.  
You can read the logs with `docker compose logs`.

## Step 2 - Configure the reverse proxy

It's advised to use the piwigo container behing a Reverse proxy like NGINX

!!! info
    Piwigo supports being hosted on a domain, subdomain, and/or subpath; whatever you choose, it's advised to not use the Piwigo release number in the URL.

You can use the following Nginx config examples : 

!!! Warning ""

    If you changed piwigo_port in `.env` you will also need to modify the `proxy_pass` section to reflect that.  
    **Keep in mind that Docker will ignore all your firewall rules by design.**

=== "Host on a domain or sub domain"

    ```nginx
    server {
      listen 80;
      server_name my_domain.tld;
      location / {
        proxy_pass http://127.0.0.1:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
      }
    }
    ```

=== "Host on a subpath"

    f you intend to host Piwigo on a subpath like `my_domain.tld/gallery`, you will need to forward it to the container by adding `proxy_set_header X-Forwarded-Prefix /gallery`

    ```nginx
    server {
      listen 80;
      server_name my_domain.tld;
      location /gallery/ {
        proxy_pass http://127.0.0.1:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Prefix /gallery;
      }
    }
    ```

## Step 3 - Configuration

Once the container is started and your reverse proxy is configured, open a web browser to the web address you are hosting Piwigo on. Piwigo will detect nothing is installed yet, and redirect you to the installation page

<figure markdown="span">
    ![](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629150900-80ede7d4-me.webp)
    <figcaption>Installation side</figcaption>
</figure>

Fill in MySQL database connection settings with the following :

- Host : `piwigo-db:3306`
- User : `piwigodb_user`
- Password : Use the password you wrote in the `.env` file
- Database name : `piwigodb`
- A prefix for Piwigo table names : `piwigo_` 

The following is required to create the webmaster account :

- An account identifier, chosen by you
- A password you have to enter twice, for checking
- Your email address, so that visitors can contact you

Run the “Start Install” action.

<figure markdown="span">
    ![](https://ressources.piwigo.com/i?/uploads/c/v/7/cv7jpz6hf8//2026/06/29/20260629150900-9d12dd40-la.webp)
    <figcaption>Successful installation</figcaption>
</figure>

You will be informed about either success or failure of the installation process.

## Step 4 - First connection

Once the installation is finished, you can go into your gallery. Login with your webmaster account, and you can reach the administration panel.

<figure markdown="span">
    ![](https://ressources.piwigo.com/uploads/c/v/7/cv7jpz6hf8//2026/06/26/20260626155501-7cf8f4d0.webp)
    <figcaption>Piwigo is installed</figcaption>
</figure>
