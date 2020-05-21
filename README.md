# Repositorio para el proyecto final de WWW

## Instalacion de dependencias.

Se usara la version de PostgreSQL del repositorio de Ubuntu para este proyecto, algunas dependencias son necesarias para usar el driver ***psycopg2***  

#### Instalacion de PostgreSQL y PgAdmin3 (en caso de no poseerlos)

```sh
$ sudo apt install postgresql postgresql-contrib pgadmin3 libpq-dev python3-dev python-dev gcc
```

#### Depedencia de psycopg2 

```sh
$ sudo apt install libpq-dev python3-dev build-essential
```

#### Ambiente virtual de trabajo

Se recomienda hacer uso de ambiente virtuales de python para el proyecto, en caso de no tener instalado ***virtualenv*** hacer lo siguiente:

```sh
$ sudo apt install virtualenv
```

Luego para crear su ambiente virtual IMPORTANTE especificar que la version de python del ambiente sea la tercera:

```sh
$ virtualenv nombre_del_ambiente -p python3
```

Esto creara una carpeta con el nombre de ambiente que le haya asignado.
Seguidamente activar el ambiente virtual.

#### Activación del ambiente

```sh
$ source nombre_del_ambiente_creado/bin/activate
```

Una vez se haya activado el ambiente instalar las librerias del proyecto las cuales estan incluidas en el archivo ***requirements.txt***
#### Instalacion de librerias

```sh
$ pip install -r requirements.txt
```

En caso de usar una libreria nueva o actualizar una libreria existente, guardar los cambios en el archivo ***requirements.txt*** asi

```sh
$ pip freeze > requirements.txt
```
