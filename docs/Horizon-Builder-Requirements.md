# Horizon Builder

## Project Objective

To develop an OpenSource character creation application for Dungeons and Dragons 5th Edition, as a spiritual successor to the Aurora Builder application.

### Project Background

Aurora Builder was a character building application developed by Bas Driessen and released for public consumption in _year_. The application allows users to create XML files and import them as content into the application. This method has allowed Aurora Builder to support every D&D 5e source to date, along with numerous 3rd party sources and a significant body of homebrew content. The author eventually decided to abandon development on the Aurora Builder application for various reasons, and did not share the source code before ceasing contact, shutting down the Patreon, and all but disappearing. 
In the wake of this situation, several community members stepped up to maintain the Legacy of Aurora Builder. They continue to maintain the repositories of GitHub indices allowing the content to be shared and available for use by those creating characters. They also assist anyone who wishes to create homebrew content for Aurora and how to implement it.
From within this community of creators and codeheads, several attempts have been made to produce a successor to Aurora Builder. These have begun with the goal of trying to rectify many of the issues faced by Aurora left unfinished by its original author. Without access to the original code, this was almost impossible, and required starting from the ground up. Due to the sheer amount of work required to develop an application like this, all previous attempts have gone unfulfilled.
Horizon will be the exception, achieving where previously we have not been able to. The app will support 5e character creation, from official, 3rd party and homebrew sources, and provide tools for the D&D community to develop their own content for inclusion into the application. Horizon's aims are to incorporate the hard work produced in supporting Aurora, build upon it, fix the internal troubles, and add new and enhanced features, while staying true to its roots and providing compatibility to ingest and inherit Aurora files for use with the new Horizon app, ensuring continuity with past content and into the future. By remaining OpenSource from inception, the hope is that Horizon Builder will continue for as long as there is a community who wants to use it.

## Project Team

Add yourselves here:
* Owner - GustavoSchip
* TEAM TITLE - NAME
* TEAM TITLE - NAME
* TEAM TITLE - NAME

## Project Scope

### In Scope

* New ground-up application
  * Localised installation and server-hosted web application
* Ability to ingest and support previously developed Aurora Builder content
* Stats, Races, Sub-Races, Classes, Sub-classes, Feats, Skills, Traits, Features, Spells, Weapons, Armour, Items, and other character-related information within the D&D 5e game
* A Character Sheet output, incorporating various upgrades from the original Aurora character sheets.

   
### Out of Scope

*

## Functional Requirements

### System Expectations

|**ID**|**Requirement**|**MoSCoW**|**Status**|**Submitted by**|
|:----:|:--------------|:--------:|:--------:|:--------------:|
|1     |

### Application Features

## Non-functional Requirements

### System Expectations

### Application Features

## The Dumping Ground

### Yet to be Incorporated

* Ability to add a custom standard array (Fresh)
* More UI customization (Fresh)
* Ability to buy items for a custom amount (Fresh)
* Spell point support (Fresh)
* filter out specific types of elements from a source. For example, maybe someone likes a lot of one source but doesn't want specifically the spells
* plugin support sometime after ALPHA, maybe add some hooks/overrides so that they can expand them that way for functionallity and the generics can be done via config (can be set in app) with like the basic color/accent setter base theme dark/light you know the drill
* sticking to the element structure of previous works, making classes for new app
* companion as a separate entity/object, managed on its own section in the sheet
* ability to import existing aurora XML, parse and ingest, convert to Horizon files, and store (locally or via web-storage with other content files)
* use of IDs to differentiate components, link components together, and generally organise the structure of content
* compatibility with XML, but also JSON and YML for futureproofing
* minimise the necessity to remake existing Aurora content for Horizon.
* utilise JSON flexibility for ease of code versatility
* working documentation to assist new content creators/app maintenance and troubleshooting (READMEs etc)
* fix "inline" features issue (formatting? RTF?)
* streamline how the app runs - caching content rather than loading on startup every time, etc
* Content structures will be simplified as much as possible to allow approachability for content creators
* continue use of the "internals-extended.XML" content, as it is genuinely useful
* app must run on all major desktop OS, and browser hosting, and (stretch) mobile devices (via webhosting?)
* ability to make gestalt characters (one character with two classes/subclasses parallel, not multiclassed, etc)
* inclusion of alternative casting methods, such as mana, hp cost, etc.
* support for character sheet tracking of sorcerer points, ki points, superiority dice, inspiration dice, and other rechargable consumables.
* spells should have bespoke variables to track V S M components, and be able to add additional categories should another type be required.
* ability to calculate AC using a non-standard formula/edit the base formula in a modular way - eg using Int instead of Dex etc.
* ability to have items grant features
* ability to have armour be customisable, have its own traits, and have stats directly impact the calculations, which can be customised by the user.
* system will support a custom plugin library maintained alongside the main app repository
* Ability to enact application-wide functionality or enhancement, eg 1st of april feature be like, change all fields to google translate with pirate language
* the application will support languages other than English (supported language list TBA)
* the content must allow a user to script a change in name, description, or other information prior to being populated onto the character sheet that shows differently to the UI display in the application eg Aurora's <alt=""/> feature.
* the application will standardise code so that additional content creators are utilising a similar set of tools, to enhance compatibility, and streamline the homebrew process.
* The application will support a VisualStudioCode plugin similar to the AuroraSnippets plugin, to assist homebrewers in creating Horizon Builder content.
* the application will provide clear and explanatory error messaging, eg. if there is a problem parsing data, loading from cache, reading a content file import, starting the app, and other circumstances as identified by the project team or end user.
* Where possible, the latest versions of code platform will be used, but backwards compatibility is preferrable.
* ability to specify multiple damage types on the same weapon without having to edit the attacks on the character sheet (Done)
* ability to change the Attribute associated with a weapon for calculating hit and damage
* a more dynamic and capable display setup for items and how they work - moving away from the need to define everything as part of the item description.
* capable of assigning properties to an item that affect their contents (eg Bag of Holding reduces weight of all content items to 0 etc)
* Item starter bundles for classes (based on class source information) so users dont have to individually select starting gear etc.
* APIs should sort and send data based on their endpoints
* The application will have 3 main delivery modes: Local All (Default), Local GUI and Server / Back end, front end, API - **need to define which we are going with, and what that means for future reqs**.
* Character sheets will be produced by the system
* Character sheets will be modular, incorporating various segments as and when they are enabled as part of the character creation process
* character sheets will print to PDF
* The character sheet PDF will contain form fillables allowing for app-external editing
* the app will provide a way to generate and preview the character sheet output from within the application, and allow this output preview to be saved as a PDF file.
* the application will allow the importing of Aurora indices and Horizon indices, sharing an index URL for both, allowing the content to be used by both applications. 
* Need to consider how to add or remove features from an Item (Koda)
* Ability to add incidental modifiers to AC or Health (in app, but also as fields in PDF) (Koda)
* Process to handle Spell manipulation - may be too dynamic for this type of application - could be sectioned off for a future "tabletop" plugin for realtime use at table? (Koda)
* Ability to cater for additional proficiencies above and beyond those contained in the sources (and show them on the sheet) (Koda)
* ability to set requirements for a feature, trait, feat, skill, item etc eg. class-restricted items (Koda)
* ability to track current HP in the app (Stacy Skye)
* ability to use RTF (or similar) within the character sheet PDF output. (stacy Skye)

### Awaiting further discussion with Dev team

* The following is here because I pulled it from Discord but didn't understand the tech speak. I didn't want it to fade into the aether, but it needs explanation to be of worth to anyone but the devs as far as a requirement goes:
  * So that my implemented --server-only tag can be run as headless, after this has been sorted we should explore the GUI/system that uses the API that can be both in the same process or standalone so that the server is somewhere else, like on a different computer, example: Raspberry Pi. 
  * And the standalone GUI flag or --gui-only can make it skip the server and parser to only launch GUI and the --port and --address get reused as the new target host (address:port)
  * This is a nice way of doing it, it also makes it possible to isolate the server in docker and run the GUI client native, for the speed and feel of native, while the server is in a isolated supported container, that is a possible use case besides like seperate computer
### Put on Hold for a rainy day

