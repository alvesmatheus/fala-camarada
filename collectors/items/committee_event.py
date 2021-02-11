from scrapy import Item, Field

class CommitteeEventItem(Item):
    id_evento = Field()
    categoria_evento = Field()
    comissao = Field()
    categoria_comissao = Field()
    data = Field()
    horario = Field()
