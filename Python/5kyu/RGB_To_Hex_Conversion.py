"""
Instructions:

The rgb() method is incomplete.
Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned.
The valid decimal values for RGB are 0 - 255.
Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb(r, g, b):
    def rgb_round(x):
        return min(255, max(x, 0))
    return ("{:02X}" * 3).format(rgb_round(r), rgb_round(g), rgb_round(b))


if __name__ == '__main__':
    print(hex(3))
    print(rgb(1, 3, 4))  # returns FFFFFF
    print(rgb(255, 255, 300))  # returns FFFFFF
    print(rgb(0, 0, 0))  # returns 000000
    print(rgb(148, 0, 211))  # returns 9400D3)
