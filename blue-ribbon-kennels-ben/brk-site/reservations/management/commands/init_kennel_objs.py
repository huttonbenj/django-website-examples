from django.core.management.base import BaseCommand
from reservations.models import Kennel, Reservation
import time, schedule, datetime, threading
from schedule import Scheduler

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        objs = Kennel.objects.all()
        if not objs and not len(objs) == 56:
            for i in range(1, 57):
                new_obj = Kennel(number=i)
                new_obj.save()