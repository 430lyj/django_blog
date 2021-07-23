from django.db import models
from django.db.models.deletion import CASCADE
from account.models import CustomUser

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=CASCADE)
    title = models.CharField(max_length=30)
    writer = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank = True, null = True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=CASCADE)
    body = models.TextField()
    blog = models.ForeignKey(Blog, null=False, on_delete=CASCADE)
