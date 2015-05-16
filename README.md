# Project-P3-Item-Catalog

Project Description:

This repository contains a sample app that I put together and has all the requirements asked to complete
in Project 3 for Udacity's Full Stack Web Developer Nanodegree.

It's a website that enables users to list items for sale or giveaways, registrations is done using only a
social ID and it implements OAuth1 and OAuth2. Does not retain any passwords or implements a user accounts
database, it will only store an ID so it can relate to the items sold.

I've used a very easy to implement authentication and authorization python library , Authomatic :
 http://peterhudec.github.io/authomatic/index.html
, to manage the login session I've used LoginManager from Flask.

For protection against CSFR I've used Flask-SeaSurf : https://flask-seasurf.readthedocs.org/en/latest/

What does this example achieve :

It passes al the requirements asked for in 'Project-P3-Item-Catalog' final project :
 - Implements JSON endpoints and feeds with AtomFeeds ( ex. http://127.0.0.1:8080/recent.atom )
 - Using third party authorization/authentication with Authomatic library ( GitHub, Twitter and Google+ )
 - Items stored are categorised, they can be selected and viewed from the drop-down menu.
 - Search in page implemented.
 - Items have images and can be uploaded and managed ( delete/update ).
 - CRUD implemented, using forms to update/edit/delete items, including replacing item images.
 - When a user account is deleted all the images are also deleted from the static directory.
 - Using a base template so template pages can inherit the styles.
 - Responsive design, mobile device ready using Bootstrap 3.
 - Using Flask-SeaSurf library to prevent CSRF attacks and also Flask-WTF.

How to install and test:

1 - Install vagrant if you don't have it, use the excellent Udacity's link : https://www.udacity.com/wiki/ud197/install-vagrant

2 - Clone this repository and cd to main folder 'Project-P3-Item-Catalog' it should look like this :

    -rw-rw-r-- 1 g g   26 May 15 14:40 README.md
    -rw-rw-r-- 1 g g  267 May 15 14:40 pg_config.sh
    -rw-rw-r-- 1 g g  591 May 15 14:45 Vagrantfile
    drwxrwxr-x 4 g g 4.0K May 15 15:01 FinalProject3-Item-Catalog



 
 

