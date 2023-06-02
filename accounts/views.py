from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from .models import CustomUser
from .forms import CustomUserChangeForm
from django.urls import reverse_lazy


class AccountDetailView(TemplateView):
    template_name = "account/account_detail.html"


class AccountUpdateView(UpdateView):
    model = CustomUser
    # form_class = CustomUserChangeForm
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy('account_detail')
    template_name = 'account/account_update.html'

    def get_object(self, queryset=None):
        return self.request.user
