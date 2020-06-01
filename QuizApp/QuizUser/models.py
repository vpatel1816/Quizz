from django.db import models

# Create your models here.

class quiz_que(models.Model):
	question = models.TextField(max_length=200)
	A = models.CharField(max_length=50)
	B = models.CharField(max_length=50)
	C = models.CharField(max_length=50)
	D = models.CharField(max_length=50)
	ans = models.CharField(max_length=1)
	

	def __str__(self):
		return self.question


