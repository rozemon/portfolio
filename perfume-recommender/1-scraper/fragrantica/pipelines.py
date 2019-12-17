# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FragranticaPipeline(object):
    def process_item(self, item, spider):
	for key in item:
		if (key == 'love') or (key == 'like') or (key == 'dislike') or (key == 'winter') or (key == 'spring') or (key == 'summer') or (key == 'autumn') or (key == 'day') or (key == 'night'):	
			a = item[key]
			b = a[a.find("height: ") + 8: a.find("px; background")]
			b = int(b)
			item[key] = b
		elif (key == 'lpoor') or (key == 'lweak') or (key == 'lmoderate') or (key == 'llong') or (key == 'lverylong') or (key == 'ssoft') or (key == 'smoderate') or (key == 'sheavy') or (key == 'senormous') or (key == 'votanti') :
			item[key] = int(item[key])
			 
	
	somma = (item['love'] + item['like'] + item['dislike']) / float(100)
	if (somma != 0):
		item['love'] = int(round(item['love'] / float(somma)))
		item['like'] = int(round(item['like'] / float(somma)))
		item['dislike'] = int(round(item['dislike'] / float(somma)))
	somma = (item['winter'] + item['spring'] + item['summer'] + item['autumn']) / float(100)	
	if (somma != 0):				
		item['winter'] = int(round(item['winter'] / float(somma)))
		item['spring'] = int(round(item['spring'] / float(somma)))
		item['summer'] = int(round(item['summer'] / float(somma)))
		item['autumn'] = int(round(item['autumn'] / float(somma)))       
	somma = (item['day'] + item['night']) / float(100)
	if (somma != 0):	
		item['day'] = int(round(item['day'] / float(somma)))
		item['night'] = int(round(item['night'] / float(somma)))
	somma = (item['lpoor'] + item['lweak'] + item['lmoderate'] + item['llong'] + item['lverylong']) / float(100)
	if (somma != 0):
		item['lpoor'] = int(round(item['lpoor'] / float(somma)))
		item['lweak'] = int(round(item['lweak'] / float(somma)))
		item['lmoderate'] = int(round(item['lmoderate'] / float(somma)))
		item['llong'] = int(round(item['llong'] / float(somma)))
		item['lverylong'] = int(round(item['lverylong'] / float(somma)))
	somma = (item['ssoft'] + item['smoderate'] + item['sheavy'] + item['senormous']) / float(100)
	if (somma != 0):
		item['ssoft'] = int(round(item['ssoft'] / float(somma)))
		item['smoderate'] = int(round(item['smoderate'] / float(somma)))
		item['sheavy'] = int(round(item['sheavy'] / float(somma)))
		item['senormous'] = int(round(item['senormous'] / float(somma)))

	return item
