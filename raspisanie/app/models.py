from django.db import models

class Days(models.Model):
	
	title = models.CharField(max_length = 30)
	
	lesson1 = models.CharField(max_length = 50, null=True, blank=True)
	time1 = models.CharField(max_length = 15, null=True, blank=True)
	teacher1 = models.CharField(max_length = 55, null=True, blank=True)

	lesson2 = models.CharField(max_length = 50, null=True, blank=True)
	time2 = models.CharField(max_length = 15, null=True, blank=True)
	teacher2 =models.CharField(max_length = 55, null=True, blank=True)

	lesson3 = models.CharField(max_length = 50, null=True, blank=True)
	time3 = models.CharField(max_length = 15, null=True, blank=True)
	teacher3 = models.CharField(max_length = 55, null=True, blank=True)
	
	lesson4 = models.CharField(max_length = 50, null=True, blank=True)
	time4 = models.CharField(max_length = 15, null=True, blank=True)
	teacher4 = models.CharField(max_length = 55, null=True, blank=True)
	
	lesson5 = models.CharField(max_length = 50, null=True, blank=True)
	time5 = models.CharField(max_length = 15, null=True, blank=True)
	teacher5 = models.CharField(max_length = 55, null=True, blank=True)

	def __str__(self):
		return self.title
