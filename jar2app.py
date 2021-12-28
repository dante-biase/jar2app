#!/usr/local/bin/python3

from pathlib import Path
from os.path import exists, join
from shutil import copy2, copytree
from subprocess import call

import click
from py2x import Resources

from src.callbacks import *


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
@click.option("-n","--name",
			default=None,
			help="app name")
def main(jar_file, icon_file, destination_directory, name):
	# ---------------------------------------------- setup app variables -----------------------------------------------
	jar_file = Path(jar_file)
	jar_file_parent_directory = Path(jar_file.absolute()).parent
	app_name = name if name else jar_file.stem
	app_name = app_name.rstrip(".app")+ ".app"
	app_jar = f"{app_name}.jar"
	if not destination_directory:
		app_target_path = join(jar_file_parent_directory, app_name)
	else:
		app_target_path = join(destination_directory, app_name)

	# ------------------------------- create new app in destination folder from template -------------------------------
	if exists(app_target_path):
		overwrite = ""
		while not (overwrite == 'y' or overwrite == 'n'):
			overwrite = str(input(f"{app_target_path} already exists. Replace? [y/n]: ")).strip().lower()

		if overwrite == 'y':
			rmtree(app_target_path)
		else:
			exit(0)

	copytree(Resources.get("template.app"), app_target_path)

	# -------------------------------------------- copy input files to app ---------------------------------------------
	copy2(jar_file, join(app_target_path, "Contents/MacOS", app_jar))
	if icon_file:
		copy2(icon_file, join(app_target_path, "Contents/Resources/application.icns"))

	# ----------------------------------------- update arguments in app runner -----------------------------------------
	app_runner = join(app_target_path, "Contents/MacOS/runner")
	with open(app_runner, "r") as file:
		file_contents = file.read()

	file_contents = file_contents \
		.replace("[APP_JAR]", app_jar) \
		.replace("[APP_NAME]", app_name)
	
	with open(app_runner, "br+") as file:
		file.truncate(0)
		file.write(bytes(file_contents, "ascii"))
	# ----------------------------------------------- show app in finder -----------------------------------------------
	call(["open", "-R", app_target_path])


if __name__ == "__main__":
	main()
