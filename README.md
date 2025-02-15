# Book Recs - Recomendações de livros com IA

Este projeto é uma aplicação que utiliza a API Gemini para gerar recomendações de livros com base nos gostos da usuária. A ideia é permitir que usuárias forneçam informações sobre seus interesses literários para que a IA recomende livros que se encaixam nesses perfis.

O objetivo desta aplicação é exemplificar como é simples e rápido criar uma app que utiliza IA para gerar recomendações personalizadas. Ela foi criada com o intuito de servir como um tutorial para quem deseja entender o processo de integração com APIs e a criação de uma app funcional de maneira prática. A intenção foi manter o projeto o mais simples possível, além de demostrar as inúmeras possibilidades do uso de tecnologias como IA para personalizar a experiência do usuário.

## Funcionalidade

- A usuária pode inserir sua chave da API Gemini e um prompt descrevendo seus gostos literários (ex: livros preferidos, autoras, gêneros, etc.).
- A IA gera recomendações de livros com base nas informações fornecidas, levando em consideração o estilo literário, os temas, o tom da obra e mais.
- A interface foi construída com a biblioteca [Gradio](https://gradio.app/) para tornar o uso simples e interativo.

## Como usar

### Instalação

1. Clone o repositório:

    ```bash
    git clone <link-do-repositorio>
    cd <nome-do-repositorio>
    ```
2. Crie um ambiente virtual e ative-o:

    ```bash
    # No Windows
    python -m venv venv
    venv\Scripts\activate

    # No macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

4. Você precisará de uma chave da API Gemini. Para obter uma chave, siga as instruções em [Google Gemini](https://cloud.google.com/genai). Procure por modelos [sem custo financeiro](https://ai.google.dev/pricing?hl=pt-br#2_0flash). 

### Executando a aplicação

Para iniciar a aplicação, basta rodar o seguinte comando:

```bash
python3 app.py
```

Isso abrirá a interface interativa no seu navegador, onde você poderá inserir sua chave de API Gemini e um prompt para obter as recomendações de livros.

### Exemplo de uso

- Insira a chave da API Gemini.
- Descreva seus gostos literários, como por exemplo: "Gosto de romances históricos com personagens complexos, como os de Margaret Atwood e Kazuo Ishiguro. Também gosto de ficção científica que explore temas de identidade e tecnologia, como Kindred: Laços de Sangue, de Octavia Butler."
- Clique em "OK!" e veja suas recomendações!

## Estrutura do projeto

- suggestions.py: Contém a lógica para fazer a requisição à API Gemini e gerar as recomendações de livros com base no prompt da usuária.
- `app.py`: A aplicação principal, que utiliza o Gradio para criar a interface de usuário.
- `contents.py`: Contém o conteúdo de algumas variáveis de texto longas, como parte do prompt que será usado pela IA.

## Tecnologias

- Google Gemini API
- Gradio
- Python 3.x


