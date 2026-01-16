def cummax(x):
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
        return "The list is empty"




def cumsum(x):
    try:
        if len(x) == 0:
            print("Inside")
            raise Exception
        
        output = []
        sumValue = 0

        for num in x:
            if not isinstance(num, int):
                output = []
                sumValue = 0
                raise ValueError
            else:
                output.append(sumValue + num)
                sumValue += num

        return output
    except ValueError:
        return "A valueError occured: A list mustly only contain number!"
    except:
        return "The list is empty!"



def sanitizing(word):
    special_char = ["!",",",".","/","@","#","$","%","^","&","*","(",")","-"]
    output_string = ""
    for char in word:
        if char not in special_char:
            output_string += char

    return output_string

def tokenize(s):
    try:
        if len(s) == 0:
            raise Exception

        words_list = s.lower().split(" ")
        print(words_list)

        output_list = []

        for words in words_list:
            output = sanitizing(words)
            if output not in output_list and len(output) > 0:
                output_list.append(output)
        
        return output_list
    except Exception:
        return "Some error occured!"


def anagram(word_list):
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
        return "The List is empty!"


def biagram(word_list):
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
        return "The List is empty!"
    

def count_words(s):
    try:
        if len(s) == 0:
            raise Exception
        words_list = s.lower().split(" ")
        anagram_dict = anagram(words_list)
        biagram_dict = biagram(words_list)

        return anagram_dict | biagram_dict # type: ignore
    except:
        return "The string is empty!"



def ifelse(test_list, yes_list, no_list):
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
        return "A ValueError occurred: The input lists have different length"
    