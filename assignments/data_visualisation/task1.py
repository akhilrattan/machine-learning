import numpy as np

temperatures = np.random.randint(15, 41, 30)

print("Daily Temperatures:")
print(temperatures)

mean_temp = np.mean(temperatures)

median_temp = np.median(temperatures)

std_temp = np.std(temperatures)

print("\nMean Temperature:", mean_temp)
print("Median Temperature:", median_temp)
print("Standard Deviation:", std_temp)

normalized = (temperatures - np.min(temperatures)) / (
    np.max(temperatures) - np.min(temperatures)
)

print("\nNormalized Temperatures:")
print(normalized)

temp_matrix = temperatures.reshape(5, 6)

print("\nTemperature Matrix (5x6):")
print(temp_matrix)

transpose_matrix = temp_matrix.T

print("\nTranspose Matrix:")
print(transpose_matrix)

rainfall = np.random.randint(1, 20, (5, 6))

print("\nRainfall Matrix:")
print(rainfall)

addition = temp_matrix + rainfall

print("\nAddition:")
print(addition)


multiplication = temp_matrix * rainfall

print("\nMultiplication:")
print(multiplication)