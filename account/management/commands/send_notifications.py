from django.core.management.base import BaseCommand
from account.utils import create_notification_functions

class Command(BaseCommand):
    help = 'Send automatic notifications'

    def handle(self, *args, **options):
        create_notification_functions()
        self.stdout.write(self.style.SUCCESS('Notifications sent successfully'))