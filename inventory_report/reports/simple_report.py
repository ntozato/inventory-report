from datetime import date
from collections import Counter

# lista_teste = [
#   {
#     "id": "1",
#     "nome_do_produto": "Nicotine Polacrilex",
#     "nome_da_empresa": "Target Corporation",
#     "data_de_fabricacao": "2020-02-18",
#     "data_de_validade": "2022-09-17",
#     "numero_de_serie": "CR25 1551 4467 2549 4402 1",
#     "instrucoes_de_armazenamento": "instrucao 1"
#   },
#   {
#     "id": "2",
#     "nome_do_produto": "fentanyl citrate",
#     "nome_da_empresa": "Target Corporation",
#     "data_de_fabricacao": "2019-12-06",
#     "data_de_validade": "2022-12-25",
#     "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
#     "instrucoes_de_armazenamento": "instrucao 2"
#   },
#   {
#     "id": "3",
#     "nome_do_produto": "NITROUS OXIDE",
#     "nome_da_empresa": "Galena Biopharma",
#     "data_de_fabricacao": "2019-12-22",
#     "data_de_validade": "2023-11-07",
#     "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
#     "instrucoes_de_armazenamento": "instrucao 3"
#   }
# ]


class SimpleReport:
    def data_de_fabricacao_mais_antiga(data):
        dates = []

        for product in data:
            dates.append(product["data_de_fabricacao"])

        return min(dates)

    def data_de_validade_mais_proxima(data):
        data_atual = str(date.today())
        dates = []

        for product in data:
            if product["data_de_validade"] >= data_atual:
                dates.append(product["data_de_validade"])

        return min(dates)

    # https://qastack.com.br/programming/2600191/how-can-i-count-the-occurrences-of-a-list-item
    def empresa_maior_estoque(data):
        companies = []

        for product in data:
            companies.append(product["nome_da_empresa"])

        count = Counter(companies)

        return max(count)

    @classmethod
    def generate(cls, data):
        data_fabricacao = cls.data_de_fabricacao_mais_antiga(data)
        data_validade = cls.data_de_validade_mais_proxima(data)
        estoque = cls.empresa_maior_estoque(data)

        fabricacao = f"Data de fabricação mais antiga: {data_fabricacao}"
        validade = f"Data de validade mais próxima: {data_validade}"
        emp = f"Empresa com maior quantidade de produtos estocados: {estoque}"

        return f"{fabricacao}\n{validade}\n{emp}\n"


# print(SimpleReport.generate(lista_teste))
