from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class crawl(CrawlSpider):
    name ="spider"
    allowed_domains=["mausam.imd.gov.in","city.imd.gov.in"]
    start_urls=["https://mausam.imd.gov.in/responsive/departmentalweb.php"]
    rules= (
        # Follow all links within the domain
        Rule(LinkExtractor(allow=("mausam.imd.gov.in")), follow=True),
        # Extract and process only links containing "citywx/city_weather"
        Rule(LinkExtractor(allow=("citywx/city_weather",)), callback="weather"),
    )
    # to filter use a::text type ka kuch to get all links use getall()
    def weather(self,response):
        yield{
            "URL":response.url,
            "Place":response.xpath('//font/text()')[0].get(),
            "MaxTemp":response.xpath('//font/text()')[5].get().strip(),
            "MinTemp":response.xpath('//font/text()')[11].get().strip(),
            "Rainfall(mm)":response.xpath('//font/text()')[17].get().strip(),
            "Relative_Humidity(17:30)":response.xpath('//font/text()')[21].get().strip(),
            "Sunset":response.xpath('//font/text()')[23].get().strip(),
            "Sunrise":response.xpath('//font/text()')[25].get().strip(),
            "Moonset":response.xpath('//font/text()')[27].get().strip(),
            "Moonrise":response.xpath('//font/text()')[29].get().strip(),
            "Weather_Today":(response.xpath('//font/text()')[38].get()).strip(),
            "Day1":((response.xpath('//font/text()')[39].get()).strip()),
            "Weather_on_"+((response.xpath('//font/text()')[39].get()).strip()):(response.xpath('//font/text()')[42].get()).strip(),
            
            "Day2":((response.xpath('//font/text()')[43].get()).strip()),
            "Weather_on_"+((response.xpath('//font/text()')[43].get()).strip()):(response.xpath('//font/text()')[46].get()).strip(),
            
            "Day3":((response.xpath('//font/text()')[47].get()).strip()),
            "Weather_on_"+((response.xpath('//font/text()')[47].get()).strip()):(response.xpath('//font/text()')[50].get()).strip(),
            
            "Day4":((response.xpath('//font/text()')[51].get()).strip()),
            "Weather_on_"+((response.xpath('//font/text()')[51].get()).strip()):(response.xpath('//font/text()')[54].get()).strip(),
            
            "Day5":((response.xpath('//font/text()')[55].get()).strip()),
            "Weather_on_"+((response.xpath('//font/text()')[55].get()).strip()):(response.xpath('//font/text()')[58].get()).strip(),
            
            "Day6":((response.xpath('//font/text()')[59].get()).strip()),
            "Weather_on_"+((response.xpath('//font/text()')[59].get()).strip()):(response.xpath('//font/text()')[62].get()).strip(),
            
        }

print("crawled")