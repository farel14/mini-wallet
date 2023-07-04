import json
from django.http import HttpResponse
# from rest_framework.response import Response

class ResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    # def __call__(self, request):
    #     # Middleware logic before the view is called
    #     try:
    #         response = self.get_response(request)
    #         # Middleware logic after the view is called
    #         formatted_response = self.format_response(response)
    #         return formatted_response
    #     except Exception as e:
    #         # Handle the error and create an error response
    #         data = {
    #             'status': 'error',
    #             'message': str(e)  # Use the error message in the response
    #         }
    #         response = HttpResponse(json.dumps(data), content_type='application/json', status=500)
        
    #     return response

    def __call__(self, request):
        response = self.get_response(request)
        # Modify the response as needed
        wrapped_response = {
            'status': 'success',
            'data': response.content,
        }
        return HttpResponse(content=wrapped_response, status=response.status_code)
        # return HttpResponse(wrapped_response, status=response.status_code)
    

    def process_response(self, request, response):
        # Modify the response as needed
        wrapped_response = {
            'status': 'success',
            'data': response.content,
        }
        return wrapped_response

    def format_response(self, response):
        if response.status_code == 200 or response.status_code == 201:
            data = response.data
            formatted_data = {
                'status': 'success',
                'data': data
            }
            response.data = formatted_data
        return response
