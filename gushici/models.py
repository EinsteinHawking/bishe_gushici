from django.db import models
import mongoengine
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