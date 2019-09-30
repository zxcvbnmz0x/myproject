from django.db import models

# Create your models here.
class Tools(models.Model):
    def getModelResult(model,*orders,**wheres):
        ret=model.objects
        ret=ret.filter(**wheres)
        for order in orders:
            ret=ret.order_by(order)
        return ret
