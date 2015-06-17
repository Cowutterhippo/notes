import json as JSON

class json( object ):

    def process_request( self, request ):

        if( 'json' in request.META.get('CONTENT_TYPE') ):
            request.json = JSON.loads( request.body.decode('utf-8') )

    # may be used, please leave for refernace.
    # def process_response(self, request, response):

    #     if getattr(request, 'locale', False):
    #         response.cookies['locale'] = request.locale
