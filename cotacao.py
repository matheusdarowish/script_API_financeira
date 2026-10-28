import urllib.request
import json

def buscar_cotacoes():
    """
    Função que faz uma requisição HTTP para a AwesomeAPI 
    usando apenas as bibliotecas nativas do Python.
    """
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    
    print("Conectando ao servidor financeiro...\n")
    
    try:
        # Criando a requisição web nativa
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        # Abrindo a conexão e lendo os dados
        with urllib.request.urlopen(req) as resposta:
            dados = json.loads(resposta.read().decode('utf-8'))
            
        # Extraindo os valores numéricos
        dolar = float(dados['USDBRL']['bid'])
        euro = float(dados['EURBRL']['bid'])
        bitcoin = float(dados['BTCBRL']['bid'])
        
        # Exibindo no terminal de forma formatada
        print("=== COTAÇÕES EM TEMPO REAL ===")
        print(f"💵 Dólar Comercial: R$ {dolar:.2f}")
        print(f"💶 Euro: R$ {euro:.2f}")
        # Truque simples para formatar o Bitcoin com separador de milhar
        print(f"🪙 Bitcoin: R$ {bitcoin:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print("==============================")
        
    except Exception as e:
        print(f"Erro inesperado no sistema: {e}")

# Ponto de execução do script
if __name__ == "__main__":
    buscar_cotacoes()