from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def receive_request(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode()) # Получить данные из тела запроса
        print(data) # Вывести данные в консоль
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)