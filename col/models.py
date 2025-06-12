from django.db import models
class col(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField()
    branch=models.TextField()
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
class Meta:
    verbose_name = "col"
    verbose_name_plural = "cols"
