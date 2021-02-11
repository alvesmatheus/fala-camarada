from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

from collectors.items import CommitteeSpeechItem
from collectors.utils.processors import (
    fix_parenthesis,
    remove_doubt_notation,
    remove_escape_chars,
    remove_excessive_whitespaces,
    remove_transcription_notations,
)

class CommitteeSpeechLoader(ItemLoader):
    default_item_class = CommitteeSpeechItem
    default_output_processor = TakeFirst()

    orador_in = MapCompose(
        remove_escape_chars, remove_doubt_notation,
        remove_excessive_whitespaces, fix_parenthesis, str.strip
    )

    transcricao_in = MapCompose(
        remove_escape_chars, remove_doubt_notation,
        remove_transcription_notations, remove_excessive_whitespaces,
        fix_parenthesis, str.strip
    )
