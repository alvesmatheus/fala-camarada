import os
import re

import pandas as pd

RAW_DATA_DIR_PATH = 'data/raw'
READY_DATA_DIR_PATH = 'data/ready'

RAW_COMMITTEE_SCHEDULE_PATH = 'data/raw/agenda_comissoes.csv'
READY_COMMITTEE_SCHEDULE_PATH = 'data/ready/metadados_transcricoes.csv'

TARGET_YEARS = [year for year in range(1995, 2022)]


def fix_committee_schedule():
    raw_committee_schedule = pd.read_csv(RAW_COMMITTEE_SCHEDULE_PATH)
    committee_schedule = raw_committee_schedule.drop_duplicates('id_evento')

    committee_schedule.replace(
        'AP c/ Convidado',
        'Audiência Pública com Convidado',
        inplace=True)

    committee_schedule.replace(
        'AP c/ Ministro',
        'Audiência Pública com Ministro',
        inplace=True)

    committee_schedule = committee_schedule.fillna({
        'categoria_comissao': 'Outros',
        'categoria_evento': 'Outros'
    })

    committee_schedule.to_csv(READY_COMMITTEE_SCHEDULE_PATH, index=False)


def fix_committee_speeches():
    for year in TARGET_YEARS:
        data_path = f'{RAW_DATA_DIR_PATH}/discursos_comissoes_{year}.csv'
        year_speeches = pd.read_csv(data_path)

        events = year_speeches['id_evento'].drop_duplicates().values.tolist()

        for event in events:
            speeches = year_speeches[year_speeches['id_evento'] == event]

            dir_path = f'{READY_DATA_DIR_PATH}/{year}'
            filename = f'''{str(event).replace('/', '-')}'''

            speeches.to_csv(f'{dir_path}/{filename}.csv', index=False)


def main():
    if not os.path.exists(READY_DATA_DIR_PATH):
        os.mkdir(READY_DATA_DIR_PATH)

    for year in TARGET_YEARS:
        path = f'{READY_DATA_DIR_PATH}/{year}'

        if not os.path.exists(path):
            os.mkdir(path)

    fix_committee_schedule()
    fix_committee_speeches()


if __name__ == '__main__':
    main()
