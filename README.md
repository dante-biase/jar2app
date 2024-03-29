![Image description](imgs/banner.png)


# jar2app

**jar2app** is an extremely simple, python based, command line tool to package JAR files into Mac OS applications, based off a [tutorial](http://www.zitnik.si/wordpress/2016/02/21/creating-a-mac-os-app-from-a-runnable-jar-file/) created by Slavko Žitnik.

![](imgs/demo.gif)

## Compatibility
- macOS
- Python >= 3.6

## Dependencies
- [Click](https://click.palletsprojects.com/en/7.x/#documentation)
- [py2x](https://github.com/dante-biase/py2x)


## Installation and Usage

|          	| Installation                                                                                                                          	| Usage                           	|
|----------	|---------------------------------------------------------------------------------------------------------------------------------------	|---------------------------------	|
| **Homebrew** 	| $ brew install dante-biase/x2x/jar2app                                                                                          	| $ jar2app JAR_FILE [OPTIONS]      	|
| **Manual**   	| $ git clone https://github.com/dante-biase/jar2app.git<br>$ cd jar2app<br>$ pip3 install -r requirements.txt<br> 	| $ python3 jar2app.py JAR_FILE [OPTIONS] 	|

### JAR_FILE
- specifies the jar file to be converted into an application, required

### [OPTIONS]
```
  -i, --icon_file               TEXT    icon to give the app
  -d, --destination_directory   TEXT    directory to create the app in
  -n, --name                    TEXT    app name
  --help                                print this message and exit
```
## NOTES
1. if `name` not specified, the resultant application will be named with the stem of `JAR_FILE`
2. if `destination_directory` not specified, the resultant application will be placed in the same directory as `JAR_FILE`
