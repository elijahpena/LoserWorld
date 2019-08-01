from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Profile, Post, Comment

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

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostDetailView(generic.DetailView):
    model = Post

class CommentCreateView(CreateView):
    model = Comment
    fields = ['content', 'image']
    
    def get_success_url(self):
        return reverse_lazy('social:post_detail', args=[self.kwargs['post_id']])

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_id'])
        return super(CommentCreateView, self).form_valid(form)


class CommentDetailView(generic.DetailView):
    model = Comment

class CommentListView(generic.ListView):
    model = Comment

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_id'])
