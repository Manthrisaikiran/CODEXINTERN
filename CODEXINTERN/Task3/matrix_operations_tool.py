# ============================================================
# Project: CODEXINTERN - Task 3
# Title: Matrix Operations Tool using NumPy
# ============================================================
# Description:
# This Python program allows users to input two square matrices 
# and perform basic matrix operations using NumPy. 
# Supported operations include:
#   1. Addition (A + B)
#   2. Subtraction (A - B)
#   3. Multiplication (A × B)
#   4. Transpose of matrices
#   5. Determinant calculation
# The program features an interactive command-line interface
# to display results in a structured and clear format.
# ============================================================

import numpy as np

def input_matrix(n):
    """Takes user input to create a matrix of size n x n"""
    print(f"\nEnter elements row by row for a {n}x{n} matrix:")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print(f"Invalid row length! Please enter exactly {n} elements.")
            return input_matrix(n)
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix, name="Result"):
    """Displays a matrix with a title"""
    print(f"\n{name}:")
    print(matrix)

def matrix_operations():
    """Interactive menu for performing matrix operations"""
    print("\n==== MATRIX OPERATIONS TOOL ====")
    n = int(input("Enter size of square matrices (n x n): "))
    
    print("\n--- Matrix A ---")
    A = input_matrix(n)
    print("\n--- Matrix B ---")
    B = input_matrix(n)

    while True:
        print("\nChoose Operation:")
        print("1. Addition (A + B)")
        print("2. Subtraction (A - B)")
        print("3. Multiplication (A × B)")
        print("4. Transpose of A and B")
        print("5. Determinant of A and B")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            result = A + B
            display_matrix(result, "A + B")

        elif choice == '2':
            result = A - B
            display_matrix(result, "A - B")

        elif choice == '3':
            result = np.dot(A, B)
            display_matrix(result, "A × B")

        elif choice == '4':
            display_matrix(A.T, "Transpose of A")
            display_matrix(B.T, "Transpose of B")

        elif choice == '5':
            det_A = np.linalg.det(A)
            det_B = np.linalg.det(B)
            print(f"\nDeterminant of A: {det_A:.2f}")
            print(f"Determinant of B: {det_B:.2f}")

        elif choice == '6':
            print("\nExiting Matrix Operations Tool. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please select an option between 1–6.")

if __name__ == "__main__":
    matrix_operations()
