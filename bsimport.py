#import statements
from bs4 import BeautifulSoup
import requests
import csv

#get the response data as text
response = requests.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
data = response.text

#using BeautifulSoup parse with html.parser
soup = BeautifulSoup(data, "html.parser")

#create empty lists to be populated after
major_list = []
early_career_pay = []
mid_career_pay = []

#get data from website and use for loop to append each data one-by-one
[major_list.append(major.getText().strip()) for major in soup.select("td.csr-col--school-name span.data-table__value")]
[early_career_pay.append(pay.getText().strip()) for pay in soup.select("td.csr-col--right span.data-table__value")[0:71:3]]
[mid_career_pay.append(pay.getText().strip()) for pay in soup.select("td.csr-col--right span.data-table__value")[1:71:3]]

#link the 3 lists together by index
linked_list = list(zip(major_list, early_career_pay, mid_career_pay))

# print(linked_list)

#using csv import to save the data into a csv file
with open("major.csv", "w", newline='') as file:
    writer = csv.writer(file)
    #writerow will determine the headings of each column
    writer.writerow(['Major', 'Early Career Pay', 'Mid-Career Pay'])
    for data in linked_list:
        writer.writerow(data)

# THANK YOU! IF YOU FOUND THIS HELPFUL PLEASE LEAVE A STAR. TO MAKE EDITS, FORK OR CONTRIBUTE AND LET ME KNOW.
# THIS CSV FILE CAN BE USED IN DATA SCIENCE WORK
# CREATED BY ME45Y63 AT 5:28PM ON THE 12TH OF MARCH 2023