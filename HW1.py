def cummax(x):
    """
    Input: Take a list as a parameters
    Input:
        x (list): A list of comparable elements.

    Description:
        Returns a list where each element is the maximum value seen so far.
        Prints a ValueError message and returns None if the list is empty.

    Output:
        list or None
    """
    try:

        if len(x) == 0:
            raise ValueError

        previous_max = x[0]
        output = []
        for i in x:
            if i >= previous_max:
                previous_max = i
            
            output.append(previous_max)
        return output
    except ValueError:
        print("A ValueError occurred: the input list is an empty list")
        return None 




def cumsum(x):
    """
    Input:
        x (list): A list of integers.

    Description:
        Returns a list of cumulative sums of the elements in the list.
        Prints a ValueError message and returns None if the list contains
        non-integer values or is empty.

    Output:
        list or None
    """
    try:
        if x == None or len(x) == 0:
            return []
        
        output = []
        sumValue = 0

        for num in x:
            if not isinstance(num, (int,float)):
                output = []
                sumValue = 0
                raise ValueError
            else:
                output.append(sumValue + num)
                sumValue += num

        return output
    except ValueError:
        print("A ValueError occurred: List must contain only numbers")
        return None



def sanitizing(word):
    special_char = ["!",",",".","/","@","#","$","%","^","&","*","(",")","-","?"]
    output_string = ""
    for char in word:
        if char not in special_char:
            output_string += char

    return output_string

def unique_tokens(s):
    """
    Input:
        s (str): A string of words.

    Description:
        Tokenizes the string into lowercase, alphanumeric-only words
        and returns a list of unique tokens.
        Prints an error message and returns None if the string is empty.

    Output:
        list or None
    """
    if len(s) == 0:
        return []

    words_list = s.lower().split(" ")

    output_list = []

    for words in words_list:
        output = sanitizing(words)
        if output not in output_list and len(output) > 0:
            output_list.append(output)
        
    return output_list


def anagram(word_list):
    """
    Input:
        word_list (list): A list of strings.

    Description:
        Returns a dictionary counting occurrences of each sanitized anagram.
        Prints an error message and returns None if the list is empty.

    Output:
        dict or None
    """
    try:
        output_dict = {}
        if len(word_list) == 0:
            raise Exception

        for i in word_list:
            sanitized_string = sanitizing(i)

            if sanitized_string in output_dict:
                output_dict[sanitized_string] += 1
            else:
                output_dict[sanitized_string] = 1
            
        return output_dict
    except Exception:
        print("The list is empty!") 
        return None 


def biagram(word_list):
    """
    Input:
        word_list (list): A list of strings.

    Description:
        Returns a dictionary counting occurrences of sanitized word pairs
        (bigrams) from consecutive elements in the list.
        Prints an error message and returns None if the list is empty.

    Output:
        dict or None
    """
    try:
        output_dict = {}
        if len(word_list) == 0:
            raise Exception

        for i in range(0, len(word_list) - 1):
            merged_words = word_list[i] + " " + word_list[i + 1]
            sanitized_string = sanitizing(merged_words)
            if sanitized_string not in output_dict:
                output_dict[sanitized_string] = 1
            else:
                output_dict[sanitized_string] += 1
            
        return output_dict
    except Exception:
        print("The list is empty!") 
        return None 
    

def count_words(s):
    """
    Input:
        s (str): A string of words.

    Description:
        Returns a dictionary containing counts of anagrams and bigrams
        from the input string.
        Prints an error message and returns None if the string is empty.

    Output:
        dict or None
    """
    try:
        if len(s) == 0:
            raise Exception
        words_list = s.lower().split(" ")
        anagram_dict = anagram(words_list)
        biagram_dict = biagram(words_list)

        return anagram_dict | biagram_dict # type: ignore
    except:
        print("The list is empty!") 
        return None 



def ifelse(test_list, yes_list, no_list):
    """
    Input:
        test_list (list): A list of boolean values.
        yes_list (list): A list of values used when test_list is True.
        no_list (list): A list of values used when test_list is False.

    Description:
        Returns a list where elements are selected from yes_list or no_list
        based on the corresponding boolean value in test_list.
        Prints an error message and returns None if the lists are empty
        or have different lengths.

    Output:
        list or None
    """
    try:
        if len(test_list) == 0:
            raise Exception
        elif len(test_list) != len(yes_list) or len(test_list) != len(no_list):
            raise Exception

        output_list = []

        for i in range(0, len(test_list)):
            if test_list[i]:
                output_list.append(yes_list[i])
            else:
                output_list.append(no_list[i])
            
        
        return output_list
    except Exception:
        print("A ValueError occurred: The input lists have different length")
        return None
    