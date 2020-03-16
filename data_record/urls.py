from django.urls import path
from . import views



app_name="data_record"
urlpatterns=[path('',views.home_page,name="home_page"),
             path('log_in/',views.log_in,name="log_in"),
             path('check_passwd/',views.check_passwd,name="check_passwd"),
             path('data_analysis/',views.data_analysis,name="data_analysis"),
             path('display/',views.display,name="display"),
             path('contact/',views.contact,name="contact"),
             path('search-form/',views.search_form,name="search_form"),
             path('search/',views.search,name="search"),
             path('upload/',views.upload,name="upload"),
             path('upload_file/',views.upload,name="upload"),
             path('<int:History_id>/',views.detail,name="detail"),
             path('<int:History_id>/result/',views.result,name="result"),
             path('<int:History_id>/vote/',views.vote,name="vote"),
             path(r'add/<year:num_n>/',views.time_add,name="time_add")
]
