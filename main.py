import pandas as pd

# Carregar dados Costumer da neki
df = pd.read_csv("data/Customer Churn.csv.csv")

taxa_churn = df["Exited"].mean() * 100

# Churn por Atividade
churn_por_atividade = df.groupby("IsActiveMember")["Exited"].mean() * 100

# Churn por Número de Produtos
churn_por_produtos = df.groupby("NumOfProducts")["Exited"].mean() * 100

# Churn na Faixa de Score
df["ScoreRange"] = pd.cut(
    df["CreditScore"],
    bins=[300, 500, 650, 750, 900],
    labels=["Baixo", "Medio", "Bom", "Excelente"]
)

churn_por_score = df.groupby("ScoreRange", observed=False)["Exited"].mean() * 100

# Churn na Faixa de Saldo
df["BalanceRange"] = "Zero"

non_zero = df["Balance"] > 0

df.loc[non_zero, "BalanceRange"] = pd.qcut(
    df.loc[non_zero, "Balance"],
    q=3,
    labels=["Baixo", "Medio", "Alto"]
)

churn_por_saldo = df.groupby("BalanceRange")["Exited"].mean() * 100

# Chunr por Faixa Etária
df["AgeRange"] = pd.cut(
    df["Age"],
    bins=[18, 30, 40, 50, 60, 100],
    labels=["18-30", "30-40", "40-50", "50-60", "60+"]
)

#Idade geral
churn_por_idade = df.groupby("AgeRange")["Exited"].mean() * 100
print(churn_por_idade)

#Comparativo idade X geografia
pivot_age_geo = pd.pivot_table(
    df,
    values="Exited",
    index="AgeRange",
    columns="Geography",
    aggfunc="mean"
) * 100

print(pivot_age_geo)

#Tempo de relacionamento

df["TenureRange"] = pd.cut(
    df["Tenure"],
    bins=[-1, 2, 5, 8, 10],
    labels=["0-2 anos", "3-5 anos", "6-8 anos", "9-10 anos"]
)

#analises finais
churn_por_Tempo_de_relacionamento = df.groupby("TenureRange")["Exited"].mean() * 100

churn_por_sexo = df.groupby("Gender")['Exited'].mean() * 100


pd.pivot_table(
    df,
    values="Exited",
    index="Gender",
    columns="AgeRange",
    aggfunc="mean"
) * 100

pd.pivot_table(
    df,
    values="Exited",
    index="Gender",
    columns="Geography",
    aggfunc="mean"
)