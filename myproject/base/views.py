from django.shortcuts import render,redirect
from .models import Post,History  

# Create your views here.
def home(request):
    all_data=Post.objects.all()

    return render(request,'home.html',{'data':all_data})

def add(request):
    if request.method == 'POST':
        post_data = request.POST['post']
        caption_data = request.POST['caption']
        Post.objects.create(post=post_data, caption=caption_data)
        return redirect('home')

    return render(request, 'add.html')

def edit(request, pk):
    edit_post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post_data = request.POST['post']
        caption_data = request.POST['caption']
        edit_post.post = post_data
        edit_post.caption = caption_data
        edit_post.save()
        return redirect('home')

    return render(request, 'edit.html', {'data': edit_post})

def delete_(request, pk):
    del_post = Post.objects.get(id=pk)
    History.objects.create(post=del_post.post, caption=del_post.caption)
    del_post.delete()
    return redirect('home')


def history(request):
    his = History.objects.all()
    return render(request, 'history.html', {'his': his})


def restore(request, pk):
    restore = History.objects.get(id=pk)
    Post.objects.create(post=restore.post, caption=restore.caption)
    restore.delete()
    return redirect('history')


def del_his(request, pk):
    his = History.objects.get(id=pk)
    his.delete()
    return redirect('history')