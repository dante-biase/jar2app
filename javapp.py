#!/usr/bin/python3

from os import mkdir
from os.path import basename, exists
from shutil import copy2, copytree, rmtree
from subprocess import call

import click


def assert_input_file_existance(ctx, param, file_path):
	if not exists(file_path):
		raise click.BadParameter(f"{file_path} does not exist.")
	else:
		return file_path


def assert_destination_directory_existance(ctx, param, file_path):
	if file_path == "bin":
		if exists("bin"):
			rmtree("bin")

		mkdir("bin")
	else:
		assert_input_file_existance(ctx, param, file_path)

	return file_path


@click.command()
@click.argument("jar",
                callback=assert_input_file_existance)
@click.option("-i", "--icon",
              default="template.app/Contents/Resources/application.icns",
              callback=assert_input_file_existance,
              help="what icon to give the app")
@click.option("-d", "--destination",
              default="bin",
              callback=assert_destination_directory_existance,
              help="what directory to create the app in")
def main(jar, icon, destination):

	# ---------------------------------------------- setup app variables -----------------------------------------------
	app_name = basename(jar).rstrip(".jar")
	app_path = f"{destination}/{app_name}.app"

	# ------------------------------ create new app in Applications folder from template -------------------------------
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
	copy2(jar, f"{app_path}/Contents/MacOS/{app_name}.jar")
	if icon:
		copy2(icon, f"{app_path}/Contents/Resources/application.icns")

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
