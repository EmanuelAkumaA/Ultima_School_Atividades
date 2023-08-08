import requests

# Classe iteradora que percorre os modelos de carros de uma marca usando a API da FIPE
class ApiFipeIterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelos = self.get_modelos()

    # O método __iter__ agora usa um loop for para simplificar a iteração
    def __iter__(self):
        for modelo in self.modelos:
            yield {"nome": modelo["nome"], "id": modelo["codigo"]}

    # Obtém a lista de modelos de carros para a marca da API da FIPE
    def get_modelos(self):
        url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos"
        response = requests.get(url)
        response.raise_for_status()  # Trata erros de solicitação
        modelos = response.json()["modelos"]
        return modelos

# Função para listar os códigos e nomes das marcas disponíveis
def listar_codigos_marcas():
    url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
    response = requests.get(url)
    response.raise_for_status()  # Trata erros de solicitação
    marcas = response.json()
    for marca in marcas:
        print(f"{marca['codigo']} - {marca['nome']}")

# Função para buscar os veículos de uma marca
def buscar_veiculos(marca_id):
    iterator = ApiFipeIterator(marca_id)
    # Usa list comprehension para criar a lista de veículos de forma mais eficiente
    veiculos = [{"nome": modelo["nome"], "id": modelo["id"]} for modelo in iterator]
    return veiculos

print("Lista de IDs das marcas disponíveis:")
listar_codigos_marcas()

# Solicita ao usuário um ID de marca e busca os veículos dessa marca
marca_id = int(input('Digite o ID de uma marca: '))
veiculos = buscar_veiculos(marca_id)

# Imprime os veículos da marca selecionada de maneira organizada
print("Veículos da marca selecionada:")
for veiculo in veiculos:
    print(f"ID: {veiculo['id']}, Nome: {veiculo['nome']}")
