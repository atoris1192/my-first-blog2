from django.utils import timezone
from .models import Post # Post 関数呼び出し
from django.shortcuts import render, get_object_or_404

## published_date is collect
def post_list(request):
  posts = Post.objects.filter(published_data__lte=timezone.now()).order_by('published_data')
  return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {'post': post})