#!/usr/bin/python3

from os import mkdir
from os.path import basename, isfile, isdir, exists
from shutil import copy2, copytree, rmtree
from subprocess import call

from callbacks import *
import click

@click.command()
@click.argument("jar_file",
                callback=check_jar_file)
@click.option("-i", "--icon_file",
              default="template.app/Contents/Resources/application.icns",
              callback=check_icon_file,
              help="what icon_file to give the app")
@click.option("-d", "--destination_directory",
              default="bin",
              callback=check_destination_directory,
              help="what directory to create the app in")
def main(jar_file, icon_file, destination_directory):

	# ---------------------------------------------- setup app variables -----------------------------------------------
	app_name = basename(jar_file).rstrip(".jar_file")
	app_path = f"{destination_directory}/{app_name}.app"

	# ------------------------------- create new app in destination folder from template -------------------------------
	if exists(app_path):
		overwrite = ""
		while not (overwrite == 'y' or overwrite == 'n'):
			overwrite = str(input(f"{app_path} already exists. Replace? [y/n] "))

		if overwrite == 'y':
			rmtree(app_path)
		else:
			exit(0)

	copytree("template.app", app_path)

	# -------------------------------------------- copy input files to app ---------------------------------------------
	copy2(jar_file, f"{app_path}/Contents/MacOS/{app_name}.jar")
	if icon_file:
		copy2(icon_file, f"{app_path}/Contents/Resources/application.icns")

	# ----------------------------------------- update arguments in app runner -----------------------------------------
	app_runner = f"{app_path}/Contents/MacOS/runner"
	with open(app_runner, "r") as file:
		file_contents = file.read()

	file_contents = file_contents \
		.replace("[APP_JAR]", f"{app_name}.jar") \
		.replace("[APP_NAME]", app_name)

	with open(app_runner, "br+") as file:
		file.truncate(0)
		file.write(bytes(file_contents, "ascii"))

	# ----------------------------------------------- show app in finder -----------------------------------------------
	call(["open", "-R", app_path])


if __name__ == "__main__":
	main()
