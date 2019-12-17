from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from fragrantica.items import FragranticaItem

class FragranticaSpider(CrawlSpider):
	name = 'fragrantica'
	start_urls = ['http://www.fragrantica.com'] 
	allowed_domains = ["fragrantica.com", "fimgs.net"]
    	rules = (Rule(LxmlLinkExtractor(), callback = 'parse_profumo', follow = True),)
    		
	def parse_profumo(self, response):
		hxs = Selector(response)
		item = FragranticaItem()
		checknome = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/h1/span')
		if (checknome):		
			item['nome'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/h1/span')[0].xpath('text()').extract()[0]
			checkgruppo = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/p/span[2]/span[1]').xpath('text()').extract()
			if (checkgruppo):
				item['gruppo'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/p/span[2]/span[1]').xpath('text()').extract()[0]
			else:
				item['gruppo'] = "Sconosciuto"
			item['love'] = response.xpath('//*[@id="clsloveD"]/@style').extract()[0]
			item['like'] = response.xpath('//*[@id="clslikeD"]/@style').extract()[0]
			item['dislike'] = response.xpath('//*[@id="clsdislikeD"]/@style').extract()[0]
			item['winter'] = response.xpath('//*[@id="clswinterD"]/@style').extract()[0]
			item['spring'] = response.xpath('//*[@id="clsspringD"]/@style').extract()[0]
			item['summer'] = response.xpath('//*[@id="clssummerD"]/@style').extract()[0]
			item['autumn'] = response.xpath('//*[@id="clsautumnD"]/@style').extract()[0]
			item['day'] = response.xpath('//*[@id="clsdayD"]/@style').extract()[0]
			item['night'] = response.xpath('//*[@id="clsnightD"]/@style').extract()[0]
			item['votanti'] = response.xpath('//*[@id="peopleD"]/text()').extract()[0]
			item['lpoor'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[7]/div[1]/div/table/tr[1]/td[2]/text()').extract()[0]
			item['lweak'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[7]/div[1]/div/table/tr[2]/td[2]/text()').extract()[0]
			item['lmoderate'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[7]/div[1]/div/table/tr[3]/td[2]/text()').extract()[0]
			item['llong'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[7]/div[1]/div/table/tr[4]/td[2]/text()').extract()[0]
			item['lverylong'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[7]/div[1]/div/table/tr[5]/td[2]/text()').extract()[0]
			item['ssoft'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[7]/div[2]/table/tr/td/table/tr[1]/td[2]/text()').extract()[0]
			item['smoderate'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[7]/div[2]/table/tr/td/table/tr[2]/td[2]/text()').extract()[0]
			item['sheavy'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[7]/div[2]/table/tr/td/table/tr[3]/td[2]/text()').extract()[0]
			item['senormous'] = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[7]/div[2]/table/tr/td/table/tr[4]/td[2]/text()').extract()[0]
			notatop = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/div/div/div[6]/div[1]/p[1]')
			item['top'] = []
			for span in notatop:
				item['top'] = notatop.xpath('span/img/@alt').extract()
			notamiddle = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/div/div/div[6]/div[1]/p[2]')
			item['middle'] = []
			for span in notamiddle:
				item['middle'] = notamiddle.xpath('span/img/@alt').extract()
			notabase = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/div/div/div[6]/div[1]/p[3]')
			item['base'] = []
			for span in notabase:
				item['base'] = notabase.xpath('span/img/@alt').extract()
			accordi = response.xpath('/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[1]')
			item['main_accords'] = []
			if (accordi.xpath('div/span/text()').extract() != "" ):
				for span in accordi:
					item['main_accords'] = accordi.xpath('div/span/text()').extract()
				item['main_accords'].pop(0)
			item['image_urls'] = response.xpath('//*[@id="mainpicbox"]/img/@src').extract()
		
		return item
