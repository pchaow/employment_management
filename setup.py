from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in employment_management/__init__.py
from employment_management import __version__ as version

setup(
	name="employment_management",
	version=version,
	description="Employment Management Apps",
	author="Zezembly Co.,Ltd.",
	author_email="admin@zezembly.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
