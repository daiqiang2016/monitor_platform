from redisco import models

# Create your models here.
class CrawlModel(models.Model):
    day = models.Attribute(required=True, unique= False)
    desc= models.Attribute(required=True, unique= False)
    cnt = models.Attribute(required=True, unique= False)
