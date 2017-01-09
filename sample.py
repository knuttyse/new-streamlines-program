import numpy as np
sqrt = np.sqrt

class Sample:
    
    def __init__(self, Jc):
        self.shape = np.shape(Jc)
        self.Jc = Jc
        self.Jx = np.zeros(self.shape)
        self.Jy = np.zeros(self.shape)
        self.Nx = self.shape[0]
        self.Ny = self.shape[1]

    # ---------------------------------------------
    # Functions for finding a new starting position:

    """
    Given a list of positions (rectangle), returns the position
    with the highest value of Jc and zero current.
    If (-1, -1) is returned, it means that it is time to stop
    the simulation.
    """
    def find_max_element(self, rectangle):
        maxJc = -1
        max_pos = (-1,-1)

        for pos in rectangle:
            localJc = self.Jc[pos]

            # If Jc is larger and there is no current in the pixel:
            if localJc > maxJc and self.Jx[pos] == 0 and self.Jy[pos] == 0:
                maxJc = localJc
                max_pos = pos

        return max_pos        
        
    """
    Returns the n-th outermost position elements in the sample.
    It is used for finding a suitable starting point for pushing 
    current.
    """
    def find_rectangle(self, n):
        indices = []        
        for i in range(n, Nx-n):
            indices.append(i, n)
            indices.append(i, Ny-n)
        for j in range(n+1, Ny-n-1):
            indices.append(j, n)
            indices.append(j, Ny-n)        

    def find_new_start(self, n):
        rectancle = self.find_rectangle(n)
        return self.find_max_element(rectangle)
    # ---------------------------------------

    """
    Finds the general starting direction of the new stream.
    This is done by finding the average direction of the 
    vector field from the neighbours.
    """
    def general_starting_direction(self, starting_point):
        i,j = starting_point
        neighbours = self.all_neighbours(i, j)
        neighbours_Jx = [self.Jx[n] for n in neighbours]
        neighbours_Jy = [self.Jy[n] for n in neighbours]
        avgx = sum(neighbours_Jx)/len(neighbours_Jx)
        avgy = sum(neighbours_Jy)/len(neighbours_Jy)
        return avgx, avgy

    """
    Given a starting point, starts a new stream.
    """
    def start_new(self, starting_point):
        i, j = starting_point
        if (i, j) == (-1, -1):
            return -1
        jx, jy = self.general_starting_direction(starting_point)
        vx, vy = np.sign(jx), np.sign(jy)
        last_pos = starting_point[0]-vx, starting_point[1]-vy

        Jx, Jy = 0,0
        if abs(jx) > abs(jy):
            Jx = self.Jc[starting_point]
        else:
            Jy = self.Jc[starting_point]

        result = self.push_current(i, j, last_pos, Jx, Jy)
        return result

    #----------------------------------------
    """
    Returns the distance between the edge marked 
    with axis and k.
    """
    def distance_from_edge(self, k, axis):
        N = self.shape[axis]
        return min(abs(k-N), abs(N-k))

    def minimum_distance_from_edges(self, pos):
        one = distance_from_edge(self, pos[0], 0)
        two = distance_from_edge(self, pos[1], 1)
        return one, two

    """
    get the compare function evaluated at position (i,j)
    """
    def get_compare1(self, pos1, pos2, i, j):
        """
        Compare the priority of two positions.
        The pixel closest to the previous pixel
        is prioritized.
        """
        def compare1(self, pos1, pos2, i=i, j=j):
            neighbours_of_previous_position = self.diag_neighbours(i, j)
            pos1_is_close = pos1 in neighbours_of_previous_position
            pos2_is_close = pos2 in neighbours_of_previous_position
            return pos1_is_close - pos2_is_close
        return compare1
        
    """
    Which pixel is closest to an edge?
    """
    def compare2(self, pos1, pos2):

        distances1 = self.minimum_distance_from_edges(pos1)
        distances2 = self.minimum_distance_from_edges(pos2)

        if min(distance1) == distance2:
            
        return distance1 > distance2 - distance1 < distance2

    """
    From 3 canditates, sort after priorities:

    """
    def prioritize(self, i, j, candidates):
        compare1 = get_compare1(self, pos1, pos2, i, j):
        #sorted(myList, key=lambda x: -fitness(x))
        sorted(candidates, key=lambda x: -fitness(x))

    """
    Push current Jx, Jy into i, j
    Either Jx == 0 or Jy == 0
    last_pos might be an out of range of the sample!!!!
    """
    def push_current(self, i, j, last_pos, Jx, Jy):
        if Jx*self.Jx[i,j] < 0 or Jy*self.Jy[i,j] < 0:
            return (0,0)
        candidates = self.orthog_neighbours(i, j):
        candidates.remove(last_pos)
        
        legal = [c for c in candidates if self.J_in(c[0], c[1])/Jc[c]<1]

        # Remember to remove candidates that have 
        # opposing sign in the current!!!

        pushedJx = # ????
        pushedJy = # ????
        for pos in legal:
            if Jx > epsilon and Jy > epsilon:
                return 0
            pushedJx, pushedJy = self.push_current():
            Jx -= pushedJx
            Jy -= pushedJy
        
        if success:
            return True
        else:
            self.jx[i,j] -= jx
            self.jy[i,j] -= jy


    """
    The neighbours that are like:
    ______
    |_N_N_|
    |__O__|
    |_N_N_|
    """
    def diag_neighbours(self, i, j):
        neighbours = []
        if i+1 < self.Nx and j+1 < self.Ny:
            neighbours.append((i+1, j+1))
        if i-1 >= 0 and j-1 >= 0:
            neighbours.append((i-1, j-1))
        if i-1 >= 0 and j+1 < Ny:
            neighbours.append((i-1, j+1))
        if i+1 >= 0 and j-1 >= 0:
            neighbours.append((i+1, j-1))

    """
    The neighbours that are like:
    ______
    |__N__|
    |_NON_|
    |__N__|
    """
    def orthog_neighbours(self, i, j):
        neighbours = []
        if j+1 < self.Ny:
            neighbours.append((i, j+1))
        if j-1 >= 0:
            neighbours.append((i, j-1))
        if i+1 < self.Nx:
            neighbours.append((i+1, j))
        if i-1 >= 0:
            neighbours.append((i-1, j))
        return neighbours
        
    """
    Return all neighbours of a pixel
    ______
    |_XXX_|
    |_XOX_|
    |_XXX_|
    """
    def all_neighbours(self, i, j):
        neighbours = []
        neighbours.append(orthog_neighbours(self, i, j))
        neighbours.append(diag_neighbours(self, i, j))
        return neighbours

    def find_next_pixel(self, i, j):
        diagonal_neighbours = diag_neighbours(self, i, j)
        orthogonal_neighbours = orthog_neighbours(self, i, j)

    """
    Current out of pixel (i,j)
    """
    def J_out(self, i, j):
        return sqrt(self.jx**2 + self.jy**2)

    """
    Current into pixel (i,j)
    """
    def J_in(self, i, j):
        neighbours = self.orthog_neighbours(self, i, j)
        Jx = 0.0
        Jy = 0.0
        for x, y in neighbours:
            if self.Jx[x,y] > 0 and i > x:
                Jx += self.Jx[x,y]
            if self.Jx[x,y] < 0 and i < x:
                Jx += self.Jx[x,y]
            if self.Jy[x,y] > 0 and j > y:
                Jy += self.Jy[x,y]
            if self.Jy[x,y] < 0 and j < y:
                Jy += self.Jy[x,y]        
        return (Jx, Jy)

    """
    Returns True if the pixel is on the boundary.
    """
    def is_on_boundary(self, i, j):
        return i == 0 or i == self.Nx-1 or j == 0 or j == self.Ny-1:

    """
    Returns a list of neighbours (list of tuples) that have True as value 
    in the boolean matrix. Does not return indices that are
    out of bounds or (i,j) itself.
    """
    def find_one_neighbours(self, i, j):
        options = []
        if j+1 < self.Ny and self.boolean_matrix[i, j+1] == 1:
            options.append((i, j+1))
        if j-1 >= 0 and self.boolean_matrix[i, j-1] == 1:
            options.append((i, j-1))
        if i+1 < self.Nx and self.boolean_matrix[i+1, j] == 1:
            options.append((i+1, j))
        if i-1 >= 0 and self.boolean_matrix[i-1, j] == 1:
            options.append((i-1, j))
        return options
