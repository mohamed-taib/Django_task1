from django.shortcuts import render

# Create your views here.
def v_add_numbers(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        result = num1 + num2
    else:
        result = None

    return render(request, 'index.html', {'result': result})

from .models import CalculatedResult , Student


def v_add_numbers2(request):
    result = None  # Définir la variable result en dehors de la logique de POST

    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        result = num1 + num2

        # Enregistrer les valeurs dans la base de données
        CalculatedResult.objects.create(
            num1=num1,
            num2=num2,
            result=result
        )

    # Récupérer l'historique des calculs depuis la base de données
    history = CalculatedResult.objects.all().order_by('-id')

    return render(request, 'index2.html', {'history': history, 'result': result})


def v_add_etd(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName', '0')
        last_name = request.POST.get('lastName', '0')
        student_id = float(request.POST.get('studentId', 0))
        
        # Enregistrer les valeurs dans la base de données
        Student.objects.create(
            first_name=first_name, 
            last_name=last_name,   
            student_id=student_id   
        )

    std = Student.objects.all()  # Fetch all students
    return render(request, 'index3.html', {'std': std})
               

def home (request) :
    return render (request , 'index4.html')
 