## Python

### Instalación de python

Herramientas > Quick add > python-3.6

### Instalación de pip

Copiar el contenido de https://bootstrap.pypa.io/get-pip.py

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Instalación
```
python get-pip.py
```

Agregar variables de entorno de Laragon a las variables de Usuario y reiniciar

Comprobar versiones de python y pip
```
python --version
pip --version
```

Instalar módulo de entorno virtual
```
pip install virtualenv
```

### Creación de un proyecto

Crear carpeta del proyecto

Crear entorno virtual de desarrollo
```
virtualenv -p python3 env
```

Activar entorno virtual
```
. env/Scripts/activate
```

### Instalación de flask

```
pip install flask
```
Listar módulos del entorno virtual
```
pip list
```
Desactivar entorno virtual
```
deactivate
```