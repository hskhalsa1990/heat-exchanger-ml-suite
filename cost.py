def total_cost(Area, U, Q, dp_hot, dp_cold, hours=8000):
    # Capital Cost - Peters & Timmerhaus correlation
    capital = 20000 + 1500 * (Area ** 0.8)
    # Pumping Cost
    pump_power = (dp_hot + dp_cold) * 0.001 * 50 / 0.7
    operating = pump_power * hours * 0.12
    # Energy Saving vs Old Design
    return {'Capital_Cost_USD': round(capital,2), 'Annual_Operating_USD': round(operating,2), 'Total_Annual_Cost': round(capital/10 + operating,2)}