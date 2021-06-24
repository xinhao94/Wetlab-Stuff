# lambda value caclculator for droplet experiments

import math

def lambda_cal():
  flag = 'Y'
  while (flag=='Y' or flag=='y'):
    cell_density = int(input("Enter cell density (CFU/mL):"))
    droplet_diameter = int(input("Enter droplet diameter (um):"))
    # Convert droplet diameter to meter
    droplet_diameter = droplet_diameter / 1e6
    # Calculate droplet volume in cubic meter
    droplet_volume = (4/3) * math.pi * math.pow(droplet_diameter/2, 3)
    print("Droplet volume:", int(droplet_volume*1e15), "pL")
    # Convert droplet volume to mL
    droplet_volume = droplet_volume * 1e6
    droplet_number = 1 / droplet_volume
    print("In 1 mL, number of droplets:", format(droplet_number/1e6, '.2f'), "million")
    ans = cell_density / droplet_number
    print("lambda value:", format(ans, '.2f'))
    flag = input("Continue calculation? (Y/N):")

  print("######Calculation completed######")
  
lambda_cal()
