import pandas as pd
import csv
import os
from pathlib import Path

class PreProcessing:
    hasFile = False

    def load_tse_data(path_to_file, cod_mun, party_prefix):
        path = Path('data/chunks')
        text = ''
        with open('data/chunks/chunk_00.csv', encoding='Latin-1') as header_file:
            text += header_file.readline()
        for i, file in enumerate(path.iterdir()):
            with open(file, encoding='Latin-1') as f:
                for line in f:
                    if cod_mun in line and line.split(';')[19][:2] == party_prefix:
                        text += line
