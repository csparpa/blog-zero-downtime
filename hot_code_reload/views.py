import json
from django.http import HttpResponse
from django.views.generic import View
from .constants import EXPECTED_MESSAGE_VALUE


class PingView(View):

    def get(self, request):
        data = {
            "message": EXPECTED_MESSAGE_VALUE
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
