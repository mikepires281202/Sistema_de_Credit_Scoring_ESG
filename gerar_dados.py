import pandas as pd
import numpy as np
import random

print("A gerar dados sintéticos ESG para 2000 empresas...")

# Fixar a semente para que os dados gerados sejam sempre os mesmos
np.random.seed(42)
num_empresas = 2000

setores = ['Tecnologia', 'Indústria', 'Energia', 'Varejo', 'Agricultura']
dados = []

for i in range(num_empresas):
    setor = random.choice(setores)
    
    # 1. Gerar Finanças e Emissões baseadas na realidade do setor
    if setor == 'Tecnologia':
        receita = np.random.normal(50, 20)
        margem = np.random.normal(0.25, 0.10)
        emissao = np.random.normal(100, 50)
    elif setor in ['Energia', 'Indústria']:
        receita = np.random.normal(200, 100)
        margem = np.random.normal(0.12, 0.05)
        emissao = np.random.normal(5000, 2000)
    else: # Varejo, Agricultura
        receita = np.random.normal(80, 30)
        margem = np.random.normal(0.15, 0.08)
        emissao = np.random.normal(800, 300)
        
    # 2. Métricas Gerais
    divida = receita * np.random.uniform(0.1, 1.8) # Dívida pode ser até 1.8x a receita
    agua = emissao * np.random.uniform(0.5, 2.0)
    governanca = np.clip(np.random.normal(65, 15), 0, 100) # Score de 0 a 100
    certificacao = np.random.choice([0, 1], p=[0.8, 0.2]) # Apenas 20% têm selo verde
    
    # 3. A "Mágica" da correlação (Risco de Crédito)
    # Empresas com muita dívida, alta emissão, sem selo verde e baixa governança têm maior risco
    probabilidade_falha = 1 / (1 + np.exp(-((divida/max(receita,1))*1.5 + (emissao/4000) - (governanca/100)*3 - certificacao)))
    inadimplente = 1 if np.random.rand() < probabilidade_falha else 0

    # Guardar a linha da empresa
    dados.append({
        'id_empresa': f'EMP{i+1000}',
        'setor': setor,
        'receita_mi': round(max(receita, 2), 2),
        'margem_lucro': round(margem, 3),
        'divida_mi': round(max(divida, 0), 2),
        'emissao_co2_ton': round(max(emissao, 10), 2),
        'consumo_agua_m3': round(max(agua, 10), 2),
        'score_governanca': round(governanca, 1),
        'certificacao_verde': certificacao,
        'historico_inadimplencia': inadimplente # 1 = Deu calote (Mau crédito), 0 = Pagou certo (Bom crédito)
    })

# Converter para DataFrame e salvar em CSV
df = pd.DataFrame(dados)
df.to_csv('dados_empresas_esg.csv', index=False)

print(f"Sucesso! Arquivo 'dados_empresas_esg.csv' criado com {len(df)} empresas.")