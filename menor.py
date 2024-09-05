import pandas as pd
from fpdf import FPDF

def exibir_matriculas_menores_em_pdf(arquivo_csv,nome_arquivo_pdf='matriculas_menores.pdf'):
    
    df = pd.read_csv(arquivo_csv, skiprows=1, low_memory=False)
    
    df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
    
    menores_idade = df[df['idade'] < 18]

    matriculas = menores_idade['matricula'].tolist()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell (200, txt="Matriculas de alunos menores de idade", ln=1, align='C')

for matricula in matriculas:
    pdf.cell(200, 10, txt=str(matricula), ln=1)

    pdf.output(nome_arquivo_pdf)
