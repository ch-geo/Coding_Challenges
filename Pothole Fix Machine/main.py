from test import test_solution
from solution import solution 

testCases = [["", 0],
             [".......", 0],
             ["....x....", 1],
             ["..x..x..x..", 3],
             ["x..x..x...", 3],
             ["...x..x..x", 3],
             ["abc", 0],
             ["....x....x....", 2],
             ["." * 1000000 + "x" + "." * 1000000, 1],
             ["x" * 1000000, 333334],
             ["x.x.x.x.x.x.x.x.x.x.x.x.x", 7],
             ["xxx...xxx.xx", 3]]



if __name__ == '__main__':
    test_solution(testCases)
    
    input = ".x.x.x.x.x."
    min_moves = solution(input)
    print(min_moves)