# gauss elimination 
# curr_row = specific row iteration # we are on
# pivot = first non-zero element in that row

import numpy as np

def gaussian_elimination(A): 

    pivot_row = 0 

    for pivot_col in range(min(A.shape[0], A.shape[1])):
        
        # Swap row with highest element in col
        max_i = np.argmax(abs(A[pivot_row:, pivot_col]) + pivot_row)
        
        # find highest value in pivot column under current row
        # swap row to current row

        temp = A[pivot_row, :].copy()
        A[pivot_row, :] = A[max_i, :]
        A[max_i, :] = temp

        # find a fraction that corresponds to the ratio of the
        # value in that column to the pivot itself. 
        # Subtract the current pivot row multiplied by 
        # the fraction from each corresponding element

        if A[pivot_row, pivot_col] == 0:
            continue

        # fraction = a(curr_row, piv_col) / A(pivot_row, pivot_col)
        # subtract current_row - fraction * pivot_row

        for r in range(pivot_row +1, A.shape[0]): 
            frac = -A[r, pivot_col] / A[pivot_row, pivot_col]
            # Add rows
            A[r, :] += frac * A[pivot_row, :]
        
        pivot_row += 1

def main():
    A = np.array([[2, 3, 4, 6],
                  [1, 2, 3, 4,],
                  [3, -4, 0, 10]], dtype=float)
    print(A, "\n")
    gaussian_elimination(A)
    print("new", A)


main()