from django.db import models

# Create your models here.

class HashIdentifier(models.Model):
	activeStatus= models.BooleanField(default=True)
	hashIdentifierString = models.CharField(max_length=100)

	def __str__(self):
		return self.hashIdentifierString

class ContentHash(models.Model):
	contentHashString = models.CharField(max_length=100)
	hashIdentifierKey = models.OneToOneField(HashIdentifier,default=1 ,on_delete=models.CASCADE)

	def __str__(self):
		return self.contentHashString

