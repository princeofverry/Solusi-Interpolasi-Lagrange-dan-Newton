import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Lagrange interpolation function


def lagrange_interpolation(x, y, xp):
    yp = 0
    n = len(x)
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += p * y[i]
    return yp

# Newton interpolation function


def newton_interpolation(x, y, xp):
    n = len(x)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = (diff_table[i + 1, j - 1] -
                                diff_table[i, j - 1]) / (x[i + j] - x[i])

    yp = 0
    product_terms = 1
    for i in range(n):
        yp += diff_table[0, i] * product_terms
        product_terms *= (xp - x[i])
    return yp

# Testing the interpolations


def test_interpolations():
    # Test points
    test_points = [7.5, 17.5, 27.5, 37.5]

    print("Lagrange Interpolation Tests")
    for point in test_points:
        print(f"x = {point}: y = {lagrange_interpolation(x, y, point)}")

    print("\nNewton Interpolation Tests")
    for point in test_points:
        print(f"x = {point}: y = {newton_interpolation(x, y, point)}")


# Run tests
test_interpolations()

# Interpolation over the range 5 <= x <= 40
x_test = np.linspace(5, 40, 100)
y_lagrange = [lagrange_interpolation(x, y, xp) for xp in x_test]
y_newton = [newton_interpolation(x, y, xp) for xp in x_test]

# Plotting Lagrange Interpolation
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro', label='Data points')
plt.plot(x_test, y_lagrange, 'b-', label='Lagrange Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Polinom Lagrange')
plt.grid(True)
plt.savefig('lagrange_interpolation.png')
plt.show()

# Plotting Newton Interpolation
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro', label='Data points')
plt.plot(x_test, y_newton, 'g--', label='Newton Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Polinom Newton')
plt.grid(True)
plt.savefig('newton_interpolation.png')
plt.show()

# Plotting Both Interpolations
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro', label='Data points')
plt.plot(x_test, y_lagrange, 'b-', label='Lagrange Interpolation')
plt.plot(x_test, y_newton, 'g--', label='Newton Interpolation')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Polinom Lagrange dan Newton')
plt.grid(True)
plt.savefig('combined_interpolation.png')
plt.show()
