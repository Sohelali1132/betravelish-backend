from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "status": "ok",
        "message": "Betravelish Backend API is running 🚀"
    })
