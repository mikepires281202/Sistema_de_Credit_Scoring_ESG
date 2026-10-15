import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

print("Iniciando a leitura do banco de dados...")

# 1. Conectar ao banco de dados SQLite
conexao = sqlite3.connect('banco_esg.db')
df = pd.read_sql('SELECT * FROM historico_empresas', conexao)

# 2. Preparar os dados para a IA
# Computadores não entendem texto ("Tecnologia", "Varejo"), então transformamos o Setor em colunas numéricas
df_ml = pd.get_dummies(df, columns=['setor'], drop_first=True)

# O que queremos prever (Alvo / Target)
y = df_ml['historico_inadimplencia']

# O que vamos usar para prever (Features) - tiramos o ID e a própria resposta
X = df_ml.drop(['id_empresa', 'historico_inadimplencia'], axis=1)

# 3. Separar dados para Treino (80%) e Teste (20%)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Treinar a Inteligência Artificial (Random Forest)
print("Treinando o modelo de Machine Learning. Aguarde...")
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_treino, y_treino)

# 5. Testar a precisão
precisao = modelo.score(X_teste, y_teste)
print(f"Precisão do modelo: {precisao * 100:.2f}%")

# 6. Criar o Credit Score (Nota de Crédito)
print("Calculando o Score ESG para todas as empresas...")
# A IA calcula a probabilidade matemática da empresa ser BOA pagadora
probabilidades = modelo.predict_proba(X)
prob_boa_pagadora = probabilidades[:, 0] 

# Transformamos essa probabilidade em uma nota de mercado (0 a 1000)
df['credit_score'] = (prob_boa_pagadora * 1000).astype(int)

# Criamos uma classificação para o Dashboard
def classificar_risco(score):
    if score >= 750: return 'Risco Baixo (Aprovado)'
    elif score >= 500: return 'Risco Médio (Análise Manual)'
    else: return 'Risco Alto (Reprovado)'

df['status_credito'] = df['credit_score'].apply(classificar_risco)

# 7. Salvar os resultados para o Power BI
df.to_sql('resultados_scoring', conexao, if_exists='replace', index=False)
conexao.close()

print("Sucesso! Análise concluída. Tabela 'resultados_scoring' pronta no banco de dados.")
