from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserReg
from .models import Post

def index(request): 
	post = Post.objects.filter() 
	return render(request, 'blog/index.html', {"posts": post}) 

def kaknespatb(request, pk): 
	post = get_object_or_404(Post, pk=pk) 
	return render(request, 'blog/kaknespatb.html', {"post": post})

def login(request):
	return render(request, 'blog/login.html')

def registration(request):
	if request.method == "POST":
		form = UserReg(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'{username} создан!')
			return redirect('login')
	else:
		form = UserReg()
	return render(request, 'blog/registration.html', {'form': form})

def create(request):
	if not request.user.is_anonymous:
		if request.method == "POST":
			form = {
				'text': request.POST["text"],
				'title': request.POST["title"]
			}
			if form["text"] and form["title"]:
				title = form["title"]
				if Post.objects.filter(title=title).exists():
					form['errors'] = u"Введите другой заголовок..."
					return render(request, 'blog/create.html', {'form': form})
				else:
					Post.objects.create(text=form["text"], title=form["title"], author=request.user)
					post = Post.objects.get(title=form['title'])
					return redirect('kaknespatb', pk=post.id)
			else:
				form['errors'] = u"Не все поля заполнены"
				return render(request, 'blog/create.html', {'form': form})
		else:
			return render(request, 'blog/create.html', {})
	else:
		raise Http404