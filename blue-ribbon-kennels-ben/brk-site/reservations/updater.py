from apscheduler.schedulers.background import BackgroundScheduler
from reservations.models import Reservation, Kennel
from django.db.models import Q
import datetime

def mark_unbooked():
    today = datetime.datetime.today()
    reservations = Reservation.objects.filter(Q(end_date__lte=today) | Q(end_date_additional__lte=today) | Q(pickup_date__lte=today))
    expire_today = [res for res in reservations if res.kennel.booked == True]
    if len(expire_today) > 0:
        for res in expire_today:
            res.kennel.booked = False
            res.kennel.save()
            res.status = 'closed'
            res.save()
    reservations_start = Reservation.objects.filter((Q(end_date__gte=today) | Q(end_date_additional__gte=today) | Q(pickup_date__gte=today)) & Q(start_date__lte=today))
    if len(reservations_start) > 0:
        for res in reservations_start:
            # this will fire the signal logic
            res.save()
    return 

def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(mark_unbooked, 'cron', day_of_week='mon-sun', hour=12)
    scheduler.add_job(mark_unbooked, 'interval', seconds=2)
    scheduler.start()

start()