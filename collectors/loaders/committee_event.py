from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

from collectors.items import CommitteeEventItem
from collectors.utils.processors import (
    apply_time_pattern,
    fix_committee_names,
    get_committee_category,
    remove_escape_chars,
    remove_excessive_whitespaces
)

class CommitteeEventLoader(ItemLoader):
    default_item_class = CommitteeEventItem
    default_output_processor = TakeFirst()

    id_evento_in = MapCompose(str.strip)

    categoria_evento_in = MapCompose(str.strip)

    comissao_in = MapCompose(fix_committee_names, str.strip)

    categoria_comissao_in = MapCompose(
        fix_committee_names, get_committee_category, str.strip
    )

    data_in = MapCompose(str.strip)

    horario_in = MapCompose(
        remove_escape_chars, remove_excessive_whitespaces, str.strip,
        apply_time_pattern
    )
