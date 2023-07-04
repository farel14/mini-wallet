from django.http import JsonResponse


def response_wrapper(data, status=200):
    response_data = {}
    if (status == 200) or (status == 201):
        response_data = {
            'status': 'success',
            'data': data
        }
    else:
        response_data = {
            "data": {
                "error": data
            },
            "status": "fail"
            }

    return JsonResponse(response_data, status=status)