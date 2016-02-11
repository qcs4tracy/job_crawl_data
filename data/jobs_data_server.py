import jobs_pb2
import pymongo
import conf
import time, datetime

mongodb_conf = conf.MONGO_DB
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class JobInfoServicer(jobs_pb2.BetaJobsServiceServicer):

    db_colletion = 'amz_jobs'
    default_limit = 20
    required_fields = [u'id_icims', u'title', u'location', u'timestamp',
                       u'description_short', u'feed_date', u'time_ago']

    def __init__(self):
        self.db_host = mongodb_conf.get('host', 'localhost')
        self.db_port = mongodb_conf.get('port', 27017)
        self.db_name = mongodb_conf.get('dbs')[0]
        self.client = pymongo.MongoClient(host=self.db_host, port=self.db_port)
        # self.db = self.client[self.db_name]
        self.db = self.client[self.db_name]
        self.jobs_dao = self.db[self.db_colletion]
        self._now = time.mktime(datetime.datetime.today().timetuple())


    def GetJobs(self, request, context):
        jobset = self.findRecentJobs(request.offset, request.resultLimit)
        for job in jobset:
            yield self._makeJob(job)

    def findRecentJobs(self, offset=0, limit=default_limit):
        return self.jobs_dao.find({}, sort=[('timestamp', pymongo.DESCENDING)], skip=offset,
                        limit=limit, projection=self.required_fields)

    def GetCount(self, request, context):
        cnt = self.jobs_dao.count()
        return jobs_pb2.Int(number=cnt)

    def close(self):
        # close the db connection
        self.client.close()

    def _makeJob(self, props):
        job = jobs_pb2.JobInfo()
        job.id_icims = props['id_icims']
        job.title = props['title']
        job.location = props['location']
        job.description_short = props['description_short']
        job.feed_date = props['feed_date']
        job.time_ago = self._time_ago(props['timestamp'])
        return job

    def _time_ago(self, timestamp):
        delta = datetime.timedelta(seconds=(self._now - timestamp))
        if delta.days > 0:
            return 'about %d days ago' % (delta.days,)
        _sec_per_hour = 60*60
        sec = delta.seconds
        hour = sec/_sec_per_hour
        if hour > 0:
            return 'about %d hours ago' % (hour, )
        mins = sec/60
        if mins > 0:
            return 'about %d minutes ago' % (mins, )
        return 'Just Posted'



def serve():
    server = jobs_pb2.beta_create_JobsService_server(JobInfoServicer())
    server.add_insecure_port('[::]:55001')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
  serve()