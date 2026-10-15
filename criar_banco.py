import pandas as pd
import sqlite3

print("A iniciar a transferência de dados para o SQLite...")

# 1. Ler o ficheiro CSV que acabámos de criar
df = pd.read_csv('dados_empresas_esg.csv')

# 2. Criar a ligação à base de dados (se não existir, o SQLite cria o ficheiro automaticamente)
conexao = sqlite3.connect('banco_esg.db')

# 3. Enviar o DataFrame do Pandas para dentro de uma tabela chamada 'historico_empresas'
df.to_sql('historico_empresas', conexao, if_exists='replace', index=False)

# 4. Fechar a ligação por segurança
conexao.close()

print("Sucesso! A base de dados 'banco_esg.db' foi criada e populada com 2000 registos.")
