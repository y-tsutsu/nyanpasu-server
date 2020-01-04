from channels import Group
from django.http import HttpResponse


def publish(request):
    msg = request.GET.get('msg', 'null')
    Group('nyanpasu').send({'text': msg})

    return HttpResponse('Published!')
