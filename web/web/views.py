from django.contrib.auth.models import User
import subprocess
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

class InitData(APIView):

    def get(self, request, format=None):
        
        # restore database
        subprocess.run(["/usr/local/bin/python",
                            "/usr/src/app/manage.py", "truncate", "--apps", "auth"])
        subprocess.run(["/usr/local/bin/python", "/usr/src/app/manage.py",
                            "loaddata", "/usr/src/app/fixtures/auth-user.json"])
        return Response({'success': True})