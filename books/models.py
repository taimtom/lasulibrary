from django.db.models import Q
from django.db import models

class BookQuerySet(models.QuerySet):
	def search(self,query=None):
		qs=self
		if query is not None:
			look_up=(Q(title__icontains=query)|
                    Q(isbn__icontains=query)|
                    Q(author__icontains=query)|
                    Q(published_date__icontains=query)|
					Q(classification__iexact=query))

			qs=qs.filter(look_up).distinct()
		return qs

class BookManager(models.Manager):
	def get_queryset(self):
		return BookQuerySet(self.model, using=self._db)

	def search(self,query=None):
		return self.get_queryset().search(query)
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    classification=models.CharField(max_length=10)
    isbn=models.IntegerField()
    image=models.FileField(upload_to="document/image")
    document=models.FileField(upload_to="document")
    published_date=models.DateField()
    slug=models.SlugField()
    
    objects=BookManager()


    def __str__(self):
        return self.title