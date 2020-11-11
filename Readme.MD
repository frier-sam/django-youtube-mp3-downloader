Developed on Python3.6
## Run Locally
  Install ffmpeg on your local machine.
  clone the repo and go to the clone location and run
  ```
  pip install -r requirements-local.txt
  ```
  This will install the required python packages
  Then Run
  ```
  python manage.py runserver
  ```

  You will find the app running on http://localhost:8000

## Deploy to heroku

  Create a heroku account and create a app with <yourappname>
  install heroku-cli on your local machine.
  Login into your heroku on cli Using
  ```
  heroku login
  ```
  the add the repo to your heroku account
  ```
  heroku git:remote -a <yourappname>
  ```
  Add the build packs
  ```
  heroku buildpacks:set heroku/python
  heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
  ```
  finally push to deploy on heroku
  ```
  git push heroku master
  ```
