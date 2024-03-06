companies = {}

while True:
    data = input()

    if data == 'End':
        break

    company, employee_id = data.split(' -> ')

    if company not in companies:
        companies[company] = []

    companies[company].append(employee_id) if employee_id not in companies[company] else ...


for company, employees in companies.items():
    print(company)
    for employee_id in employees:
        print(f'-- {employee_id}')