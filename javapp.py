#!/usr/local/bin/python3

from os.path import basename, exists
from shutil import copy2, copytree, rmtree
from subprocess import call
from sys import argv


def assert_exists(file_path):
	if not exists(file_path):
		raise FileNotFoundError(f'{file_path} does not exist.')


if __name__ == "__main__":
	# --------------------------------------------- parse input arguments ----------------------------------------------
	args = argv[1:]
	app_jar = args[0]
	assert_exists(app_jar)
	app_name = basename(app_jar).rstrip('.jar')
	if len(args) == 2:
		app_icon = args[1]
		assert_exists(app_icon)
	else:
		app_icon = None

	# ------------------------------ create new app in Applications folder from template -------------------------------
	app_path = f'/Applications/{app_name}.app'
	if exists(app_path):
		overwrite = ''
		while not (overwrite == 'y' or overwrite == 'n'):
			overwrite = str(input(f'{app_path} already exists. Replace? [y/n] '))

		if overwrite == 'y':
			rmtree(app_path)
		else:
			exit(0)

	copytree('template.app', app_path)

	# -------------------------------------------- copy input files to app ---------------------------------------------
	copy2(app_jar, f'{app_path}/Contents/MacOS/{app_name}.jar')
	if app_icon:
		copy2(app_icon, f'{app_path}/Contents/Resources/application.icns')

	# ----------------------------------------- update arguments in app runner -----------------------------------------
	app_runner = f'{app_path}/Contents/MacOS/runner'
	with open(app_runner, 'r') as file:
		file_contents = file.read()

	file_contents = file_contents \
		.replace("[APP_JAR]", f'{app_name}.jar') \
		.replace("[APP_NAME]", app_name)

	with open(app_runner, 'br+') as file:
		file.truncate(0)
		file.write(bytes(file_contents, 'ascii'))

	# ----------------------------------------------- show app in finder -----------------------------------------------
	call(["open", "-R", app_path])
