#!/usr/bin/env python3

import json
from os.path import basename
from re import match
from sys import exit
from pathlib import Path

import warnings
import click
from pandas import read_csv
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from time import sleep
import subprocess

__VERSION__ = "0.0.1"

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
@click.argument("file")
def cli(database, host, port, timeout, file):
    """Import a CAT FILE to MongoDB"""

    # Connect to MongoDB client
    # click.echo("....................................")
    # click.echo(f"Connecting to {host}:{port}")
    # click.echo("....................................")
    # print()
    # mongo_client = MongoClient(host, port, serverSelectionTimeoutMS=timeout)
    # check_connection(mongo_client, host, port)

    # Create database and collections
    # db = mongo_client[database]
    # cinmuebles = db["Inmuebles"]
    fill_char = click.style('=', fg='yellow')
    cat_file_lines = line_count(file)
    print(cat_file_lines)
    cat_file = open(file, "r")
    with open(file, "r") as cat_file:
        with click.progressbar(cat_file, label='Loading...', fill_char=fill_char, length=cat_file_lines, show_percent=True, show_pos=True) as lines:
            for line in lines:
                sleep(0.01)
                # print(line)
                # cinmuebles.insert_one(cat_to_json_inmuebles(line)) 

    click.echo(click.style("Import complete!", fg="green"))

def cat_to_json_inmuebles(line):
    x = {
    "_id": "1",
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    return json.dumps(x)

def get_field_value(line, val_format, ini_char, length):
    # Text format
    if val_format == 'X':
        return line[ini_char:ini_char + val_format]
    
    elif val_format == 'N':
        return int(line[ini_char:ini_char + val_format])
    else:
        return ""


def process_line(line):
    x = {
    "_id": "1",
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    return json.dumps(x)

def check_connection(mongo_client, host, port):
    try:
        mongo_client.server_info()
    except ServerSelectionTimeoutError as e:
        click.echo(f"Connection error while attempting to connect to {host}:{port}")
        exit(1)

def line_count(filename):
    #Every line has 1000 characters 
    return int(Path(filename).stat().st_size / 1000)

if __name__ == "__main__":
    cli()
