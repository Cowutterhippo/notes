from django.db import models
from django.contrib.auth.models import User

category_choices = (
	( 'news', 'news' ),
	( 'help', 'help'),
	( 'user', 'user'),
)

# Create your models here.
class Post( models.Model ):
	title = models.CharField( max_length=200, unique=True)
	content = models.TextField()
	slug = models.CharField( max_length=200 )
	category = models.CharField( max_length=200, choices=category_choices )
	created_at = models.DateField( auto_now_add=True )
	updated_at = models.DateField( auto_now=True )
	user_id = models.ForeignKey( User )
	is_public = models.BooleanField( default=True )

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