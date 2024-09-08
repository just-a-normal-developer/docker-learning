from django.http import HttpResponse


def main_page(request):
    return HttpResponse("congrats your container is working successfully")
