calories=[320 ,550, 210, 480, 600, 150, 400]
heavy_meals= []
for num in calories:
     if num >= 400:
         heavy_meals.append(num)
print(heavy_meals)

