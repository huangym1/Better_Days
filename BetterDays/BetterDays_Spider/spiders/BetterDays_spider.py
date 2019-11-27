# -*- coding: utf-8 -*-
import scrapy
from BetterDays.BetterDays_Spider.items import BetterdaysItem
import json
import datetime


class BetterdaysSpiderSpider(scrapy.Spider):
	name = 'BetterDays_spider'
	allowed_domains = ['m.maoyan.com']
	# current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	current_time = "2019-10-28 18:46:27"
	end_time = "2019-10-25 09:00:00" #上映时间
	start_urls = ["http://m.maoyan.com/mmdb/comments/movie/1218029.json?_v_=yes&offset=0&startTime={}".format(current_time)]

	def parse(self, response):
		response = json.loads(response.text)
		cmts = response['cmts']
		hcmts = response['hcmts'] # 热门评论
		count = 0 # 每一个json一共有15条评论，拿到最后一条评论的时间减去1，作为下一个URL的startTime
		item = BetterdaysItem()
		for cmt in cmts:
			try:
				item['id'] = cmt['userId']
				item['nickname'] = cmt['nickName']
				item['cityname'] = cmt['cityName'] if 'cityName' in cmt.keys() else None
				item['content'] = cmt['content'] if 'cityName' in cmt.keys() else None
				item['gender'] = cmt['gender'] if 'gender' in cmt.keys() else 0
				item['score'] = cmt['score'] if 'cityName' in cmt.keys() else None
				item['approve'] = cmt['approve'] if 'cityName' in cmt.keys() else None
				item['time'] = cmt['startTime'] if 'cityName' in cmt.keys() else None
				yield item
				count += 1
				if count >= 15:
					last_comment_time = item['time']
					current_t = datetime.datetime.strptime(last_comment_time,"%Y-%m-%d %H:%M:%S") - datetime.timedelta(seconds=1)
					if str(current_t) >= self.end_time:
						url = "http://m.maoyan.com/mmdb/comments/movie/1218029.json?_v_=yes&offset=0&startTime={}".format(current_t)
						yield scrapy.Request(url,callback=self.parse,meta={"item":item})
					else:
						print("信息已全部搜集完成！")
			except Exception as e:
				print("信息提取错误 "+str(e))