class Matrix:
    """"
    Defining the constructor

    ul = upper left
    ur = upper right
    bl = below left
    br = below right
    """
    def __init__(self, ul, ur, bl, br):
        self.__ul = ul
        self.__ur = ur
        self.__bl = bl
        self.__br = br

    # Getters and setters

    def get_ul(self):
        return self.__ul

    def set_ul(self, ul):
        self.__ul = ul

    def get_ur(self):
        return self.__ur

    def set_ur(self, ur):
        self.__ur = ur

    def get_bl(self):
        return self.__bl

    def set_bl(self, bl):
        self.__bl = bl

    def get_br(self):
        return self.__br

    def set_br(self, br):
        self.__br = br

    # define the 2 methods

    def add(self, matrix):
        ul = self.__ul + matrix.get_ul()
        ur = self.__ur + matrix.get_ur()
        bl = self.__bl + matrix.get_bl()
        br = self.__br + matrix.get_br()
        return Matrix(ul, ur, bl, br)

    # to do
    def mul(self, matrix):
        ul = (self.__ul * matrix.get_ul()) + (self.__ur * matrix.get_bl())
        ur = (self.__ul * matrix.get_ur()) + (self.__ur * matrix.get_br())
        bl = (self.__bl * matrix.get_ur()) + (self.__br * matrix.get_bl())
		br = (self.__bl * matrix.get_ur()) + (self.__br * matrix.get_bl())
		return Matrix(ul, ur, bl, br)

    # define the toString() method

    def __str__(self):
        return str(self.__ul) + " " + str(self.__ur) + " " + str(self.__bl) + " " + str(self.__br)

if __name__ == '__main__':

	matrix_1 = Matrix(4,5,6,7)

	print(matrix_1)

	matrix_2 = Matrix(2,2,2,1)

	print(matrix_2)

	matrix_3 = matrix_2.add(matrix_1)

	print(matrix_3)
	
	matrix_4 = matrix_2.mul(matrix_1)
	
	print(matrix_4)
