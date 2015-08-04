from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.http import JsonResponse
import mistune

md = mistune.Markdown()

class IndexView( View ):
    template = 'blog/index.html'

    def get( self, request ):

        return render( request, self.template , request.context_dict )

class Create( View ):
    template = 'blog/create.html'

    def get( self, request ):
        if request.user.is_anonymous():
            return redirect( '/' )

        request.context_dict['form'] = PostForm()

        return render( request, self.template, request.context_dict )
    
    def post( self, request ):
        form = PostForm( request.POST )

        if form.is_valid():
            data = form.cleaned_data
            data['user_id'] = User.objects.get( id=request.user.id )
            data = Post.objects.create( **data )

            return redirect( 'post/{}'.format( data.slug ) )

        request.context_dict['form'] = form

        return render( request, self.template, request.context_dict )

class Edit( View ):
    template = 'blog/create.html'

    def get( self, request, id ):
        if request.user.is_anonymous():
            return redirect( '/' )

        request.context_dict['form'] = PostForm( instance=Post.objects.get( id=id ) )

        return render( request, self.template, request.context_dict )

    def post( self, request, id ):
        post = Post.objects.get( id=id )
        form = PostForm( request.POST, instance=post )

        if form.is_valid():
            post = form.save()

            return redirect( '/blog/post/{}'.format( post.slug ) )

        request.context_dict['form'] = form

        return render( request, self.template, request.context_dict )
        


class BlogDisplayView( View ):
    template = 'blog/display.html'
    
    def get( self, request, slug ):

        request.context_dict['post'] = Post.objects.get( slug=slug )
        request.context_dict['content'] = md( request.context_dict['post'].content )
        print( request.context_dict['content'] )
        return render( request, self.template, request.context_dict )

class APIget( View ):
    def get( self, request ):
        p = Post.objects.all()
        return JsonResponse( p[0].as_json() )

    def post( self, request ):
        return JsonResponse( request.json )

    def put( self, request ):
        return JsonResponse( request.json )

    def delete( self, request ):
        return JsonResponse( request.json )
