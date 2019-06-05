from django.shortcuts import render,redirect
from django.http import HttpResponse
from difflib import SequenceMatcher
from .models import User,Work,Author,Tags,Sessions,Likes,Collections

from django.core.paginator import Paginator

import difflib
# Create your views here.

##测试函数
def test(request):


    a = 'hello'

    works = Work.objects(name = '赵将军歌')
    arr = []
    for work in works:
        cont = work.content
        arr1 = cont.split("。")


        for str in arr1:
            arr2 = str.split('，')
            for st in arr2:
                arr.append(st)
            print(arr2)
    tags = Tags.objects

    # 计算正确率
    str1 = '静夜思李白，举头望明月'
    str2 = '静夜思李白，<br>举头望太阳'
    s = SequenceMatcher()
    str2 =str2.replace('<br>','')
    print(str2)
    s.set_seqs(str1, str2)
    r = s.ratio()
    r = r*100
    r = int(r)

    # 错误字段高亮显示
    str1 = str1.replace('，','\r')
    str1 = str1.replace('。','\n')
    str2 = str2.replace('，','\r')
    str2 = str2.replace('。','\n')
    str1 = str1.splitlines()
    str2 = str2.splitlines()
    d = difflib.HtmlDiff()
    diff = d.make_file(str1, str2,context=True, fromdesc='你的默写', todesc='正确答案',)

    return render(request,'index.html',{'str':r,"diff":diff})

#跳转到指定页的页面
def index_page(request,pageid):
    print(pageid)
    allList = Work.objects.order_by("likecount")
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
    for w in works:
        print(w.name)
    tags1 =Tags.objects
    tags = list(set(tags1))
    n = 0
    #实现分页
    allList = Work.objects.order_by("-likecount")
    paginator = Paginator(allList,6)

    #测试paginator
    # print(paginator.count)
    # print(paginator.num_pages)
    total_pages = paginator.num_pages
    # print(paginator.page_range)

    #首页显示第一页
    page = paginator.page(1)

    #测试page
    # print(page.has_next())#是否有下一页
    # print(page.has_other_pages())#是否有其他页
    # print(page.has_previous())#是否有前一页
    # print(page.next_page_number())#下一页的页码
    # # print(page.previous_page_number())#前一页的页码
    # print(page.start_index())#该页开始元素的索引
    # print(page.end_index())#该页最后的元素的索引
    # previous_page = ''
    # if page.previous_page_number()
    # previous_page = page.previous_page_number()
    # next_page = page.next_page_number()
    # 'previous': previous_page, 'next': next_page

    #获取session
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    lks = []
    likes =Likes.objects

    for like in likes:
        lks.append(like.wkname)

    print(lks)

    colls =[]

    collections=Collections.objects
    for coll in collections:
        colls.append(coll.wkname)


    return render(request,'poemLearning.html',{'username':username,'works':page,'count':n,'tags':tags,'end_page':total_pages,"likes":lks,'collections':colls})


# #首页重定向
# def gushici(request):
#     return redirect('/')

#显示登录界面
def logsign(request):
    return render(request,'login.html')

def log(request):
    u_phone = request.POST.get('form-username')
    password = request.POST.get('form-password')

    # 存储session


    works = Work.objects
    tags1 =Tags.objects
    tags = list(set(tags1))
    n = 0
    #实现分页
    allList = Work.objects
    paginator = Paginator(allList,6)
    #首页显示第一页
    page = paginator.page(1)

    print(password)
    user = User.objects(phone=u_phone)
    pwd =''
    for a in user:
        pwd = a.password


    if user:
        if password == pwd:
            sess = Sessions()
            for a in user:
                sess.session = a.username
            sess.save()
            sessions = Sessions.objects
            print(sessions)
            for a in sessions:
                username = a.session
                print(username)
            return redirect('/')
            # return render(request,'login.html',{'check':False})
        else:
            return render(request,'login.html',{'check':True,'item':'密码'})
    else:
        return render(request,'login.html',{'check':True,'item':'手机号'})



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

    print(page)


    total_pages = paginator.num_pages
    authors = Author.objects
    works = Work.objects
    #获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    return render(request, 'authors.html', {'username': username, 'authors': page,'end_page':total_pages, 'works': works})


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
    print(page)
    total_pages = paginator.num_pages
    return render(request,'authors.html',{'username':username,'authors':page,'end_page':total_pages,'works':works})

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

    return render(request,'quanpian.html',{'username':username})

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
        #存储到我的默写里
        write = Writes()
        #如果我的默写里存在该首诗，则不保存
        name =''
        isnothas = Writes.objects(workname=q_title)
        for a in isnothas:
            name = a.workname

        if(name == q_title):
            print(write)
        #否则保存这首诗
        else:
            write.username = username
            write.workname = q_title
            for wk in result:
                write.wk_author = wk.author
                write.wk_dynasty = wk.dynasty
                write.wk_content = wk.content
            write.save()
            print(write)
        #判断是否默写正确
        for work in result:
            a = work.name
            b = work.author
            if q_author != b:
                return render(request, 'quanpian.html', {'result': '作者写错了','username':username})
            c = work.content
            answer = c
            print('1:\n'+c)
            #content 正确的诗词去除标点符号
            c = str(c).replace('<br>','')
            c = str(c).replace('<br>', '')
            c = str(c).replace('，','')
            c = str(c).replace('。','')
            c = str(c).replace('！', '')
            c = str(c).replace('\n', '')
            #write_work 书写的诗词去除标点符号
            print('2:\n' + c)
            ww = q_content
            print('3.0:\n' + ww)
            ww = ww.replace('，', '')
            print('3.1:\n' + ww)
            ww = ww.replace('。', '')
            print('3.2:\n' + ww)
            ww = ww.replace('！', '')
            print('3.3:\n' + ww)
            ww = ww.replace('？', '')
            print('3.4:\n' + ww)
            ww = ww.replace('\r\n', '')
            print('3:\n' + ww)
            s = SequenceMatcher()
            s.set_seqs(c, ww)
            r = s.ratio()
            r = r * 100
            r = int(r)
            print(r)
            #highlight_answer 高亮的答案
            hla = answer
            hla = hla.replace('<br>', '')
            hla = hla.replace('，', '\n')
            hla = hla.replace('。', '\n')
            hla = hla.replace('？', '\n')
            hla = hla.replace('！', '\n')
            hla = hla.strip()
            print('4:\n' + hla)
            #highlight_write 高亮的默写
            hlw = q_content
            hlw = hlw.replace('，', '\n')
            hlw = hlw.replace(',', '\n')
            hlw = hlw.replace('。', '\n')
            hlw = hlw.replace('？', '\n')
            hlw = hlw.replace('！', '\n')
            print('5:\n' + hlw)
            str1 = hlw.splitlines()
            str2 = hla.splitlines()
            print('6:')
            print(str1)
            print('7:')
            print(str2)
            d = difflib.HtmlDiff()
            diff = d.make_file(str1, str2, context=True, fromdesc='你的默写', todesc='正确答案', )
            if c != ww:
                return render(request, 'quanpian.html', {'result': '内容有错，快来核对一下','username':username,'q_c':q_content, 'title':a,'author':b,'content': answer,'ratio':r,'diff':diff})
            else:
                return render(request, 'quanpian.html',{'result': '恭喜你！全对了','username':username,'q_c':q_content, 'title': a, 'author': b, 'content': answer,'ratio':r,'diff':diff })
    else:
        return render(request,'quanpian.html',{'result':'题目写错了','username':username})


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

def updateSafe(request):
    new_username = request.POST.get('username')
    new_phonenum = request.POST.get('phonenumber')
    new_password = request.POST.get('login_password')
    name = ''
    sessions = Sessions.objects
    for a in sessions:
        name = a.session
    user = User.objects(username=name)
    for u in user:
        if new_username:
            u.username = new_username
            sessions = Sessions.objects
            for a in sessions:
                a.session =new_username
                a.save()
        if new_password:
            u.password = new_password
        if new_phonenum:
            u.phone = new_phonenum
        u.save()


    return redirect('/update/')
def mycoll(request):
    # 获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    # works = Work.objects[4:8]

    colls = Collections.objects.order_by("-collect_time")
    return render(request, 'my_coll.html',{'username':username,'works':colls})

def mylike(request):
    # 获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    works = Work.objects
    print(works)

    likes = Likes.objects(user=username).order_by("-like_time")
    print(likes)


    return render(request, 'my_like.html',{'username':username,'works':likes})

def mycreate(request):
    # 获取sessions
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    write = Writes.objects(username=username).order_by("-wk_time")

    return render(request, 'my_create.html',{'username':username,'works':write})

def showput(request):
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    create =Creates.objects(user=username)
    for c in create:
        print(c.id)
    return render(request, 'my_put.html', {'username': username, 'creates': create.order_by('-cteate_time')})

from .models import Creates
def show_society(request):
    username =''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    creates = Creates.objects.order_by("-create_time")
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

def delete_cr(request,workname):

    put = Writes.objects(workname=workname)
    put.delete()

    return redirect('/create/')

def delete_put(request,putid):

    print(putid)

    put = Creates.objects(id=putid)
    print(put)

    put.delete()

    print(Creates.objects(id=putid))


    return redirect('/put/')

def delete_cre(request,putid):

    print(putid)

    put = Creates.objects(id=putid)
    print(put)

    put.delete()

    print(Creates.objects(id=putid))


    return redirect('/society/')

    # return render(request,'society.html',{'username':username,'creates':creates})




def show_tag(request):
    return redirect('/')

def tiankong(request):


    return render(request,'tiankong.html')

import re

def starttiankong(request):
    title = request.POST.get('title')

    works = Work.objects(name=title)
    print(works)

    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session
    if works:
        #存储默写内容
        write = Writes()
        write.username = username
        write.workname = title
        for wk in works:
            write.wk_author = wk.author
            write.wk_dynasty = wk.dynasty
            write.wk_content = wk.content
        write.save()
        print(write)

        arr = []
        for work in works:
            cont = work.content
            # arr1 = cont.split("。|!|?")   #python 内建的split只能使用单个分隔符
            cont = cont.replace('<br>','')

            arr1 = re.split(r'[。？！]',cont)


            print(arr1)

            for str in arr1:
                arr2 = str.split('，')
                for st in arr2:
                    arr.append(st)

        length = len(arr)
        print(length)
        return render(request, 'tiankong.html', {'str': arr[:length-1],'answer':False,'title':title,'username':username})
    else:
        return render(request, 'tiankong.html', {'error': '该篇诗词不存在，请换一篇默写！','username':username})


def restarttiankong(request):
    return redirect('/tiankong/')

def tagswk(request,tagname):

    print(tagname)

    if Work.objects(name=tagname):
        workl = Work.objects(name=tagname)

    elif Work.objects(author=tagname):
        workl = Work.objects(author=tagname)
        print(workl)

    elif Work.objects(dynasty=tagname):
        workl = Work.objects(dynasty=tagname)

    else:
        workl = Work.objects(tags=tagname)

    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    tags1 = Tags.objects
    tags = list(set(tags1))


    return render(request,'result.html',{'works': workl,'tags': tags,'username':username})


def safelike(request,workname):
    print(workname)
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    if Likes.objects(wkname=workname):

        lks = Likes.objects(wkname=workname)
        wks = Work.objects(name=workname)
        for l in wks:
            l.likecount = l.likecount-1
            l.save()
        lks.delete()


    else:

        like = Likes()
        like.wkname = workname
        like.user = username

        wks = Work.objects(name=workname)
        for l in wks:
            l.likecount = l.likecount + 1
            print("喜欢的个数："+str(l.likecount))
            l.save()
        for wk in wks:
            like.author=wk.author
            like.dynasty=wk.dynasty
            like.content=wk.content
            like.tags=wk.tags

        like.save()




        # for wk in work:
        #     wk.islike = True
        #     wk.save()



        l = Likes.objects
        print(l)

    return redirect("/")

def safecollect(request,workname):
    print(workname)
    username = ''
    sessions = Sessions.objects
    for a in sessions:
        username = a.session

    if Collections.objects(wkname=workname):
        lks = Collections.objects(wkname=workname)
        lks.delete()
    else:
        colls = Collections()
        colls.wkname = workname
        wks = Work.objects(name=workname)
        for wk in wks:
            colls.author=wk.author
            colls.dynasty=wk.dynasty
            colls.content=wk.content
            colls.tags=wk.tags
        # print(workname)
        colls.user = username
        # print(username)
        colls.save()
        l = Collections.objects
        print(l)

    return redirect("/")

def review(request):
    return redirect('/write/')


