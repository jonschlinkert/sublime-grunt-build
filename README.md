# sublime-grunt-build

> Enables you to run actual Gruntfile.js builds from Sublime Text 2.


## Getting Started

### Install package control
First, install **Package Control** for Sublime Text 2:
  * [Sublime Package Control](http://wbond.net/sublime_packages/package_control): this is the easiest way to install this package
  * After installing Package Control, restart Sublime Text.


### Install sublime-grunt-build

#### Option #1: Install module using package control
  * Now inside Sublime Text open the Command Palette (`command+shift+p` on OS X, or `ctrl+shift+p` on Linux/Windows).
  * Select "Package Control: Install Package", after a few seconds a list will appear. Search for `sublime-grunt-build` and click to install.


#### Option #2: Install module directly
If you weren't able to find the package on Package Control, go to your Sublime Text `Packages` directory, located here:
  * OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
  * Linux: `~/.Sublime Text 2/Packages/`
  * Windows: `%APPDATA%/Sublime Text 2/Packages/`


Add the `sublime-grunt-build` module:

**Without Git**: Download the latest source zip from [github](https://github.com/jonschlinkert/sublime-grunt-build/zipball/master) and extract the files into a new folder inside your Sublime Text "Packages" directory.


**With Git**: Clone the repository in your Sublime Text "Packages" directory:
```
git clone git://github.com/jonschlinkert/sublime-grunt-build.git
```


## Grunfile
Add a Gruntfile to in your project root.


### Build System > Grunt

* In Sublime Text 2, go to `Tools > Build System`, and select `Grunt` as your build system
* To build: `ctrl + b` on Linux/Windows or `command + b` on OS X


## build-on-save

The build-on-save feature was added in v1.1.  To enable  `build-on-save`, you first have to save your project in Sublime Text by going to `Project > Save Project As`. Then go to your project folder and  `settings` line from the example below to your `myProject.sublime-project` file.

> For each project that you want to take advantage of this feature, you will have to modify the the `.sublime-project` file.


### Build Settings

In your project folder

```json
{
  "folders":
  [
    { "path": "/C/path-to-your-project-here" }
  ],
  "settings": { "build_on_save": 1 }
}
```
To build on save, keep the value at `1`. To disable build on save, change the value to `0`.


### A build-on-save word of caution

> Running `grunt` every time you hit `ctrl + s` will be a great productivity booster _when used wisely_.  But if you have lots of processor-intensive tasks that take more than a few seconds to run, this feature might get annoying pretty fast.



## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Lint and test your code using [Grunt](http://gruntjs.com/).


## Release History
v0.1.1  build-on-save added
v0.0.1  first commit

## License
Copyright (c) 2013 Jon Schlinkert
Licensed under the MIT license.
