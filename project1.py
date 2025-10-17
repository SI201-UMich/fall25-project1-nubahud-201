# SI 201 Project 1
# Your name: Nubah Uddin
# Your student id: 75937331
# Your email: nubahud@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): ChatGPT
# If you worked with generative AI also add a statement for how you used it.
# Statement: I asked ChatGPT hints on creating test cases using a large dataset in a csv file with unittest, implementing a dictionary to map the species to their bill lengths according 
# to a category for species_bill_length function, and how to skip null values in a dataset

import os
import csv
import unittest


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
        
    def min_bill_length(self, year):
        """
        Find each species' minimum bill length for a specific year
        INPUT: Year (string)
        OUTPUT: each species minimum bill length for a specific year (dictionary)

        """

        year_bill = self.species_bill_length(int(year.strip(' "')))
        min_bill = {}
        for species, bill_lengths in year_bill.items():
            if not bill_lengths:
                continue
            smallest_length = float(min(bill_lengths))
            min_bill[species] = smallest_length
        return min_bill
        
    def avg_bill_length(self, island):
        """
        Find the average bill length for each species on an island
        INPUT: island (string)
        OUTPUT: each species minimum bill length for a specific island (dictionary)

        """
        island_bill = self.species_bill_length(island.strip(' "').title())
        avg_bill = {}
        for island_species, lengths in island_bill.items():
            avg_bill[island_species] = (sum(lengths) / len(lengths))
        return avg_bill

    
    def show_results(self, island, year, filename):
        """
        Writes the calculated penguin species and bill length results based on a year or an island
        INPUT: island (string), year (string), filename (string)
        OUTPUT: None (outputs to a file)
        """

        with open(filename, "w") as file:
            year_results = self.min_bill_length(year)
            island_results = self.avg_bill_length(island)
            for year_species, year_length in year_results.items():
                file.write(f"In {year}, the minimum bill length for the species {year_species} is {year_length} millimeters.\n")

            for species_island, length_island in island_results.items():
                file.write(f"\nOn the island {island}, the average bill length for the species {species_island} is {length_island} millimeters.")



class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.penguins = Project_1('test_penguins.csv')
        self.penguins.make_data_dict()

    def test_min_bill_length(self):
        #general cases for min_bill_length
        test_year1 = '2007'
        year_min_bill_1 = self.penguins.min_bill_length(test_year1)
        year_expected_min_1 = {'Adelie': 36.6, 'Gentoo': 42.932}
        self.assertEqual(year_min_bill_1, year_expected_min_1)
        
        test_year2 = '2008'
        year_min_bill_2 = self.penguins.min_bill_length(test_year2)
        year_expected_min_2 = {'Adelie': 34.523, 'Gentoo': 43.6}
        self.assertEqual(year_min_bill_2, year_expected_min_2)

        #edge cases for min_bill_length
        expected_empty = {}

        invalid_year1 = "0"
        actual_empty_dict1 = self.penguins.min_bill_length(invalid_year1)
        self.assertEqual(actual_empty_dict1, expected_empty)

        invalid_year2 = "-2034"
        actual_empty_dict2 = self.penguins.min_bill_length(invalid_year2)
        self.assertEqual(actual_empty_dict2, expected_empty)

        weird_format_year = ' "  2007" '
        weird_min_bill = self.penguins.min_bill_length(weird_format_year)
        weird_expected_min = {'Adelie': 36.6, 'Gentoo': 42.932}
        self.assertEqual(weird_min_bill, weird_expected_min)

    def test_avg_bill_length(self):
        #general cases for avg_bill_length
        avg_island1 = 'Biscoe'
        avg_bill_length_1 = self.penguins.avg_bill_length(avg_island1)
        expected_avg1 = {'Adelie': 34.523, 'Gentoo': 45.758}
        self.assertEqual(avg_bill_length_1, expected_avg1)

        avg_island2 = 'Dream'
        avg_bill_length_2 = self.penguins.avg_bill_length(avg_island2)
        expected_avg2 = {'Adelie': 37.5, 'Chinstrap': 50.866}
        self.assertEqual(avg_bill_length_2, expected_avg2)

        #edge cases for avg_bill_length

        invalid_island = 'Biscoe123'
        invalid_avg = self.penguins.avg_bill_length(invalid_island)
        expected_invalid = {}
        self.assertEqual(invalid_avg, expected_invalid)

        weird_format_island = '   dReAm'
        weird_island_avg = self.penguins.avg_bill_length(weird_format_island)
        weird_island_expected = {'Adelie': 37.5, 'Chinstrap': 50.866}
        self.assertEqual(weird_island_avg, weird_island_expected)




def main():
    penguins = Project_1("penguins.csv")   
    penguins.make_data_dict()              
    penguins.show_results("Dream", "2009", "results.txt")

if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)
    
    

