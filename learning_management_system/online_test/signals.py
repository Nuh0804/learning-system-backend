from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Result, Answer

@receiver(post_save, sender = Answer)
def create_result_for_test_done_by_user(sender, **kwargs):
    if kwargs['created']:
        Result.objects.create(user = kwargs['instance'])