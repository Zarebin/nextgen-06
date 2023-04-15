from django.db import models

# Create your models here.
class browser_count(models.Model):
    browser = models.CharField(max_length=50)
    visitsCount = models.IntegerField(default=1)

    def __str__(self):
        return self.browser+ ':' + str(self.visitsCount)
