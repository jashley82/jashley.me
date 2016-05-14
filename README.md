# jashley.me
source code for my website, built on django

- Heroku development parity achieved through the use of docker-compose
- Watchdog script for CI badassery

https://devcenter.heroku.com/articles/docker

Install the Docker plugin for Heroku
``` heroku plugins:install heroku-docker ```

Create a tarball and push it to Heroku for deployment
``` heroku docker:release ```

Build  development environment manually
``` docker-compose build && docker-compose up ```

Or via the watchdog script
``` python watcher.py ```
