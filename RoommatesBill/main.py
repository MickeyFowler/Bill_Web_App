from RoommatesBill.files.apartment import Bill, Roommate
from reports import PdfReport, FileShare

bill_input = float(input("Please enter the bill amount: "))
date_input = input("Please enter rent period: ")
name1 = input("Please enter your name: ")
days_in_house1 = int(input(f"Please enter how many days {name1} spent in the house: "))
name2 = input("Please enter your roommate's name: ")
days_in_house2 = int(input(f"Please enter how many days {name2} spent in the house: "))

the_bill = Bill(amount=bill_input, period=date_input)
roommate1 = Roommate(name=name1, days_in_house=days_in_house1)
roommate2 = Roommate(name=name2, days_in_house=days_in_house2)

print(f"{roommate1.name} pays: ", roommate1.pays(bill=the_bill, flatmate2=roommate2))
print(f"{roommate2.name} pays: ", roommate2.pays(bill=the_bill, flatmate2=roommate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(roommate1, roommate2, bill=the_bill)
file_sharer = FileShare(filepath=pdf_report.filename)
print(file_sharer.share())
