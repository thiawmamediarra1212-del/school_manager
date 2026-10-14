from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Bienvenue dans School Manager</h1>"
        "<ul>"
        "<li><a href='/students/'>Liste des étudiants</a></li>"
        "<li><a href='/students/1/'>Détail de l'étudiant 1</a></li>"
        "<li><a href='/about/'>À propos de l'école</a></li>"
        "</ul>"
    )


def student_list(request):
    return HttpResponse("Liste des étudiants")


def student_detail(request, id):
    return HttpResponse(f"Détail de l'étudiant {id}")


def about(request):
    return HttpResponse("School Manager est une application de gestion d'école.")
