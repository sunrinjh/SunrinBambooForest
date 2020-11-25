from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.CharField(max_length=200)
    post_time=models.DateTimeField(auto_now_add=True)
    post_img=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.post_title
    @classmethod
    def create(cls, post_title,post_text,post_img=None):
        post = cls(post_title=post_title,post_text=post_text,post_img=post_img)
        return post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_text
    @classmethod
    def create(cls, post,text):
        comment = cls(post=post,comment_text=text)
        return comment
