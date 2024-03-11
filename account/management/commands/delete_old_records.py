from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from account.models import EmployeeDetails

class Command(BaseCommand):
    help = 'Deletes EmployeeDetails records older than 60 days'

    def handle(self, *args, **options):
        # Calculate the cutoff date (today - 60 days)
        cutoff_date = timezone.now() - timedelta(days=60)
        
        # Delete records older than the cutoff date
        deleted_count, _ = EmployeeDetails.objects.filter(task_date__lt=cutoff_date).delete()
        
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} old EmployeeDetails records'))