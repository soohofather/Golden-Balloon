from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
    path("c_create/<int:pk>", views.c_create, name="c_create"),
    path("c_delete/<int:a_pk>/<int:c_pk>", views.c_delete, name="c_delete"),
    path("like/<int:pk>", views.like, name="like"),
    path("notice/", views.notice, name="notice"),
    path("notice/n_create/", views.n_create, name="n_create"),
    path("notice/n_detail/<int:pk>", views.n_detail, name="n_detail"),
    path("notice/n_delete/<int:pk>", views.n_delete, name="n_delete"),
    path("notice/n_update/<int:pk>", views.n_update, name="n_update"),
    path("reviews/", views.reviews, name="reviews"),
    path("reviews/create", views.r_create, name="r_create"),
    path("reviews/<int:pk>", views.r_detail, name="r_detail"),
    path("reviews/delete/<int:pk>", views.r_delete, name="r_delete"),
    path("reviews/update/<int:pk>", views.r_update, name="r_update"),
    path("reviews/c_create/<int:pk>", views.r_c_create, name="r_c_create"),
    path("reviews/c_delete/<int:a_pk>/<int:c_pk>", views.r_c_delete, name="r_c_delete"),
    path("reviews/like/<int:pk>", views.r_like, name="r_like"),
    path("faq/", views.faq, name="faq"),
    path("faq/faq_create/", views.faq_create, name="faq_create"),
    path("faq/faq_detail/<int:pk>", views.faq_detail, name="faq_detail"),
    path("faq/faq_delete/<int:pk>", views.faq_delete, name="faq_delete"),
    path("faq/faq_update/<int:pk>", views.faq_update, name="faq_update"),
    path("search/", views.search, name="search"),
    path("searchfail/", views.searchfail, name="searchfail"),
]
