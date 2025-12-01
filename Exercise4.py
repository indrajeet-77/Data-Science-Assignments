""" 
Exercise 4: Problem Statement (Question): Hospital Billing System
A hospital charges its patients based on the following:

· Room charges per day: ₹2,000

· Doctor consultation fee (flat): ₹1,500

· Lab test charges: Based on the number of tests taken. Each test costs ₹300

· Medicine charges: Total cost of medicines provided

· Discount: If the total bill (before discount) exceeds ₹10,000, a 10% discount is applied

Write a Python program to calculate the final bill for a patient who:

· Stayed for 4 days

· Had 3 lab tests

· Had medicine charges of ₹2,400
"""

def calculate_bill(stayed_days: int, lab_tests: int, medicine_charges: int) -> float:

    ROOM_CHARGES_PER_DAY = 2000
    DOCTOR_CONSULTATION_FEE = 1500
    LAB_TEST_CHARGE = 300
    DISCOUNT_APPLIED=False
    total_bill = (
        ROOM_CHARGES_PER_DAY * stayed_days +
        DOCTOR_CONSULTATION_FEE +
        lab_tests * LAB_TEST_CHARGE +
        medicine_charges
    )
    if total_bill > 10000:
        DISCOUNT_APPLIED=True
        total_bill *= 0.9

    return [total_bill,DISCOUNT_APPLIED]

stayed_days = 4
lab_tests = 3
medicine_charges = 2400

final_bill = calculate_bill(stayed_days, lab_tests, medicine_charges)
if final_bill[1]:
  print("Discount applied")
else:
  print("No discount applied")
print(f"The final bill for the patient is: {final_bill[0]:.2f}")

# Time Complexity: O(1)
# Space Complexity: O(1)