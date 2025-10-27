import requests
import sqlite3
from datetime import datetime

API_KEY = "44c11ec53e4ca9272685d6f7765f8f44"  # coloque sua chave ativa aqui
URL = "https://api.openweathermap.org/data/2.5/weather"

con = sqlite3.connect("clima.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS historico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cidade TEXT,
    temperatura REAL,
    descricao TEXT,
    data_hora TEXT
)
""")
con.commit()

def consultar_clima(cidade):
    try:
        params = {
            "q": cidade,
            "appid": API_KEY,
            "units": "metric",  # Celsius
            "lang": "pt_br"
        }

        resposta = requests.get(URL, params=params)
        dados = resposta.json()

        if resposta.status_code == 200 and "main" in dados:
            temperatura = dados["main"]["temp"]
            descricao = dados["weather"][0]["description"]

            print(f"\n🌤  Clima em {cidade.title()}:")
            print(f"Temperatura: {temperatura}°C")
            print(f"Descrição: {descricao}")

            salvar_no_banco(cidade, temperatura, descricao)
        else:
            print("\n❌ Cidade não encontrada. Tente outro nome (ex: sao paulo, rio de janeiro).")
    except Exception as e:
        print(f"\nErro: {e}")

def salvar_no_banco(cidade, temperatura, descricao):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("INSERT INTO historico (cidade, temperatura, descricao, data_hora) VALUES (?, ?, ?, ?)",
                   (cidade, temperatura, descricao, data_hora))
    con.commit()

def mostrar_historico():
    print("\n=== Histórico de Consultas ===")
    cursor.execute("SELECT cidade, temperatura, descricao, data_hora FROM historico ORDER BY id DESC LIMIT 10")
    registros = cursor.fetchall()

    if len(registros) == 0:
        print("Nenhum registro ainda.")
    else:
        for cidade, temp, desc, dh in registros:
            print(f"{dh} | {cidade.title()} | {temp}°C | {desc}")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Consultar clima de uma cidade")
        print("2 - Ver histórico")
        print("3 - Sair")

        opc = input("Escolha: ")

        if opc == "1":
            cidade = input("\nDigite a cidade: ").strip().lower()
            consultar_clima(cidade)
        elif opc == "2":
            mostrar_historico()
        elif opc == "3":
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida.")

menu()
