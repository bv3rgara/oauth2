from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from .serializers import ResourceSerializer
from oauth2_provider.decorators import protected_resource
from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider.models import Application
import random, string, base64, hashlib


class CodeView(APIView):

    def post(self, request, *args, **kwargs):
        app = Application.objects.filter(
            name=request.data.get("name_app", None)
        ).first()
        code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
        code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
        code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
        url = f'http://127.0.0.1:8000/oauth2/authorize/?response_type=code&code_challenge={code_challenge}&code_challenge_method=S256&client_id={app.client_id}&redirect_uri={app.redirect_uris}'
        return Response({'url': url, 'code_verifier': code_verifier})


@api_view(['GET'])
@protected_resource()
def def_resource(request):
    return Response(ResourceSerializer({'data': 'get data protegida'}).data)
