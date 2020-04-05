![Image description](https://i.ibb.co/mzXDq1t/javapp.png)


# javapp

**javapp** is an extremely simple, python based, command line tool to package JAR files into Mac OS applications.

All source code is based off [this tutorial](http://www.zitnik.si/wordpress/2016/02/21/creat.ing-a-mac-os-app-from-a-runnable-jar-file/) created by Slavko Žitnik.

## Installation

```bash
$ git clone https://github.com/dante-biase/javapp.git

```

## Usage

### Basic Usage
```bash
$ cd javapp
$ python3 javapp.py <jar_file> [<app_icon>]
```
>arguments are **ordered**.
#### `<jar_file>`
- 1st argument, required
- specifies the jar file to convert into an application **and specifies the output-application's name**
    + the stem of the output-application will be named with the stem of the path specified in <jar_file>

#### `[<app_icon>]`
- 2nd argument, optional
- specifies output application's icon
- for recommended icon specifications - size, resolution, etc. - refer to this [guide](https://developer.apple.com/design/human-interface-guidelines/macos/icons-and-images/app-icon/)

#### `output path?`
- As of now, **the application will always be created in `/Applications`**
- Functionality will be added in the future to specify this path

