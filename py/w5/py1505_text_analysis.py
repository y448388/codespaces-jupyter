# ‐--‐‐‐--‐-‐-‐‐-‐-‐‐-‐‐‐--‐-‐--‐------‐--‐-‐-‐‐-‐--‐--‐-‐-‐‐-‐‐‐‐‐‐-‐‐-‐-‐‐---‐--‐-‐--‐-‐-‐‐---‐‐-
#
# 1. Add the function `countTextWords' that implements Algorithm 1 (see Canvas). The map shall be
#    returned as a Python dictionary. You can test your code using the provided files
#    text-ironic.txt and text-robinson-crusoe.txt.
#
# 2. Some of the words that occur only once do so because they appear in uppercase or contain
#    special symbols like colons, parentheses, dots, etc.. Create a function `simplifyWord' that
#    has one string argument w. It shall return the lowercase version of w with each of the
#    following special symbols removed:
#      "." (dot), "," (comma), ";" (semicolon), "?" (question mark), ":" (colon),
#      "!" (exclamation mark), "(" and ")" (parentheses), "-" (dash/minus), "&" (ampersand),
#      "'" (single quotation mark), and '"' (double quotation mark).
#    For instance, invocation of simplifyWord("Fourty-two!") should return just "fourtytwo".
#    Test your simplifyWord code for some inputs, but only if one runs the module, not when
#    importing.
#    Use this function in your implementation of `countTextWords' to count only the simplified
#    words instead of the ones with capital letters or special symbols.
#
# 3. Add the function `mostFrequent' that has one dict argument, representing tau, whose values
#    are integers, as well as one integer argument k. It shall implement Algorithm 2 (see Canvas)
#    and return the new map tau' by means of a new dictionary.
#    Add the function `twentyFrequent' that accepts a file name as a parameter, runs
#    `countTextWords' (which uses `simplifyWords') for it, and returns the result of mostFrequent
#    applied to the word count map with k = 20.
#
# Note that in order to complete the task you need to have a sign-off interview with one of the teachers.
#
# --‐---‐-‐‐-‐-‐----‐--‐‐--‐‐‐--‐‐-‐-‐-‐-‐-‐--‐‐‐‐‐----‐‐-‐-‐-‐-‐-‐--‐‐---‐‐--‐‐-‐‐‐‐-‐-‐--‐-‐‐‐-‐‐


# import string


def simplifyWord(w=''):
    # return w.translate(w.maketrans('', '', string.punctuation)).lower()
    simplify_w = w.translate(w.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')).lower() # repr(string.punctuation)
    if simplify_w != '':
        return simplify_w 


def countTextWords(file_name='default'):
    map_pi = dict()
    try:
        file_name = str(file_name)
        with open(file_name, "r") as text:
            for current_line in text:
                if current_line != "\n":
                    line_words = current_line.split()
                    for current_word in line_words:
                        current_word = simplifyWord(current_word)
                        if current_word != None and current_word not in map_pi:
                            map_pi[current_word] = 1
                        elif current_word in map_pi:
                            map_pi[current_word] += 1
        return map_pi
    except:
        print(f'FileNotFoundError: {file_name} not found')


def mostFrequent(dict_map=dict(), k=0):
    try:
        if (isinstance(k, int) and k >= 0):
            dict_map = dict(dict_map)
            list_l = [(value, key) 
                for key, value in dict_map.items() 
                if isinstance(value, int)]
            list_l.sort(key=lambda x: x[0])
            if len(list_l) >= k:
                tuple_yx_star = list_l[-k]
            list_l = [tuple_yx 
                      for tuple_yx in list_l 
                      if tuple_yx[0] >= tuple_yx_star[0]]
            map_tau = dict()
            for i in list_l:
                map_tau[i[1]] = i[0]
            return map_tau
    except:
        print('Error in mostFrequent')


def twentyFrequent(file_name_main='default'):
    return mostFrequent(countTextWords(file_name_main), 20)


if __name__ == '__main__':
    print(twentyFrequent('text-ironic.txt'))
    print(twentyFrequent('text-robinson-crusoe.txt'))
    print(countTextWords('text-robinson-crusoe.txt'))