import numpy as np

temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

temp_mar_np = np.array(temp_mar)

avg_temp = np.mean(temp_mar_np)
print("The average sea surface temperature in 2014 is:", round(avg_temp, 1), "ºC.")

coldest_month_index = np.argmin(temp_mar_np)
coldest_month = months[coldest_month_index]
coldest_temp = temp_mar_np[coldest_month_index]
print("The month in which the sea surface has been coldest is", coldest_month, "with a temperature of", coldest_temp, "ºC.")

warmest_month_index = np.argmax(temp_mar_np)
warmest_month = months[warmest_month_index]
warmest_temp = temp_mar_np[warmest_month_index]
print("The month in which the sea surface has been warmest is", warmest_month, "with a temperature of", warmest_temp, "ºC.")
