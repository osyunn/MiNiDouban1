from django.db import models

# Create your models here.
from django.db import models
class Book(models.Model) :
    title = models.CharField(max_length=100,verbose_name="书名")
    description = models.TextField(verbose_name="书籍简介")
    image = models.ImageField(upload_to='movie/images/',verbose_name="书籍封面" )
    url = models.URLField(blank=True,verbose_name="电子书资源")

    class Meta:
        verbose_name = '读书'
        verbose_name_plural=verbose_name

