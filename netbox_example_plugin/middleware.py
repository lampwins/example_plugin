class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #print("after")
        return self.get_response(request)


class TestPrependMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #print("before")
        return self.get_response(request)
