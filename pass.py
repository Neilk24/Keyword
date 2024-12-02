for x in range(30):

    if x%20==0:
        print('Twist')

    elif x%15==0:
        print('fizzbuzz')

    elif x%5==0:
        print('fizz')

    elif x%3==0:
        print('buzz')

    elif x%2==0:
        pass

    else:
        print(x)