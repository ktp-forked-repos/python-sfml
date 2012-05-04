class Size:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __repr__(self):
        return "({0}, {1})".format(self.width, self.height)

    def __str__(self):
        return "({0}, {1})".format(self.width, self.height)

    def __iter__(self):
        return iter((self.width, self.height))

    def __getitem__(self, key):
        if key == 0: return self.width
        else: return self.height
        
    def __setitem__(self, key, value):
        if key == 0: self.width = value
        else: self.height = value
        
    def __add__(self, other):
        x, y = other
        return Size(max(self.width + x, 0), max(self.height + y, 0))

    def __sub__(self, other):
        x, y = other
        return Size(max(self.width - x, 0), max(self.height - y, 0))
        
    def __mul__(self, other):
        x, y = other
        return Size(max(self.width * x, 0), max(self.height * y, 0))
        
    def __truediv__(self, other):
        x, y = other
        return Size(max(self.width / x, 0), max(self.height / y, 0))
        
    def __floordiv__(self, other):
        x, y = other
        return Size(max(self.width // x, 0), max(self.height // y, 0))

    def __mod__(self, other):
        x, y = other
        return Size(max(self.width % x, 0), max(self.height % y, 0))

    def __divmod__(self, other):
        return self // other, self % other

    def __radd__(self, other):
        x, y = other
        return Size(max(x + self.width, 0), max(y + self.height, 0))

    def __rsub__(self, other):
        x, y = other
        return Size(max(x - self.width, 0), max(y - self.height, 0))

    def __rmul__(self, other):
        x, y = other
        return Size(max(x * self.width, 0), max(y * self.height, 0))
        
    def __rtruediv__(self, other):
        x, y = other
        return Size(max(x / self.width, 0), max(y / self.height, 0))
        
    def __rfloordiv__(self, other):
        x, y = other
        return Size(max(x // self.width, 0), max(y // self.height, 0))
        
    def __rmod__(self, other):
        x, y = other
        return Size(max(x % self.width, 0), max(y % self.height, 0))
        
    def __iadd__(self, other):
        x, y = other
        
        self.width += x
        self.height += y
        
        if self.width < 0: self.width = 0
        if self.height < 0: self.height = 0
        
        return self
        
    def __isub__(self, other):
        x, y = other
        
        self.width -= x
        self.height -= y
        
        if self.width < 0: self.width = 0
        if self.height < 0: self.height = 0
        
        return self
        
    def __imul__(self, other):
        x, y = other
        
        self.width *= x
        self.height *= y
        
        if self.width < 0: self.width = 0
        if self.height < 0: self.height = 0
        
        return self
        
    def __itruediv__(self, other):
        x, y = other
        
        self.width /= x
        self.height /= y
        
        if self.width < 0: self.width = 0
        if self.height < 0: self.height = 0
        
        return self
        
    def __ifloordiv__(self, other):
        x, y = other
        
        self.width //= x
        self.height //= y
        
        if self.width < 0: self.width = 0
        if self.height < 0: self.height = 0
        
        return self
        
    def __imod__(self, other):
        x, y = other
        
        self.width %= x
        self.height %= y
        
        if self.width < 0: self.width = 0
        if self.height < 0: self.height = 0
        
        return self
        
    def __lt__(self, other):
        x, y = other
        return self.width < x or self.height < y
        
    def __le__(self, other):
        x, y = other
        return self.width <= x or self.height <= y
        
    def __eq__(self, other):
        x, y = other
        return self.width == x and self.height == y
        
    def __ne__(self, other):
        x, y = other
        return self.width != x or self.height != y
        
    def __gt__(self, other):
        x, y = other
        return self.width > x or self.height > y
        
    def __ge__(self, other):
        x, y = other
        return self.width >= x or self.height >= y
            
    def _get_width(self):
        return self._width

    def _set_width(self, width):
        self._width = width

    def _get_height(self):
        return self._height

    def _set_height(self, height):
        self._height = height

    width = property(_get_width, _set_width)
    height = property(_get_height, _set_height)