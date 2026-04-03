day = int(input())
month = int(input())
year = int(input())

def is_leap_year(y):
	return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
if year <= 0:
	print("Invalid Date")
else:
	days_in_month = {
		1: 31, 2: 29 if is_leap_year(year) else 28, 3: 31,
		4: 30, 5: 31, 6: 30,
		7: 31, 8: 31, 9: 30,
		10: 31, 11: 30, 12: 31
	}

	if month < 1 or month > 12:
		print("Invalid Date")
	else:

		if day < 1 or day > days_in_month[month]:
			print("Invalid Date")
		else:
			day += 1
			if day > days_in_month[month]:
				day = 1
				month += 1
				if month > 12:
					month = 1
					year += 1
			print(f"{day:02d}-{month:02d}-{year}")

