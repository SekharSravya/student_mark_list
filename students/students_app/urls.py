from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    url(r'^$', views.index),
    url('best_faculty/', best_faculty),
    url('best_pass_faculty/', best_pass_faculty),
    url('worst_faculty/', worst_faculty),
    url('best_student/',best_student),
    url('challenger/',challenger),
    url('best_math_student/',best_math_student),
    url('subject_average/',sub_avg)
]
