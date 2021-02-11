import re

import pandas as pd
from scrapy import Spider, Request
from bs4 import BeautifulSoup

from collectors.loaders import CommitteeSpeechLoader
from collectors.utils.constants import (
    COMMITTEES_SCHEDULE_PATH,
    SPEECH_SPEAKER_PATTERN,
    COMMITTEE_SPEECH_URL
)

class CommitteeSpeechSpider(Spider):
    name = 'coletor-discursos-comissoes'
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['id_evento', 'ordem_discurso', 'orador',
                               'transcricao']
    }


    def __init__(self, year=None):
        events = pd.read_csv(COMMITTEES_SCHEDULE_PATH)

        if year:
            events = events[events['data'].str.contains(year)]

        event_ids = events['id_evento'].drop_duplicates().values.tolist()
        self.event_ids = event_ids


    def start_requests(self):
        for event_id in self.event_ids:
            query = {'event_id': event_id}
            url = COMMITTEE_SPEECH_URL.format_map(query)

            yield Request(url=url, callback=self.parse, meta=query)


    def parse(self, response):
        body = response.css('body').get()
        speeches = BeautifulSoup(body, 'html.parser').get_text()
        sections = re.split(SPEECH_SPEAKER_PATTERN, speeches)[1:]

        if sections:
            section_order = range(0, len(sections), 2)
            event_id = response.meta['event_id']

            for order in section_order:
                loader = CommitteeSpeechLoader()

                loader.add_value('id_evento', event_id)
                loader.add_value('ordem_discurso', (order // 2) + 1)
                loader.add_value('orador', sections[order])
                loader.add_value('transcricao', sections[order + 1])

                yield loader.load_item()
