from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Post,Comment,Photo
from  django.urls import reverse
# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

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
    ip=get_client_ip(request)
    post = get_object_or_404(Post, id=post_id)
    coment=Comment.create(post,request.POST['comment'],ip)
    coment.save()
    return HttpResponseRedirect(reverse('detail', args=(post_id,)))
def postWrite(request):
    try:
        title=request.POST['title']
        text=request.POST['text']
        ip=get_client_ip(request)
        post=Post.create(title,text,ip)
        post.save()
        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = post
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
        return HttpResponseRedirect(reverse('index', args=()))

    except KeyError:
        return render(request, 'forest/write.html')

    