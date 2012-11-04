Grunt Builds from Sublime Text 2
================================

This is a very basic package that makes it simple to kick off grunt builds while working in Sublime Text 2.

## Prerequisites
 * node.js
 * grunt, 
 * whatever grunt tasks you prefer 

## Getting started:
 1. Install this package using the instructions below
 2. Put grunt.js (for Grunt 0.4.0, use gruntfile.js) in your project root
 3. In Sublime Text 2, go to Tools > Build System and select "Grunt"
 4. To initiate a build: control+b on Linux/Windows, command+b on OS X


### Installing 

 * [Sublime Package Control](http://wbond.net/sublime_packages/package_control): this is the easiest way to install this package
 * After installing Package Control, you must restart Sublime Text, and then open the Command Palette (command+shift+p on OS X, or ctrl+shift+p on Linux/Windows). Select "Package Control: Install Package", after a few seconds a list will appear. Search for "sublime-grunt-build" and click to install.
 * Without Git: Download the latest source zip from [github](https://github.com/jonschlinkert/sublime-grunt-build/zipball/master) and extract the files into a new folder inside your Sublime Text "Packages" directory.
 * With Git: Clone the repository in your Sublime Text "Packages" directory:

    ```git clone git://github.com/jonschlinkert/sublime-grunt-build.git```

The "Packages" directory is located at:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux:
    `~/.Sublime Text 2/Packages/`
* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`
