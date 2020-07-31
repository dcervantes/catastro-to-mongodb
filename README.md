# Catastro to Mongodb
<h2>[English]</h2>

Script de migración de datos del Catastro (en formato Catalog CP Backup - dBASE IV) a Mongodb
Definición de estructura del fichero CAT: http://www.catastro.minhap.es/documentos/formatos_intercambio/catastro_fin_cat_2006.pdf

Como descargarlo: http://www.catastro.minhap.es/ayuda/manual_descargas_cat.pdf


## Usage
![Peek 2020-07-31 21-12](https://user-images.githubusercontent.com/3668610/89069491-87b97700-d373-11ea-999b-2fe6fde22cbd.gif)

```text
catastro-to-mongodb$ python3 catastro_to_mongodb.py -h
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

Import `catastro.CAT` to a `catastro` database:

```bash
$ python3 catastro_to_mongodb.py -d catastro ./catastro
```

```txt
....................................
Connecting to 0.0.0.0:27017
....................................

Import complete!
```


## License

 GPL-3.0 License  [**David Cervantes Caballero**](https://github.com/dcervantes)
