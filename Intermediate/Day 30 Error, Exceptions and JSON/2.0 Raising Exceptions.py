# suppose you building a BMI calculator, and you do not want the height to be greater than 3m

height = float(input('Enter your height:\n'))
weight = float(input('Enter your weight:\n'))

if height >= 3:
    raise ValueError('This height is too much for a human')
else:
    BMI = weight/(height**2)
    print(round(BMI, 2))
