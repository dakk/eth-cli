from setuptools import find_packages
from setuptools import setup

setup(name='ethcli',
	version='0.1',
	description='Ethereum simple cli',
	author='Davide Gessa',
	setup_requires='setuptools',
	author_email='gessadavide@gmail.com',
	packages=['ethcli'],
	entry_points={
		'console_scripts': [
			'ethcli=ethcli.ethcli:main',
		],
	},
)
