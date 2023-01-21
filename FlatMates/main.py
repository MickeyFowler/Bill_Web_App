from flat import Bill, Flatmate
from reports import PdfReport, FileShare

bill_input = float(input("Please enter the bill amount: "))
date_input = input("Please enter rent period: ")

name1 = input("Please enter your name: ")
days_in_house1 = int(input(f"Please enter how many days {name1} spent in the house: "))

name2 = input("Please enter your roommate's name: ")
days_in_house2 = int(input(f"Please enter how many days {name2} spent in the house: "))

the_bill = Bill(amount=bill_input, period=date_input)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)

file_sharer = FileShare(filepath=pdf_report.filename)
print(file_sharer.share())
