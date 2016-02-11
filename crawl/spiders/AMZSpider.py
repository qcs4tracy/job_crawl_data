import scrapy
import json
from ..items import AmzJob
import logging


class AMZSpider(scrapy.Spider):
    name = 'amazon.jobs'

    query_params = {
        'base_query': 'Software+Engineer',
        'offset': '0',
        'category[]': 'software-development',
        'location[]': 'seattle-wa'
    }

    default_headers = {
        '/User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'
    }

    batch_size = 10

    def __init__(self, *args, **kwargs):
        super(AMZSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.amazon.jobs/en/search']
        self._offset = 0
        self._nread = 0
        self._nhits = -1
        self._decoder = json.JSONDecoder()

    def make_requests_from_url(self, url):
        newurl = self._assemble_url(url)
        return scrapy.Request(newurl)

    def _assemble_url(self, url):
        query_param_str = []
        for k, v in self.query_params.iteritems():
            query_param_str.append('%s=%s' % (k, v))
        query_string = '&'.join(query_param_str)
        return '%s?%s' % (url, query_string)

    def parse(self, response):

        props = response.xpath('//div[@data-react-props and @data-react-class="SearchPage"]')
        jobs_info = self._decoder.decode(props.xpath('@data-react-props').extract()[0])

        if self._nhits < 0:
            self._nhits = jobs_info.get('hits', 0)
            self.log('Hits %d' % (self._nhits), logging.INFO)

        off = jobs_info.get('offset', -1)
        self._offset = self._offset + self.batch_size if off < 0 else off + jobs_info.get('resultLimit', self.batch_size)
        self.query_params['offset'] = self._offset
        jobs = jobs_info.get('jobs', [])

        self.log('Get %d records from request[ %s ]' % (len(jobs), response.url), logging.INFO)

        for job in jobs:
            item = AmzJob()
            for field, value in job.iteritems():
                item[field] = value
            yield item

        self._nread += len(jobs)
        self.log('%d records read..' % (self._nread,), logging.INFO)
        # there maybe more remaining records
        if len(jobs) > 0:
            yield self.make_requests_from_url(self.start_urls[0])
