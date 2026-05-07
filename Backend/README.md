# Backend

Este directorio contiene el backend del proyecto.

IMPORTANTE: antes de crear o activar el entorno virtual, sitúate en la carpeta `Backend`:

```bash
cd Backend
```

Crear y activar el entorno virtual (Windows - PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

Si PowerShell bloquea la activación, ejecuta esto en la misma sesión antes de activar:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Crear y activar el entorno virtual (Windows - CMD):

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

Crear y activar el entorno virtual (Linux / macOS - bash):

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar dependencias (con el entorno activado):

```bash
pip install -r requirements.txt
```

Agrega `venv/` a tu `.gitignore` para evitar subir el entorno virtual.

# GitHub (No sean negros)
Por favor, sean responsables con las branches del github. Si van a hacer cambios creen una rama basada en el master.
Una vez terminen de hacer cambios, por favor creen el pull request correspondiente.