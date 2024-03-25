from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from spot_deals.models.spot_deals import SpotDeal
from spot_deals.models.spot_deals import CryptoAsset


# получение данных из бд
def index(request):
    asset = CryptoAsset.objects.all()
    return render(request, "index.html", {"people": asset})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        asset = CryptoAsset()
        asset.full_name = request.POST.get("full_name")
        asset.ticker = request.POST.get("ticker")
        asset.consensus_type = request.POST.get("consensus")
        asset.token_birth_date = request.POST.get("date_issue")
        asset.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        asset = CryptoAsset.objects.get(id=id)

        if request.method == "POST":
            asset.full_name = request.POST.get("full_name")
            asset.ticker = request.POST.get("ticker")
            asset.consensus_type = request.POST.get("consensus")
            asset.token_birth_date = request.POST.get("date_issue")
            asset.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": asset})
    except CryptoAsset.DoesNotExist:
        return HttpResponseNotFound("<h2>Asset not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        asset = CryptoAsset.objects.get(id=id)
        asset.delete()
        return HttpResponseRedirect("/")
    except CryptoAsset.DoesNotExist:
        return HttpResponseNotFound("<h2>Asset not found</h2>")
