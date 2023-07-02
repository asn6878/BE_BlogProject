from django.db import models
from user.models import CustomUser as User
import datetime

class Blog(models.Model):
    blog_img = models.ImageField(null=True)
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_description = models.CharField(max_length=200)
    created_time = models.DateTimeField('date created')
    def __str__(self):
        return self.title

class Today(models.Model): # 블로그의 방문자 수를 나타내는 클래스
    today_day = models.IntegerField(default=0) # 당일 방문객 수
    today_total = models.IntegerField(default=0) # total 방문객 수
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return "금일 방문자" + str(self.today_total)

class Category(models.Model): # 게시물을 분류할 수 있는 카테고리
    name = models.CharField(max_length=30)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content_img = models.ImageField(null=True)
    likes = models.ManyToManyField(User, related_name='post_like') # 게시글 좋아요 중개 테이블
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 날짜
    likes = models.ManyToManyField(User, related_name='comment_like') # 댓글 좋아요 중개 테이블

    def __str__(self):
        return self.comment

class Tag(models.Model): # 게시글에 달리는 태그(해시태그)
    tag = models.CharField(max_length=30)
    blog = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.tag
