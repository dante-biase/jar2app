from os import mkdir
from shutil import rmtree

from src.assertions import *


def check_jar_file(ctx, param, file_path):
	assert_file_type(file_path, '.jar')
	return Path(file_path).absolute()


def check_icon_file(ctx, param, file_path):
	if file_path:
		assert_file_type(file_path, '.icns')
		file_path = Path(file_path).absolute()

	return file_path


def check_destination_directory(ctx, param, directory_path):
	if directory_path:
		assert_is_dir(directory_path)
		directory_path = Path(directory_path).absolute()

	return directory_path
