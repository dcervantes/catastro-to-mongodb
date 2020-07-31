import setuptools

from catastro_to_mongodb import __VERSION__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="catastro-to-mongodb",
    version=__VERSION__,
    author="David Cervantes Caballero",
    author_email="david.cervantes.caballero@gmail.com",
    description="Migration Script from Catastro files ( Catalog CP Backup - dBASE IV ) to Mongodb",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dcervantes/catastro-to-mongodb",
    packages=setuptools.find_packages(),
    install_requires=["click", "pymongo"],
    py_modules=["csv_2_mongo"],
    entry_points={"console_scripts": ["catastro-to-mongodb=catastro_to_mongodb:cli"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: Spanish",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires='>=3.6',
)