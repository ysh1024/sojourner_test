class UserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # 사용자 에이전트 정보를 로깅 레코드에 추가
        setattr(request, 'http_user_agent', request.META.get('HTTP_USER_AGENT', '-'))

        return response