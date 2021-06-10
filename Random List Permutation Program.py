def random_permutations_function(user_list,number) :
    from random import randrange
    n = 1
    result_list = []
    length = len(user_list)
    while n <= number :
        copy_list = user_list[:]
        for x in range(0,length-1,1) :
            random = randrange(x,length)
            copy_list[x],copy_list[random] = copy_list[random],copy_list[x]
        result_list = result_list + [copy_list]
        n = n+1
    return result_list
def main() :
    user_input = list(eval(input('>> Please enter Numbers/Strings seperated by comma : ')))
    number = eval(input('>> what number of Random Permutations to generate ? : '))
    result = random_permutations_function(user_input,number)
    print()
    print('>> Random Permutation(s) of provided elements : ',result)
    print()
main()
