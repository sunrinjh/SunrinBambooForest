from django.db import models

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.CharField(max_length=200)
    post_time=models.DateTimeField(auto_now_add=True)
    host_ip=models.CharField(max_length=20)
    def __str__(self):
        return self.post_title
        
    @classmethod
    def create(cls, post_title,post_text,ip):
        post = cls(post_title=post_title,post_text=post_text,host_ip=ip)
        return post

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_time=models.DateTimeField(auto_now_add=True)
    host_ip=models.CharField(max_length=20)
    def __str__(self):
        return self.comment_text
    @classmethod
    def create(cls, post,text,ip):
        comment = cls(post=post,comment_text=text,host_ip=ip)
        return comment
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    host_ip=models.CharField(max_length=20)
    def __str__(self):
        return self.host_ip
    
    @classmethod
    def create(cls, post,ip):
        like = cls(post=post,host_ip=ip)
        return like