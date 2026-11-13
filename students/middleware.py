class SimpleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Before the view executes
        print("Before View: Request received")

        response = self.get_response(request)

        # After the view executes
        print("After View: Response generated")

        return response

#Django initializes the middleware when it builds the middleware chain.
#get_response is the next middleware or the final Django request handler in the chain.   
#__call__()    his method runs when a request passes through your middleware.