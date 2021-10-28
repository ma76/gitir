from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.views.generic import ListView
from code_app.form import UserCodeForm
from code_app.models import UserCode

### Define Main Function ###
def readFile(path):
    with open(path, encoding ='utf-8') as f:
        lines = "".join(f.readlines())
        f.close()
        return lines

# Define code-List
class UserCodeList(ListView):
    template_name = 'list_codes.html'
    paginate_by = 6
    def get_queryset(self):
        return UserCode.objects.all().order_by('-id')


#Define Code-Detail
def UserCodeShower(request,*args,**kwargs):
    user_code_id = kwargs.get('pk')
    user_name =kwargs.get('user_name')
    repository =kwargs.get('repository')
    project_name =kwargs.get('project_name')
    # print(project_name)
    user_object = User.objects.get(username=user_name)
    user_code= UserCode.objects.get_userCode_by_qs(
        id=user_code_id,
        user=user_object,
        repository=repository,
        project_name=project_name
    )
    user_code_content = user_code.code_file
    try:
        # print(readFile(user_code_content.path))
        context = {
            'content': mark_safe(json.dumps(readFile(user_code_content.path))),
            'code':user_code
        }
        return render(request, 'code-detail.html', context=context)
    except :
        raise Http404()

#Define Upload-Form
@login_required(login_url='/login')
def UploadForm(request):
    user_code_form = UserCodeForm(request.POST or None,request.FILES or None)
    if user_code_form.is_valid():
        user_form_id = User.objects.get(id = request.user.id)
        project_name_form = user_code_form.cleaned_data.get('project_name')
        repository_form = user_code_form.cleaned_data.get('repository')
        file_form = request.FILES['file']
        UserCode.objects.create(user=user_form_id,project_name = project_name_form,repository=repository_form,
                                code_file=file_form)
        return redirect('/code')
    context = {
        'form': user_code_form
    }
    return render(request, 'upload-form.html', context = context)


# Define MyCode
# @login_required(login_url='/login')
class MyCode(LoginRequiredMixin,ListView):
    template_name = 'mycode.html'
    paginate_by = 6

    def get_queryset(self):
        # pk = self.kwargs.get('pk')
        request = self.request
        print(request.user.id)
        return UserCode.objects.filter(user__id=request.user.id)


# Define Search-operator
class Search(ListView):
    template_name = 'list_codes.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        # print(request.GET)
        query = request.GET.get('text')
        # print(query)
        if query is not None:
            return UserCode.objects.search(query)