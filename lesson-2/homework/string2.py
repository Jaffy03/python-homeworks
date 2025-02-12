txt = 'LMaasleitbtui'.lower()
car_brands=['BMW', "Tesla", "Lambo","Mitsubishi", "Honda", "Maseratti", "Toyota"]
for car in car_brands:
    car_lower=car.lower()
    match = True
    for i in car_lower:

        count=1
        for j in txt:
            count+=1
            if i==j:
                break
            elif count>len(txt):
                match=False
    if match:
        print(car)

            
            