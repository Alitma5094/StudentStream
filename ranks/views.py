from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Rank

from django.urls import reverse_lazy


class RankListView(ListView):
    model = Rank
    context_object_name = "rank_list"
    template_name = "ranks/rank_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Accessed")
        return context


def sort_ranks(request):
    rank_pks_order = request.POST.getlist("rank_order")
    print(request.POST)
    ranks = []
    for idx, rank_pk in enumerate(rank_pks_order, start=1):
        rank = Rank.objects.get(pk=rank_pk)
        rank.order = idx
        rank.save()
        ranks.append(rank)

    return render(request, "partials/ranks_sort.html", {"rank_list": ranks})


class RankCreateView(CreateView):
    model = Rank
    template_name = "ranks/rank_create.html"
    fields = "__all__"
    success_url = reverse_lazy("rank_list")


class RankUpdateView(UpdateView):
    model = Rank
    template_name = "ranks/rank_update.html"
    fields = "__all__"
    success_url = reverse_lazy("rank_list")


class RankDeleteView(DeleteView):
    model = Rank
    template_name = "ranks/rank_delete.html"
    success_url = reverse_lazy("rank_list")
