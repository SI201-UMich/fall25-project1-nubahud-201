# SI 201 Project 1
# Your name: Nubah Uddin
# Your student id: 75937331
# Your email: nubahud@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): ChatGPT
# If you worked with generative AI also add a statement for how you used it.  
# Asked Chatgpt hints on creating test cases using a large dataset in a csv file with unittest and species_bill_length function

import os
import csv

"""
questions to calculate:
what is the minimum bill length (mm) for each species of penguins in 2009?
What is the average bill length for each species of penguins on the island Torgersen?
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
    
    def species_bill_length(self, category):
        """
        Map penguin species to their bill lengths for for a category
        INPUT: Any category apart from species (string)
        OUTPUT: bill lengths for a penguin species according to a specific category (nested dictionary)
        """
        category_dict = {}
        for i in range(len(self.data['species'])):
            species = self.data['species'][i]
            bill_length = self.data['bill_length_mm'][i]

            for cate_name in self.data.keys():
                if cate_name != 'species' and self.data[cate_name][i] == category:
                    if species not in category_dict:
                        category_dict[species] = []
                    category_dict[species].append(float(bill_length))
        return category_dict
        

        
        
    def min_bill_length_dict(self, year):
        """
        Find each species' minimum bill length for a specific year
        INPUT: Year (string)
        OUTPUT: each species minimum bill length for a specific year (dictionary)

        """
        year_bill = self.species_bill_length(int(year))
        min_bill = {}
        for species, lengths in year_bill.items():
            if not lengths:
                continue
            smallest_length = float(min(lengths))
            min_bill[species] = smallest_length
        return min_bill
        
    def avg_bill_length_island(self, island):
        """
        Find the average bill length for each species on an island
        INPUT: Island (string)
        OUTPUT: each species minimum bill length for a specific island (dictionary)

        """

        pass

    
    def show_results(self):
        """
        Writes the calculated penguin species and bill length results based on a year or an island
        INPUT: calculation (dictionary)
        OUTPUT: None (outputs to a file)
        """

        pass



#make 4 test cases for each function (two general and two edge cases)
import unittest
class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.penguins = Project_1('test_penguins.csv')
        self.penguins.make_data_dict()
    
    def test_species(self):
        result = self.penguins.species_bill_length('Biscoe')
        expected = {'Adelie':[39.6], 'Gentoo': [42.9, 51.5]}
        self.assertEqual(result, expected)

    #do i need to do test cases for my other function apart from my calculations functions?

    def test_min_bill_length(self):
        year_min_bill = self.penguins.min_bill_length_dict('2007')
        year_expected_min = {'Adelie': 36.6, 'Gentoo': 42.9}
        self.assertEqual(year_min_bill, year_expected_min)

    def test_avg_bill_length(self):
        avg_bill = self.penguins.avg_bill_length_island('Biscoe')
        expected_avg = {'Adelie': 39.6, 'Gentoo': 47.2}
        self.assertEqual(avg_bill, expected_avg)
    




        



def main():
    pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
    main()
    

# test cases for other functions
# def test_make_data_dict(self):
#     species_row = self.penguins.data['species'][:3]
#     islands_row = self.penguins.data['island'][:3]
#     bill_length_mm_row = self.penguins.data['bill_length_mm'][:3]
#     year_row = self.penguins.data['year'][:3]

#     #check to make a list for a category (string type)
#     self.assertEqual(species_row, ['Adelie', 'Adelie', 'Adelie'])
#     self.assertEqual(islands_row, ['Torgersen', 'Torgersen', 'Biscoe'])

#     #check to make a list for a category (int and float type)
#     self.assertEqual(bill_length_mm_row, [39.5, 36.6, 39.6])
#     self.assertEqual(year_row, [2007, 2007, 2009])