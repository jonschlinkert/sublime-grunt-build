Grunt.js build system for Sublime Text 2
========================================

This package enables you to run Grunt.js builds from Sublime Text 2.

## Prerequisites
 * node.js
 * grunt,
 * whatever grunt tasks you prefer


## Getting started:
 1. Install this package using the instructions below
 2. Put grunt.js (for Grunt 0.4.0, use gruntfile.js) in your project root
 3. In Sublime Text 2, go to Tools > Build System and select "Grunt" as the build system
 4. To build: `ctrl+b` on Linux/Windows, `command+b` on OS X


### Installing

 * [Sublime Package Control](http://wbond.net/sublime_packages/package_control): this is the easiest way to install this package
 * After installing Package Control, you must restart Sublime Text, and then open the Command Palette (`command+shift+p` on OS X, or `ctrl+shift+p` on Linux/Windows). Select "Package Control: Install Package", after a few seconds a list will appear. Search for "sublime-grunt-build" and click to install.
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


## Build Grunt on Save

The build-on-save feature was added in v1.1.  To enable build-on-save, add the `settings` line from the example below to your `.sublime-project` file. For each project that you want to take advantage of this feature, you will have to modify the the `.sublime-project` file.

```json
{
  "folders":
  [
    {
      "path": "/C/path-to-your-project-here"
    }
  ],
  "settings": { "build_on_save": 1 }
}
```

_A word of caution_: Running a `Grunt` build every time you save/`ctrl+s` is a great productivity booster _when used wisely_. Make sure you use this feature with faster, more compact builds. If you have lots of tasks and heavy build system that takes more than a few seconds to run, this feature might get annoying pretty fast.

A suggestion is to set your `default` to include only the tasks that you need to run every time you save (such as compiling LESS to CSS), and run your heavier copy/compress tasks manually as necessary.
