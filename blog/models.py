from django.db import models
from datetime import date
from django.utils.text import slugify
# Create your models here.

#BlogModel, AuthorModel

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"
class AuthorModel(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length = 100)
    email = models.EmailField(null=True)
    def full_name(self):
        return f"{self.fname} {self.lname}"
    def __str__(self):
        return self.full_name()
    
    class Meta:
        verbose_name_plural = "Authors"

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False,db_index=True)
    excerpt = models.CharField(max_length=250)
    image_url = models.ImageField(upload_to="blog_images", null=True)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE,related_name="blogs")
    updated_at = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title}, {self.author}, {self.updated_at}"
    
    class Meta:
        verbose_name_plural = "Blogs"

class CommentModel(models.Model):
    commentor_name = models.CharField(max_length=150)
    commentor_email = models.EmailField()
    comment_text = models.TextField(max_length=1000)
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE,related_name="comments")