from scrapy import cmdline


cmdline.execute('scrapy crawl BetterDays_spider -o BetterDays.csv'.split())
