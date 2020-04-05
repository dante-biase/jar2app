![Image description](https://i.ibb.co/mNy4nns/banner.png)


# jar2app

**jar2app** is an extremely simple, python based, command line tool to package JAR files into Mac OS applications, based off a [tutorial](http://www.zitnik.si/wordpress/2016/02/21/creat.ing-a-mac-os-app-from-a-runnable-jar-file/) created by Slavko Žitnik.

## Compatibility
- Mac OSX
- Python >= 3.6

## Dependencies
- [Click](https://click.palletsprojects.com/en/7.x/#documentation)

## Installation

```bash
$ git clone https://github.com/dante-biase/jar2app.git
$ cd jar2app
$ pip3 install -r requirements.txt
$ chmod +x jar2app.py
```

## Usage

```bash
$ ./jar2app.py JAR_FILE [OPTIONS]
```

### JAR_FILE
> specifies the jar file to be converted into an application, required

### [OPTIONS]
```
  -i, --icon_file               TEXT    icon to give the app
  -d, --destination_directory   TEXT    directory to create the app in
  --help                                print this message and exit
```
### NOTES
1. the output app will be named with the stem of `JAR_FILE`
2. if `destination_directory` is not specified, the application will be created in `jar2app/bin`
