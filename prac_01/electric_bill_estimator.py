TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
daily_use_in_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = float(input("Enter number of billing days: "))
if tariff == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31
estimated_bill = (tariff * daily_use_in_kwh) * number_of_billing_days
print("Estimated bill: ${:,.2f}".format(estimated_bill))
