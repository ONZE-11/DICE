
import random

list=[1,2,3,4,5,6]
random.shuffle(list)
print(list)

exit=False
while (not exit):
 
    x=int(input('enter youer gusse number between 1 to 6 : '))
    r=random.choice(list)
    def taas ():
        if x==r:
            return(f'you are win ! **{r}** is correct')
        elif x>6 or x<1 :
            exit=True
        else:
            return (f'you are lose >>{r}<< is NOT real number !')
    
    print(taas())

