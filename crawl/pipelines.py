# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from utils.date import timestr_timestamp, timestamp_days_ago

# collect items into mongodb
class MongoPipeline(object):
    collection_name = 'amz_jobs'
    default_port = 27017
    default_db = 'jobs'

    def __init__(self, host, port=default_port, db=default_db):
        self.db_host = host
        self.db_port = port
        self.db_name = db
        self.mongo_client = None

    @classmethod
    def from_crawler(cls, crawler):
        db_settings = crawler.settings.get('MONGO_DB')
        return cls(
                host=db_settings.get('host', 'localhost'),
                port=db_settings.get('port', cls.default_port),
                db=db_settings.get('dbs', [cls.default_db])[0]
        )

    def open_spider(self, spider):
        self.mongo_client = pymongo.MongoClient(self.db_host, self.db_port)
        self.db = self.mongo_client[self.db_name]

    def close_spider(self, spider):
        self.mongo_client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item


# filter by jobid, no duplicates
class DuplicateFilterPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        id = item.get('id_icims', 0)
        if id in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(id)
            return item


# a filter pipeline to get rid of old records
class OldFilterPipeline(object):

    default_days = 10

    def __init__(self, indays):
        self.within = indays
        self.threshold = timestamp_days_ago(indays)

    @classmethod
    def from_crawler(cls, crawler):
        days = crawler.settings.get('WITHIN_DAYS', cls.default_days)
        return cls(indays=days)

    def process_item(self, item, spider):
        timestamp = timestr_timestamp(item['feed_date'])
        if timestamp < self.threshold:
            raise DropItem("Old record: [id: %i , feed_date: %s]" % (item['id_icims'], item['feed_date']))
        item['timestamp'] = timestamp
        return item

