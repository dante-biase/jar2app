from setuptools import setup, find_packages

setup(
    name="javapp",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=['click==7.1.1']
)