from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('test/', views.QuestionListView.as_view(), name='question_list'),
    path('test/<int:pk>/detail/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('test/<int:question_id>/vote/', views.vote, name='vote'),  
    path('test/<int:pk>/result/', views.QuestionResultView.as_view(), name='question_result'),
    path('learn/subject_list/', views.SubjectListView.as_view(), name='subject_list'),
    path('learn/subject_list/<int:pk>/detail/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('learn/music_list/', views.MusicListView.as_view(), name='music_list'),
    path('learn/music_list/<int:pk>/detail/', views.MusicDetailView.as_view(), name='music_detail'),
]