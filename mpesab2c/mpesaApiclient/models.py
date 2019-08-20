from django.db import models


class B2CResponse(models.Model):
    Resulttype = models.CharField(max_length=150,default="rt6uy424545")
    ResultCode = models.CharField(max_length=150,default="24yhjy55424")
    OriginatorConversationId = models.CharField(max_length=150,default="drgsdryht5")
    ConversationId = models.CharField(max_length=150,default="drgsdr")
    TransactionId = models.CharField(max_length=150,default="drgsd44r")
    Status=models.BooleanField(default=False)

# Create your models here.
