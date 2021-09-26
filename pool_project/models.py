from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.TextField()
    
    #?Varintlar burda olacag yeni seceneklerimiz
    option_one = models.CharField(max_length=255)
    option_two = models.CharField(max_length=255)
    option_three = models.CharField(max_length=255)
    
    #?Burda ise her bir variantda verilen ses sayi gosterilecek
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    
    
    def cem(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
    