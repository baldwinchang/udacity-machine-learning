#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

MOST_MONEY_POI = ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]
MOST_MONEY_WHO, MOST_MONEY_VALUE = (None, 0)

NUMBER_OF_QUANTIFIED_SALARIES = 0
NUMBER_OF_QUANTIFIED_EMAILS = 0
NUMBER_OF_QUANTIFIED_POI = 0
NUMBER_OF_NON_QUANTIFIED_TOTAL_PAYMENTS = 0
NUMBER_OF_NON_QUANTIFIED_TOTAL_PAYMENTS_FOR_POI = 0

for person in enron_data.keys():
    persons_data = enron_data[person]

    # Missing data is represented by a String of NaN
    if persons_data['email_address'] != 'NaN':
        NUMBER_OF_QUANTIFIED_EMAILS += 1

    if persons_data['salary'] != 'NaN':
        NUMBER_OF_QUANTIFIED_SALARIES += 1

    if persons_data['total_payments'] != 'NaN':
        total_payments = int(persons_data['total_payments'])
    else:
        total_payments = 0
        if persons_data['poi']:
            NUMBER_OF_NON_QUANTIFIED_TOTAL_PAYMENTS_FOR_POI += 1
        NUMBER_OF_NON_QUANTIFIED_TOTAL_PAYMENTS += 1

    if persons_data['poi']:
        NUMBER_OF_QUANTIFIED_POI += 1

    if person in MOST_MONEY_POI and total_payments > MOST_MONEY_VALUE:
        MOST_MONEY_WHO, MOST_MONEY_VALUE = person, total_payments

print("Of Lay, Skilling, Fastow, who took home the most money?")
print("{} gained {}".format(MOST_MONEY_WHO, MOST_MONEY_VALUE))

print("How many folks in this dataset have a quantified salary? What about a known email address?")
print("N(quantified salary): {}, N(email addresses): {}".format(NUMBER_OF_QUANTIFIED_SALARIES, NUMBER_OF_QUANTIFIED_EMAILS))

print("How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?")
print("Have NaN: {}, Percentage: {:.2f}".format(NUMBER_OF_NON_QUANTIFIED_TOTAL_PAYMENTS, NUMBER_OF_NON_QUANTIFIED_TOTAL_PAYMENTS / len(enron_data)))

print("What percentage of POIs in the dataset have NaN for their total payments?")
print("Percentage: {:.2f}".format(NUMBER_OF_NON_QUANTIFIED_TOTAL_PAYMENTS_FOR_POI / len(enron_data)))

print("If you added in, say, 10 more data points which were all POI’s, and put “NaN” for the total payments for those folks, the numbers you just calculated would change.")
print("What is the new number of people of the dataset? What is the new number of folks with “NaN” for total payments?")
print("N(people in dataset + 10): {}, N(non-quantified total payments): {}".format(len(enron_data) + 10, NUMBER_OF_NON_QUANTIFIED_TOTAL_PAYMENTS + 10))

print("What is the new number of POI’s in the dataset? What is the new number of POI’s with NaN for total_payments?")
print("N(POI): {}, N(non-quantified total payments for poi): {}".format(NUMBER_OF_QUANTIFIED_POI + 10, NUMBER_OF_NON_QUANTIFIED_TOTAL_PAYMENTS_FOR_POI + 10))