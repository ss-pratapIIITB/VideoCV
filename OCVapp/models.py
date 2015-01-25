from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class test(models.Model):
	name = models.CharField(max_length = 30)
	desc = models.CharField(max_length = 300, blank = True)

	def __unicode__(self):
		return self.name

class Questions(models.Model):
	test_id = models.ForeignKey(test)
	statement = models.CharField(max_length = 100)
	marks = models.IntegerField()

	def __unicode__(self):
		return self.statement

class Test_select(models.Model):
	test_name = models.ForeignKey(test)

	def __unicode__(self):
		return self.test_name
# class Scores(models.Model):