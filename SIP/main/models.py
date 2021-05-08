from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User=get_user_model()

class SocialIssue(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    description=models.TextField()
    submit_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} by {}".format(self.title,self.user.username)
    def get_likes(self):
        return self.likes.count()
    def get_comments(self):
        return self.comments.count()
    # video 22.7 , time -> after 14 min

class SocialIssueComments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    social_issue=models.ForeignKey(SocialIssue,on_delete=models.CASCADE,related_name="comments")
    comment=models.TextField()
    submit_date=models.DateTimeField(auto_now_add=True)

class SocialIssueLikes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    social_issue=models.ForeignKey(SocialIssue,on_delete=models.CASCADE,related_name="likes")
    timestamp=models.DateTimeField(auto_now_add=True)