# Fala Camarada

Reunindo tudo o que se fala na Câmara dos Deputados.

## Como executar

> :small_red_triangle_down: Esse tutorial assume que você possui a linguagem **[Python 3.0+](https://www.python.org/download/releases/3.0/)** instalada em sua máquina, bem como as bibliotecas **[Scrapy](https://scrapy.org/)**, **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** e **[Pandas](https://pandas.pydata.org/)**.

Inicialmente, clone esse repositório.

```sh
$ git clone https://github.com/alvesmatheus/fala-camarada.git
```

Acesse o diretório do repositório clonado.

```sh
$ cd fala-camarada
```
A seguir, antes de obter os discursos das comissões da Câmara dos Deputados, você precisará extrair a agenda de eventos destas comissões. Para isso, execute o comando a seguir.

```sh
$ scrapy crawl coletor-eventos-comissoes -o data/raw/agenda_comissoes.csv
```

Com a agenda de eventos das comissões já extraída, substitua a variável **`ano`** no comando abaixo por um valor entre **`1995`** e **`2020`** (inclusos) e execute-o. Os dados extraídos estarão disponíveis no diretório **`fala-camarada/data/raw/`**.

> ###### :heavy_exclamation_mark: Alterações no código-fonte podem ser necessárias para extração de discursos de outros anos.

 ```sh
 $ scrapy crawl coletor-discursos-comissoes -o data/raw/discursos_comissoes_<ano>.csv -a year=<ano>
 ```

**[Opcional]** Quando a extração dos discursos de comissões for concluída para todos os anos de seu interesse, execute o *script* de limpeza de dados disponibilizado. Os dados produzidos estarão disponíveis no diretório **`fala-camarada/data/ready/`**.

 ```sh
 $ python scripts/clean_data.py 
 ```

**[Opcional]** O *script* `run-collectors.sh` pode ser utilizado para executar, sequencialmente, todos os coletores referentes ao período supracitado e, em seguida, a limpeza dos dados extraídos. 
