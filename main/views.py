from django.shortcuts import render, redirect
from main.models import Kartu
from main.forms import KartuForm

# Create your views here.
def show_main(request):
    context = {
       "nama_pengirim" : "NADHIF",
        "pesan" : "Selamat Ulang Tahun",
        "wish" : "SEMOGA BISA MAKIN MANTAP",
        "wish_entries" : Kartu.objects.all()
    }

    return render(request, "home.html", context)

def create_wish(request):
    form = KartuForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    context = {"form": form}
    return render(request, "create_wish.html", context)

def delete_wish(request, id):
    wish = Kartu.objects.get(id=id)
    wish.delete()
    return redirect("main:show_main")

def show_wish(request):
    return render(request, "wish.html")

def show_clue(request):
    return render(request, "clue.html")
