import math
class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("A vector must have at least one component.")
        self.components = list(components)
        self.dimension = len(components)
    
    def __str__(self):
        return f"Vector({str(self.components)[1:-1]})"
        
    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Vectors can't be added.")
        return Vector(*[a+b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Vectors can't be subtracted")
        return Vector(*[a-b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[a*other for a in self.components])
        elif isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise ValueError("Vectors can't be dot producted")   
            return sum(a*b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Unsupported operations with *. ")
                    
    def __rmul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        return self.__mul__(scalar)

    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Zero vector can't be normalized")
        return Vector(*[round(a / mag, 3) for a in self.components])


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(f"Sum: {v3}")          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(f"Subtraction: {v4}")          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(f"Dot product: {dot_product}") # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(f"Scalar multiplication: {v5}")          # Output: Vector(3, 6, 9)

# Magnitude
print(f"Magnitude: {v1.magnitude()}")  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(f"Norm: {v_unit}")      # Output: Vector(0.267, 0.534, 0.801)
