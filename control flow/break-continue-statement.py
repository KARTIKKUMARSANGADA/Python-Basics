# The continue statement continues with the next iteration of the loop:
# The break statement breaks out of the loop entirely:int the for or while loop
print("*****first example*****")
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
    # This will print numbers from 1 to 9 except 5, because when i is 5, the continue statement will skip the rest of the loop body and move to the next iteration.
    
print("*****second example*****")

for i in range(1, 10):
    if i == 5:
        break
    print(i)
    # This will print numbers from 1 to 4, because when i is 5, the break statement will exit the loop entirely.
    
        

