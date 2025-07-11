class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base: float, exp: int) -> float:
            if exp == 0:
                return 1.0
            half = power(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            x = 1 / x
            n = -n

        return power(x, n)
