import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


logger = logging.getLogger(__name__)

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'dashborad/index.html'
    login_url = '/accounts/login/'

"""
    def get(self, request, *args, **kwargs):
        return render(request, 'dashborad/index.html')
"""


index = IndexView.as_view()
