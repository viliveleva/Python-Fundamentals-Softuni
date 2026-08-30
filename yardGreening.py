kv_meters = int(input())
one_kv_meters = 7.61
all_meters = kv_meters * one_kv_meters
price = all_meters * 0.18
final_price = all_meters - price
print(f"The final price is {final_price} lv.")
print(f"The discount is {price} lv.")