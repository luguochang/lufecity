from api import models
from rest_framework import serializers

class CourseModelSerializer(serializers.ModelSerializer):
    level=serializers.CharField(source='get_level_display')
    class Meta:
        model=models.Course
        fields='__all__'



class CourseDetailModelSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='course.title')
    course_img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')
    chapter=serializers.SerializerMethodField()
    recommend = serializers.SerializerMethodField()
    class Meta:
        model = models.CourseDetail
        fields = ['title','course_img','level','why','recommend','chapter']

    def get_chapter(self,obj):
        queryset=obj.course.chapter_set.all()
        return [{'num':row.num,'name':row.name } for row in queryset]

    def get_recommend(self,obj):
        queryset=obj.recommend_courses.all()
        return [{'id':row.id,'title':row.title} for row in queryset]



