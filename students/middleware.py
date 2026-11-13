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