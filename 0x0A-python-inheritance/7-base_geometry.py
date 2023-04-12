#!/usr/bin/python3

"""python3 -c 'print(__import__("7-base_geometry").__doc__)"""
class BaseGeometry:
    """Reprsent base geometry.
       python3 -c 'print(__import__("my_module").MyClass.__doc__)	
    """

    def area(self):
        """Not yet implemented.
           python3 -c 'print(__import__("7-base_geometry").area.__doc__)
	"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """python3 -c 'print(__import__("7-base_geometry").integer_validator.__doc__)
	Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
