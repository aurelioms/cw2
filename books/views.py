from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from books.models import Books
# Create your views here.


def index(request):
    return render(request, 'cw2/index.html')


@csrf_exempt
def books_api(request: HttpRequest):
    if request.method == 'GET':
        return JsonResponse({
            'books': [
                book.to_dict()
                for book in Books.objects.all()
            ]
        })

    if request.method == 'POST':
        body = json.loads(request.body)
        book = Books(title=body.get('title'),
                     author=body.get('author'),
                     publisher=body.get('publisher'),
                     stock=body.get('stock'))
        book.save()
        return JsonResponse({
            'data': "Success"
        })

    if request.method == 'PUT':
        print(request.body)
        body = json.loads(request.body)
        print(body)
        update = Books.objects.get(pk=body.get('id'))
        update.title = body.get('title')
        update.author = body.get('author')
        update.publisher = body.get('publisher')
        update.stock = body.get('stock')
        update.save()
        return JsonResponse({
            'data': "Success"
        })
