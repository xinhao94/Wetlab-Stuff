# M9 Media Calculator

from prettytable import PrettyTable

def M9_Calculator(M9):
  M9 = float(M9)
  MgSO4 = M9 * 0.002
  Glucose = M9 * 0.02
  CaCl2  = M9 * 0.0001
  Casamino_Acid = M9 * 0.01
  
  table = PrettyTable(['Index', 'Component', 'Volume'])
  table.add_row(['1', '1x M9 Salt', '{} mL'.format(M9)])
  
  if MgSO4 < 1:
    table.add_row(['2', '1M MgSO4', '{} μL'.format(1000 * MgSO4)])
  else:
    table.add_row(['2', '1M MgSO4', '{} mL'.format(MgSO4)])
  
  if Glucose < 1:
    table.add_row(['3', '20% Glucose', '{} μL'.format(1000 * Glucose)])
  else:
    table.add_row(['3', '20% Glucose', '{} mL'.format(Glucose)])
    
  if CaCl2 < 1:
    table.add_row(['4', '1M CaCl2', '{} μL'.format(1000 * CaCl2)])
  else:
    table.add_row(['4', '1M CaCl2', '{} mL'.format(CaCl2)])
    
  if Casamino_Acid < 1:
    table.add_row(['5', 'Casamino Acid', '{} μL'.format(1000 * Casamino_Acid)])
  else:
    table.add_row(['5', 'Casamino Acid', '{} mL'.format(Casamino_Acid)])
 
  print(table)
 
M9_vol = input('Please enter the volume of 1x M9 salt in mL: ')
M9_Calculator(M9_vol)
