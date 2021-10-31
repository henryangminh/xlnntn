import os

grammars = []
for filename in os.listdir('grammars'):
    if not filename.startswith('merge'):
        with open (f'grammars/{filename}', 'r') as f:
            grammar = f.readlines()
            for i in range(len(grammar)):
                grammar[i] = grammar[i].replace('\n', '')
                grammars.append(grammar[i])

grammars = list(dict.fromkeys(grammars))
# print(grammars)

with open ("grammars/merge.cfg", 'w') as f:
    for grammar in grammars:
        f.write(f"{grammar}\n")