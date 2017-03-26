
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        import re
        m1 = re.match(r'(-?\d+)\+(.*?)i', a)
        a1 = int(m1.group(1))
        b1 = int(m1.group(2))
        m2 = re.match(r'(-?\d+)\+(.*?)i', b)
        a2 = int(m2.group(1))
        b2 = int(m2.group(2))
        r1 = a1*a2 - (b1*b2)
        r2 = a1*b2 + a2*b1
        r = '{}+{}i'.format(r1, r2)
        return r

        


class Test(unittest.TestCase):

    def test(self):
        case = ["1+-1i", "1+-1i"]
        assert Solution().complexNumberMultiply(case[0], case[1]) == "0+-2i"
        case = ["1+1i", "1+1i"]
        assert Solution().complexNumberMultiply(case[0], case[1]) == "0+2i"
        case =["78+-76i", "-86+72i"]
        assert Solution().complexNumberMultiply(case[0], case[1]) == "-1236+12152i"
        case = ["1+0i", "1+0i"]
        assert Solution().complexNumberMultiply(case[0], case[1]) == '1+0i'

if __name__ == '__main__':
    unittest.main()
