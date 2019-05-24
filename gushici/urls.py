
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.index,name='main'),
    path('test/',views.test),
    #url(r'^index/(\d+)/$',views.test,name='index'),
    path('<int:pageid>/',views.index_page,name='index'),
    # path('gushici/',views.gushici),
    path('log/',views.logsign,name='log'),
    path('sign/',views.showregist,name='sign'),
    path('sign/register/',views.regist,name='success'),
    path('login/',views.log,name='login'),
    path('write/', views.show_write,name='write'),
    path('write/result/',views.checkwrite,name='result'),
    path('authors/', views.show_au_page,name='authors'),
    path('authors/<int:pageid>',views.show_authors,name='authorspage'),
    path('works/', views.show_wk_page,name='works'),
    path('works/<int:pageid>',views.show_works,name='workspage'),
    # path('u/',views.user_web,name='user_web'),
    path('quit/',views.quit,name='quit'),
    path('search/',views.search),
    # path('search/<int:pageid>',views.search_page,name='result'),
    path('update/',views.updateinfo,name='update'),
    path('like/',views.mylike,name='like'),
    path('create/',views.mycreate,name='create'),
    path('u/',views.mycoll,name='user_web'),
    path('society/',views.show_society,name='society'),
    path('society/creations/',views.society,name='safe_put'),
    path('delete/',views.delete_cr,name='delete'),
    path('del/<str:workname>',views.delete_cr,name='del'),
    path('put/',views.showput,name='myput'),

    path('delete_put/',views.delete_put),
    path('delput/<str:putid>',views.delete_put,name="delput"),

    path('delcre/<str:putid>',views.delete_cre,name="delcre"),


    path('tag/',views.show_tag,name='showtag'),
    path('tag/<str:tagname>',views.tagswk,name='tagfilt'),

    path('tiankong/',views.tiankong,name='tiankong'),
    path('tiankong/start/',views.starttiankong,name='start'),

    path('like/<str:workname>',views.safelike,name='like'),
    path('collect/<str:workname>',views.safecollect,name='collect'),

]