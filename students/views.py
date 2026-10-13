from django.http import HttpResponse


def home(request):
    return HttpResponse("Bienvenue dans School Manager")


def student_list(request):
    return HttpResponse("Liste des etudiants")


def student_detail(request, id):
    return HttpResponse(f"Detail de l'etudiant {id}")
