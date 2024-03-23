bill = float(input("Enter the bill amount: ")) 
num_people = int(input("Enter the number of people: "))  
new_amount = 150 * 1.12
each_person_bill = new_amount / num_people
bill_pay = round(each_person_bill, 2)  
print("Each person needs to pay:", bill_pay)
