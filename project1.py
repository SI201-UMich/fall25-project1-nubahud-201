import os
import csv

"""
questions to calculate:
what is the minimum bill length (mm) for each species of penguins in 2009?
What is the average bill
"""

class Project_1:
    def __init__(self, filename):
        self.base_path = os.path.abspath(os.path.dirname(__file__))
        self.full_path = os.path.join(self.base_path, filename)
        self.data = {
        'species': [],
        'island': [],
        'bill_length_mm': [],
        'bill_depth_mm': [],
        'flipper_length_mm': [],
        'body_mass_g': [],
        'sex': [],
        'year': []
    }
    
    
    def species_bill_length(self):
        
        pass
    def min_bill_length_dict(self):
        pass

            

penguins = Project_1('penguins.csv')
penguins.make_data_dict()
print(penguins)
    

