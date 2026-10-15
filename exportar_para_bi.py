import pandas as pd
import sqlite3

print("A exportar os dados para o Power BI...")

# Ligar à base de dados e extrair os dados da IA
conexao = sqlite3.connect('banco_esg.db')
df = pd.read_sql('SELECT * FROM resultados_scoring', conexao)
conexao.close()

# Exportar para CSV pronto para consumo analítico
df.to_csv('dados_scoring_bi.csv', index=False, encoding='utf-8-sig')

print(f"Sucesso! Ficheiro 'dados_scoring_bi.csv' criado com {len(df)} empresas pontuadas.")