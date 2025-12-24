daily_sales = [10, 30, 60, 65, 45]

total_cups = sum(sales for sales in daily_sales if sales >20) 
print(total_cups)
