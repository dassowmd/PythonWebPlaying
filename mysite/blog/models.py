from django.db import models

class Post(models.Model):
    title = models.CharField(max_length =140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Accounts(models.Model):
    idAccount_Totals = models.IntegerField()
    Year = models.IntegerField()
    Month = models.IntegerField()
    Account_Type = models.CharField(max_length=45)
    Current_Or_Long_Term = models.CharField(max_length = 45)
    Account_Name = models.CharField(max_length = 180)
    Amount = models.FloatField()
    Notes = models.CharField(max_length = 300)
    URL = models.CharField(max_length = 300)
