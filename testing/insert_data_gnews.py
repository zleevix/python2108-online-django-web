import os
import sys
import django
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()
from myapp.models import Article, Source
http_request = requests.get("https://gnews.io/api/v4/top-headlines?lang=en&token=e475a885ba8edfe954857e136e0de025")
data = http_request.json()
for article in data['articles'][:100]:
    new_article = Article.objects.create(
        title=article['title'],
        description=article['description'],
        content=article['title'],
        url=article['url'],
        image=article['image'],
        published_date=article['publishedAt'],
    )
    Source.objects.create(
        article=new_article,
        name=article['source']['name'],
        url=article['source']['url'],
    )