import unidecode

def generate_html_links(year, month, file_names):

    html_links = ""
    base_url = "INSIRA-O-PADRÃO-DA-URL"

    for file in file_names:
        file_url = unidecode.unidecode(file).replace(' ', '-')
        link = f'<li><a href="{base_url}{year}/{month}/{file_url}.pdf">{file}</a></li>\n'
        html_links += link

    return html_links

# Como usar:
year = input("Digite o ano: ")
month = input("Digite o mês: ")
file_names_input = input("Digite os nomes dos arquivos, separados por vírgula: ")

file_names = [name.strip() for name in file_names_input.split(',')]

html_output = generate_html_links(year, month, file_names)
print(html_output)

pip install unidecode
