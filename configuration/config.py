"""  Configuración de Rutas
"""

di_routes = {"595":"refs/595.txt",
             "1581_1":"refs/1581_1.txt",
             "1581_2":"refs/1581_2.txt",
             "584":"refs/584.txt",
             "1068_1": "refs/1068_1.txt",
             "1068_2": "refs/1068_2.txt",
             "197": "refs/197.txt",
             "1148": "refs/1148.txt"}

import os
from pathlib import Path

pa_path_origin = Path("C:/Users/DELL/Respaldo/DON VILLA NUEVO/UNIVERSITY/Proyecto/PYTHON/GitHub/LeetCode/")
ls_files = os.listdir(pa_path_origin)

for file in ls_files:
    pa_path = pa_path_origin / file

    if ".sql" in file:
        pa_path_sql = Path(f"{pa_path_origin}/exercice_sql/{file}")
        pa_path.rename(pa_path_sql)

    if ".py" in file:
        pa_path_py = Path(f"{pa_path_origin}/exercice_python/{file}")
        pa_path.rename(pa_path_py)

# Finite Incantatem
