# 📋 Gerador de Cadastros

Uma ferramenta com interface gráfica para geração de dados aleatórios de cadastro com capacidade de envio para APIs.

## 📝 Descrição

O **Gerador de Cadastros** é uma aplicação Python que utiliza a biblioteca Gradio para criar uma interface web amigável, permitindo gerar dados aleatórios para testes e desenvolvimento. É ideal para popular bancos de dados, testar APIs RESTful ou criar massa de dados para testes de software.

## ✨ Funcionalidades

- ✅ **Configuração dinâmica de campos**: Adicione, remova e limpe campos conforme necessário
- 🔄 **Geração de dados diversos**: Nomes, emails, CPF, telefone, endereços e muito mais
- 📊 **Visualização em tabela ou JSON**: Visualize dados em formato tabular ou estruturado
- 🌐 **Integração com APIs**: Verifique e envie dados para endpoints de API
- ⏱️ **Controle de intervalo**: Configure o tempo entre requisições para evitar sobrecarga
- 📋 **Logs detalhados**: Acompanhe o progresso e resultado das operações de envio

## 🚀 Tipos de dados suportados

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| Nome | Nomes e sobrenomes brasileiros | João Silva |
| Email | Endereços de email válidos | joaosilva123@gmail.com |
| CPF | CPF com dígitos verificadores válidos | 123.456.789-09 |
| Telefone | Números de telefone brasileiro | (11) 98765-4321 |
| Data de Nascimento | Datas formatadas | 15/03/1985 |
| CEP | CEP brasileiro | 12345-678 |
| Endereço | Endereços com número | Avenida Paulista, 123 |
| Cidade | Cidades brasileiras | São Paulo |
| Estado | Siglas de estados brasileiros | SP |
| Senha | Senhas seguras alfanuméricas | a7B9c!2DxY |
| Valor | Valores monetários em formato BR | R$ 1.234,56 |
| Slug | Texto formatado para URLs | joao-silva-123 |

## 🛠️ Requisitos

- Python 3.7+
- Biblioteca Gradio
- Outras dependências listadas no arquivo `requirements.txt`

## 📦 Instalação

pip install -r requirements.txt

ou

pip install gradio requests Pillow python-dateutil

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerador-cadastros.git
   cd gerador-cadastros
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como usar

1. Execute o aplicativo:
   ```bash
   python app.py
   ```

2. Acesse a interface web através do navegador (normalmente em `http://127.0.0.1:7860`).

3. Use a interface para configurar campos, gerar dados e enviar para APIs.

### Passo a passo

1. **Adicione campos**:
   - Digite um nome para o campo (ex: "nome_completo")
   - Selecione o tipo de dado (ex: "Nome")
   - Clique em "➕ Adicionar Campo"

2. **Configure a quantidade**:
   - Use o controle deslizante para definir quantos registros deseja gerar

3. **Gere os dados**:
   - Clique em "🔄 Gerar Dados"
   - Visualize os resultados na aba "Tabela de Dados" ou "JSON"

4. **Envie para uma API** (opcional):
   - Insira a URL da API
   - Verifique se o servidor está respondendo com "🔍 Verificar Servidor"
   - Configure o intervalo entre envios
   - Clique em "📤 Enviar Dados"
   - Acompanhe o progresso nos logs

## 🧠 Como funciona

O sistema usa funções geradoras para criar dados aleatórios mas consistentes:

- Nomes são combinações aleatórias de nomes e sobrenomes brasileiros comuns
- CPFs são gerados com dígitos verificadores válidos
- Emails podem ser baseados em nomes gerados anteriormente
- Slugs podem ser derivados dos nomes para criar identificadores web-friendly

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novos recursos ou tipos de dados
- Enviar pull requests

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📞 Contato

Para dúvidas, sugestões ou problemas, abra uma issue no GitHub ou entre em contato pelo email: [jefferson_jsp@hotmail.com]# GeradorDeDadosPython
