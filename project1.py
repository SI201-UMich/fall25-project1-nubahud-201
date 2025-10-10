# SI 201 Project 1
# Your name: Nubah Uddin
# Your student id: 75937331
# Your email: nubahud@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code
import os
import csv

"""
questions to calculate:
what is the minimum bill length (mm) for each species of penguins in every year?
What is the average bill length for each species of penguins on an island?
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
        """
        
        Load csv file and convert the data into a data structure.
        INPUT: Name of the csv file (string)
        OUTPUT: A dictionary with keys as the name of the categories and values as a list of the values from the dataset

        """

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
        return self.data
    
    def species_bill_length(self):
        """
        Map penguin species to their bill lengths for for a category
        INPUT: Any category apart from species (string)
        OUTPUT: bill lengths for a penguin species according to a specific category (nested dictionary)
        """
        pass
    def min_bill_length_dict(self):
        """
        Find each species' minimum bill length for a specific year
        INPUT: Year (string)
        OUTPUT: each species minimum bill length for a specific year (dictionary)

        """

        pass

    def avg_bill_length_island(self):
        """
        Find the average bill length for each species on an island
        INPUT: Island (string)
        OUTPUT: each species minimum bill length for a specific island (dictionary)

        """

        pass
    def show_results(self):
        pass


import unittest
class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.file = Project_1('penguins.csv')
        self.penguins = self.file.make_data_dict()
        
    def test_make_data_dict(self):
        species = self.penguins['species'][:3]
        islands = self.penguins['island'][:3]
        bill_length_mm = self.penguins['bill_length_mm'][:3]
        year = self.penguins['year'][:3]

        #check to make a list for a category (string type)
        self.assertEqual(species, ['Adelie', 'Adelie', 'Adelie'])
        self.assertEqual(islands, ['Torgersen', 'Torgersen', 'Torgersen'])

        #check to make a list for a category (int and float type)
        self.assertEqual(bill_length_mm, [39.1, 39.5, 40.3])
        self.assertEqual(year, [2007, 2007, 2007])

        


def main():
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
    main()
    

