# API Base - Lista de Presentes

Este repositório contém a estrutura base para uma API em Flask que gerencia uma lista de presentes. Os métodos da API ainda não estão implementados, cabendo ao desenvolvedor a responsabilidade de completar as funcionalidades.

## Como Usar

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. **Instale as dependências:**
   ```bash
   pip install flask
   ```

3. **Execute a aplicação:**
   ```bash
   python app.py
   ```

## 📌 O que falta implementar?
Os métodos da API estão definidos, mas ainda não possuem lógica implementada. Você deve completar as seguintes funções no arquivo `app.py`:

- `add_gift()`: Adicionar um novo presente.
- `update_gift(gift_id)`: Alterar um presente existente.
- `delete_gift(gift_id)`: Remover um presente.
- `list_gifts()`: Listar todos os presentes.
- `get_gift_by_id(gift_id)`: Buscar um presente por ID.
- `most_expensive_gift()`: Obter o presente mais caro.
- `random_gift()`: Selecionar um presente aleatório.
- `list_sorted_by_name()`: Listar presentes ordenados por nome.
- `list_sorted_by_value()`: Listar presentes ordenados por valor.

## Estrutura do Projeto
```
/
│── app.py          # Código principal da API
│── README.md       # Este arquivo
│── requirements.txt # Dependências (opcional)
```

## 📄 Licença
Este é um projeto acadêmico. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário!

