from django.db import models 

class Post(models.Model): 

	class Meta(): 
		db_table = 'post' 
		verbose_name = "Статья" 
		verbose_name_plural = "Статьи" 
		ordering = ["create"] 

	title = models.CharField("Заголовок", max_length=100) 
	text = models.TextField("Текст статьи", max_length=1500) 
	create = models.DateTimeField("Создан", auto_now_add=True) 
	author = models.CharField("Автор", max_length=100) 

	def __str__(self): 
		return self.title