import scrapy
import datetime
class Movies(scrapy.Spider):
    # The name of the scraper
    name = 'movies_data'
    # This var contains the list of the domains it can scrape
    allowed_domains = ['https://www.themoviedb.org']
    # The start page it wants to scrape Limited to 200 pages
    start_urls = [f'https://www.themoviedb.org/movie?language=en-US&page={x}'for x in range(1,200)]

    def parse(self,response):
        movie_title =  response.xpath("//div[@class='flex']/a/text()").extract()
        movie_desc  = response.css(".overview::text").extract()
        movie_link  =  response.xpath("//p[@class='view_more']/a[@class='result']/@href").extract()
        # Data in the hashmap form
        data = zip(movie_title,movie_desc,movie_link)
        
        for item in data:
            scraped_info = {
                    'time_stamp':datetime.datetime.now(),
                   # 'page':response.url,
                    'movie_title':item[0],
                    'movie_desc':item[1],
                    'movie_url':'https://www.themoviedb.org/'+item[2]
                    }
            yield scraped_info

