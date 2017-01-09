from my_functions import *
from sample import Sample
import numpy as np
import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_find_next_pixel(self):
	Nx = 3
	Ny = 3
        Jc = np.zeros((Nx,Ny))
        sample = Sample(Jc)
        sample.boolean_matrix[0,1] = False
        sample.boolean_matrix[0,0] = False
        nxt = find_next_pixel(0,0)
        self.assertEqual(nxt, (1,0))
        sample.boolean_matrix[nxt] = False
        nxt = find_next_pixel(nxt)
        self.assertEqual(nxt, (2,0))

        sample.boolean_matrix[nxt] = False
        nxt = find_next_pixel(nxt)
        self.assertEqual(nxt, (2,1))

        sample.boolean_matrix[nxt] = False
        nxt = find_next_pixel(nxt)
        self.assertEqual(nxt, (2,2))

        sample.boolean_matrix[nxt] = False
        nxt = find_next_pixel(nxt)
        self.assertEqual(nxt, (1,2))

        sample.boolean_matrix[nxt] = False
        nxt = find_next_pixel(nxt)
        self.assertEqual(nxt, (0,2))

        sample.boolean_matrix[nxt] = False
        nxt = find_next_pixel(nxt)
        self.assertEqual(nxt, ())
    
    def test_find_zero_neighbours(self):
	Nx = 3
	Ny = 3
        Jc = np.zeros((Nx,Ny))
        sample = Sample(Jc)

        sample.boolean_matrix = np.ones((Nx,Ny), dtype=bool)
        result = sample.find_one_neighbours(1,1)
        expected = [(1,2), (1,0), (2,1), (0,1)]
        self.assertEqual(result, expected)

        sample.boolean_matrix[1,0] = False
        result = sample.find_one_neighbours(0,0)
        expected = [(0,1)]
        self.assertEqual(result, expected)

        sample.boolean_matrix[0,1] = False
        result = sample.find_one_neighbours(0, 0)
        expected = []
        self.assertEqual(result, expected)

        result = sample.find_one_neighbours(2,2)
        expected = [(2,1), (1,2)]
        self.assertEqual(result, expected)


    def test_next_border_element(self):
	Nx = 3
	Ny = 3
	matrix = np.zeros((Nx,Ny))
        start = (0,0)
        expected = ((1,0), (2,0), (2,1), (2,2), (1,2), (0,2), (0,1), (0,0))

        for ex in expected:
            out = next_border_element(matrix, Nx, Ny, start[0], start[1])
            self.assertEqual(out, ex)
            start = out

    def test_is_on_boundary(self):
	Nx = 3
	Ny = 3
        Jc = np.zeros((3,3))
        sample = Sample(Jc)

        self.assertTrue(sample.is_on_boundary(0, 0))
        self.assertTrue(sample.is_on_boundary(0, 1))
        self.assertTrue(sample.is_on_boundary(0, 2))
        self.assertTrue(sample.is_on_boundary(2, 0))
        self.assertTrue(sample.is_on_boundary(2, 1))
        self.assertTrue(sample.is_on_boundary(2, 2))
        self.assertTrue(sample.is_on_boundary(1, 0))
        self.assertTrue(sample.is_on_boundary(1, 2))

        self.assertFalse(sample.is_on_boundary(1, 1))

if __name__ == '__main__':
    unittest.main()

'''
def zero_neighbours(boolean_matrix, i, j):
    options = []
    if boolean_matrix[i, j+1] == 0:
        options.append((i, j+1))
    if boolean_matrix[i, j-1] == 0:
        options.append((i, j-1))
    if boolean_matrix[i+1, j] == 0:
        options.append((i+1, j))
    if boolean_matrix[i-1, j] == 0:
        options.append((i-1, j))
'''
