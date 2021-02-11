import pandas as pd
from scrapy import Spider, Request

from collectors.loaders import CommitteeEventLoader
from collectors.utils.constants import (
    DEFAULT_START_YEAR,
    DEFAULT_FINAL_YEAR,
    DATE_PATTERN,
    COMMITTEES_SCHEDULE_URL,
    COMMITTEE_EVENT_SELECTORS
)

class CommitteeEventSpider(Spider):
    name = 'coletor-eventos-comissoes'
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['id_evento', 'categoria_evento', 'comissao',
                               'categoria_comissao', 'data', 'horario']
    }


    def __init__(self):
        start_date = f'{DEFAULT_START_YEAR}-01-01'
        end_date = f'{DEFAULT_FINAL_YEAR}-12-31'

        date_range = pd.date_range(start_date, end_date)
        self.dates = date_range.strftime(DATE_PATTERN).tolist()


    def start_requests(self):
        for date in self.dates:
            query = {'start_date': date, 'final_date': date}
            url = COMMITTEES_SCHEDULE_URL.format_map(query)

            yield Request(url=url, callback=self.parse)


    def parse(self, response):
        events = response.css('table tbody tr')

        if events:
            for event in events:
                loader = CommitteeEventLoader(selector=event)

                for field_name, selector in COMMITTEE_EVENT_SELECTORS.items():
                    loader.add_css(field_name=field_name, css=selector)

                yield loader.load_item()
