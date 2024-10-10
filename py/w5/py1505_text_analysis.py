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


