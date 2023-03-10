from django.db import models

#venv\Scripts\activate aktive etmeyi unutma ctrl c to stop the server
class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
a=ToDoList(name="suat")
a.save()
b=ToDoList(name="biyik")
b.save()
class Item(models.Model):
    todo = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    
