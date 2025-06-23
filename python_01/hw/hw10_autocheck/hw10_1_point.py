from random import randrange

class Point:
 
    def __init__(self,x,y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, x):
        if type(x) == int or type(x) == float:
            self.__x = x

    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            print("Error: invalid index")
        
    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        
        if index == 1:
            return self.coordinates.y
    
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
    
    def __call__(self, value = None):
        return (self.coordinates.x*value, self.coordinates.y*value) if value else (self.coordinates.x, self.coordinates.y)
        
    def __add__(self, vector):
        new_x = self.coordinates.x + vector[0]
        new_y = self.coordinates.y + vector[1]
        return Vector(Point(new_x, new_y))

    def __sub__(self, vector):
        new_x = self.coordinates.x - vector[0]
        new_y = self.coordinates.y - vector[1]
        return Vector(Point(new_x, new_y))
    
    def __mul__(self, vector):
        return self.coordinates.x * vector[0] + self.coordinates.y * vector[1]
    
    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return not (self == vector)

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()  


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []

        for _ in range(randrange(max_vectors)):
            point = Point(randrange(max_points),randrange(max_points))
            self.vectors.append(point)
        
    def __next__(self):
        if self.current_index < len(self.vectors):
            current_vector = self.vectors[self.current_index]
            self.current_index += 1
            return current_vector
        
        raise StopIteration
        

class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors,self.max_points)


########### __init__ and getter/setter ###########      
point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10 

point.x = 6
point.y = 8

print(point.x)  # 6
print(point.y)  # 8

########### Vector ###############################
point2 = Point("14", "9")

print(point2.x)  # 6
print(point2.y)  # 8 

########### __getitem__/__setitem__ ##############
vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Встановлюємо координату x вектора 10

print(vector[0])  # 10
print(vector[1])  # 10

############# __str__ ############################
point = Point(1, 10)
vector = Vector(point)

print(point)  # Point(1,10)
print(vector)  # Vector(1,10)

############# __call__ ###########################
vector = Vector(Point(1, 10))
print(vector())  # (1, 10)

vector = Vector(Point(1, 10))
print(vector(5))  # (5, 50)

##############__add__/__sub__#####################
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)

############## __mul__ ###########################
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

scalar = vector2 * vector1

print(scalar)  # 110

############### len ##############################
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

print(vector1.len())  # 10.04987562112089
print(vector2.len())  # 14.142135623730951

################ comparison ######################
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))

print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True

################ __iter / __next__ ################
vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)
