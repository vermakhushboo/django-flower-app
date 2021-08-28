from django.db import models

class Flower(models.Model):
    flower_name = models.CharField(max_length = 20)
    flower_color = models.CharField(max_length = 20)
    added_on = models.DateTimeField(auto_now_add = true)

    def __str__(self):
        return self.flower_name

