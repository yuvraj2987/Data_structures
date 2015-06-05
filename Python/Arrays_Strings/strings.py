

def isUnique(string):
    char_map = {}
    for char in string:
        if char in char_map:
            return False
        #  else
        char_map[char] = None
    # for ends
    return True


def compareStrPerm2(str1, str2):
    """
        check if str2 is permutation of str1
    """
    if len(str1) != len(str2):
        return False
    char_count = {}
    for ch in str1:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    # end of str1 char counting
    for ch in str2:
        if ch not in char_count:
            return False
        char_count[ch] -= 1
    # end of str2 char counting
    for ch in char_count.keys():
        if char_count[ch] != 0:
            return False
    # end of for
    return True



# --- Test methods
def test_unique_char_string():
    """
    """
    methods = [isUnique]
    for method in methods:
        print "Testing %s" % (str(method))
        print "Test1: Unique string"
        s = "abcd"
        if method(s):
            print "passed"
        else:
            print "failed"
        print "Test2: No unique string"
        s = "abca"
        if method(s):
            print "Failed"
        else:
            print "Passed"
        print "Test3: Duplicate characters"
        if method(s):
            print "Failed"
        else:
            print "Passed"


def test_compare_str_perm():
    methods = [compareStrPerm2]
    for m in methods:
        print "Testing %s" % (str(m))
        print "Test1: unequal strings"
        s1 = "abcd"
        s2 = "bc"
        if m(s1, s2):
            print "Failed!!"
            return
        else:
            print "Passed!!"
        print "Test2: success case"
        s2 = "cdab"
        if not m(s1, s2):
            print "Failed!!"
            return
        else:
            print "Passed!!"
        print "Test3: failed case"
        s2 = "abcf"
        if m(s1, s2):
            print "Failed!!"
            return
        else:
            print "Passed!!"

    # end of for
    print "Success"




def main():
    print "String based questions"
    test_unique_char_string()
    test_compare_str_perm()


if __name__ == '__main__':
    main()
