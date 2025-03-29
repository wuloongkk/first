years = [year for year in range(1000, 3000) if year % 7 == 0 and year % 5 != 0]
for i in range(0, len(years), 5):
    print("#".join(map(str, years[i:i+5])))