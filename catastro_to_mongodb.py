#!/usr/bin/env python3

import json
import warnings
import click

from pathlib import Path
from sys import exit
from jsonschema import validate, ValidationError, SchemaError
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

__VERSION__ = "1.0.1"
__SCHEMA_VERSION__ = 1

warnings.filterwarnings("ignore", category=DeprecationWarning)


@click.command()
@click.help_option("-h", "--help")
@click.version_option(__VERSION__, "-v", "--version", message="Version %(version)s")
@click.option(
    "-d",
    "--database",
    metavar="name",
    default="catastro",
    help="Database name.",
    show_default=True,
)
@click.option(
    "-H",
    "--host",
    metavar="host",
    default="0.0.0.0",
    help="Host name.",
    show_default=True,
)
@click.option(
    "-p",
    "--port",
    metavar="port",
    default=27017,
    help="Port number.",
    show_default=True,
)
@click.option(
    "-t",
    "--timeout",
    metavar="sec",
    default=5,
    help="Connection timeout (seconds).",
    show_default=True,
)
@click.argument("file", metavar='CAT_FILE')
def cli(database, host, port, timeout, file):
    """Import a CAT FILE to MongoDB

    \b
    Migration Script from Catastro files ( Catalog CP Backup - dBASE IV ) to Mongodb
    More info: https://github.com/dcervantes/catastro-to-mongodb
    """

    # Connect to MongoDB client
    click.echo("....................................")
    click.echo(f"Connecting to {host}:{port}")
    click.echo("....................................")
    print()
    mongo_client = MongoClient(host, port, serverSelectionTimeoutMS=timeout)
    check_connection(mongo_client, host, port)

    # Create database and collections
    db = mongo_client[database]
    colecciones = {}
    fill_char = click.style('=', fg='yellow')
    cat_file_lines = line_count(file)
    cat_file = open(file, "r")
    # read file
    json_schemas = {}
    json_dict = {}
    tipos = ["11", "13", "14", "15", "16", "17"]
    for tipo in tipos:
        with open('./schemas/tipo' + tipo + '.json', 'r') as schema:
            json_schemas[tipo] = json.loads(schema.read())
            db["Schemas"].insert_one(json_schemas[tipo])
        with open('./dict/tipo' + tipo + '.json', 'r') as dic:
            json_dict[tipo] = json.loads(dic.read())
        colecciones[tipo] = db[json_schemas[tipo]["title"]]
    with open(file, "r") as cat_file:
        with click.progressbar(cat_file, label='Importing CAT file to Mongodb...', fill_char=fill_char, length=cat_file_lines, show_percent=True, show_pos=True) as lines:
            for line in lines:
                tipo = line[:2]
                if tipo in tipos:
                    colecciones[tipo].insert_one(cat_to_json(
                        line, json_schemas[tipo], json_dict[tipo]))

    click.echo(click.style("Import complete!", fg="green"))


def cat_to_json(line, json_schemas, json_dict):

    result = {}
    result["version"] = __SCHEMA_VERSION__
    for pkey, pvalue in json_dict.items():
        result[pkey] = {}
        for skey, svalue in pvalue.items():
            value = get_field_value(line, svalue)
            if value != "":
                result[pkey][skey] = value

    validate_json(result, json_schemas)

    return result


def get_field_value(line, data):
    val_format = data["val_format"]
    ini_char = int(data["ini_char"]) - 1
    length = int(data["length"])
    end_char = ini_char + length
    value = line[ini_char:end_char].strip()
    # Text format
    if val_format == 'X' and value != "":
        if "dict" in data:
            return data["dict"][value]
        return value

    elif val_format == 'N' and value != "":
        if "decimal" in data:
            value = float(value)
            value /= 10**int(data["decimal"])
            return value
        return int(value)
    else:
        return ""


def validate_json(validJson, schema):
    try:
        validate(validJson, schema)

    except SchemaError as e:
        print(e)

    except ValidationError as e:
        print(e)

        print("---------")
        print(e.absolute_path)

        print("---------")
        print(e.absolute_schema_path)


def check_connection(mongo_client, host, port):
    try:
        mongo_client.server_info()
    except ServerSelectionTimeoutError as e:
        click.echo(
            f"Connection error while attempting to connect to {host}:{port}")
        exit(1)


def line_count(filename):
    # Every line has 1000 characters
    return int(Path(filename).stat().st_size / 1000)


if __name__ == "__main__":
    cli()
