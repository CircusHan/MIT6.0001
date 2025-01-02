######################################
# EXAMPLE: Exceptions with summing digits in a string
######################################
names = ['Ana', 'John', 'Matt', 'Katy']
grades=['A+', 'B' , 'A', 'A']

dict_stu = {'Ana' : 'A+', 'John' : 'B', 'Matt' : 'A', 'Katy' : 'A'}
print(dict_stu['Matt'])
print(grades[names.index('Matt')])

# l = [2, 3, 4]
# try:
#     print(l[4])
#     a
# except IndexError:
#     print("No such element")
# except NameError:
#     print("It is not an initialized element")
#
# def f():
#     result = 10 / 0
# try:
#     d = int("this is a string")
# except:
#     print("It is not an integer")
#     raise ZeroDivisionError("Division by zero")
#
# import traceback
# try:
#     # 예외가 발생할 가능성이 있는 코드
#     f()
# except Exception as e:
#     # 예외 객체를 변수 e에 저장
#     print(f"예외 발생: {type(e).__name__}")  # 예외의 종류 출력
#     print(f"예외 메시지: {e}")  # 예외 메시지 출력
#     tb = traceback.extract_tb(e.__traceback__)
#     for frame in tb:
#         print(f"파일: {frame.filename}, 라인: {frame.lineno}, 함수: {frame.name}")

# Not using exceptions
def sum_digits(s):
    """ s is a non-empty string containing digits
    Returns sum of all characters that are digits """
    total = 0
    for char in s:
        #if char in '0123456789':
            try:
                val = int(char)
                total += val
            except :
                raise ValueError("String contained a character")
    return total

# print(sum_digits("123"))
try:
    print(sum_digits("123abc"))
except:
    pass

# Using exceptions around potentially problematic code
# Print that an error happened and let the program keep going
def sum_digits_except(s):
    """ s is a non-empty string containing digits
    Returns sum of all characters that are digits """
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            print("couldn't convert character", char)
    return total

# print(sum_digits_except("123"))
# print(sum_digits_except("123abc"))


# Raising our own more informative error
# This is typically what you'd be asked to do in this class
def sum_digits_raise(s):
    """ s is a non-empty string containing digits
    Returns sum of all characters that are digits """
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            raise ValueError("string contained a character") 
    return total
            
# print(sum_digits_raise("123"))
# print(sum_digits_raise("123abc"))
def pairwise_div(Lnum, Ldenom):
    """
    Lnum and Ldenom are non-empty lists of equal lengths containing numbers
    Returns a new list whose elements are the pairwise division of an element in Lnum by an element in Ldenom.
    Raise a ValueError if Ldenom contains 0.
    """
    l = []
    for i in range(len(Lnum)) :
        try:
            Result = Lnum[i]/Ldenom[i]
            l.append(Result)
        except:
            raise ZeroDivisionError("Ldenom contains 0.")
    return l
# For example:
# L1 = [4,5,6]
# L2 = [1,2,3]
# print(pairwise_div(L1, L2)) # prints [4.0,2.5,2.0]
# L1 = [4,5,6]
# L2 = [1,0,3]
# print(pairwise_div(L1, L2)) # raises a ValueError

# Note the assert statement activates when s is passed as ""
def sum_digits_assert(s):
    """ s is a non-empty string containing digits
    Returns sum of all characters that are digits """
    assert len(s) != 0, "s is empty"
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            raise ValueError("string contained a character") 
    return total
#
# print(sum_digits_assert(""))
#print(sum_digits_assert("123"))
# print(sum_digits_assert("123abc"))

def pairwise_div(Lnum, Ldenom):
    """
    Lnum and Ldenom are non-empty lists of equal lengths
    containing numbers
    Returns a new list whose elements are the pairwise division of an element in Lnum by an element in Ldenom. Raise a ValueError if Ldenom contains 0.
    """
    assert len(Lnum) != 0 and len(Ldenom) != 0, "Ldenom contains 0."
    l = []
    for i in range(len(Lnum)):
        try:
            Result = Lnum[i] / Ldenom[i]
            l.append(Result)
        except:
            raise ZeroDivisionError("Ldenom contains 0.")
    return l
L1 = [4,5,6]
L2 = [1,2,3]
print(pairwise_div(L1, L2)) # prints [4.0,2.5,2.0]
# L1 = [4,5,6]
# L2 = [1,0,3]
# print(pairwise_div(L1, L2)) # raises a ValueError
# L1 = [3,5,6]
# L2 = []
# print(pairwise_div(L1, L2))

print(sum(L1)/len(L1))

def get_stats(class_list):
    avg = 0
    new_stats = []
    for elem in class_list:
        try:
            #assert len(elem[1]) != 0, "This list is empty"
            new_stats.append([elem[0],elem[1],sum(elem[1])/len(elem[1])])
        except ZeroDivisionError:
            new_stats.append([elem[0],elem[1],0.0])
    return new_stats
test_grades = [[['peter', 'parker'], [10.0,55.0,85.0]], [['bruce', 'wayne'], [10.0,80.0,75.0]],
               [['captain', 'america'], [80.0,10.0,96.0]],
               [['deadpool'], []]]

print(get_stats(test_grades))


######################################
# EXAMPLE: Exceptions with user input
######################################

def divide_nums1():
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print(a/b)

# divide_nums1()


def divide_nums2():
    try:
        a = int(input("Tell me one number: "))
        b = int(input("Tell me another number: "))
        print(a/b)
    except:
        print("Bug in user input")

# divide_nums2()


def divide_nums3():
    try:
        a = int(input("Tell me one number: "))
        b = int(input("Tell me another number: "))
        print("a/b = ", a/b)
        print("a+b = ", a+b)
    except ValueError:
        print("Could not convert to a number.")
    except ZeroDivisionError:
        print("Can't divide by zero")
        print("a/b = infinity")
        print("a+b =", a+b)
    except:
        print("Something went very wrong.")

# divide_nums3()



#########################################
########### YOU TRY IT ##################
##########################################
def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of 
        equal lengths containing numbers

    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 

    Raise a ValueError if Ldenom contains 0. """
    # your code here
    # challenge: write this with list comprehension!

    
# For example:
L1 = [4,5,6]
L2 = [1,2,3]    
# print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]

L1 = [4,5,6]
L2 = [1,0,3]    
# print(pairwise_div(L1, L2))  # raises a ValueError

## to run after introducing assertions
L1 = [4,5,6,7,8]
L2 = [1,8,3]    
# print(pairwise_div(L1, L2))  # raises an AssertionError

L1 = []
L2 = []    
# print(pairwise_div(L1, L2))  # raises an AssertionError


#########################################


#######################################
## EXAMPLE: Longer exceptions and lists example
#######################################
def get_stats(class_list, avg_func):
    """ class_list is a list of student info: 
            * name as a list
            * grades as a list
        avg_func is a function that takes in a list and returns a float
    """
    new_stats = []
    for person in class_list:
        new_stats.append([person[0], person[1], avg_func(person[1])])
    return new_stats 

test_grades = [[['peter', 'parker'], [10.0, 55.0, 85.0]], 
               [['bruce', 'wayne'], [10.0, 80.0, 75.0]],
               [['captain', 'america'], [80.0,10.0,96.0]],
               [['thor'], []]]

## Note in the get_stats function calls below, 
## we are passing the various avg1/2/3 function names as params
## to test different avg function behaviours with the same data

# avg function: version without an exception
def avg1(grades):
    return (sum(grades))/len(grades)
# print(get_stats(test_grades, avg1))
    

# avg function: version with an exception
def avg2(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
# print(get_stats(test_grades, avg2))


# avg function: version with an exception
def avg3(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
        return 0.0
# print(get_stats(test_grades, avg3))


# avg function: version with assert
def avg4(grades):
    assert len(grades) != 0, 'warning: no grades data'
    return sum(grades)/len(grades)
# print(get_stats(test_grades, avg4))


#########################################
########### ANSWERS TO YOU TRY IT ##################
##########################################
def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of 
        equal lengths containing numbers

    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 

    Raise a ValueError if Ldenom contains 0. """
    assert (len(Lnum) == len(Ldenom)), 'lists not equal length'
    assert Lnum != [], 'list is empty'
    if 0 in L2:
        raise ValueError
    else:
        L = []
        for i in range(len(Lnum)):
            L.append(Lnum[i]/Ldenom[i])
        return L
    ## with list comprehensions
    ## return [Lnum[i]/Ldenom[i] for i in range(len(Lnum))]

    
# For example:
L1 = [4,5,6]
L2 = [1,2,3]    
# print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]

L1 = [4,5,6]
L2 = [1,0,3]    
# print(pairwise_div(L1, L2))  # raises a ValueError

##############################################
################### AT HOME ###################
################################################
def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of equal lengths
        containing numbers
    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 
    Raise a ValueError if L2 contains 0 or if the code can't 
    perform the division for some reason. """
    # your code here


##############################################
################### ANSWERS TO AT HOME ###################
################################################
def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of equal lengths
        containing numbers
    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 
    Raise a ValueError if L2 contains 0 or if the code can't 
    perform the division for some reason. """
    assert (len(Lnum) == len(Ldenom)) and (len(Ldenom) != 0)
    L = []
    for i in range(len(Lnum)):
        try:
            L.append(Lnum[i]/Ldenom[i])
        except:
            raise ValueError
    return L
