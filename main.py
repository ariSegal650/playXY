countersArray=[]
boardArray=[]
countMoves = 0

def DefineDynamicArray(rows, cols):
    dArray=[]
    for r in range(rows):
        newRow=[]
        for c in range(cols):
            newRow.append(0)
        dArray.append(newRow)
    return dArray
def Show2DArray(arr):
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            print(arr[r][c], end=" ")
        print()
    print()
    print()
#                                       MAIN

rows=(int)(input("Enter rows : "))
cols=(int)(input("Enter cols : "))
seq=(int)(input("Enter sequnce : "))
boardArray=DefineDynamicArray(rows, cols)
countersArray=DefineDynamicArray(rows, cols)
Show2DArray(boardArray)
Show2DArray(countersArray)

max_o = 0;
max_x = 0;
r=(int)(input("Enter row : "))
c=(int)(input("Enter col : "))
tor=(int)(input("Enter 1/2 : "))
tor_1 = True #תור אחד = איקס = נכון. תור שני שווה עיגול לא נכון  בוליאני
while(r>=0):
    #מוודא שאין דריסה של ערך קיים
    if(boardArray[r][c] == 0):       
        boardArray[r][c]=tor
        Show2DArray(boardArray)

        for i in range(0, seq):
             #מוודא שאין דריסה של ערך קיים
            if(countersArray[r][c] != 99 ):
                if(tor_1):#בדיקה שאין ערך בטווח של תור 1 ששורף את הרצף של הטווח
                    if(countersArray[r][c] >= 0):
                     countersArray[r][c]+=1
                    else:
                      countersArray[r][c] = 99
                #בדיקה שאין ערך בטווח של תור 2 ששורף את הרצף של הטווח
                elif(tor_1 == False):
                   if(countersArray[r][c] <= 0):
                    countersArray[r][c]+=(-1)
                   else:
                      countersArray[r][c] = 99
                c-=1
            #מוודא שלא תהיה גלישה
            if(c < 0):
                   break
            #בודק שאין ריבוע של היריב לאורך הטווח של הניצחון
            if(boardArray[r][c] != tor and boardArray[r][c] != 0):
                countersArray[r][c] = 99
    else:
           print("Sorry, the place is taken")   
            #גלישה , ללכת ל99
    Show2DArray(countersArray)
    

    if(tor_1):
        print("tor 2") 
        tor = 2
        tor_1 = False
    else:
        print("tor 1") 
        tor = 1
        tor_1 = True

    r=(int)(input("Enter row : "))
    c=(int)(input("Enter col : "))


   
    

   # tor=(int)(input("Enter 1/2 : "))

