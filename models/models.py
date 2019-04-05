#To open csv files, we need to import the CSV library
import csv

# users
characters = []
with open('characters.csv', 'rb') as user_file:
    spam_reader = csv.DictReader(user_file)
    for row in spam_reader:
        characters.append(row)

# apprearance
appearances = []
with open('episode_per_season.csv') as appearance_file:
    spam_reader = csv.DictReader(appearance_file)
    for row in spam_reader:
        appearances.append(row)
