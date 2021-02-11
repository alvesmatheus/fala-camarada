from scrapy import Item, Field

class CommitteeSpeechItem(Item):
    id_evento = Field()
    ordem_discurso = Field()
    orador = Field()
    transcricao = Field()
