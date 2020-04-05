from os.path import exists, isdir
from pathlib import Path

from click import BadParameter


def assert_existence(path):
	if not exists(path):
		raise BadParameter(f"\"{path}\" does not exist.")


def assert_is_file(path):
	assert_existence(path)
	if isdir(path):
		raise BadParameter(f"{path} is a directory.")


def assert_file_type(file_path, type_extension):
	assert_is_file(file_path)
	if Path(file_path).suffix != type_extension:
		raise BadParameter(f"{file_path} is not a {type_extension.lstrip('.')} file.")


def assert_is_dir(path):
	assert_existence(path)
	if not isdir(path):
		raise BadParameter(f"{path} is not a directory.")
