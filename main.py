import pandas as pd
import matplotlib.pyplot as plt

# Dados simulados de requisitos para Junior Analyst
data = {
    'Habilidade': ['Excel', 'SQL', 'Python', 'Power BI', 'Inglês', 'SQL', 'Excel', 'Python', 'SQL', 'Comunicação'],
    'Frequência': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
contagem = df.groupby('Habilidade').sum().sort_values(by='Frequência', ascending=False)

# Criando o gráfico
plt.figure(figsize=(10, 6))
contagem.plot(kind='bar', color='green', legend=False)
plt.title('Habilidades mais pedidas: Junior Analyst 2026')
plt.ylabel('Quantidade de Menções')
plt.xticks(rotation=45)
plt.tight_layout()

# Salva o gráfico automaticamente na pasta do projeto
plt.savefig('grafico_vagas.png')
plt.show()
print("Sucesso! O gráfico 'grafico_vagas.png' foi gerado na sua pasta.")