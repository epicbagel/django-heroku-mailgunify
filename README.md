# django-heroku-mailgunify

Automatic MailGun configuration on Heroku.

## Install

To install the latest version of ``django-heroku-mailgunify``, simply run

```
pip install -e git://github.com/epicbagel/django-heroku-mailgunify.git#egg=django-heroku-mailgunify-dev
``` 


## Usage

Modify your Django ``settings.py`` file and add:

``` python
from mailgunify import *
```

That's it. It's normally best to create a separate heroku.py settings file, together with a local.py which can make use of the dummy email backend.
