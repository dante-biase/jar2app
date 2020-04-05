![Image description](https://i.ibb.co/mzXDq1t/javapp.png)


# javapp

**javapp** is an extremely simple, python based, command line tool to package JAR files into Mac OS applications.

All source code is based off [this tutorial](http://www.zitnik.si/wordpress/2016/02/21/creat.ing-a-mac-os-app-from-a-runnable-jar-file/) created by Slavko Žitnik.

## Compatability
- Python >= 3.6

## Dependencies
- [Click](https://click.palletsprojects.com/en/7.x/#documentation)

## Installation

```bash
$ git clone https://github.com/dante-biase/javapp.git
$ cd javapp
$ pip3 install -r requirements.txt
$ chmod +x javapp.py
```

## Usage

```bash
$ ./javapp.py JAR_FILE [OPTIONS]
```

### JAR_FILE
- specifies the jar file to be converted into an application

### [OPTIONS]
```
  -i, --icon_file               TEXT    icon to give the app
  -d, --destination_directory   TEXT    directory to create the app in
  --help                                print this message and exit
```
### NOTES
- the output app will be named with the stem of `JAR_FILE`
- if `destination_directory` is not specified, the application will be created in `javapp/bin`
