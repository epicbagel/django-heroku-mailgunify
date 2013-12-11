from setuptools import setup, find_packages
import mailgunify
setup(name='django-heroku-mailgunify',
	version = mailgunify.__version__,
	packages = find_packages(),
	license='The MIT License',
	platforms=['OS Independent'],
	keywords='django, mailgun',
	author='Jon Bolt',
	author_email='jon@epicbagel.com',
	url="https://github.com/epicbagel/django-heroku-mailgunify",
)
