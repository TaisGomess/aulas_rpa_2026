Cenário:

1. Nome do Processo
2. É viável para RPA? (Sim / Não)
3. Justificativa baseada nos 4 critérios essenciais (Repetitividade, Regras de Negócio, Tipo de Dados, Volume).
4. Mapeamento Passo a Passo das Ações do Robô

# Avaliação de Processo — RPA

## Cenário

### 1. Nome do Processo

**Conciliação bancária diária**

### 2. É viável para RPA?

**Sim.**

### 3. Justificativa baseada nos 4 critérios essenciais

* **Repetitividade:** O processo é realizado diariamente e segue uma sequência de tarefas que se repete.
* **Regras de Negócio:** A comparação é baseada em regras fixas, utilizando informações como CNPJ e valor das transações.
* **Tipo de Dados:** Os dados são estruturados, provenientes de um arquivo `.csv` e do sistema ERP.
* **Volume:** O processo pode envolver uma grande quantidade de transações, tornando a automação útil para reduzir o trabalho manual e o tempo de execução.

Dessa forma, o processo apresenta características adequadas para automação utilizando RPA.

### 4. Mapeamento Passo a Passo das Ações do Robô

1. Acessar o sistema utilizado para obter o extrato bancário.
2. Baixar o extrato bancário diário no formato `.csv`.
3. Abrir e ler os dados do arquivo `.csv`.
4. Acessar o sistema ERP.
5. Consultar as baixas financeiras realizadas no período.
6. Comparar as informações do extrato bancário com as informações do ERP, utilizando CNPJ e valor como regras de comparação.
7. Identificar as transações que possuem correspondência.
8. Identificar as transações que não possuem correspondência.
9. Registrar ou apresentar o resultado da conciliação.
10. Finalizar o processo e disponibilizar as divergências para análise humana.
