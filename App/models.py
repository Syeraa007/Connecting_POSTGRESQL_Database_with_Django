from django.db import models

# Create your models here.
class Topic(models.Model):
    topic=models.CharField(max_length=100,primary_key=True)

    def __str__(self) -> str:
        return self.topic

class Page(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100) 
    url=models.URLField()

    def __str__(self) -> str:
        return self.name
    
class Record(models.Model):
    name=models.ForeignKey(Page,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.author