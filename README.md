# jashley.me
https://devcenter.heroku.com/articles/container-registry-and-runtime

Install these packages for Postgresql and Pillow support.
``` sudo apt-get install libpq-dev postgresql postgresql-contrib ```
``` sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk ```

Use ./generate-secret-key.py to create SECRET_KEY and NEVERCACHE_KEY, 
set them in your environment.

Build  development environment manually
``` docker-compose build && docker-compose up ```

Or via the watchdog script
``` python watcher.py ```
