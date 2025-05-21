import gradio as gr
import random
import requests
import string
import json
from datetime import datetime, timedelta
import re
import time
import sys
import os
import io
from PIL import Image, ImageDraw, ImageFont
import base64

if sys.platform == 'win32':
    import os
    os.system('color')

def gerar_nome_aleatorio():
    nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Juliana", "Fernando", "Mariana", 
             "Lucas", "Camila", "Rafael", "Patrícia", "Rodrigo", "Aline", "Marcos", "Tatiana"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Lima", "Pereira", "Ferreira", "Costa", 
                  "Rodrigues", "Almeida", "Nascimento", "Carvalho", "Gomes", "Martins", "Araújo"]
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

def gerar_slug(texto=None):
    if not texto:
        palavras = ["projeto", "sistema", "aplicativo", "tecnologia", "ferramenta", "blog", "site", 
                   "pagina", "artigo", "noticia", "produto", "servico", "categoria", "usuario"]
        texto = f"{random.choice(palavras)}-{random.choice(palavras)}-{random.randint(1, 999)}"
    
    slug = texto.lower()
    
    import unicodedata
    slug = unicodedata.normalize('NFKD', slug).encode('ASCII', 'ignore').decode('ASCII')
    
    slug = re.sub(r'\s+', '-', slug)
    
    slug = re.sub(r'[^a-z0-9\-]', '', slug)
    
    slug = re.sub(r'\-+', '-', slug)
    
    slug = slug.strip('-')
    
    return slug

def gerar_email_aleatorio(nome=None):
    if nome:
        nome_limpo = re.sub(r'[^\w]', '', nome.lower().replace(" ", ""))
        email = f"{nome_limpo}{random.randint(1, 999)}@"
    else:
        letras = ''.join(random.choices(string.ascii_lowercase, k=8))
        email = f"{letras}@"
    
    dominio = random.choice(["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "empresa.com.br"])
    return email + dominio

def gerar_cpf_aleatorio():
    cpf = [random.randint(0, 9) for _ in range(9)]
    
    soma = sum((cpf[i] * (10 - i)) for i in range(9))
    resto = soma % 11
    cpf.append(0 if resto < 2 else 11 - resto)
    
    soma = sum((cpf[i] * (11 - i)) for i in range(10))
    resto = soma % 11
    cpf.append(0 if resto < 2 else 11 - resto)
    
    return f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"

def gerar_telefone_aleatorio():
    ddd = random.randint(11, 99)
    numero = random.randint(900000000, 999999999)
    return f"({ddd}) {numero//10000}-{numero%10000}"

def gerar_data_aleatoria(anos_min=18, anos_max=70):
    hoje = datetime.now()
    dias_aleatorios = random.randint(anos_min*365, anos_max*365)
    data = hoje - timedelta(days=dias_aleatorios)
    return data.strftime("%d/%m/%Y")

def gerar_cep_aleatorio():
    return f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"

def gerar_endereco_aleatorio():
    ruas = ["Rua das Flores", "Avenida Brasil", "Rua São Paulo", "Avenida Paulista", 
            "Rua 7 de Setembro", "Avenida Rio Branco", "Rua Tiradentes", "Avenida Getúlio Vargas"]
    return f"{random.choice(ruas)}, {random.randint(1, 999)}"

def gerar_cidade_aleatoria():
    cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Brasília", 
               "Curitiba", "Fortaleza", "Recife", "Porto Alegre", "Manaus"]
    return random.choice(cidades)

def gerar_estado_aleatorio():
    estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", 
               "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    return random.choice(estados)

def gerar_senha_aleatoria(tamanho=10):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choices(caracteres, k=tamanho))
    return senha

def gerar_valor_aleatorio(min_val=10, max_val=10000):
    return f"R$ {random.uniform(min_val, max_val):.2f}".replace('.', ',')

def gerar_imagem_aleatoria():
    try:
        largura, altura = 200, 200
        cores = [
            (255, 0, 0),    # Vermelho
            (0, 255, 0),    # Verde
            (0, 0, 255),    # Azul 
            (255, 255, 0),  # Amarelo
            (255, 0, 255),  # Magenta
            (0, 255, 255),  # Ciano
            (255, 165, 0),  # Laranja
            (128, 0, 128)   # Roxo
        ]
        
        img = Image.new('RGB', (largura, altura), color=(240, 240, 240))
        draw = ImageDraw.Draw(img)
        
        forma = random.choice(['círculo', 'retângulo', 'linhas', 'texto', 'padrão'])
        
        if forma == 'círculo':
            cor = random.choice(cores)
            raio = random.randint(30, 80)
            centro_x = random.randint(raio, largura - raio)
            centro_y = random.randint(raio, altura - raio)
            draw.ellipse((centro_x - raio, centro_y - raio, centro_x + raio, centro_y + raio), fill=cor)
        
        elif forma == 'retângulo':
            cor = random.choice(cores)
            x1 = random.randint(10, largura // 2)
            y1 = random.randint(10, altura // 2)
            x2 = random.randint(x1 + 40, largura - 10)
            y2 = random.randint(y1 + 40, altura - 10)
            draw.rectangle((x1, y1, x2, y2), fill=cor)
        
        elif forma == 'linhas':
            for _ in range(15):
                cor = random.choice(cores)
                x1 = random.randint(0, largura)
                y1 = random.randint(0, altura)
                x2 = random.randint(0, largura)
                y2 = random.randint(0, altura)
                largura_linha = random.randint(1, 5)
                draw.line((x1, y1, x2, y2), fill=cor, width=largura_linha)
        
        elif forma == 'texto':
            try:
                cor = random.choice(cores)
                texto = ''.join(random.choices(string.ascii_uppercase, k=random.randint(3, 6)))
                tamanho_fonte = random.randint(40, 80)
                try:
                    fonte = ImageFont.truetype("arial.ttf", tamanho_fonte)
                except:
                    fonte = ImageFont.load_default()
                
                text_width, text_height = draw.textsize(texto, font=fonte) if hasattr(draw, 'textsize') else (100, 50)
                x = (largura - text_width) // 2
                y = (altura - text_height) // 2
                draw.text((x, y), texto, font=fonte, fill=cor)
            except Exception:
                draw.text((50, 80), "ABC", fill=random.choice(cores))
        
        elif forma == 'padrão':
            tamanho_bloco = random.randint(10, 40)
            for x in range(0, largura, tamanho_bloco):
                for y in range(0, altura, tamanho_bloco):
                    cor = random.choice(cores)
                    draw.rectangle((x, y, x + tamanho_bloco, y + tamanho_bloco), fill=cor)
        
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        
        return img_buffer
    except Exception as e:
        return None

geradores = {
    "Nome": gerar_nome_aleatorio,
    "Email": gerar_email_aleatorio,
    "CPF": gerar_cpf_aleatorio,
    "Telefone": gerar_telefone_aleatorio,
    "Data de Nascimento": gerar_data_aleatoria,
    "CEP": gerar_cep_aleatorio,
    "Endereço": gerar_endereco_aleatorio,
    "Cidade": gerar_cidade_aleatoria,
    "Estado": gerar_estado_aleatorio,
    "Senha": gerar_senha_aleatoria,
    "Valor": gerar_valor_aleatorio,
    "Slug": gerar_slug,
    "Imagem": gerar_imagem_aleatoria
}

def verificar_servidor(url):
    try:
        if not url.strip():
            return "❌ Por favor, forneça uma URL válida."
        
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"✅ Servidor respondeu com sucesso! Status: {response.status_code}"
        else:
            return f"⚠️ Servidor respondeu, mas com status: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return "❌ Não foi possível conectar ao servidor. Verifique a URL ou se o servidor está ativo."
    except requests.exceptions.Timeout:
        return "⏱️ Tempo de conexão esgotado. O servidor está demorando muito para responder."
    except requests.exceptions.InvalidURL:
        return "❌ URL inválida. Verifique o formato da URL."
    except Exception as e:
        return f"❌ Erro ao verificar servidor: {str(e)}"

def main():
    campos = []
    valores_gerados = {}
    app = None
    
    def adicionar_campo(nome_campo, tipo_campo):
        if nome_campo and tipo_campo:
            campos.append({"nome": nome_campo, "tipo": tipo_campo})
            return gr.Dataframe(value=[[campo["nome"], campo["tipo"]] for campo in campos], 
                               headers=["Nome do Campo", "Tipo de Dado"])
        return gr.Dataframe(value=[[campo["nome"], campo["tipo"]] for campo in campos], 
                           headers=["Nome do Campo", "Tipo de Dado"])
    
    def remover_ultimo_campo():
        if campos:
            campos.pop()
        return gr.Dataframe(value=[[campo["nome"], campo["tipo"]] for campo in campos], 
                           headers=["Nome do Campo", "Tipo de Dado"])
    
    def limpar_campos():
        campos.clear()
        return gr.Dataframe(value=[], headers=["Nome do Campo", "Tipo de Dado"])
    
    def gerar_dados(quantidade):
        dados_gerados = []
        imagens = []
        
        for _ in range(quantidade):
            registro = {}
            nome_valor = None
            
            for campo in campos:
                nome_campo = campo["nome"]
                tipo_campo = campo["tipo"]
                
                if tipo_campo == "Nome":
                    valor = geradores[tipo_campo]()
                    nome_valor = valor
                elif tipo_campo == "Email" and nome_valor:
                    valor = gerar_email_aleatorio(nome_valor)
                elif tipo_campo == "Slug" and nome_valor:
                    valor = gerar_slug(nome_valor)
                elif tipo_campo == "Imagem":
                    img_buffer = geradores[tipo_campo]()
                    if img_buffer:
                        imagens.append((nome_campo, img_buffer))
                        valor = f"[IMAGEM_{len(imagens)}]"
                    else:
                        valor = "[ERRO AO GERAR IMAGEM]"
                else:
                    if tipo_campo in geradores:
                        valor = geradores[tipo_campo]()
                    else:
                        valor = f"Tipo '{tipo_campo}' não suportado"
                
                registro[nome_campo] = valor
            
            dados_gerados.append(registro)
        
        valores_gerados.clear()
        valores_gerados.update({"dados": dados_gerados, "imagens": imagens})
        
        headers = [campo["nome"] for campo in campos]
        rows = []
        for registro in dados_gerados:
            rows.append([registro[campo] for campo in headers])
        
        return (
            gr.Dataframe(value=rows, headers=headers),
            json.dumps(dados_gerados, indent=2, ensure_ascii=False)
        )
    
    def enviar_para_api(url, json_data, intervalo_segundos):
        try:
            if not url.strip():
                return "❌ Por favor, forneça uma URL válida."
            
            dados = json.loads(json_data)
            
            logs = []
            
            success_count = 0
            error_count = 0
            
            for i, registro in enumerate(dados, 1):
                logs.append(f"Processando ({i}/{len(dados)}): Registro {i}")
                
                dados_envio = registro.copy()
                
                for campo, valor in registro.items():
                    if isinstance(valor, str) and valor.startswith("[IMAGEM_") and valor.endswith("]"):
                        try:
                            indice_imagem = int(valor.replace("[IMAGEM_", "").replace("]", "")) - 1
                            if 0 <= indice_imagem < len(valores_gerados.get("imagens", [])):
                                nome_campo, imagem_buffer = valores_gerados["imagens"][indice_imagem]
                                imagem_base64 = base64.b64encode(imagem_buffer.getvalue()).decode('utf-8')
                                dados_envio[campo] = f"data:image/png;base64,{imagem_base64}"
                        except:
                            logs.append(f"⚠️ Não foi possível processar a imagem para o campo {campo}")
                
                headers = {'Content-Type': 'application/json'}
                try:
                    logs.append(f"Enviando para {url}...")
                    response = requests.post(url, json=dados_envio, headers=headers)
                    
                    if response.status_code in [200, 201]:
                        success_count += 1
                        logs.append(f"✅ Sucesso! Status: {response.status_code}")
                    else:
                        error_count += 1
                        logs.append(f"❌ Erro: {response.status_code}")
                        logs.append(f"Resposta: {response.text}")
                except Exception as e:
                    error_count += 1
                    logs.append(f"❌ Exceção: {str(e)}")
                
                if i < len(dados):
                    logs.append(f"Aguardando {intervalo_segundos} segundos antes do próximo envio...")
                    time.sleep(intervalo_segundos)
            
            logs.append(f"\n--- Resumo do processamento ---")
            logs.append(f"Total de registros: {len(dados)}")
            logs.append(f"Enviados com sucesso: {success_count}")
            logs.append(f"Erros de envio: {error_count}")
            
            return "\n".join(logs)
        except Exception as e:
            return f"❌ Erro ao processar dados: {str(e)}"
    
    app = gr.Blocks(title="Gerador de Cadastros")
    with app:
        gr.Markdown("# 📋 Gerador de Cadastros")
        gr.Markdown("""
        Este aplicativo permite gerar dados de cadastro aleatórios e enviá-los para uma API.
        
        ### Como usar:
        1. Adicione os campos desejados
        2. Escolha a quantidade de registros para gerar
        3. Clique em "Gerar Dados"
        4. Visualize os dados gerados
        5. Envie para uma API (opcional)
        """)
        
        with gr.Row():
            with gr.Column(scale=3):
                with gr.Group():
                    gr.Markdown("### Configuração dos Campos")
                    with gr.Row():
                        nome_campo = gr.Textbox(label="Nome do Campo", placeholder="Ex: nome_completo")
                        tipo_campo = gr.Dropdown(label="Tipo de Dado", choices=list(geradores.keys()))
                    
                    with gr.Row():
                        adicionar_btn = gr.Button("➕ Adicionar Campo", variant="primary")
                        remover_btn = gr.Button("🗑️ Remover Último", variant="secondary")
                        limpar_btn = gr.Button("🧹 Limpar Campos", variant="secondary")
            
            with gr.Column(scale=3):
                tabela_campos = gr.Dataframe(headers=["Nome do Campo", "Tipo de Dado"], interactive=False)
        
        with gr.Row():
            with gr.Column():
                quantidade = gr.Slider(minimum=1, maximum=100, value=5, step=1, label="Quantidade de Registros")
                gerar_btn = gr.Button("🔄 Gerar Dados", variant="primary")
        
        with gr.Tabs():
            with gr.TabItem("Tabela de Dados"):
                dados_gerados_tabela = gr.Dataframe(interactive=False)
            
            with gr.TabItem("JSON"):
                json_output = gr.Textbox(label="Dados em formato JSON", lines=10)
        
        with gr.Group():
            gr.Markdown("### Enviar para API")
            with gr.Row():
                url_api = gr.Textbox(label="URL da API", placeholder="https://sua-api.com/cadastros")
                verificar_btn = gr.Button("🔍 Verificar Servidor", variant="secondary")
            
            status_servidor = gr.Textbox(label="Status do Servidor", interactive=False)
            
            with gr.Row():
                enviar_btn = gr.Button("📤 Enviar Dados", variant="primary")
                intervalo = gr.Slider(minimum=1, maximum=30, value=5, step=1, label="Intervalo entre envios (segundos)")
            
            resultado_api = gr.Textbox(label="Resultado do Envio", interactive=False, lines=15)
        
        adicionar_btn.click(adicionar_campo, inputs=[nome_campo, tipo_campo], outputs=tabela_campos)
        remover_btn.click(remover_ultimo_campo, inputs=[], outputs=tabela_campos)
        limpar_btn.click(limpar_campos, inputs=[], outputs=tabela_campos)
        gerar_btn.click(gerar_dados, inputs=[quantidade], outputs=[dados_gerados_tabela, json_output])
        verificar_btn.click(verificar_servidor, inputs=[url_api], outputs=status_servidor)
        enviar_btn.click(enviar_para_api, inputs=[url_api, json_output, intervalo], outputs=resultado_api)
        
    return app

if __name__ == "__main__":
    app = main()
    app.launch(quiet=False)