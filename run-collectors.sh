#!/bin/bash

echo "Extraindo a agenda de comissões da Câmara dos Deputados..."
scrapy crawl coletor-eventos-comissoes -o data/raw/agenda_comissoes.csv
echo -e "Agenda de comissões da Câmara dos Deputados extraída! \n"

echo -e "Iniciando extração das transcrições de eventos da Câmara dos Deputados...\n"
for ano in `seq 1995 2020`
  do
    echo "Extraindo transcrições de ${ano}..."
    scrapy crawl coletor-discursos-comissoes -o data/raw/discursos_comissoes_${ano}.csv -a year=${ano}
  done

echo -e "\nTranscrições de eventos da Câmara dos Deputados extraídas! \n"

echo -e "Iniciando limpeza dos dados extraídos..."
python scripts/clean_data.py
echo -e "Limpeza dos dados extraídos concluída!"

exit
