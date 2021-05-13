from and_gate import AND
from or_gate import OR
from nand_gate import NAND

def NOT(x):
    return NAND(x,x)

def NAND_AND(x1, x2):
    y = NAND(x1,x2)
    return NOT(y)

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = NAND_AND(xs[0], xs[1])
        print('OR'+str(xs) + " -> " + str(y))
