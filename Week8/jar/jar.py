class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies if not 0 else 0

    def deposit(self, n):
        if n < 0 or self._cookies +n > self._capacity:
            raise ValueError(f"Can't have more than {self._capacity}")
        self._cookies += n

    def withdraw(self, n):
        if n < 0 or self._cookies < n:
            raise ValueError()
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
