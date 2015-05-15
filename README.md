# Project-P3-Item-Catalog

Project Description:

This repository contains a sample app that I put together and has all the requirements asked to complete
in Project 3 for Udacity's Full Stack Web Developer Nanodegree.

It's a website that enables user can post items for sale or giveaways, registrations is done using only a
social ID so it implements OAuth1 and OAuth2, Does not retain any passwords or implements a user accounts
database, it will only store an ID used so it can relate to the items sold.

I've used a very easy to implement authentication and authorization python library :
Authomatic http://peterhudec.github.io/authomatic/index.html
to manage the login session I've used LoginManager from Flask.

For protection against CSFR I've used Flask-seaSurf : https://flask-seasurf.readthedocs.org/en/latest/

What does this example achieve :

It passes al the requirements asked for in 'Project-P3-Item-Catalog' final project :
 - Implements JSON endpoints and feeds with AtomFeeds.
 - Items stored are categorised and they can be viewed from th drop-down menu.
 - Search result queries can be done and viewed in the page.
 - Items have images that can be uploaded and managed ( delete/update ).
 - Using forms to update/edit/delete items, includes replacing the images.
 - When a user account is deleted all the images are also deleted from the static directory.
 - Using a base template so template pages can inherit any CSS and the Bootstrap.
 
 

