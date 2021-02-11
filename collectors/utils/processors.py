import re

from collectors.utils.constants import (
    COMMITTEE_CATEGORY_PATTERNS,
    DOUBT_NOTATION_PATTERN,
    PERMANENT_COMMITTEE_NAMES,
    TRANSCRIPTION_NOTATION_PATTERN,
    WRONG_COMMITTEE_NAMES
)


def apply_time_pattern(time):
    return time.replace('*', '').replace('h', ':')


def fix_committee_names(committee_name):
    for mistake, committee_id in WRONG_COMMITTEE_NAMES.items():
        if committee_name == mistake:
            return PERMANENT_COMMITTEE_NAMES[committee_id]

    return committee_name


def fix_parenthesis(text):
    return text.replace('( ', '(').replace(' )', ')')


def get_committee_category(committee_name):
    if committee_name in PERMANENT_COMMITTEE_NAMES.values():
        return 'Comissão Permanente'

    for pattern, category in COMMITTEE_CATEGORY_PATTERNS.items():
        if pattern in committee_name:
            return category

    return 'Outros'


def remove_doubt_notation(text):
    return re.sub(DOUBT_NOTATION_PATTERN, ' ', text)


def remove_escape_chars(text):
    for escape_char in ['\r', '\t', '\n']:
        text = text.replace(escape_char, ' ')

    return text


def remove_excessive_whitespaces(text):
    return ' '.join(text.split())


def remove_transcription_notations(text):
    return re.sub(TRANSCRIPTION_NOTATION_PATTERN, ' ', text)
