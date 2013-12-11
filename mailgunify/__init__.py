# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import os

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'

#: Mailgun api key for using the REST API
MAILGUN_API_KEY = MAILGUN_ACCESS_KEY = os.environ.get("MAILGUN_API_KEY")

#: Mailgun SMTP server host
MAILGUN_SMTP_SERVER = MAILGUN_SERVER_NAME = os.environ.get("MAILGUN_SMTP_SERVER")

#: Mailgun SMTP server login
MAILGUN_SMTP_LOGIN = os.environ.get("MAILGUN_SMTP_LOGIN")

#: Mailgun SMTP server password
MAILGUN_SMTP_PASSWORD = os.environ.get("MAILGUN_SMTP_PASSWORD")

#: Mailgun SMTP server port
MAILGUN_SMTP_PORT = int(os.environ.get("MAILGUN_SMTP_PORT", 0)) or None

#: Email host for sending mail
EMAIL_HOST = MAILGUN_SMTP_SERVER

#: Email server username
EMAIL_HOST_USER = MAILGUN_SMTP_LOGIN

#: Email server password
EMAIL_HOST_PASSWORD = MAILGUN_SMTP_PASSWORD

#: Email server SMTP port
EMAIL_PORT = MAILGUN_SMTP_PORT