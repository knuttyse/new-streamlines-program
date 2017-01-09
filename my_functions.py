import numpy as np
np = np
#np.zeros = np.zeros

def find_next_pixel(bool_matrix, i, j, direction_x, direction_y):
    neighbours = find_zero_neighbours(boolean_matrix, i, j, Nx, Ny)
    
    return (k, j)

def next_border_element(matrix, Nx, Ny, i, j):
	# corners:
	if i == 0 and j == 0:
		return 1, j
	if i == Nx-1 and j == 0:
		return i, j+1
	if i == Nx-1 and j == Ny-1:
		return i-1, j
	if i == 0 and j == Ny-1:
		return i, j-1
	# along the sides:
	if i == 0:
		return i, j-1
	if i == Nx-1:
		return i, j+1
	if j == 0:
		return i+1, j
	if j == Ny-1:
		return i-1, j
	else:
		return (-1,-1)
