import numpy as np
import pandas as pd

bills = np.array([1500, 2500, 3500, 4000, 2000, 5000])

print("Mean Bill:", np.mean(bills))
print("Median Bill:", np.median(bills))
print("Maximum Bill:", np.max(bills))
print("Minimum Bill:", np.min(bills))

df = pd.DataFrame({
    'Consumer': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Electricity Bill': bills
})

print("\nElectricity Bill Data:")
print(df)

print("\nConsumers with bills above 3000:")
print(df[df['Electricity Bill'] > 3000])
