import numpy as np
import pandas as pd

rents = np.array([2000, 3500, 4500, 5000, 3000, 6000])

print("Mean Rent:", np.mean(rents))
print("Median Rent:", np.median(rents))
print("Maximum Rent:", np.max(rents))
print("Minimum Rent:", np.min(rents))

df = pd.DataFrame({
    'Room': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
    'Room Rent': rents
})

print("\nHotel Room Rent Data:")
print(df)

print("\nRooms with rent above 4000:")
print(df[df['Room Rent'] > 4000])
