#!/usr/local/bin/python3
import sys
import os

from os import getcwd
from os.path import exists, dirname
from pathlib import Path
from shutil import copy2, copytree
from subprocess import call

from py2x import Resources
import click

from callbacks import *

@click.command()
@click.argument("jar_file",
                callback=check_jar_file)
@click.option("-i", "--icon_file",
              default=None,
              callback=check_icon_file,
              help="icon to give the app")
@click.option("-d", "--destination_directory",
              default=None,
              callback=check_destination_directory,
              help="directory to create the app in")
@click.option("-t","--title",
			default=None,
			help="title to display in toolbar")
def main(jar_file, icon_file, destination_directory,title):
	# ---------------------------------------------- setup app variables -----------------------------------------------
	jar_file = Path(jar_file)
	jar_file_parent_directory = Path(dirname(jar_file.absolute()))
	app_name = f"{jar_file.stem}.app"
	if not destination_directory:
		app_target_path = f"{jar_file_parent_directory.absolute()}/{app_name}"
	else:
		app_target_path = f"{destination_directory}/{app_name}"

	# ------------------------------- create new app in destination folder from template -------------------------------
	if exists(app_target_path):
		overwrite = ""
		while not (overwrite == 'y' or overwrite == 'n'):
			overwrite = str(input(f"{app_target_path} already exists. Replace? [y/n] "))

		if overwrite == 'y':
			rmtree(app_target_path)
		else:
			exit(0)

	copytree(Resources.get("template.app"), app_target_path)

	# -------------------------------------------- copy input files to app ---------------------------------------------
	copy2(jar_file, f"{app_target_path}/Contents/MacOS/{app_name}.jar")
	if icon_file:
		copy2(icon_file, f"{app_target_path}/Contents/Resources/application.icns")

	# ----------------------------------------- update arguments in app runner -----------------------------------------
	app_runner = f"{app_target_path}/Contents/MacOS/runner"
	with open(app_runner, "r") as file:
		file_contents = file.read()

	file_contents = file_contents \
		.replace("[APP_JAR]", f"{app_name}.jar") \
		.replace("[APP_NAME]", title if title else jar_file.stem)
	
	with open(app_runner, "br+") as file:
		file.truncate(0)
		file.write(bytes(file_contents, "ascii"))
	# ----------------------------------------------- show app in finder -----------------------------------------------
	call(["open", "-R", app_target_path])


if __name__ == "__main__":
	main()
