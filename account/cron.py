from django_cron import CronJobBase, Schedule
from account.management.commands.delete_old_records import Command as DeleteOldRecordsCommand

class DeleteOldRecordsCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # Run every day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'account.delete_old_records_cron_job'

    def do(self):
        # Call the management command to delete old records
        DeleteOldRecordsCommand().handle()