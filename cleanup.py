import os
import pandas as pd
import random
import math
import re

def add_to_clipboard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)


df_facts = pd.read_csv('funfacts.csv')
print(df_facts)
i=0
for fact in df_facts['fact']:
    if str.isdigit(fact[0]):
        stripped_fact = re.search('[0-9]{0,4}. (.*)', fact).group(1)
        print(stripped_fact)
    elif len(fact) < 126:
        print(fact)
