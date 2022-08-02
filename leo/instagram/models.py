from django.db import models
from uuid  import uuid4
from django.utils import timezone

# Create your models here.
# python3 manage.py makemigrations instagram
# python3 manage.py migrate instagram

# def uuid_name_upload_to(instance,filename):
#         app_label=instance.__class__._meta.app_label # 앱 별로
#         cls_name= instance.__class__.__name__.lower() # 모델 별로
#         ymd_path = timezone.now().strftime('%Y/%m/%d')
#         uuid_name=uuid4().hex
#         extension= os.path.splitext(filename)[-1].lower()
#         return '/'.join([app_label,cls_name,ymd_path,uuid_name[:2],uuid_name+extension])

class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public= models.BooleanField(default=False,verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass



    # def __str__(self):
    #     # return f"Custom Post Object ({self.id})"
    #     return self.message

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description ="메세지 글자수"

