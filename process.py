import nltk
import os

for i in ['a', 'b', 'c', 'd']:
# for i in ['merge']:
# for i in ['e']:
  gramma = nltk.data.load(f'file:grammars/merge.cfg')

  rd_parser = nltk.parse.chart.BottomUpLeftCornerChartParser(gramma)

  for filename in os.listdir('sentences'):
      if filename.startswith(f'{i}'): 
        with open (f'sentences/{filename}', 'r') as f:
          sent = f.read()

        print(sent)
        sent = sent.split()
        for tree in rd_parser.parse(sent):
          print(tree)
          tree.draw()
      
        print("\n======================================================\n")