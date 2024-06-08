import uuid
import random
import string
from django.db import models
from utils.models import BaseModel
from django.conf import settings
from apps.management.models import User

class News(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts')
    title = models.CharField(max_length=255, null=False)
    subtitle = models.TextField(null=False)
    first_paragraph = models.TextField(null=False)
    second_paragraph = models.TextField(null=True, blank=True)
    third_paragraph = models.TextField(null=True, blank=True)
    fourth_paragraph = models.TextField(null=True, blank=True)
    fifth_paragraph = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title
    
class SavedNews(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_news')
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f'Saved news {self.news.title} by user {self.user.name}'