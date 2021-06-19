from.import views
from django.urls import path
app_name = 'healthapp'
urlpatterns = [
    path('',views.home,name="home"),
    path('docdetail/<int:doc_id>/',views.docdetail,name="docdetail"),
    path('news',views.news,name='news'),
    path('patient', views.patient, name='patient'),
    path('success',views.success,name='success'),
    path('alldoclist',views.allDocList,name='allDocList'),
    path('<slug:d_slug>/',views.allDocList,name='doclist_by_department'),
    path('<slug:d_slug>/<slug:doc_slug>/', views.docDet, name='doclistdetail'),

]
