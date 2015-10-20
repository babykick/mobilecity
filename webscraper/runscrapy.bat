Rem scrapy crawl meituan_spider
Rem scrapy crawl project_spider
scrapy crawl douban_spider -a keyword="图书"
scrapy crawl dianping_spider -t jsonlines -o data/dianping.jsonl