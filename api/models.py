from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=16)

class Token(models.Model):
    user=models.OneToOneField(to='UserInfo',on_delete=models.CASCADE)
    token=models.CharField(max_length=128)


class Course(models.Model):
    title=models.CharField(max_length=32)
    course_img = models.CharField(verbose_name='课程图片', max_length=64)
    level_choices = (
        (1, '初级'),
        (2, '中级'),
        (3, '高级'),
    )
    level = models.IntegerField(verbose_name='课程难易程度', choices=level_choices, default=1)

    def __str__(self):
        return self.title
class CourseDetail(models.Model):
    course = models.OneToOneField(to='Course',on_delete=models.CASCADE)
    slogon = models.CharField(verbose_name='口号', max_length=255)
    why = models.CharField(verbose_name='为什么要学？', max_length=255)
    recommend_courses = models.ManyToManyField(verbose_name='推荐课程', to='Course', related_name='rc')

    def __str__(self):
        return "课程详细：" + self.course.title

class Chapter(models.Model):
    """
    章节
    """
    num =  models.IntegerField(verbose_name='章节')
    name = models.CharField(verbose_name='章节名称',max_length=32)
    course = models.ForeignKey(verbose_name='所属课程',to='Course',on_delete=models.CASCADE)

    def __str__(self):
        return self.name