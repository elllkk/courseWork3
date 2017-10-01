from django.db import models

class Table_field(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    def publish(self):
        self.save()
    #def __str__(self):
       # return self.title
#
# Create yname = models.CharField(max_length=100, primary_key=True)our models here.

    def __str__(self):
        return "x=" + str(self.x) + ";y=" + str(self.y)