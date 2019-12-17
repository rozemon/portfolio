# -*- coding: utf-8 -*-

# Scrapy settings for fragrantica project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fragrantica'

SPIDER_MODULES = ['fragrantica.spiders']
NEWSPIDER_MODULE = 'fragrantica.spiders'
ITEM_PIPELINES = ['fragrantica.pipelines.FragranticaPipeline',]

ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Googlebot'



FEED_EXPORTERS = {
    'csv': 'fragrantica.my_project_csv_item_exporter.MyProjectCsvItemExporter',
}

CSV_DELIMITER = ";" 


ITEM_PIPELINES = {'fragrantica.pipelines.FragranticaPipeline': 1, 'scrapy.contrib.pipeline.images.ImagesPipeline': 10,}
IMAGES_STORE = '/home/rosario/fragrantica/Immagini'

