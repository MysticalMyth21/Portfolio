''' This program calculates the total cost of a holiday
including hotel, flights and car rental costs'''

# Get user input for holiday details
city_flight = str(input("What city are you flying to ? ").strip().title())
num_nights = int(input("How many nights will you be staying at a hotel ? "))
rental_days = int(input("How many days will you be renting a car for ? "))

# Function to calculate the cost of the hotel
def hotel_cost (num_nights):
    # Calculates hotel cost based on rate per night
    cost_per_night = int(1000)
    return num_nights * cost_per_night

#Function to calculate the cost of the flight
def plane_cost (city_flight):
    # Calculates flight cost based on price for destination
    if city_flight == "Cape Town":
        return 2500
    elif city_flight == "Durban":
        return 1500
    elif city_flight == "Johannesburg":
        return 2000
    elif city_flight == "Port Elizabeth":
        return 1800
    else: 
        return 2200

# Function to calculate car rental cost
def rental_car_cost (rental_days):
    # Calculates car rental cost based on daily rate
    daily_rental_cost = int(400)
    return rental_days * daily_rental_cost

# Function to calculate total holiday cost
def holiday_cost (num_nights, city_flight, rental_days):
    # Takes three arguments and calls the other three functions
    return hotel_cost(num_nights) + plane_cost(city_flight) + rental_car_cost(rental_days)

# Calculate individual costs and total holiday cost
total_hotel = hotel_cost(num_nights)
total_plane = plane_cost(city_flight)
total_car = rental_car_cost(rental_days)
total_holiday = holiday_cost(num_nights, city_flight, rental_days)

# Display the formatted summary of all holiday costs
print ("\n--- Holiday Details ---")
print (f"City: {city_flight}")
print (f"Hotel Cost for {num_nights} nights: R{total_hotel}") 
print (f"Plane Cost: R{total_plane}")
print (f"Car Rental Cost for {rental_days} days: R{total_car}")
print (f"Total Holiday Cost: R{total_holiday}")
