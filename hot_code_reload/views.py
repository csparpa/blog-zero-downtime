import json
import time
from django.http import HttpResponse
from django.views.generic import View


class PingView(View):

    def get(self, request):
        data = {
            "message": "hey!",
            "timestamp": int(time.time())
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
