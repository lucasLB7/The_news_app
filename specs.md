## specifications & app details ##

This app was created in Flask for the moringa core course.

# general structure of the files #

The app is costucted in a way that allows for deployment to heroku and is capable of being developed further:

- root folder contains the root depencancies for the app.

Our beaf & potatoes of the app are located in the app sub-folder and contain our cache, mian, staic, templates an initialization of the app our models and requests...

Requests are made to news api with a key that is located on the heroku server (the api key is otherwise unaccessible to cleints).



1. Requests:

The requests are key for the parsing of the data from tthe json files:

```
def configure_requests(app):
    global api_key , news_url, news_article
    api_key = app.config['NEWS_API_KEY']
    news_url = app.config['NEWS_SOURCES_URL']
    news_article = app.config['NEWS_ARTICLES_URL']
```
__In the above example we create the configure_request function that takes in the app as argument.__

The purpose of this function is to store & retreive data from the api key & url origin.

