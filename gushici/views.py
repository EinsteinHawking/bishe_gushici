from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import User,Work,Author,Tags,Sessions

from django.core.paginator import Paginator
# Create your views here.

##测试函数
def test(request):

    # # name = ['lang','li','lu','bai','wang']
    # s ='lang'
    # a = User.objects(username = s)
    # for user in a:
    #     print(a.password)
    #
    # #分页
    # # allList = Work.objects
    # # paginator = Paginator(allList,10)
    # # page = paginator.page(pageid)
    authors = Author.objects
    allList = Author.objects
    paginator = Paginator(allList,6)
    page = paginator.page(2)

    return render(request,'index.html',{'cus_list':page})

#跳转到指定页的页面
def index_page(request,pageid):
    print(pageid)
    allList = Work.objects
    paginator = Paginator(allList,6)
    total_pages = paginator.num_pages
    page = paginator.page(pageid)
    tags1 = Tags.objects
    tags = list(set(tags1))
    return render(request,'poemLearning.html',{'works':page,'tags':tags,'end_page':total_pages})

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

    #测试paginator
    print(paginator.count)
    print(paginator.num_pages)
    total_pages = paginator.num_pages
    print(paginator.page_range)

    #首页显示第一页
    page = paginator.page(1)

    #测试page
    print(page.has_next())#是否有下一页
    print(page.has_other_pages())#是否有其他页
    print(page.has_previous())#是否有前一页
    print(page.next_page_number())#下一页的页码
    # print(page.previous_page_number())#前一页的页码
    print(page.start_index())#该页开始元素的索引
    print(page.end_index())#该页最后的元素的索引
    # previous_page = ''
    # if page.previous_page_number()
    # previous_page = page.previous_page_number()
    # next_page = page.next_page_number()
    # 'previous': previous_page, 'next': next_page

    #获取session
    username = ''
#   username =request.session.get('name')
    sessions = Sessions.objects
    print(sessions)
    for a in sessions:
        username = a.session
        print(username)
    print(username)
    return render(request,'poemLearning.html',{'username':username,'works':page,'count':n,'tags':tags,'end_page':total_pages})


# #首页重定向
# def gushici(request):
#     return redirect('/')

#显示登录界面
def logsign(request):
    return render(request,'login.html')

def log(request):
    u_name = request.POST.get('form-username')
    password = request.POST.get('form-password')
    # 存储session
    sess = Sessions()
    sess.session = u_name
    sess.save()
    sessions = Sessions.objects
    print(sessions)
    for a in sessions:
        username = a.session
        print(username)

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
    #获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    return render(request, 'authors.html', {'username': username, 'authors': page, 'works': works})


def show_authors(request,pageid):
    authors = Author.objects
    works = Work.objects
    # username = request.session.get('name')
    #获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    allList = Author.objects
    paginator = Paginator(allList,6)
    page = paginator.page(pageid)
    return render(request,'authors.html',{'username':username,'authors':page,'works':works})

# 显示作品
def show_wk_page(request):
    tags1 = Tags.objects
    tags = list(set(tags1))[:10]
    # username = request.session.get('name')
    #获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    n = 0
    allList = Work.objects
    paginator = Paginator(allList, 6)
    total_pages = paginator.num_pages
    page = paginator.page(1)
    return render(request, 'works.html', {'username': username, 'works': page, 'tags': tags,'end_page':total_pages})

def show_works(request,pageid):

    tags1 =Tags.objects
    tags = list(set(tags1))[:10]

    # username = request.session.get('name')
    #获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    n = 0
    allList = Work.objects
    paginator = Paginator(allList, 6)
    total_pages = paginator.num_pages
    page = paginator.page(pageid)

    return render(request,'works.html',{'username':username,'works':page,'tags':tags,'end_page':total_pages})

#在线默写
def show_write(request):
    # username = request.session.get('name')
    #获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    return render(request,'writeFromMemory.html',{'username':username})

from .models import Writes

def checkwrite(request):
    q_title = request.POST.get('title')
    q_author = request.POST.get('author')
    q_content = request.POST.get('content')

    print(q_title)
    print(q_author)
    print(q_content)

    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    result = Work.objects(name=q_title)
    if result:
        write = Writes()
        write.username = username
        write.workname = q_title
        for wk in result:
            write.wk_author = wk.author
            write.wk_dynasty = wk.dynasty
            write.wk_content = wk.content
        write.save()
        print(write)

        for work in result:
            a = work.name
            b = work.author
            if q_author != b:
                return render(request, 'writeFromMemory.html', {'result': '作者写错了','username':username})
            c = work.content
            if q_content != c:

                return render(request, 'writeFromMemory.html', {'result': '内容有错，快来核对一下','username':username,'q_c':q_content, 'title':a,'author':b,'content': c })
            else:

                return render(request, 'writeFromMemory.html',{'result': '恭喜你！全对了','username':username,'q_c':q_content, 'title': a, 'author': b, 'content': c })
    else:
        return render(request,'writeFromMemory.html',{'result':'题目写错了','username':username})


    return render(request,'index.html')

#个人中心
def user_web(request):
    username = request.session.get('name')
    user = User.objects(username='郎勇')
    #获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session


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
        # 获取sessions
        username = ''
        sessions = Sessions.objects
        for a in sessions:
            username = a.session


        tags1 = Tags.objects
        tags = list(set(tags1))
        return render(request, 'result.html', {'works': allList,'query':q, 'tags': tags,'username':username})

    else:
        return  redirect('/')

def quit(request):
    # request.session.flush()
    sessions = Sessions.objects.delete()

    return redirect('/')

# def search_page(request, pageid):
#     allList = Work.objects
#     paginator = Paginator(allList, 6)
#     page = paginator.page(pageid)
#     tags = Tags.objects
#
#     return render(request, 'result.html', {'works': page, 'tags': tags})

def updateinfo(request):
    # 获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    return render(request,'update_userinfo.html',{'username':username})

def mycoll(request):
    # 获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    works = Work.objects[4:8]
    return render(request, 'my_coll.html',{'username':username,'works':works})

def mylike(request):
    # 获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    works = Work.objects
    return render(request, 'my_like.html',{'username':username,'works':works})

def mycreate(request):
    # 获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    write = Writes.objects(username=username)

    return render(request, 'my_create.html',{'username':username,'works':write})

def showput(request):
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    create =Creates.objects(user=username)
    return render(request, 'my_put.html', {'username': username, 'creates': create})

from .models import Creates
def show_society(request):
    username =''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    creates = Creates.objects
    return render(request,'society.html',{'username':username,'creates':creates})

def society(request):

    cont = request.POST.get('content')
    print(cont)
    username =''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    if cont:
        print('2'+cont)
        cre = Creates()
        cre.user = username
        cre.content = cont
        cre.save()
        creates = Creates.objects
        return redirect('/society/')
    else:

        creates = Creates.objects
        return redirect('/society/')

def delete_cr(request):
    return redirect('/society/')





# #上传图片
# from .models import UserInfo
# def updateInfo(request):
#     if request.method == 'POST':
#         photo = request.FILES['photo']
#
#         if photo:
#             phototime = request.user.username + str(time.time()).split('.')[0]
#             photo_last = str(photo).split('.')[-1]
#             photoname = 'photos/%s.%s' % (phototime, photo_last)
#             img = Image.open(photo)
#             img.save('media/' + photoname)
#
#             count = UserInfo.objects.filter(user=request.user).update(
#                 photo=photoname
#             )
#             if count:
#                 # 设置一个session，然后跳转到对应的页面，此处简易写写
#                 return HttpResponse('上传成功')
#             else:
#                 return HttpResponse('上传失败')
#
#         return HttpResponse('图片为空')


