Projeto de análise de dados exploratoria, para verificar taxa de churn em clientes de uma instituição bancaria.

Etapas: Análise com python | pandas
        Criação de dashboard para visualização com Power Bi



Dashboard: mostrando principais Drivers como Idades, Gendes e Geography
<img width="1316" height="757" alt="{C7C9BFAF-BD32-471C-8AFB-E225E9FE8BC6}" src="https://github.com/user-attachments/assets/f936ecba-0188-40c8-8638-f9f426968980" />


Conclusão:
Ao analisar a planilha podemos notar que se trata de uma instituição financeira pois as colunas no dataset contam com “saldo bancario”, ‘possui cartão de credito ?”, “score de credito”.

as perguntas propostas pela neki são oque seguinificam os dados analisados:

Os dados analisados mostram uma extensa planilha de usuarios que estão ativos ou desativaram suas contas, podemos notar padroes consistentes entre pessoas que sairam e pessoas que se matem ativas podendo chegar a uma analisa certeira dos motivos ou indicadores que mais influenciam essa tomada de decisão

Os indicadores que mais estão influenciando o churn no momento  são em ordem de peso:
Idade
Geografia

Gender
Produtos

Saldo

A idade se apresenta como o principal driver da estrutura de churn. A análise identificou que clientes entre 50 e 60 anos registram taxa de churn de 56,2%, significativamente superior às demais faixas etárias com 22,3 pontos percentuais acima do grupo imediatamente anterior (40–50 anos).

Esse efeito é ainda mais acentuado quando observamos clientes de 50 a 60 anos residentes na Alemanha, indicando uma interação relevante entre faixa etária e geografia.

Ao aprofundar a análise geográfica, verifica-se que a Alemanha apresenta a maior taxa de churn em todas as faixas etárias e segmentações avaliadas, independentemente do *driver* analisado (idade ou número de produtos ou etc). Esse padrão sugere uma possível influência de fatores estruturais do mercado local, refletindo um cenário de menor retenção quando comparado aos demais países.

Diante desse contexto, seria estratégico desenvolver ações segmentadas para o público alemão, com foco em retenção e aumento de vínculo. Um estudo mais aprofundado sobre o perfil do investidor alemão pode auxiliar na compreensão desse comportamento e orientar ofertas mais aderentes às expectativas desse mercado.

Sob a ótica do ciclo de vida financeiro, o pico de churn entre 50 e 60 anos pode estar associado a um momento de reorganização patrimonial, fase em que clientes tendem a revisar investimentos, buscar melhores taxas e otimizar a estrutura financeira, migrando para instituições com portfólio mais atrativo.

Observa-se, contudo, que após os 60 anos há redução na taxa de churn, posicionando essa faixa entre as menores taxas relativas. Esse comportamento sugere maior estabilidade, perfil mais conservador e menor propensão à migração, possivelmente decorrente de consolidação financeira e menor apetite por mudança podendo estar atrelado a aposentadoria.

Considerando esse cenário, uma estratégia eficaz poderia incluir iniciativas direcionadas ao público de 40 a 50 anos, grupo que combina saldo médio elevado e bom score de crédito, antecipando ofertas de investimento e ampliando o portfólio de produtos como forma de aumentar o engagement e reduzir o risco futuro de churn.

Também foi possivel analisar o tempo de relacionamento cliente X banco para notar se influencia na taxa de churn porem mostrou apenas que a análise do tempo de relacionamento (Tenure) não demonstrou impacto significativo sobre o churn, uma vez que as taxas permaneceram estáveis entre as faixas analisadas, variando em torno de 20%. Dessa forma, Tenure não se caracteriza como um driver relevante quando comparado a variáveis como idade e geografia.

Um fator muito importante que foi analisado é o Gender, A análise indica que clientes do sexo feminino apresentam taxa de churn consistentemente superior em todas as faixas etárias e regiões analisadas, sugerindo um possível padrão comportamental que merece investigação adicional, uma boa pedida seria a instituição realizar um fit cultural interno e externo para analisar oque tem feito para melhorar a retenção do publico feminino, se possuiem ou não produtos e serviços que possam agregar possitivamente este publico, ou ate mesmo estrategias de marketing para esse “nicho”

Dados analisados | Pesos na analise:

Balance - Saldo bancario não mostrou impacto tão siguinificativo sendo apenas um potencializador em faixas etarias mais elevadas, mas não sendo um driver principal

Age - Muito alto, sendo nosso Driver dominante quando o assunto é o churn dos filiados, mostrando uma maxima de 56% na faixa etaria 50-60

Tenure - O tempo de relacionamento mostrou taxas estaveis entre as faixas etarias, variando em torno de 20%.

Exited ←- campo alvo

Geograph - Mostra forte indicador de churn entre todos graficos mostrando possível diferença estrutural no comportamento do mercado alemão.

Gender - Forte indicador, mostrando um alerta de atenção para com o publico feminino
