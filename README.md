🌱 Sistema de Credit Scoring ESG com Machine Learning

Este projeto é um pipeline end-to-end de Engenharia de Dados e Ciência de Dados, desenvolvido para automatizar a avaliação de risco financeiro de empresas com base em métricas tradicionais e indicadores ESG (Ambiental, Social e Governança).

🚀 O Problema de Negócio
Avaliar o risco de crédito corporativo para financiamentos verdes é um processo manual e moroso. Bancos necessitam de identificar se uma empresa com alta emissão de carbono possui, de facto, maior risco de incumprimento.

⚙️ A Solução (Arquitetura)
O sistema processa dados financeiros e de sustentabilidade de 2.000 empresas, injetando-os num banco de dados relacional. Em seguida, um algoritmo de Machine Learning analisa o perfil corporativo e gera um Score de Risco (0-1000), que é consumido por um Dashboard interativo.

*   **ETL & Base de Dados:** Python (Pandas) e SQLite.
*   **Inteligência Artificial:** Scikit-Learn (Random Forest Classifier). A IA cruzou variáveis de Dívida vs. Receita e Emissões vs. Governança, atingindo uma precisão de ~63% (modelo probabilístico realista).
*   **Business Intelligence:** Power BI (modelação semagregações e visuais orientados a KPI de risco).
*   **Orquestração:** Automação em Batch (.bat) para execução instantânea do pipeline.

🛠️ Como Executar
Basta rodar o ficheiro `executar_pipeline.bat`. O sistema irá reconstruir o banco SQLite, treinar a Inteligência Artificial e gerar o ficheiro consumível para o Power BI automaticamente.