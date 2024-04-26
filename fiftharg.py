def fifth(*args):
    # if args[-1] == None :
    #     return "Not enough arguments"
    

    if len(args) >= 5:
        return type(args[-1])
    return "Not enough arguments"

    # elif type(args[6]) == None:
        # return "Not enough arguments"
#print(fifth(1, 2, 3, 4, 5))

print(fifth('zero','one','two','three','four','five'))


# assert_equals(fifth('a',2,3,4,[5]),list)
# Test.assert_equals(fifth('zero','one','two','three','four','five'),str)
# Test.assert_equals(fifth(1,2,3,4,'5'),str)
# Test.assert_equals(fifth(1,2,3,4,5),int)
# Test.assert_equals(fifth(1,2,3),'Not enough arguments')