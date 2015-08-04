from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core import serializers

category_choices = (
	( 'news', 'news' ),
	( 'help', 'help'),
	( 'user', 'user'),
)

# Create your models here.
class Post( models.Model ):
	title = models.CharField( max_length=200, unique=True)
	content = models.TextField()
	slug = models.SlugField( max_length=200 )
	category = models.CharField( max_length=200, choices=category_choices )
	created_at = models.DateField( auto_now_add=True )
	updated_at = models.DateField( auto_now=True )
	user_id = models.ForeignKey( User )
	is_public = models.BooleanField( default=True )

	def save( self, *args, **kwargs ):
		self.slug = slugify( self.title )

		return super( Post, self ).save( *args, **kwargs )

	def as_json( self, *args, **kwargs ):

		return self.__dict__

class Comment( models.Model ):
	content = models.TextField()
	created_at = models.DateField( auto_now_add=True )
	updated_at = models.DateField( auto_now=True )
	post_id = models.ForeignKey( Post )
	user_id = models.ForeignKey( User )

class Like( models.Model ):
	user_id = models.ForeignKey( User )
	post_id = models.ForeignKey( Post )
	created_at = models.DateField( auto_now_add=True )
