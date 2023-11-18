from unicodedata import category
from django.shortcuts import render,HttpResponse
from medicine.models import Medicine,MedicineType
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
    m_type = MedicineType.objects.all()
    medicines = Medicine.allMedicines()
    type = request.GET.get('category')
    if type=='all':
        medicines = Medicine.allMedicines()
    else:
        medicines = Medicine.getMedicines(type)
    
    data = {}
    data['medicines'] = medicines
    data['m_type'] = m_type
    data['type'] = type
    return render(request, 'index.html', data)

def searchMatch(query,item):
    if query in item.salt.lower() or query in item.name.lower() or query in item.pack.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    m_type = MedicineType.objects.all()
    medicines = []

    if query:
        typeMed = Medicine.objects.values('category', 'id')
        cats = {item['category'] for item in typeMed}

        for cat in cats:
            prodtemp = Medicine.objects.filter(category=cat)
            prod = [item for item in prodtemp if searchMatch(query.lower(), item)]

            if len(prod) != 0:
                medicines.extend(prod)

    data = {'medicines': medicines, 'm_type': m_type}
    return render(request, 'index.html', data)
