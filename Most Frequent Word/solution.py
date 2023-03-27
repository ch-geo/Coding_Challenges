'''
Given a string str, return the most freequent word. 
Only char stings given.
Bonus: Make it case insensitive
'''

def solution(str):
    # Check if input string is not empty
    if str:
        
        # Split the string into words and convert them to lowercase
        # This way the function is not case sensitive
        words = str.lower().split()
        
        word_count = {}
        max_count = 0
        
        for word in words:
            
            # If the word is already in the dictionary, increase its count
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            
            # If the count of the current word is greater than the maximum count seen so far,
            # update the maximum count and set the most_frequent_word variable to the current word
            if word_count[word] > max_count:
                max_count = word_count[word]
                most_frequent_word = word

            # If the count of the current word is equal to the maximum count seen so far,
            # append the current word to the most_frequent_word variable with a space separator
            elif word_count[word] == max_count:
                most_frequent_word += ' ' + word

        return most_frequent_word
    else:
        return 'No string given'