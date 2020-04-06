from os import mkdir
from shutil import rmtree

from assertions import *


def check_jar_file(ctx, param, file_path):
	assert_file_type(file_path, '.jar')
	return file_path


def check_icon_file(ctx, param, file_path):
	assert_file_type(file_path, '.icns')
	return file_path


def check_destination_directory(ctx, param, directory_path):
	if exists("bin"):
		rmtree("bin")

	if directory_path == "bin":
		mkdir("bin")
	else:
		assert_is_dir(directory_path)

	return directory_path
