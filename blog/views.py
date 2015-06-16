from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.models import User
from django.utils.text import slugify

class IndexView(View):
    template = 'blog/index.html'

    def get( self, request ):

        return render( request, self.template , request.context_dict )

class Create(View):
    template = 'blog/create.html'

    def get(self, request):
        if request.user.is_anonymous():
            return redirect( '/' )

        request.context_dict['form'] = PostForm()

        return render( request, self.template, request.context_dict )
    
    def post(self, request):
        form = PostForm( request.POST )

        if form.is_valid():
            data = form.cleaned_data
            data['user_id'] = User.objects.get( id=request.user.id )
            data['slug'] = slugify( request.POST['title'] )
            data = Post.objects.create( **data )

            return redirect( 'post/{}'.format( data.slug ) )

        request.context_dict['form'] = form

        return render( request, self.template, request.context_dict )

class Edit(View):
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
            form.save()
            # data = form.cleaned_data
            # data['user_id'] = User.objects.get( id=request.user.id )
            # data['slug'] = slugify( request.POST['title'] )
            # data = post.update( **data )

            return redirect( '/blog/post/{}'.format( slugify( form.cleaned_data['title'] ) ) )

        request.context_dict['form'] = form

        return render( request, self.template, request.context_dict )
        


class BlogDisplayView(View):
    template = 'blog/display.html'
    
    def get( self, request, slug ):
        request.context_dict['post'] = Post.objects.get( slug=slug )

        return render( request, self.template, request.context_dict )