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
            job_designation = response.css('p[class="MuiTypography-root jss55 MuiTypography-body2 MuiTypography-colorPrimary MuiTypography-noWrap"]::text').extract()
            job_experience = response.css('p[class="MuiTypography-root jss53 MuiTypography-body2"]::text').extract()
            job_salary = response.xpath("//div[@style='margin-right:15px' and @class='jss44']//text()").extract()
            job_info = response.css('p[class="MuiTypography-root jss53 MuiTypography-body2 MuiTypography-colorPrimary"]::text').extract()
            # job_type = response.xpath("//div[@style='margin-right: 25px;']//p//span//text()").extract()
            job_location = response.xpath("//ul//p[@class='MuiTypography-root MuiTypography-body2 MuiTypography-colorPrimary']/text()").extract()

            for j in range(len(job_title)):
                yield {
                "job_title" : job_title[j].strip(),
                "comapny_name" : company_name[j].strip(),
                "job_designation" : job_designation[j].strip(),
                "job_experience" : job_experience[j].strip(),
                "job_salary" : job_salary[j].strip(),
                "job_info" : job_info[j].strip(),
                # "job_type" : job_type[j].strip(),
                "job_location" : job_location[j].strip()  if j < len(job_location) else ''
            }   