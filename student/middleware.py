from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    def __call__(self, request):
        # Log the request details
        print(f"Request Method: {request.method}, Request Path: {request.path}")
        # Call the next middleware or view
        response = self.get_response(request)
        return response

    def process_response(self, request, response):
        print(response)
        print("##############################")
        return response
        

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # Log the request details
        print(f"Request Method: {request.method}, Request Path: {request.path}")
        # Call the next middleware or view
        response = self.get_response(request)
        return response