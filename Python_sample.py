n = int(input())
year = n / 365
years_int = int(year)
weeks = n - (years_int * 365)
weeks_in = weeks / 7
weeks_int = int(weeks_in)
days = weeks_in - (weeks_int * 7)
days_int = int(days)
print(years_int)
print(weeks_int)
print(days_int)
