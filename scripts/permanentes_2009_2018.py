import os

import pandas as pd

DADOS_AGENDA_COMISSOES = 'data/ready/metadados_comissoes.csv'

CARACTERISTICAS_DADOS_TCC = {
    'ano': [ano for ano in range(2009, 2019)],
    'categoria_comissao': ['Comissão Permanente'],
    'categoria_evento': [
        'Audiência Pública com Convidado',
        'Audiência Pública com Ministro',
        'Debates',
        'Fórum',
        'Fórum de Debate',
        'Grupo de Trabalho',
        'Reunião Extraordinária',
        'Reunião Ordinária',
        'Reunião Técnica',
        'Palestra',
        'Seminário',
        'Simpósio'
    ]
}

eventos_alvo = pd.read_csv(DADOS_AGENDA_COMISSOES)
eventos_alvo['ano'] = eventos_alvo['data'].apply(lambda data: int(data[-4:]))

for coluna, valores in CARACTERISTICAS_DADOS_TCC.items():
    eventos_alvo = eventos_alvo[eventos_alvo[coluna].isin(valores)]

dados_tcc = pd.DataFrame(columns=['id_evento', 'categoria_evento', 'comissao',
                                  'ano', 'data', 'transcricao'])

for indice, evento in eventos_alvo.iterrows():
    id_evento = evento['id_evento'].replace('/', '-')

    arquivo_transcricao = f'''data/ready/{evento['ano']}/{id_evento}.csv'''

    if os.path.exists(arquivo_transcricao):
        dados_transcricao = pd.read_csv(arquivo_transcricao).fillna('')
        transcricao = dados_transcricao['transcricao']
        transcricao = ' | '.join(transcricao.values.tolist())

        dados_tcc = dados_tcc.append(
            {
                'id_evento': evento['id_evento'],
                'categoria_evento': evento['categoria_evento'],
                'comissao': evento['comissao'],
                'ano': evento['ano'],
                'data': evento['data'],
                'transcricao': transcricao
            },
            ignore_index=True
        )

dados_tcc.to_csv(
    'data/ready/transcricoes_comissoes_permanentes.csv',
    index=False
)
