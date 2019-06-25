from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.MemoListView.as_view(),
        name='memo_list'),

    url(r'^detail/(?P<pk>\d+)/$',
        views.MemoDetailView.as_view(),
        name='memo_detail'),

    url(r'^create/$',
        views.MemoCreateView.as_view(),
        name='memo_create'),

    url(r'^update/(?P<pk>\d+)/$',
        views.MemoUpdateView.as_view(),
        name='memo_update'),

    url(r'^delete/(?P<pk>\d+)/$',
        views.MemoDeleteView.as_view(),
        name='memo_delete'),
]