@echo off
echo =======================================================
echo     SISTEMA DE CREDIT SCORING ESG - INICIANDO PIPELINE
echo =======================================================
echo.

echo [1/4] A extrair e estruturar dados brutos...
python criar_banco.py
echo.

echo [2/4] A executar Inteligencia Artificial (Random Forest)...
python treinar_modelo.py
echo.

echo [3/4] A preparar base de dados para o Power BI...
python exportar_para_bi.py
echo.

echo =======================================================
echo PROCESSAMENTO CONCLUIDO COM SUCESSO!
echo O Power BI ja pode ser atualizado.
echo =======================================================
pause