# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class FragranticaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	nome = scrapy.Field()
	gruppo = scrapy.Field()
	love = scrapy.Field()
	like = scrapy.Field()
	dislike = scrapy.Field()
	winter = scrapy.Field()
	spring = scrapy.Field()
	summer = scrapy.Field()
	autumn = scrapy.Field()
	day = scrapy.Field()
	night = scrapy.Field()
	votanti = scrapy.Field()
	lpoor = scrapy.Field()
	lweak = scrapy.Field()
	lmoderate = scrapy.Field()
	llong = scrapy.Field()
	lverylong = scrapy.Field()
	ssoft = scrapy.Field()
	smoderate = scrapy.Field()
	sheavy = scrapy.Field()
	senormous = scrapy.Field()
	main_accords = scrapy.Field()
	top = scrapy.Field()
	middle = scrapy.Field()
	base = scrapy.Field()
	images = scrapy.Field()
	image_urls = scrapy.Field()
	
