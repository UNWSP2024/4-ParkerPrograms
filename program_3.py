#Nathan Parker
#2/11/25
#Program #3: Average Rainfall

#get the number of years from the user
number_of_years = int(input('Enter the number of years: '))

#set total_rainfall to 0
total_rainfall = 0

#get the rainfall for each month in each year from the user and add it to total_rainfall
for years in range(number_of_years):
    for month in range(12):
        rainfall = float(input('Enter the rainfall in inches for a month: '))
        total_rainfall += rainfall

#calculate the number of months
number_of_months = number_of_years * 12

#calculate the average rainfall per month
average_rainfall_per_month = total_rainfall / number_of_months

#display the number of months, the total rainfall, and the average rainfall per month
print(f'''Number of months: {number_of_months}
Total rainfall: {total_rainfall:,} in.
Average rainfall per month: {average_rainfall_per_month:,} in.''')
