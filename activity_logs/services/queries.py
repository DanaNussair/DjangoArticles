from activity_logs.models import ActivityLog
from activity_logs.serializers import ActivityLogSerializer

class ActivityLogQueries():
  def get_activities(self, args):
    return ActivityLog.objects.filter(**args)