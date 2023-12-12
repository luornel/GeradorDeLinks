# Gerador de Links HTML para Arquivos PDF

## Sobre o Algoritmo

Este algoritmo foi desenvolvido para facilitar a geração de links HTML para arquivos PDF armazenados na biblioteca de mídia do WordPress do Portal TJRS. Ele permite ao usuário inserir um ano, um mês e uma lista de nomes de arquivos, visando formatar corretamente o diretório, e em seguida, o algoritmo gera automaticamente uma lista de links HTML, prontos para serem usados em websites ou em documentos HTML.

Os links são formatados para apontar para os arquivos PDF localizados na URL padrão do Portal, seguidos pelo ano e mês especificados, e pelo nome do arquivo. A ferramenta também ajusta os nomes dos arquivos para o formato de URL, removendo acentos e substituindo espaços por hífens.

## Como Usar

Instalação: Certifique-se de que Python está instalado em seu sistema. Este script foi testado com Python 3.8+. Além disso, instale a biblioteca unidecode utilizando o comando `pip install unidecode`.

Execução: Execute o script em um ambiente Python que suporte GUI, como Python IDLE, PyCharm ou diretamente no terminal (caso esteja usando um sistema operacional com interface gráfica).

Entrada de Dados: Quando o programa for iniciado, insira o ano, o mês e os nomes dos arquivos conforme solicitado. Os nomes dos arquivos devem ser separados por vírgulas.

Geração dos Links: Após a inserção dos dados, o programa irá gerar a lista de links HTML. Estes links podem ser copiados e usados conforme necessário.

## Requisitos

Python 3.8 ou superior.
Biblioteca unidecode instalada.

## Limitações

O algoritmo foi projetado especificamente para o formato de URL e estrutura de pastas do site www.tjrs.jus.br. Modificações podem ser necessárias para adaptá-lo a diferentes estruturas de URLs ou requisitos de formatação.

## Resultado

O script irá gerar e imprimir a tabela HTML correspondente às entradas fornecidas.

Exemplo resultado:
```
Digite o ano: 2023
Digite o mês: 12
Digite os nomes dos arquivos, separados por vírgula: Alpha, Beta, Charlie, Delta

<li><a href="//www.tjrs.jus.br/static/2023/12/Alpha.pdf">Alpha</a></li>
<li><a href="//www.tjrs.jus.br/static/2023/12/Beta.pdf">Beta</a></li>
<li><a href="//www.tjrs.jus.br/static/2023/12/Charlie.pdf">Charlie</a></li>
<li><a href="//www.tjrs.jus.br/static/2023/12/Delta.pdf">Delta</a></li>
```
