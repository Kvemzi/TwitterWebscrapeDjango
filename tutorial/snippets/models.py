from django.db import models

class Twitter(models.Model):
    '''
        Twitter model for Twitter snippets created by webscraping tweets from twitter.
        Sorted by created by atribute for timeline of tweets.
    '''
    author_id = models.BigIntegerField()
    tweet_id = models.BigIntegerField(primary_key=True)
    tweet = models.TextField()
    created_at = models.DateTimeField()
    author_name = models.CharField(max_length=100)
    author_username = models.CharField(max_length=100)
    url_to_tweet = models.TextField(max_length=500)
    
    class Meta:
        ordering = ['created_at']