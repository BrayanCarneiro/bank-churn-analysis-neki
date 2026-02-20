import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/Customer Churn.csv.csv")

print(dataframe.head())
print("=======================")
print(dataframe.describe())
print("=====================")  
print(dataframe.isnull().sum())


#Pesquisando e fazendo perguntas para meu dataframe, para responder perguntar e aprofundar a analise final
taxa_churn = dataframe["Exited"].mean() *100
print(f"Taxa geral de churn: {taxa_churn:.2f}")

age_analysis = dataframe.groupby("Age")["Exited"].agg(["count", "sum"])
age_analysis["churn_%"] = (age_analysis["sum"] / age_analysis["count"]) *100


geo_analysis = dataframe.groupby("Geography")["Exited"].mean() * 100
print(geo_analysis)

geo_analysis.plot(kind="bar")
plt.title("Churn por País (%)")
plt.ylabel("% de Churn")
plt.xticks(rotation = 0)
plt.show()

active_analysis  = dataframe.groupby("IsActiveMember")["Exited"].mean() *100
print(active_analysis)

prod_analysis = dataframe.groupby("NumOfProducts")["Exited"].mean() *100
print(prod_analysis)


credit_analysis = dataframe.groupby("CreditScore")["Exited"].mean() * 100

dataframe["ScoreRange"] = pd.cut(
    dataframe["CreditScore"],
    bins=[300,500,650,750,900],
    labels=["Baixo", "Medio", "Bom", "Excelente"],
    

)
score_group = dataframe.groupby("ScoreRange",observed=False)["Exited"].mean() * 100 
print(score_group)

dataframe["BalanceRange"] = "Zero"

non_zero = dataframe["Balance"] > 0

dataframe.loc[non_zero, "BalanceRange"] = pd.qcut(
    dataframe.loc[non_zero, "Balance"],
    q= 3,
    labels=["Baixo", "Medio", "Alto"]

)

balance_analysis = dataframe.groupby("BalanceRange")["Exited"].mean() * 100
print(balance_analysis)

print(dataframe.groupby("BalanceRange")["IsActiveMember"].mean())

print(pd.crosstab(dataframe["BalanceRange"], dataframe["NumOfProducts"]))


dataframe["AgeRange"] = pd.cut(
    dataframe["Age"],
    bins=[18, 30, 40, 50, 60, 100],
    labels=["18-30", "30-40", "40-50", "50-60", "60+"]
)

print(dataframe.groupby("AgeRange")["Exited"].mean() * 100)
print(dataframe.groupby("AgeRange")["Balance"].mean())
print(dataframe.groupby(["AgeRange", "BalanceRange"])["Exited"].mean() * 100)

print(pd.crosstab(
    dataframe["AgeRange"],
    dataframe["HasCrCard"],
    values=dataframe["Exited"],
    aggfunc="mean"
) * 100)



#colinha pro story telling, idade é o fator principal no churn dos filiados, porem dentro da idades a geografia e o saldo na conta impactam.