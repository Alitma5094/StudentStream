from django.urls import path
from .views import RankListView, RankCreateView, RankUpdateView, RankDeleteView, sort_ranks

urlpatterns = [
    path("", RankListView.as_view(), name="rank_list"),
    path("sort/", sort_ranks, name="sort_ranks"),
    path("create/", RankCreateView.as_view(), name="rank_create"),
    path("<uuid:pk>/update/", RankUpdateView.as_view(), name="rank_update"),
    path("<uuid:pk>/delete/", RankDeleteView.as_view(), name="rank_delete"),
]
