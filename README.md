# 🌦️ Projeto: App de Clima em Python

Aplicativo simples de **linha de comando (CLI)** feito em **Python**, que consulta o **clima em tempo real** de qualquer cidade usando a **API do OpenWeather**, e salva automaticamente o histórico em um **banco de dados SQLite**.

---

## 🚀 Tecnologias Utilizadas
- 🐍 **Python 3**
- 🌐 **Requests** (para consumir a API)
- 🗃️ **SQLite3** (para armazenar o histórico)
- ⏱️ **Datetime** (para registrar data e hora das consultas)

---

## 💡 Funcionalidades
✅ Consulta a temperatura e descrição atual do clima em qualquer cidade  
✅ Retorna dados em tempo real direto da internet  
✅ Salva automaticamente o histórico de consultas com data e hora  
✅ Permite visualizar o histórico dentro do próprio terminal  

---

## 📸 Demonstração
🧩 Exemplo de execução no terminal:
```
=== MENU ===
1 - Consultar clima de uma cidade
2 - Ver histórico
3 - Sair

Digite a cidade: sao paulo
🌤 Clima em Sao Paulo:
Temperatura: 26°C
Descrição: céu limpo
```

🗃️ Exemplo do histórico salvo:
```
28/10/2025 14:32 | Sao Paulo | 26°C | céu limpo
28/10/2025 09:15 | Rio De Janeiro | 29°C | poucas nuvens
```

---

## ⚙️ Como Executar o Projeto

1️⃣ **Clone ou baixe** este repositório:
```bash
git clone https://github.com/BarbozaLast/clima-python.git
```

2️⃣ **Entre na pasta** do projeto:
```bash
cd clima-python
```

3️⃣ **Instale a biblioteca necessária**:
```bash
pip install requests
```

4️⃣ **Adicione sua chave da API** do OpenWeather dentro do arquivo `clima.py`:
```python
API_KEY = "SUA_CHAVE_AQUI"
```

5️⃣ **Execute o projeto**:
```bash
python clima.py
```

---

## 🧠 Conceitos aprendidos
Durante o desenvolvimento deste projeto, pratiquei:
- Manipulação de **APIs REST** com Python  
- Tratamento de **JSONs** retornados de requisições  
- Uso básico de **SQLite** para persistência de dados  
- Organização de código e boas práticas  

---

## 🧑🏾‍💻 Autor
**Lucas Barboza**  
💼 Estudante de Análise e Desenvolvimento de Sistemas  
🌍 [LinkedIn](https://www.linkedin.com/in/barbozalast) | [GitHub](https://github.com/BarbozaLast)

---

⭐ *Se este projeto te ajudou ou te inspirou, deixe uma estrela no repositório!*
