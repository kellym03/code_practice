import numpy as np

# Define the vectors
a = np.array([3, -1, 2])
b = np.array([0, -1, 1])

# 1. Calculate the dot product (a . b)
dot_product = np.dot(a, b)
# (3*0) + (-1*-1) + (2*1) = 0 + 1 + 2 = 3

# 2. Calculate the magnitude (norm) of each vector
norm_a = np.linalg.norm(a)
# sqrt(3^2 + (-1)^2 + 2^2) = sqrt(9 + 1 + 4) = sqrt(14) ≈ 3.7417
norm_b = np.linalg.norm(b)
# sqrt(0^2 + (-1)^2 + 1^2) = sqrt(0 + 1 + 1) = sqrt(2) ≈ 1.4142

# 3. Calculate the cosine of the angle
cos_theta = dot_product / (norm_a * norm_b)
# 3 / (sqrt(14) * sqrt(2)) ≈ 0.5669

# 4. Calculate the angle in degrees
angle_radians = np.arccos(cos_theta)
angle_degrees = np.degrees(angle_radians)
# 55.462... degrees

# 5. Round the angle to the nearest degree
rounded_angle = round(angle_degrees)

print(rounded_angle)