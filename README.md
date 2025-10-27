# GameBar-File-Ordering
Código para ordenar screenshots y videos obtenidos con la aplicación Xbox GameBar. Tengo la impresión de que sirve para archivos en español, por eso escribo esto en este idioma.

Now it works in all date and time formats, at least in the ones I've tried so far"

## Uso
* Simplemente ejecuta `python main.py` (o como ejecutes tus cóigos de python) en la carpeta ".../Capturas" o donde se guarden tus grabaciones de GameBar
* Ejecuta `python undoErrors.py` si se te crearon carpetas con el nombre del juego y la fecha u hora. Va a devolver los juegos a la carpeta base y eliminará las carpetas vacías. Debes poner el nombre del juego en `GAME=""`

## Use
* Execute `python main.py`
* Execute `python undoErrors.py` for any game folder you have with the name of the game and any date and time added to it. It will return those files to the base directory and delete empty folders. You must change the game that has problematic folders in `GAME=""` 
