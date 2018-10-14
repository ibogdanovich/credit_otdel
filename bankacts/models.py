from django.db import models

class Action(models.Model):
    shop = models.CharField(max_length=150)
    bank_id = models.IntegerField()
    last_update = models.DateTimeField()

    def __str__(self):
        return "%s (%s)" % (self.shop, self.bank_id )


class Bank(models.Model):
    name = models.CharField(max_length=150)
    ext_id = models.CharField(unique=True, max_length=150)
    
    def __str__(self):
        return self.name
