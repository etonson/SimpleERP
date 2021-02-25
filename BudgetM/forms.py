from django import forms
from BudgetM import models

class ContractChoiceForm(forms.Form):

    ContractItem=[]
    contract = models.Contract.objects.all()

    for para in contract:
        ContractItem.append([para.ContractID,para.ContractName])

    ContractChoice = forms.ChoiceField(label='合約選擇', choices=ContractItem)
