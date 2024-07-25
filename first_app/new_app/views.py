from django.shortcuts import render
from .models import chaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chais = chaiVariety.objects.all()
    return render(request, 'new_app/chai.html', {'chais': chais})


def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(request, 'new_app/chai_detail.html', {'chai': chai})