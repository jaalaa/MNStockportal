from django.db import models
import os

# Create your models here.
def upload_image_to(instance, filename):
    
    # 降順になる
    article_id = Article.objects.order_by('-id')[0]
    
    return os.path.join('static', 'article', 'image', str(article_id.id), filename)

class Article(models.Model):
    # タイトル
    title = models.CharField(default='', max_length=100)
    # 内容
    text = models.TextField(default='', )
    # 作成者
    author = models.CharField(default='', max_length=100)
    # 作成日付
    created_date = models.DateField(auto_now_add=True)
    # 更新日付
    updated_date = models.DateField(auto_now=True)
    # img
    image = models.ImageField(default="", blank = True, upload_to = upload_image_to)

    
