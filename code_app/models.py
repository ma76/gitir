from django.contrib.auth.models import User
from django.db import models
# Define Upload-Path
from django.db.models import Q
from django.http import Http404


def get_upload_path(instance,filename):
    path = f"code/{instance.user.username}/{instance.repository}/{instance.project_name}/{filename}"
    return  path
# Create UserCode-Manager
class UserCodeManager(models.Manager):
    def get_userCode_by_qs(self,id,user,repository,project_name):
        try:
            lookup = (
                    Q(id__exact=id) &
                    Q(user__exact=user) &
                    Q(repository__exact=repository) &
                    Q(project_name__exact=project_name)
            )
            qs = self.get_queryset().get(lookup)
            if qs is not None:
                return qs
        except : #(KeyError, UserCode.DoesNotExist)
            raise Http404()

    def search(self, query):
        lookup = (
                Q(project_name__icontains=query) |
                Q(repository__icontains=query)
        )
        return self.get_queryset().filter(lookup).distinct()


# Create your models here.
class UserCode(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    project_name = models.CharField(max_length=150)
    repository = models.SlugField(max_length=200)
    # content = models.TextField()
    code_file = models.FileField(upload_to=get_upload_path,blank=True,null=True)
    objects = UserCodeManager()
    def get_absolute_url(self):
        return f"/codes/{self.id}/{self.user.username}/{self.repository}/{self.project_name}"