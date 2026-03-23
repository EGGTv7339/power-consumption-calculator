print ("eletrolux fridge power calculator updated 2026")

# data input

power_usage = float(input("insert power usage: "))
time_used = float(input("insert time used (in hours): "))

# processing
daily_consumption_kwh = (power_usage * time_used) / 1000
average_time_used = power_usage / time_used

monthly_consumption_kwh = (daily_consumption_kwh * 30)
final_cost = (monthly_consumption_kwh * 0.85)

# results output
print (f"Monthly Consumption: {monthly_consumption_kwh} kwh.")
print (f"Estimated cost: R$ {final_cost: .2f}")
