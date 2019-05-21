from django.db import models
import mongoengine
import django.utils.timezone as timezone
# Create your models here.
'''
class New_Manage(models.Manager):
    def get_queryset(self):
        return super(New_Manage,self).get_queryset()
'''

class User(mongoengine.Document):
    username = mongoengine.StringField(primary_key=True)
    password = mongoengine.StringField(max_length=20)
    #picture = mongoengine.StringField()
    phone = mongoengine.IntField()
    c_time = mongoengine.DateTimeField("创建日期",auto_now_add=True)
    my_coll = mongoengine.StringField()
    my_like = mongoengine.StringField()
    user_objs = models.Manager()
    meta = {'collection': 'users'}

class Work(mongoengine.Document):
    name = mongoengine.StringField()
    author = mongoengine.StringField()
    dynasty = mongoengine.StringField()
    content = mongoengine.StringField()
    tags = mongoengine.ListField()

    wk_objs = models.Manager()
    meta = {'collection':'works'}

class Author(mongoengine.Document):
    name = mongoengine.StringField()
    pictureurl = mongoengine.StringField()
    message = mongoengine.StringField()

    meta = {'collection':'authors'}

class Tags(mongoengine.Document):
    tag_name=mongoengine.StringField()
    tag_url=mongoengine.StringField()
    count = mongoengine.IntField()
    meta = {'collection': 'tags'}

class Sessions(mongoengine.Document):
    session = mongoengine.StringField()
    meta = {'collection':'sessions'}

class Creates(mongoengine.Document):
    user = mongoengine.StringField()
    content = mongoengine.StringField()
    create_time = mongoengine.DateTimeField(default = timezone.now)

class Writes(mongoengine.Document):
    username = mongoengine.StringField()
    workname = mongoengine.StringField()
    wk_author = mongoengine.StringField()
    wk_dynasty = mongoengine.StringField()
    wk_content = mongoengine.StringField()
    wk_time = mongoengine.DateTimeField(default = timezone.now)

# 上传图片
# class UserInfo(models.Model):
#     user=models.OneToOneField(User)
#     photo=models.ImageField(upload_to='photos',default='user1.jpg')
#     def __unicode__(self):
#         return self.user.username