# M63 Media Calculator

from prettytable import PrettyTable


def M63_Calculator(total):
  total = int(total)
  M63_5x = 0.2 * total
  MgSO4 = 0.001 * total
  Glucose = 0.01 * total
  Thiamine = 0.0001 * total
  Casamino_Acids = 0.01 * total
  NaBr = 0.025 * total
  Water = total - (M63_5x+MgSO4+Glucose+Thiamine+Casamino_Acids+NaBr)
  
  table = PrettyTable(['Index', 'Component', 'Amount'])
  table.add_row(['1', '5x M63 Salt', '{} mL'.format(M63_5x)])
  
  if MgSO4 < 1:
    table.add_row(['2', '1M MgSO4·7H2O', '{} μL'.format(1000*MgSO4)])
  else:
    table.add_row(['2', '1M MgSO4·7H2O', '{} mL'.format(MgSO4)])
    
  if Glucose < 1:
    table.add_row(['3', '20% Glucose', '{} μL'.format(1000*Glucose)])
  else:
    table.add_row(['3', '20% Glucose', '{} mL'.format(Glucose)])
        
  if Thiamine < 1:
    table.add_row(['4', '0.5% Thiamine', '{} μL'.format(1000*Thiamine)])
  else:
    table.add_row(['4', '0.5% Thiamine', '{} mL'.format(Thiamine)])
    
  if Casamino_Acids < 1:
    table.add_row(['5', '10% Casamino Acids', '{} μL'.format(1000*Casamino_Acids)])
  else:
    table.add_row(['5', '10% Casamino Acids', '{} mL'.format(Casamino_Acids)])
    
  if NaBr < 1:
    table.add_row(['6', '4M NaBr', '{} μL'.format(1000*NaBr)])
  else:
    table.add_row(['6', '4M NaBr', '{} mL'.format(NaBr)])
    
  if Water < 1:
    table.add_row(['7', 'ddH2O', '{} μL'.format(1000*Water)])
  else:
    table.add_row(['7', 'ddH2O', '{} mL'.format(Water)])  
  
  print(table)
  

total = input('Please enter the total volume of M63 media in mL: ')
M63_Calculator(total)
