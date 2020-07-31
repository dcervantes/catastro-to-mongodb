# [Catastro to Mongodb](https://pypi.org/project/catastro-to-mongodb/)

[![PyPi release](https://img.shields.io/pypi/v/catastro-to-mongodb.svg)](https://pypi.org/project/catastro-to-mongodb/)
[![Downloads](https://pepy.tech/badge/catastro-to-mongodb)](https://pepy.tech/project/catastro-to-mongodb)
[:es:](#catastro-a-mongodb)

Migration Script from Catastro files ( Catalog CP Backup - dBASE IV ) to Mongodb

## Installation

```bash
$ pip install catastro-to-mongodb
```
## Usage
![Usage capture](https://user-images.githubusercontent.com/3668610/89082426-497d8100-d38e-11ea-87ee-92a1a54147bf.gif)

```text
Usage: catastro_to_mongodb.py [OPTIONS] CAT_FILE

  Import a CAT FILE to MongoDB

  Migration Script from Catastro files ( Catalog CP Backup - dBASE IV ) to Mongodb
  More info: https://github.com/dcervantes/catastro-to-mongodb

Options:
  -h, --help           Show this message and exit.
  -v, --version        Show the version and exit.
  -d, --database name  Database name.  [default: catastro]
  -H, --host host      Host name.  [default: 0.0.0.0]
  -p, --port port      Port number.  [default: 27017]
  -t, --timeout sec    Connection timeout (seconds).  [default: 5]

```
## Examples

### Change database name

Import `catastro.CAT` to `test` database:
```bash
$ catastro-to-mongodb --database test ./catastro.CAT
```
```bash
$ catastro-to-mongodb -d test ./catastro.CAT
```
### Change host and port

Import `catastro.CAT` to `test` database in `test.xyz:16014`:
```bash
$ catastro-to-mongodb --database test --host test.xyz --port 16014 ./catastro.CAT
```

```bash
$ catastro-to-mongodb -d test -H test.xyz -p 16014 ./catastro.CAT
```

## Database


## Sources
Definición de estructura del fichero CAT: http://www.catastro.minhap.es/documentos/formatos_intercambio/catastro_fin_cat_2006.pdf
Como descargarlo: http://www.catastro.minhap.es/ayuda/manual_descargas_cat.pdf

## UnicodeDecodeError

If this error appears is because the Ñ character is encoded in instead of utf-8
`UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd1`

Using **iconv** we can fix the CAT file encoding 

```bash
$ iconv -f ISO-8859-1 -t UTF-8 ./catastro.CAT > ./catastro_fixed.CAT
```

# [Catastro a Mongodb](https://pypi.org/project/catastro-to-mongodb/)

[![PyPi release](https://img.shields.io/pypi/v/catastro-to-mongodb.svg)](https://pypi.org/project/catastro-to-mongodb/)
[![Downloads](https://pepy.tech/badge/catastro-to-mongodb)](https://pepy.tech/project/catastro-to-mongodb)
[:gb:](#catastro-to-mongodb)

Script de migración de datos del Catastro (en formato Catalog CP Backup - dBASE IV) a Mongodb



## License (Licencia)

 GPL-3.0 License  [**David Cervantes Caballero**](https://github.com/dcervantes)
