from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import Item, Snapshot

@receiver(post_save, sender=Item)
def create_snapshot_on_create(sender, instance, created, **kwargs):
    if created:
        sanpshot = Snapshot(item=instance, estado=instance.estado, responsable=instance.responsable)
        sanpshot.save()

