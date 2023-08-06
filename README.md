# Artemis:

Projeto Artemis

## Requirements:

* Python `3.11.4`.
* Git `2.41.0` or superior.
* For production deploy, we strongly install on `Ubuntu 22.04`.

## Minimal Hardware

* 4 GB
* 2 CPUs
* 80 GB/ SSD DISK

# 1. Installation

## Download Repository

```sh
cd ~/

git clone https://github.com/DavidBrito/Artemis.git
```

## 1.1 Nginx

Install Nginx:

```sh
sudo apt update

sudo apt install nginx
```

Adjusting the Firewall:

```sh
sudo ufw allow 'Nginx Full'
```

Checking your Web Server

At the end of the installation process, Ubuntu 22.04 starts Nginx. The web server should already be up and running.

We can check with the systemd init system to make sure the service is running by typing:

```sh
systemctl status nginx
```

```sh
Output
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2023-08-06 16:08:19 UTC; 3 days ago
     Docs: man:nginx(8)
 Main PID: 2369 (nginx)
    Tasks: 2 (limit: 1153)
   CGroup: /system.slice/nginx.service
           ├─2369 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─2380 nginx: worker process
```

When you have your server’s IP address, enter it into your browser’s address bar:

```sh
http://your_server_ip
```

Replace file `/etc/nginx/sites-available/default` to this script:

```sh
server {
    listen 80 default_server;
    listen [::]:80 default_server; 
    root /var/www/html;
    index index.html;

    server_name _;

    location / {
        try_files $uri $uri/ /index.html;
        add_header Cache-Control "no-cache";
    }

    location /static {
        expires 1y;
        add_header Cache-Control "public";
    }

    location /api {
        include proxy_params;
        proxy_pass http://127.0.0.1:5000;
    }
}

```

Delete old data from default Nginx HTML Path:

```sh
rm -rf /var/www/html/*
```

Reload Services:

```sh
systemctl restart nginx
```

### 1.2 Python


Use the following command to install prerequisites for Python before installing it.

```sh
sudo apt install curl git

git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.12.0

```

Add the following to ~/.bashrc:

```sh
. "$HOME/.asdf/asdf.sh"
```

Completions must be configured by adding the following to your .bashrc:

```sh
. "$HOME/.asdf/completions/asdf.bash"
```

Download Python using following command from asdf. You can also download any latest version in place of specified bellow from ```sh asdf list all python```:
```sh
asdf plugin-add python
asdf global python 3.11.4
```

Check Python Version

```sh
python -V
```

Install Python Requirements

```sh
pip install -r requirements.txt
```

Configure Gunicorn as Service:

```sh
nano /etc/systemd/system/artemis.service
```

Copy and Paste this code on `artemis.service`. Remember to check if ARTEMIS path is correct.

```sh
[Unit]
Description=ARTEMIS Service
After=network.target

[Service]
User=root
WorkingDirectory=/root/artemis/api
Environment="PATH=/root/.asdf/installs/python/3.11.4/bin"
ExecStart=/root/.asdf/installs/python/3.11.4/bin/gunicorn -b 127.0.0.1:5000 "server:create_app('default_config')"
Restart=always

[Install]
WantedBy=multi-user.target
```

Reload Daemons:

```sh
sudo systemctl daemon-reload
```

Enable Service:

```sh
sudo systemctl start artemis
```

Check if service its running:

```sh
sudo systemctl status artemis
```

You will see a status like this:

```sh
● artemis.service - ARTEMIS Service
   Loaded: loaded (/etc/systemd/system/artemis.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2020-05-20 20:43:26 UTC; 9min ago
 Main PID: 26626 (gunicorn)
    Tasks: 2 (limit: 4704)
   CGroup: /system.slice/artemis.service
           ├─26626 /root/artemis/backend/venv/bin/python3.7 /root/artemis/backend/venv/bin/gunicorn 
           └─26646 /root/artemis/backend/venv/bin/python3.7 /root/artemis/backend/venv/bin/gunicorn 

May 20 20:43:26 artemis systemd[1]: Started ARTEMIS Service.
May 20 20:43:26 artemis gunicorn[26626]: [2020-05-20 20:43:26 +0000] [26626] [INFO] Starting gunic
May 20 20:43:26 artemis gunicorn[26626]: [2020-05-20 20:43:26 +0000] [26626] [INFO] Listening at: 
May 20 20:43:26 artemis gunicorn[26626]: [2020-05-20 20:43:26 +0000] [26626] [INFO] Using worker: 
May 20 20:43:26 artemis gunicorn[26626]: [2020-05-20 20:43:26 +0000] [26646] [INFO] Booting worker
```

# 2. Deploy on Docker

In Progress

# 3. Local Development

## 3.1 Backend Module

```sh
cd backend
pip install -r requirements.txt
python run.py
```

## 3.2 Manage Database (Flask-Migrate)

```sh
python migrate.py db migrate
python migrate.py db upgrade
```
