import pandas as pd
from mp_api.client import MPRester
from emmet.core.xas import Edge, XASDoc, Type
from emmet.core.summary import HasProps
import matplotlib as plt
from pymatgen.analysis.diffraction.core import DiffractionPattern
from pymatgen.analysis.diffraction.xrd import XRDCalculator
import pymatgen.analysis.solar.slme as solar
import warnings
import csv
from pymatgen.core.composition import Composition
import re
warnings.simplefilter(action='ignore')

mpr = MPRester("SCtRk3rApakiAaUerRgvlqbl9waADBCj")

dielectric_doc = mpr.dielectric.search()

df = pd.DataFrame(dielectric_doc)

#Composition of all Compounds with Dielectric Constants
composition_list = df.iloc[:, 5].tolist()
clean_comp_list = []
for i in composition_list:
    composition_data = i
    # Extract element symbols and organize into lists
    element_symbols = composition_data[1].elements
    element_list = [element.symbol for element in element_symbols]
    clean_comp_list.append(element_list)
    #print(element_list)

#Formula of all Compounds with Dielectric Constants
formula_pretty_list = df.iloc[:, 6].tolist() 
clean_formula_pretty_list = []
for formula_data in formula_pretty_list:
    actual_formula = formula_data[1]
    clean_formula_pretty_list.append(actual_formula)


#Dielectric Constant of all Compounds with Dielectric Constants
old_dielectric_const = df.iloc[:, 23].tolist() 
clean_dielectric_const = []
for i in old_dielectric_const:
    original_string = str(i)
    numbers_only = ''.join(filter(lambda char: char.isdigit() or char == '.', str(original_string)))
    result = float(numbers_only)
    clean_dielectric_const.append(result)

# #Make a CSV File
# # Combine the lists into a list of tuples
# combined_data = list(zip(clean_formula_pretty_list, clean_comp_list, clean_dielectric_const))

# # Define the CSV file path
# csv_file_path = 'mpi_compounds_dielectric1.csv'

# # Write data to the CSV file
# with open(csv_file_path, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)

#     # Write the header row if needed
#     writer.writerow(['Column1', 'Column2', 'Column3'])

#     # Write the data rows
#     writer.writerows(combined_data)

# print(f"CSV file '{csv_file_path}' created successfully.")

df_materials = pd.read_csv('All_data_files/mpi_compounds_dielectric.csv')

for index,value in enumerate(composition_list):
    # Given composition
    composition_data = value

    # Extract element names and numbers
    elements = composition_data[1].get_el_amt_dict()

    for z in elements.keys():
        df_materials.at[index, z] = elements[z]


df_materials = df_materials.fillna(0)

# Save the DataFrame to a CSV file
df_materials.to_csv('df_materials.csv', index=False)

