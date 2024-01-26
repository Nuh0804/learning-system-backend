from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=StudentCourse)
@receiver(post_delete, sender=StudentCourse)
def update_course_enrollment_count(sender, instance, **kwargs):
    if kwargs['created']:
        course = instance.course
        students_enrolled = StudentCourse.objects.filter(course = course.id).count()
        course.students_enroled= students_enrolled
        course.save()