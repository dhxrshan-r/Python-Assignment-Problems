employee = [ [ "Tom", 20.00, 10, 12, 7, 9, 11 ],
             [ "Leslie", 18.50, 10, 10, 10, 10, 9 ],
             [ "Tobias", 16.75, 6, 12, 6.5, 11, 6 ] ]

def process_payroll(payroll):
    result = []
    for employee in payroll:
        name = employee[0]
        pay_rate = employee[1]
        hours = 0
        for i in range(2, len(employee)):
            hours += employee[i]
        pay = hours * pay_rate
        result.append([name, pay])
    return result
print(process_payroll(employee))

