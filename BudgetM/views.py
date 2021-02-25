from django.shortcuts import render
from BudgetM import forms,models

def BudgetTable(requset):
#{{{
    ContractChoiceForm_form = forms.ContractChoiceForm(requset.POST)
    if ContractChoiceForm_form.is_valid():
        tmp_v=ContractChoiceForm_form.cleaned_data['ContractChoice']

        try:
            contract = models.Contract.objects.get(ContractID=tmp_v)
            Bud = models.BudgetAccess.objects.filter(contract=contract)
        except:
            pass

        print(Bud)
    else:
        print('error')
    return render(requset,'contact.html',locals())
#}}}
