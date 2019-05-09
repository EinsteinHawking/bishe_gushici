
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
    path('u/',views.user_web,name='user_web'),
    path('quit/',views.quit,name='quit'),
    path('search/',views.search),
    # path('search/<int:pageid>',views.search_page,name='result'),


]