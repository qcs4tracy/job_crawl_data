# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AmzJob(scrapy.Item):
    """
    All the fields are listed below:

     business_category = scrapy.Field()
     team_category = scrapy.Field()
     description = scrapy.Field()
     title = scrapy.Field()
     basic_qualifications = scrapy.Field()
     feed_date = scrapy.Field()
     preferred_qualifications = scrapy.Field()
     url_next_step = scrapy.Field()
     company_name = scrapy.Field()
     id_icims = scrapy.Field()
     job_category = scrapy.Field()
     primary_search_label = scrapy.Field()
     description_short = scrapy.Field()
     time_ago = scrapy.Field()
     location = scrapy.Field()
    
    Notice: only 'id_icims' is of type `int`
    """
    business_category = scrapy.Field()

    team_category = scrapy.Field()

    description = scrapy.Field()

    title = scrapy.Field()

    basic_qualifications = scrapy.Field()

    feed_date = scrapy.Field()

    preferred_qualifications = scrapy.Field()

    url_next_step = scrapy.Field()

    company_name = scrapy.Field()

    id_icims = scrapy.Field()

    job_category = scrapy.Field()

    primary_search_label = scrapy.Field()

    description_short = scrapy.Field()

    time_ago = scrapy.Field()

    location = scrapy.Field()

    timestamp = scrapy.Field()