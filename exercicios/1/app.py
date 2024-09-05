import pandas as pd

def contar_alunos_tarde(arquivo_csv):

    df = pd.read_csv(arquivo_csv,skiprows=1,low_memory=False)

    alunos_tarde = df[df['turno'] == 'TARDE']

    total_alunos_tarde = alunos_tarde.shape[0]

    return total_alunos_tarde

arquivo = 'data/situacaofinal2023_2.csv'
total = contar_alunos_tarde(arquivo)
print("O total de alunos que estudam a tarde é: ", total)