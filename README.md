# Cyberpunk-2077-Twitter-Sentiment-Analysis

## Objective

* Gather the data using the Twitter API.
* Store and maintain a PostgreSQL database.
* Create a live dashboard that pulls from the database and analyzes the sentiment of each tweet.

## Background Information
Cyberpunk 2077 is an upcoming action role-playing video game developed by CD Projekt. With such a large social media following, users are voicing their wishes and concerns to CD Projekt. In this project, we will monitor tweets collected and parse through the sentiment of each.

## Process:
* Data Gathering
* PostgreSQL database
* Dashboard

## Table of Contents:
* Part I: Data Gathering
  * Gathering
  * PostgreSQL
* Part II: Dashboard

## Pertinent Deliverables
* [Jupyter Notebook](https://github.com/SulmanK/Cyberpunk-2077-Twitter-Sentiment-Analysis/blob/main/Cyberpunk%202077%20Sentiment%20Analysis%20(Project%20Notebook).ipynb)
* [Dashboard](https://cyberpunk-2077-twitter-sa.herokuapp.com/)
  * The applications streams in recent tweets from that day, and performs a live update every 30 seconds to update the dataframe.
    * To have a more pleasant user experience, the application will take in tweets in the past three days to accomodate for lul periods.
    * Every hour the database is flushed to prevent any overload.
  * In the future, I plan to add in additional workers so each user's experience will be unique - currently there is only one instance of the application. 



