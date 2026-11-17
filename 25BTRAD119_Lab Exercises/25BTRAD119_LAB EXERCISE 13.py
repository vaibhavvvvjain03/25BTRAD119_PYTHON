import csv

filename = "employees.csv"

try:
    total_gross = 0
    total_deductions = 0
    total_net = 0
    count = 0

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n===== PAYROLL SUMMARY =====")
        print("Name\tGross Salary\tDeductions\tNet Salary")

        for employee in reader:
            try:
                name = employee["Name"]
                basic = float(employee["Basic"])
                allowance = float(employee["Allowance"])
                deduction = float(employee["Deduction"])

                if basic < 0 or allowance < 0 or deduction < 0:
                    print("Invalid salary data for", name)
                    continue

                gross = basic + allowance
                net = gross - deduction

                if net < 0:
                    print("Invalid deductions for", name)
                    continue

                print(name, "\t", gross, "\t\t",
                      deduction, "\t\t", net)

                total_gross += gross
                total_deductions += deduction
                total_net += net
                count += 1

            except (ValueError, KeyError):
                print("Invalid employee record. Skipping.")

    if count == 0:
        print("No valid employee records found.")
    else:
        print("\nTotal Employees:", count)
        print("Total Gross Salary:", total_gross)
        print("Total Deductions:", total_deductions)
        print("Total Net Salary:", total_net)

except FileNotFoundError:
    print("Employee CSV file not found!")