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
    def __str__(self):
        return f"{self.data}"

    def make_data_dict(self):

        with open(self.full_path) as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                if (row[1] != "NA" and row[2] != "NA"
                and row[3] != "NA"
                and row[4] != "NA"
                and row[5] != "NA"
                and row[6] != "NA"
                and row[7] != "NA"
                and row[8] != "NA"):
                    self.data['species'].append(row[1])
                    self.data['island'].append(row[2])
                    self.data['bill_length_mm'].append(float(row[3]))
                    self.data['bill_depth_mm'].append(float(row[4]))
                    self.data['flipper_length_mm'].append(int(row[5]))
                    self.data['body_mass_g'].append(int(row[6]))
                    self.data['sex'].append(row[7])
                    self.data['year'].append(int(row[8]))
    
    def species_bill_length(self):
        
        pass
    def min_bill_length_dict(self):
        pass

            

penguins = Project_1('penguins.csv')
penguins.make_data_dict()
print(penguins)
    

