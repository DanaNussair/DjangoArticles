from activity_logs.models import ActivityLog
from activity_logs.serializers import ActivityLogSerializer

class ActivityLogCommands():
  def create_activity_log(self, args={}):
    try:
      serializer = ActivityLogSerializer(data=args)
      if serializer.is_valid():
        serializer.save()
        return {'data': serializer.data}
      else:
        print('errors: ', serializer.errors)
        return {'error': 'Can not create activity log'}
    except Exception as err:
      print('Error occurred in create_activity_log: ', err)
      return {'error': 'Can not create activity log'} 