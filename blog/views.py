from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

class PostListView(ListView):
    """List all posts"""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# def post_list(request):
#     """List all posts"""
#     post_list = Post.published.all()
    
#     # Pagination with 3 posts per page
#     paginator = Paginator(post_list, 3)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         # if page_number is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html', { 'posts': posts })

def post_detail(request, year, month, day, post):
   """Display post detail"""
   post = get_object_or_404(Post, 
                            status=Post.Status.PUBLISHED,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
   return render(request, 
                 'blog/post/detail.html', 
                 { 'post': post })
   
   
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        # Form was submmited
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{ cd['name'] } recommends you read " \
                      f"{ post.title }"
            message = f"Read { post.title } at { post_url }\n\n" \
                      f"{ cd['name'] }\'s comments: { cd['comments'] }" 
            send_mail(subject, message, 'cbaah123@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', { 'post': post, 
                                                    'form': form,
                                                    'sent': sent})
    

@require_POST
def post_comment(request, post_id):
    # Post a comment
    post = get_object_or_404(Post, id=post, status=Post.Status.PUBLISHED
    comment = None
    
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(request, 'blog/post/comment.html', 
                        { 'comment': comment,
                         'form': form,
                         'post': post })
        