# [Catastro to Mongodb](https://pypi.org/project/catastro-to-mongodb/)

[![PyPi release](https://img.shields.io/pypi/v/catastro-to-mongodb.svg)](https://pypi.org/project/catastro-to-mongodb/)
[![Downloads](https://pepy.tech/badge/catastro-to-mongodb)](https://pepy.tech/project/catastro-to-mongodb)
[:es:](#catastro-a-mongodb)

Migration Script from Catastro files ( Catalog CP Backup - dBASE IV ) to Mongodb

## Installation

```bash
$ pip install catastro_to_mongodb
```
## Usage
![Peek 2020-07-31 21-12](https://user-images.githubusercontent.com/3668610/89069491-87b97700-d373-11ea-999b-2fe6fde22cbd.gif)

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

Import `catastro.CAT` to `catastro` database:

```bash
$ catastro_to_mongodb -d catastro ./catastro.CAT
```

```txt
....................................
Connecting to 0.0.0.0:27017
....................................

Import complete!

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
