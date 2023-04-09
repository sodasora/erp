from django.db import models


# Create your models here.
# model
class Product(models.Model):
    code = models.CharField(max_length=256, null=False)
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256, null=False)
    price = models.CharField(max_length=256, null=False)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)
    """
    choices 매개변수는 Django 모델 필드에서 사용하는 매개변수 중 하나로 
    해당 필드에서 선택 가능한 옵션을 지정하는 역할을 합니다. 
    변수를 통해 튜플 리스트를 받으면 첫번째 요소는 실제 DB에 저장되는 값이 되고,
    두번째 요소는 사용자가 볼 수 있는 레이블(옵션의 이름)이 됩니다.
    """

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.id:  # 생성시 id가 없음 -> 생성동작
            # do create
            print()
        else:
            print()
    # do update
