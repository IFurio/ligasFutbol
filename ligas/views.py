from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import forms
from django.shortcuts import redirect
from ligas.models import *

# Create your views here.
def index(request):
    return render(request, "index.html")


def edita_equip(request):
    return render(request, "edita_equip_ajax.html")


def nombre_equipo_existe(nombre):
    return Equip.objects.filter(nom__iexact=nombre).exists()


class EquipForm(forms.ModelForm):
    class Meta:
        model = Equip
        fields = ['nom', 'pais', 'ciutat', 'lligues']


def createequip(request):
    """form = LligaForm()
    if request.method == "POST":
        form = LligaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")

            if nombre_liga_existe(nombre):
                return HttpResponse("El nom de la lliga ja existeix. Si us plau, escull un altre nom.")

            lliga = Lliga.objects.create(nom=nombre)

            return HttpResponse("LLiga creada exitosament.")
    return render(request, "createequip.html",{
                    "form": form,
            })"""


def nombre_liga_existe(nombre):
    return Lliga.objects.filter(nom__iexact=nombre).exists()
     

class LligaForm(forms.Form):
    nombre = forms.CharField(max_length=100)


def createlliga(request):
    form = LligaForm()
    if request.method == "POST":
        form = LligaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")

            if nombre_liga_existe(nombre):
                return HttpResponse("El nom de la lliga ja existeix. Si us plau, escull un altre nom.")

            lliga = Lliga.objects.create(nom=nombre)

            return HttpResponse("LLiga creada exitosament.")
    return render(request, "createlliga.html",{
                    "form": form,
            })


class MenuForm(forms.Form):
    lliga = forms.ModelChoiceField(queryset=Lliga.objects.all())
    

def menu(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            lliga = form.cleaned_data.get("lliga")
            return redirect('classificacio',lliga.id)
    return render(request, "menu.html",{
                    "form": form,
            })


def classificacio(request, lliga_id):
    lliga = get_object_or_404(Lliga, pk=lliga_id)
    equips = lliga.equip_set.all()
    classi = []
    
    # calculem punts en llista de tuples (equip,punts)
    for equip in equips:
        punts = 0
        for partit in lliga.partit_set.filter(local=equip):
            if partit.gols_local() > partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        for partit in lliga.partit_set.filter(visitant=equip):
            if partit.gols_local() < partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        classi.append( (punts,equip.nom) )
    # ordenem llista
    classi.sort(reverse=True)
    return render(request,"classificacio.html",
                {
                    "classificacio":classi,
                    "lliga":lliga,
                })


