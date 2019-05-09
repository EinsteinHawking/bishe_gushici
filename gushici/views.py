from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import User,Work,Author,Tags

from django.core.paginator import Paginator
# Create your views here.

##测试函数
def test(request):

    # name = ['lang','li','lu','bai','wang']
    s ='lang'
    a = User.objects(username = s)
    for user in a:
        print(a.password)

    #分页
    # allList = Work.objects
    # paginator = Paginator(allList,10)
    # page = paginator.page(pageid)

    return render(request,'index.html')

#跳转到指定页的页面
def index_page(request,pageid):
    allList = Work.objects
    paginator = Paginator(allList,6)
    page = paginator.page(pageid)
    tags1 = Tags.objects
    tags = list(set(tags1))
    return render(request,'poemLearning.html',{'works':page,'tags':tags})

#古诗词网主页
def index(request):

    user=None
    works = Work.objects
    tags1 =Tags.objects
    tags = list(set(tags1))
    n = 0
    #实现分页
    allList = Work.objects
    paginator = Paginator(allList,6)
    #首页显示第一页
    page = paginator.page(1)
    #获取session
    username = ''
#   username =request.session.get('name')

    return render(request,'poemLearning.html',{'username':username,'works':page,'count':n,'tags':tags})


# #首页重定向
# def gushici(request):
#     return redirect('/')

#显示登录界面
def logsign(request):
    return render(request,'login.html')

def log(request):
    u_name = request.POST.get('form-username')
    password = request.POST.get('form-password')
    #存储session
#    request.session['name'] = u_name
#    a =request.session.get('name')
#    print(a)
    works = Work.objects
    tags1 =Tags.objects
    tags = list(set(tags1))
    n = 0
    #实现分页
    allList = Work.objects
    paginator = Paginator(allList,6)
    #首页显示第一页
    page = paginator.page(1)
    print(u_name)
    print(password)
    user = User.objects(username=u_name)
    for a in user:
        pwd = a.password


    if user:
        if password == pwd:
            return redirect('/')
            # return render(request,'login.html',{'check':False})
        else:
            return render(request,'login.html',{'check':True,'item':'密码'})
    else:
        return render(request,'login.html',{'check':True,'item':'账号'})



#显示注册界面
def showregist(request):
    return render(request,'register.html')

#注册界面，将用户信息存储到数据库
def regist(request):

    username = request.POST.get('username')
    phonenum = request.POST.get('phonenumber')
    password = request.POST.get('login_password')

    user =User()
    user.username= username
    user.phone= phonenum
    user.password = password
    user.save()

    works = Work.objects
    return render(request,'login.html')
    # return redirect('log/')

#显示作者
def show_au_page(request):
    pageid = 1
    allList = Author.objects
    paginator = Paginator(allList,6)
    page = paginator.page(pageid)
    authors = Author.objects
    works = Work.objects
    username = request.session.get('name')
    return render(request, 'authors.html', {'username': username, 'authors': page, 'works': works})


def show_authors(request,pageid):
    authors = Author.objects
    works = Work.objects
    username = request.session.get('name')

    allList = Author.objects
    paginator = Paginator(allList,6)
    page = paginator.page(pageid)
    return render(request,'authors.html',{'username':username,'authors':page,'works':works})

# 显示作品
def show_wk_page(request):
    tags1 = Tags.objects
    tags = list(set(tags1))[:10]
    username = request.session.get('name')
    n = 0
    allList = Work.objects
    paginator = Paginator(allList, 6)
    page = paginator.page(1)
    return render(request, 'works.html', {'username': username, 'works': page, 'tags': tags})

def show_works(request,pageid):

    tags1 =Tags.objects
    tags = list(set(tags1))[:10]

    username = request.session.get('name')

    n = 0
    allList = Work.objects
    paginator = Paginator(allList, 6)
    page = paginator.page(pageid)
    return render(request,'works.html',{'username':username,'works':page,'tags':tags})

#在线默写
def show_write(request):
    username = request.session.get('name')
    return render(request,'writeFromMemory.html',{'username':username})

def checkwrite(request):
    q_title = request.POST.get('title')
    q_author = request.POST.get('author')
    q_content = request.POST.get('content')

    print(q_title)
    print(q_author)
    print(q_content)

    result = Work.objects(name=q_title)
    if result:
        for work in result:
            a = work.name
            b = work.author
            if q_author != b:
                return render(request, 'writeFromMemory.html', {'result': '作者写错了'})
            c = work.content
            if q_content != c:
                return render(request, 'writeFromMemory.html', {'result': '内容有错，快来核对一下','q_c':q_content, 'title':a,'author':b,'content': c })
            else:
                return render(request, 'writeFromMemory.html',{'result': '恭喜你！全对了','q_c':q_content, 'title': a, 'author': b, 'content': c })
    else:
        return render(request,'writeFromMemory.html',{'result':'题目写错了'})





    return render(request,'index.html')

#个人中心
def user_web(request):
    username = request.session.get('name')
    user = User.objects(username='郎勇')
    return render(request,'user_main.html',{'username':username})

#搜索表单
def search(request):
    if 'q'in request.GET and request.GET['q']:
        q = request.GET['q']
        works = {}
        allList = {}
        if Work.objects(name=q):
            allList = Work.objects(name=q)
        elif Work.objects(author=q):
            allList = Work.objects(author=q)
        elif Work.objects(dynasty=q):
            allList = Work.objects(dynasty=q)
        else:
            q ='搜索不存在'

        # paginator = Paginator(allList, 6)
        # # 首页显示第一页
        # page = paginator.page(1)

        tags1 = Tags.objects
        tags = list(set(tags1))
        return render(request, 'result.html', {'works': allList,'query':q, 'tags': tags})

    else:
        return  redirect('/')

def quit(request):
    request.session.flush()

    return redirect('/')

# def search_page(request, pageid):
#     allList = Work.objects
#     paginator = Paginator(allList, 6)
#     page = paginator.page(pageid)
#     tags = Tags.objects
#
#     return render(request, 'result.html', {'works': page, 'tags': tags})



