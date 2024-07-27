from django.shortcuts import render
from .models import chaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    chais = chaiVariety.objects.all()
    return render(request, 'new_app/chai.html', {'chais': chais})


def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(request, 'new_app/chai_detail.html', {'chai': chai})


def chai_store(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarityForm()
    return render(request, 'new_app/chai_stores.html', {'stores': stores, 'form': form})