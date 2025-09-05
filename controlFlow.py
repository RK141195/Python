number = 23
guess = 23
if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here
print('Done')
# This last statement is always executed,
# after the if statement is executed.

x = 50
def func(x):
    print('x is', x)
    x=2
    print('Changed local x to', x)
func(x)
print('x is still', x)

y = 500
def func():
    y=300
    print('x is', y)
func()