# csv2Latex
Convierte una o más tablas exportadas de una hoja de calculo (.xls, .ods, etc.) a tablas de $\LaTeX$.

Cada tabla debe tener un marcador `_tabla` en la celda anterior a la primer cabecera, y el archivo csv se debe exportar con el delimitador `;`.

### Ejemplo
Archivo `medidas.csv`:
```csv
C;3.30E-07;;;;;;;;;;
R;2.20E+03;;;;;;;;;;
;;_tabla;f;fase (teorico);A;B;fase;;;;
;;;50.00;12.85;2.5;10.5;13.77;;;;
;;;100.00;24.52;4;9.5;24.90;;;;
;;;300.00;53.84;12;15;53.13;;;;
;;;600.00;69.93;8.5;9;70.81;;;;
;;;900.00;76.31;6;6.5;67.38;;;;
;;;1,200.00;79.65;9.5;10;71.81;;;;
;;;1,500.00;81.69;4;4;90.00;;;;
;;;;;;;;;;;
```

Ejecutar script.
```sh
python3 csvLatex.py medidas.csv
```

Resultado:
```latex
\begin{table}
    \centering
    \caption{Tabla de ejemplo}
    \label{tab:Tabla}
    \begin{tabular}{c | c | c | c | c}
        f & fase (teorico) & A & B & fase \\
        \hline
        50.00 & 12.85 & 2.5 & 10.5 & 13.77 \\
        100.00 & 24.52 & 4 & 9.5 & 24.90 \\
        300.00 & 53.84 & 12 & 15 & 53.13 \\
        600.00 & 69.93 & 8.5 & 9 & 70.81 \\
        900.00 & 76.31 & 6 & 6.5 & 67.38 \\
        1,200.00 & 79.65 & 9.5 & 10 & 71.81 \\
        1,500.00 & 81.69 & 4 & 4 & 90.00
    \end{tabular}
\end{table}
```
