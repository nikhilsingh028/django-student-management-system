import time

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


class TimingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()

        response = self.get_response(request)

        end_time = time.time()

        total_time = end_time - start_time

        print(
            f"Request: {request.path} | "
            f"Time: {total_time:.4f} seconds"
        )

        return response


# process_view() Suppose you want to inspect which view Django is about to execute.    

class ViewInfoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        print("View is about to execute!")
        print("View function:", view_func.__name__)
        print("URL arguments:", view_kwargs)

        return None



from django.http import HttpResponse


class ExceptionLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):

        print("Exception occurred:", exception)

        return None    