from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import PostArgsSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from common.CommonRes import create_res
from django.conf import settings

from .service import methodTestService

# Create your views here.
@swagger_auto_schema(
    method='get',
    operation_id='Get method test',
    operation_description='Get 메소드 테스트입니다.',
    query_serializer=PostArgsSerializer,
)
@swagger_auto_schema(
    method='post',
    operation_id='Post method test',
    operation_description='Post 메소드 테스트입니다.',
    request_body=PostArgsSerializer,
)
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def post_test(request):
    if request.method == 'GET':
        # Get 메소드 파라미터를 serializer로 변환
        serializer = PostArgsSerializer(data=request.query_params)
        
        # 공통 response 객체 생성
        res = create_res()

        if serializer.is_valid():
            res["result"] = serializer.initial_data
            param = serializer.initial_data

        else:
            res["code"] = "Error"
            res["result"] = "포맷이 적절하지 않습니다"

        # configs 객체 로드
        configs = getattr(settings, 'CONFIGS', None)
        print(configs)

        '''
          ####  Service 로직 ####
        '''
        # text값 중 문자 a를 숫자 1로, 문자 b를 숫자 2로 변환
        re_text = methodTestService.text_replace(param["text"])

        # text값 중 숫자 데이터 값을 합산 후, 문자는 앞에 숫자합은 뒤로 배치
        re_text = methodTestService.final_text(re_text)
        
        # Response result 값 세팅
        res["result"] = re_text

        return Response(res, status=status.HTTP_200_OK)



    elif request.method == 'POST':
        serializer = PostArgsSerializer(data=request.data)
        # print(serializer.initial_data)
        res = create_res()

        if serializer.is_valid():
            res["result"] = serializer.initial_data

            return Response(res, status=status.HTTP_200_OK)

        else:
            res["code"] = "Error"
            res["result"] = "포맷이 적절하지 않습니다"
            return Response(res, status=status.HTTP_200_OK)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

