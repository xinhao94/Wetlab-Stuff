# M9 Media Calculator

def M9_Calculator(M9):
  M9 = float(M9)
  MgSO4 = M9 * 0.002
  Glucose = M9 * 0.02
  CaCl2  = M9 * 0.0001
  Casamino_Acid = M9 * 0.01
  
  print("1x M9 Salt: {} mL".format(M9))
  
  if MgSO4 < 1:
    print("1M MgSO4: {} μL".format(1000 * MgSO4))
  else:
    print("1M MgSO4: {} mL".format(MgSO4))
  
  if Glucose < 1:
    print("20% Glucose: {} μL".format(1000 * Glucose))
  else:
    print("20% Glucose: {} mL".format(Glucose))
    
  if CaCl2 < 1:
    print("1M CaCl2: {} μL".format(1000 * CaCl2))
  else:
    print("1M CaCl2: {} mL".format(CaCl2))
    
  if Casamino_Acid < 1:
    print("10% Casamino Acid: {} μL".format(1000 * Casamino_Acid))
  else:
    print("10% Casamino Acid: {} mL".format(Casamino_Acid))
 
M9_vol = input('Please enter the volume of 1x M9 salt in mL:')
M9_Calculator(M9_vol)
