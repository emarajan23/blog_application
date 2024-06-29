from django.shortcuts import render,redirect,get_object_or_404
from .models import post
from .forms import postform


def create_post(request):
    if request.method == 'POST':
        form = postform(request.POST)
        if form.is_valid():
            form.save()
        return redirect(post_list)  
    else:
        form = postform()
    return render(request, 'app_blog/create_post.html', {'form': form})


def post_list(request):
    tasks = post.objects.all()
    context = {'tasks': tasks}
    if tasks:
        context['task'] = tasks.first()
    return render(request, 'app_blog/post_list.html', context)


def edit_post(request, post_id):
    tasks = get_object_or_404(post, id=post_id)
    if request.method == 'POST':
        form = postform(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = postform(instance=tasks)
   
    return render(request, 'app_blog/edit_post.html', {'form': form})


def edit_post_list(request):
    tasks = post.objects.all()
    return render(request, 'app_blog/edit_list_post.html', {'tasks': tasks})


def delete_post(request, post_id):
    tasks = get_object_or_404(post, id=post_id)
    if request.method == 'POST':
        tasks.delete()
        return redirect('post_list')
    return render(request, 'app_blog/delete_post.html', {'tasks': tasks})


def delete_post_list(request):
    tasks = post.objects.all()
    return render(request, 'app_blog/delete_post_list.html', {'tasks': tasks})


def filter_postby_author(request):
    auth = request.GET.get('aut')
    if auth:
        tasks = post.objects.filter(author=auth)
    else:
        tasks = post.objects.all()
    return render(request, 'app_blog/post_list.html', {'tasks': tasks, 'selected_author': auth})


def filter_postby_tag(request):
    tag= request.GET.get('tag')
    if tag:
        tasks = post.objects.filter(tag=tag)
    else:
        tasks = post.objects.all()
    return render(request, 'app_blog/post_list.html', {'tasks': tasks, 'selected_tag': tag})

  
  
  
  
  
  
  
  
  
  
  