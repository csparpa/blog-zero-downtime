from django.conf.urls import url
from hot_code_reload.views import PingView

urlpatterns = [
    url(r'^ping?$', PingView.as_view(), name="ping"),
]
