from test import test_solution
from solution import solution 

testCases = [["The quick brown fox jumps over the lazy dog", "the"],
            ["The quick brown fox jumps over the lazy dog and the quick brown cat", "the"],
            ["hello", "hello"],
            ["hello hello", "hello"],
            ["The quick brown fox jumps over the lazy dog", "the"],
            ["The quick brown fox jumps over the lazy dog", "the"],
            ["", "No string given"]]

if __name__ == '__main__':
    test_solution(testCases)

    input_str = "Input your string here"
    most_frequent_word = solution(input_str)
    print(most_frequent_word)


