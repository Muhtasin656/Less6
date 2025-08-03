def hotel_cost(nights):
    140*nights
def plane_cost(city):
    if "LA"==city:
        return 475
    elif "London"==city:
        return 300
    elif "Tampa"==city:
        return 220
def rental_car(days):
    if days>=7:
        return 40*days-50
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return rental_car(days)+hotel_cost(days)+plane_cost(city)+spending_money
print("cost of rental car",rental_car(6))
print("cost of plane ride",plane_cost("London"))