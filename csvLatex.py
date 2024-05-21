import pyperclip

def parseCsv(input: str, delim = ';'):

    if delim not in input:
        raise ValueError(f'No se encontro el delimitador "{delim}" en la ultima entrada del clipboard')

    lines = input.splitlines()

    # toma la primera linea no vacia como la cabecera
    header = lines[0]

    hcolumns = header.split(delim)

    # recupera el indice de la primera columna no vacia
    start_idx = next(i for i, col in enumerate(hcolumns) if col != '')

    header = []
    # recupera el indice+1 (excluyente) de la ultima columna
    for i, hcol in enumerate(hcolumns[start_idx:]):
        if hcol == '':
            end_idx = i + start_idx
            break
        
        # guarda la cabecera de cada columna
        header.append(hcol)

    tableLayout, headerText, bodyText = '', '', ''

    # formatea la cabecera con un \\ al final
    headerText = ' & '.join(header) + r' \\'

    # a partir de las cabeceras se determina el formato de la tabla
    tableLayout = ' | '.join('c' for col in header)

    print(tableLayout)

    body = []

    for line in lines[1:]:
        lineCols = line.split(delim)

        body.append(lineCols[start_idx:end_idx])

    parsedLines = [' & '.join(line) for line in body]
    bodyText = ' \\\\ \n\t'.join(parsedLines)

    # layout = 'c|c'
    # headerText = 'Columna 1 & Columna 2 \\\\'
    # bodyText = 'Elemento 1 & Elemento 2 \\\\' + '\n' + '\tElemento 3 & Elemento 4'

    template = """
\\begin{{table}}
    \\centering
    \\label{{tab:Tabla}}
    \\caption{{Tabla de ejemplo}}
    \\begin{{tabular}}{{{layout}}}
        {headerText}
        \\hline
        {bodyText}
    \\end{{tabular}}
\\end{{table}}
    """

    output = template.format(layout=tableLayout, headerText=headerText, bodyText=bodyText)

    pyperclip.copy(output)
    print(output)
    print("\ntabla copiada al clipboard!")

input = pyperclip.paste()
parseCsv(input)