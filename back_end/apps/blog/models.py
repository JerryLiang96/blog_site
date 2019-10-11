from django.db import models
from django.contrib.auth.models import User

# blog的分类表


class Category(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# blog的标签表


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# blog的图片表


class Image(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(
        upload_to='image/', blank=True)

    def __str__(self):
        return self.name

# blog表


class Blog(models.Model):

    # blog标题
    title = models.CharField(max_length=70)
    # blog正文
    body = models.TextField()
    # blog创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # blog摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类 Category与blog一对多关联
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    # 标签 tag与blog多对多关联
    tag = models.ManyToManyField(Tag, blank=True)
    # 图片 image与blog多对多关联
    image = models.ManyToManyField(Image, blank=True)
    # 作者 author与blog一对多关联
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return('{}:{}'.format(self.category, self.title))
