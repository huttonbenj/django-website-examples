from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Kennel, Reservation
from django.core.exceptions import ValidationError

@receiver(pre_delete, sender=Reservation)
def unbook_kennel(sender, instance, **kwargs):
    instance.kennel.booked = False
    instance.kennel.save()

@receiver(pre_save, sender=Kennel)
def transfer_kennel(sender, instance, **kwargs):
    transfer_to = instance.transfer_kennel_to
    if transfer_to:
        to_kennel = Kennel.objects.get(number=transfer_to)
        if not to_kennel.booked:
            instance.booked = False
            res = Reservation.objects.get(kennel=instance.id)
            new_kennel = Kennel.objects.get(number=instance.transfer_kennel_to)
            res.kennel = new_kennel
            instance.transer_kennel_to = None
            res.save()
            new_kennel.booked = True
            instance.transfer_kennel_to = None

@receiver(pre_save, sender=Reservation)
def unbook_kennel_on_res_save(sender, instance, **kwargs):
    same_kennel = Reservation.objects.filter(kennel=instance.kennel)
    active_res = [s for s in same_kennel if not s.id == instance.id and s.status == 'active'] 
    if instance.status == 'upcoming' and not active_res:
        instance.kennel.booked = False
        instance.kennel.save()
    if instance.status == 'closed' and not active_res:
        instance.kennel.booked = False
        instance.kennel.save()
    if instance.status == 'active':
        if active_res:
            instance.kennel = Kennel.get_availabile()
        instance.kennel.booked = True
        instance.kennel.save()