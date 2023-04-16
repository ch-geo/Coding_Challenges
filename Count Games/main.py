from test import test_solution
from solution import solution 

testCases = [['12:00', '12:00', 0],
             ['12:00', '12:45', 3],
             ['12:00', '13:00', 4],
             ['12:00', '14:45', 11],
             ['23:30', '00:15', 3],
             ['23:00', '00:00', 4],
             ['23:00', '01:15', 9],
             ['12:00', '12:30', 2],
             ['12:30', '13:00', 2],
             ['12:15', '13:45', 6]]

if __name__ == '__main__':
    
    test_solution(testCases)

    input = ["23:30", "06:15"]
    games_played = solution(input[0], input[1])


