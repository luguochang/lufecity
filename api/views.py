from api import models
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from api.serializers.course import *
import uuid
def index(request):
    pass
def login(request):
    if request.method=='POST':
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        token=uuid.uuid4()
        obj=models.UserInfo.objects.filter(username=user,password=pwd).first()

        ret={'code':'','data':{

        }}
        if obj:
            models.Token.objects.filter(user=obj).update_or_create(token=token)
            ret['code']=1001
            ret['data']['token']=token
        else:
            ret['data']['error']='登陆失败'
            ret['code']=1000
        return Response(ret)

# class CourseModelView(ViewSetMixin,APIView):
#     def list(self,request,*args,**kwargs):




class CourseDetailModelView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        ret = {}
        try:

            course_list = models.Course.objects.all()
            course_detail = CourseModelSerializer(course_list, many=True)
            ret['code'] = 1001
            ret['data'] = course_detail.data
        except Exception as e:
            ret['code'] = 1000
            ret['error'] = e

        # Response['Access-Control-Allow-Origin']='*'
        return Response(ret)


    def retrieve(self,request,*args,**kwargs):
        ret = {}
        try:
            pk=kwargs.get('pk')
            course_obj = models.CourseDetail.objects.filter(course_id=pk).first()
            print(course_obj,pk)
            course_detail=CourseDetailModelSerializer(course_obj,many=False)
            ret['code']=1001
            ret['data']=course_detail.data
        except Exception as e:
            ret['code']=1000
            ret['error']=e

        return Response(ret)

