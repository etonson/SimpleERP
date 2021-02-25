from django.db import models

class Contract(models.Model):
    ContractID = models.CharField(max_length=10)
    ContractName  = models.CharField(max_length=10)

    def __str__(self):
        return self.ContractID

class BudgetAccess(models.Model):
    contract = models.ForeignKey(Contract,on_delete=models.CASCADE)
    ItemID = models.CharField(max_length=7)
    Specification = models.CharField(max_length=10)
    Name = models.CharField(max_length=30)
    Dismantle = models.CharField(max_length=10)
    Counts = models.FloatField(null=True)
    Unit = models.CharField(max_length=5)

    def __str__(self):
        return self.ItemID
