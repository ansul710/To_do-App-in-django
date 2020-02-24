from django.shortcuts import render, redirect
from .models import TodoItems


# Create your views here.


def todoView(request):
    items = TodoItems.objects.all()
    content = {'todos': items}
    return render(request, 'todo.html', content)


def additems(request):
    new_item = TodoItems(content=request.POST['content'])
    new_item.save()
    return redirect('todohome')


def deleteitem(request, post_id):
    delete_item = TodoItems.objects.get(id=post_id)
    delete_item.delete()
    return redirect('todohome')
