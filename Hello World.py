Mileage = 12
Amount_per_litre = 40
Distance_one_way = 190
TotalDistance = 190 * 2
per_head_cost = 40

X = TotalDistance/Mileage
per_head_cost = X * Amount_per_litre / 4

if(per_head_cost % 5 == 0):
    print("True")
else:
    print(per_head_cost)
    print("False")


