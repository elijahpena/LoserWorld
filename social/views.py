from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Profile, Post, Comment
from .forms import PostForm, CommentCreateForm

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'social/home.html'
    paginate_by = 10


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('social:home'))
    else:
        form = UserCreationForm()
        context = {'form': form}
    return render(request, 'registration/create_user.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post.objects.create(user=request.user, title=form.cleaned_data['title'], content=form.cleaned_data['content'], image=form.cleaned_data['image'])
            return HttpResponseRedirect(reverse('social:home'))

    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'social/post_create.html', context)

class PostDetailView(generic.DetailView):
    model = Post

class CommentCreateView(CreateView):
    model = Comment
    fields = ['content', 'image']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=1)
        return super(CommentCreateView, self).form_valid(form)
#    form_class = CommentCreateForm
#    template_name = 'social/comment_form.html'
#
#    def form_valid(self, form):
#        self.object = form.save(commit=False)
#        self.object.user = self.request.user
#        self.object.save()
#
#    def get_form_kwargs(self, *args, **kwargs):
#        kwargs = super(CommentCreateView, self).get_form_kwargs(*args, **kwargs)
#        kwargs['user'] = self.request.user
#        return kwargs

class CommentDetailView(generic.DetailView):
    model = Comment
