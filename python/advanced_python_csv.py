import csv
email = []
with open('faculty.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            email.append(row[' email'])
with open('emails.csv', 'w') as newfile:
   for i in email:
       newfile.write(str(i) + '\n')
       