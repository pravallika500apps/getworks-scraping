import scrapy

class GetworkSpider(scrapy.Spider):
    name = "getwork"
    allowed_domains = ["getwork.org"]
    start_urls = ["https://www.getwork.org/full-time-jobs"]

    custom_settings = {
    'FEED_FORMAT': 'json',
    'FEED_URI': 'data.json'
}
    def parse(self, response):
            job_title = response.css('h5[class="MuiTypography-root jss49 textOverflow MuiTypography-h5 MuiTypography-colorPrimary"]::text').extract()
            company_name = response.css('p[class="MuiTypography-root jss49 textOverflow MuiTypography-body1 MuiTypography-colorPrimary"]::text').extract()
            # job_loctaion = response.css('div[class="jss52"]::text"]').extract()
            for j in range(len(job_title)):
                yield {
                "job_title" : job_title[j].strip(),
                "comapny_name" : company_name[j].strip()
                # "job_location" : job_loctaion[j].strip()
            }