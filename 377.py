#https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
#This program does not use any libraries
#Using the math library would probably make it more cleaner
#Fit3 function would be way more cleaner
def main():
    X = int(input ('enter the X of the crate: '))
    Y = int(input ('enter the Y of the crate: '))
    a = int(input ('enter the x for the boxes: '))
    b = int(input ('enter the y for the boxes: '))

    print('The number of boxes that can fit into the crate, for fit1, are: ')
    fit = fit1(X, Y, a, b)
    print (fit)

    print ('The number of boxes that can fit rotated in the crate are: ')
    fit = fit2(X, Y, a, b)
    print (fit)

    print('Adding in the Z dimension.')
    X = int(input ('enter the X of the crate: '))
    Y = int(input ('enter the Y of the crate: '))
    Z = int(input ('enter the Z of the crate: '))
    a = int(input ('enter the x for the boxes: '))
    b = int(input ('enter the y for the boxes: '))
    c = int(input ('enter the z of the boxes: '))

    print('The number of boxes that can fir in the crate are: ')
    fit = fit3(X, Y, Z, a, b, c)
    print(fit)
#finds how many boxes can fit in the crate
#given the X and Y of the crate
#and the a, b of the boxes (x and y)
def fit1(X, Y, a, b):
    Xfit = int(X / a)
    Yfit = int(Y / b)
    boxfit = Xfit * Yfit
    return boxfit

#finds the number of boxes that can fit into the crate
#calls the fit1 function with the a and b swapped
def fit2(X, Y, a, b):
    rotate = fit1(X, Y, b, a)
    return rotate

#find the number of boxes that can fit into the crate
#given X, Y, Z of the crate
#and the a, b, c (x, y, z) of the boxes
#calls the helper function fit3help
def fit3(X, Y, Z, a, b, c):
    Sol1 = fit3help(X, Y, Z, a, b, c)
    Sol2 = fit3help(X, Y, Z, a, c, b)
    Sol3 = fit3help(X, Y, Z, b, a, c)
    Sol4 = fit3help(X, Y, Z, b, c, a)
    Sol5 = fit3help(X, Y, Z, c, a, b)
    Sol6 = fit3help(X, Y, Z, c, b, a)
    possibleSol = [Sol1, Sol2, Sol3, Sol4, Sol5, Sol6]
    possibleSol.sort()
    return possibleSol[5]

#find the number of boxes that can fit into a crate
#called by fit3
def fit3help (X, Y, Z, a, b, c):
    Xfit = int(X / a)
    Yfit = int(Y / b)
    Zfit = int(Z / c)
    return Xfit*Yfit*Zfit


if __name__ == "__main__":
    main()
