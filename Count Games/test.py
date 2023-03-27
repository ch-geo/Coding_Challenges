from solution import solution 

def test_solution(test_cases):
    for id, test in enumerate(test_cases):
        try:
            assert solution(test[0], test[1]) == test[2]
        except AssertionError:
            print('Test Id:', id, '|| For input: "', test[0], '", "', test[1], '" got "', solution(test[0], test[1]), '" instead of "', test[2],'"')
        else:
            print('Test Id:', id, 'Successful')