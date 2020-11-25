from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Post,Comment
from  django.urls import reverse
# Create your views here.
def index(request):
    latest_post_list_Even=[]
    latest_post_list_Odd=[]
    latest_post_list=Post.objects.order_by('-post_time')[:10]
    for i in range(len(latest_post_list)):
        if i%2==0:
            latest_post_list_Odd.append(latest_post_list[i])

        else:
            latest_post_list_Even.append(latest_post_list[i])
            
    context = {'latest_post_list_Odd': latest_post_list_Odd,'latest_post_list_Even':latest_post_list_Even}
    return render(request, 'forest/index.html', context)
def detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post_id':post_id,'post': post,'len':len(post.comment_set.all())}

    return render(request, 'forest/detail.html', context)

def write(request,post_id):
    print(request.POST['comment'])
    post = get_object_or_404(Post, id=post_id)
    coment=Comment.create(post,request.POST['comment'])
    coment.save()
    return HttpResponseRedirect(reverse('detail', args=(post_id,)))
def postWrite(request):
    try:
        title=request.POST['title']
        text=request.POST['text']
        # image=request.Post.get('image')
        post=Post.create(title,text)
        post.save()
        return HttpResponseRedirect(reverse('index', args=()))

    except KeyError:
        return render(request, 'forest/write.html')

    