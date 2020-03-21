# make sure to put colon at end of conditional checks
age = 40
if age >= 18 and age < 40:
    print('you are admitted entry')
    if age >= 21:
        print('you can drink')
    else:
        print('but you cant drink')
elif age >= 40:
    print('youre too old')
else:
    print('DENIED')
