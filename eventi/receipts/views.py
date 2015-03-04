# coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from eventi.receipts.forms import ReceiptForm
from eventi.receipts.models import Receipt


def receipt(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    return render(request, 'receipts/receipt_form.html',
                  {'form': ReceiptForm()})


def create(request):
    form = ReceiptForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'receipts/receipt_form.html',
                      {'form': form})
    form.send_mail()
    obj = form.save()
    return HttpResponseRedirect('/comprovante/%d/' % obj.pk)


def detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    return render(request, 'receipts/receipt_detail.html',
                  {'receipt': receipt})
