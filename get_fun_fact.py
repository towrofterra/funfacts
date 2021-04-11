import os
import pandas as pd
import random
import math


def add_to_clipboard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)


df_facts = pd.read_csv('funfacts.csv')
random_index = math.floor(random.uniform(0, len(df_facts)))
random_fact = df_facts['fact'][random_index]
add_to_clipboard(random_fact)
