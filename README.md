# Project-P3-Item-Catalog

**Project Description:**

This repository contains a sample app that I put together and has all the requirements asked to complete
in Project 3 for Udacity's Full Stack Web Developer Nanodegree.

A working example can be seen here : http://micromarket.no-ip.biz/

It's a website that enables users to list items for sale or giveaways, registrations is done using only a
social ID and it implements OAuth1 and OAuth2. Does not retain any passwords or implements a user accounts
database, it will only store an ID so it can relate to the items sold.

I've used a very easy to implement authentication and authorization python library , Authomatic :
 http://peterhudec.github.io/authomatic/index.html
, to manage the login session I've used LoginManager from Flask.

For protection against CSFR I've used Flask-SeaSurf : https://flask-seasurf.readthedocs.org/en/latest/

**What does this example achieve :**

It passes al the requirements asked for in 'Project-P3-Item-Catalog' final project :
 - Implements JSON endpoints and feeds with AtomFeeds ( ex. http://127.0.0.1:8080/recent.atom )
 - Using third party authorization/authentication with Authomatic library. Using only GitHub, Twitter and Google+, others can be easily implemented.
 - Items stored are categorised, they can be selected and viewed from the drop-down menu.
 - Search in page.
 - Items have images and can be uploaded and managed ( delete/update ).
 - CRUD, using forms to update/edit/delete items, including replacing item images.
 - When a user account is deleted all the images are also deleted from the static directory.
 - Using a base_template.html so template pages can inherit the styles.
 - Responsive design, mobile device ready using Bootstrap 3.
 - Using Flask-SeaSurf library to prevent CSRF attacks and also Flask-WTF.

**How to install and test:**

1 - Install vagrant if you don't have it, use the excellent Udacity's link : https://www.udacity.com/wiki/ud197/install-vagrant

2 - Clone this repository and cd inside the main folder 'Project-P3-Item-Catalog' it should look like this :

 ```
    -rw-rw-r-- 1 g g   26 May 15 14:40 README.md
    -rw-rw-r-- 1 g g  267 May 15 14:40 pg_config.sh
    -rw-rw-r-- 1 g g  591 May 15 14:45 Vagrantfile
    drwxrwxr-x 4 g g 4.0K May 15 15:01 FinalProject3-Item-Catalog

 ```
 **Important:**
 In the Vagrant file you will need to set the 'synced_folder' with the local path where you cloned the project
 this will synchronize it inside vagrant thus no need to clone it again. Replace the
  <** Local Path to where you've cloned the repository **> with yours. Example : "C:/users/g/Project-P3-Item-Catalog"
 ( note the forward slashes ) If you have problems with this just remove this setting and manually clone the repository
  inside the vagrant box.
  ```
    # -*- mode: ruby -*-
    # vi: set ft=ruby :

    VAGRANTFILE_API_VERSION = "2"

    Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
      config.vm.provision "shell", path: "pg_config.sh"
      # config.vm.box = "hashicorp/precise32"
      config.vm.box = "ubuntu/trusty32"
      config.vm.synced_folder("<** Local Path to where you've cloned the repository **>" , "/home/vagrant/FinalProject3-Item-Catalog")
      config.vm.network "forwarded_port", guest: 8000, host: 8000
      config.vm.network "forwarded_port", guest: 8080, host: 8080
      config.vm.network "forwarded_port", guest: 5000, host: 5000
    end

  ```
 3 - Issue 'vagrant up'. All the requirements will be installed from the pg_config.sh. These are :
   ``````
    apt-get -qqy install python-flask python-sqlalchemy
    apt-get -qqy install python-pip
    apt-get -qqy install nginx
    apt-get -qqy install git
    pip install gunicorn
    pip install authomatic
    pip install Flask-Login
    pip install Flask-WTF
    pip install flask-seasurf
   ```
   **Gunicorn and Nginx** are only necessary if you would like to host this app on a cloud server.

 4 - Issue v'agrant ssh' to connect to vagrant box then once logged in CD inside FinalProject3-Item-Catalog. The database is already generated : salesite.db but you can also initiate
 it running 'python database_setup.py'.

 5 - To run the app issue 'python project.py' and then check it out in your browser at http://127.0.0.1:8080

 *Final note:*
  Because some providers don't accept private IP addresses I've register it using a domain name micromarket.no-ip.biz
  if you have problems testing Twitter add it into your hosts file : sudo nano /etc/hosts and add 127.0.0.1 micromarket.no-ip.biz



 
 

