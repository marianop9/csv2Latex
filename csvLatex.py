import pyperclip


def getLabelPositions(lines: list[str], label: str,
                      separator: str) -> dict[int, list[int]]:
    """Devuelve un diccionario con los numeros de linea que contienen tablas 
    y una lista con las columnas donde esta el marcador de cada una
    """
    markers: dict[int, list[int]] = {}

    for i, line in enumerate(lines):
        cols = line.split(separator)

        # obtiene los indices de los labels en cada fila
        indeces = [j for j, col in enumerate(cols) if col == label]
        # si encontro algun label agrega la lista de indices al diccionario para el nro. de fila
        if len(indeces) > 0:
            markers[i] = indeces

    return markers


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


def parseCsv(input: str, delim=';', tableLabel='_tabla'):

    if delim not in input:
        raise ValueError(
            f'No se encontro el delimitador "{delim}" en la ultima entrada del clipboard'
        )

    if tableLabel not in input:
        raise ValueError(
            f'No se encontro marcador "{tableLabel}" en la ultima entrada del clipboard'
        )

    lines = input.splitlines()

    labels = getLabelPositions(lines, tableLabel, delim)

    for lineIdx, labelCols in labels.items():
        headerLine = lines[lineIdx]
        headerLineCols = headerLine.split(delim)
        for colIdx in labelCols:
            tableLayout, headerText, bodyText = '', '', ''

            # indice de la ultima col. por defecto toma la ultima col. de la lista
            lastColIdx = len(headerLineCols) - 1
            # cabecera
            header = []
            for i, hcol in enumerate(headerLineCols[colIdx + 1:]):
                if hcol == '':
                    # ajusto el indice de la ultima col.
                    lastColIdx = colIdx + 1 + i
                    break

                # guarda la cabecera de cada columna
                header.append(hcol)

            # formatea la cabecera con un \\ al final
            headerText = ' & '.join(header) + r' \\'

            # a partir de las cabeceras se determina el formato de la tabla
            tableLayout = ' | '.join('c' for col in header)

            # cuerpo
            body = []
            for bodyLine in lines[lineIdx + 1:]:
                lineCols = bodyLine.split(delim)

                # si la primer col. de esta linea esta vacia interpreto que termina la tabla
                if lineCols[colIdx + 1] == '':
                    break
                # agrego todas las columnas de la fila
                body.append(lineCols[colIdx + 1:lastColIdx])

            # junta las columnas de cada linea
            parsedLines = [' & '.join(line) for line in body]
            # junta las lineas
            bodyText = ' \\\\ \n\t'.join(parsedLines)

            output = template.format(layout=tableLayout,
                                     headerText=headerText,
                                     bodyText=bodyText)
            print(output)

    # for line in lines[1:]:
    #     lineCols = line.split(delim)

    #     body.append(lineCols[start_idx:end_idx])

    # parsedLines = [' & '.join(line) for line in body]
    # bodyText = ' \\\\ \n\t'.join(parsedLines)

    # layout = 'c|c'
    # headerText = 'Columna 1 & Columna 2 \\\\'
    # bodyText = 'Elemento 1 & Elemento 2 \\\\' + '\n' + '\tElemento 3 & Elemento 4'


#     template = """
# \\begin{{table}}
#     \\centering
#     \\label{{tab:Tabla}}
#     \\caption{{Tabla de ejemplo}}
#     \\begin{{tabular}}{{{layout}}}
#         {headerText}
#         \\hline
#         {bodyText}
#     \\end{{tabular}}
# \\end{{table}}
#     """

#     output = template.format(layout=tableLayout,
#                              headerText=headerText,
#                              bodyText=bodyText)

#     pyperclip.copy(output)
#     print(output)
#     print("\ntabla copiada al clipboard!")

input = pyperclip.paste()
parseCsv(input)
