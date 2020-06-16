from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors


def builderpdf(filename):
    contador = 0
    with open(filename+'.csv') as datas:
        
        for data in datas:
            if contador == 0:    
                dataCollNames = data.split(',')   # definindo os nomes das colunas e transformando em lista
                pass # e para n criar uma tabela para os nomes das colunas

            data = data.split(',')   #transformando a linha csv de string para lista para o Table aceitar

            dataArray = []
            for n in range(len(data)):  # cria o array de acordo com o tamanho dos dados (colunas)
                dataArray.append([dataCollNames[n], data[n]])

            #criando o doc pdf
            pdf = SimpleDocTemplate(
                'doc'+str(contador)+'.pdf',   # <-- nomeando o doc
                pagesize=letter
            )
            
            table = Table(dataArray)    # <-- alimentando a tabela com os dados

            style = TableStyle([    # <-- estilizando a tabela
                ('BACKGROUND', (0, 0), (0, 6), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('BOX', (0, 0), (-1, -1), 1, colors.grey),
                ('LINEBEFORE', (0, 0), (1, 6), 1, colors.black),
                ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black)
            ])

            table.setStyle(style)   # <-- aplicando o estilo 

            elems = []
            elems.append(table)    # <-- cria uma lista com os elementos da tabela (motivo: pq sim)
            pdf.build(elems)    # <-- cria os pdf

            contador += 1   # <-- contador para o nome do arquivo ir mudando, para nao ir se sobrepondo um ao outro

builderpdf('datas')
