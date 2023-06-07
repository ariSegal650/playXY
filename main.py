countersArray=[]
boardArray=[]
heightArry=[]
slantTopToRighet=[]
slantTopToLeft=[]

countMoves = 0
def winerr(r):
    queshien3(r)
    if(max_x>=seq):
        print("the winner is x")
    else:
        print("the winner is y")
def queshien2(r,rows):
     
      for i in range(0, rows):
          if(boardArray[r][i]==2):
              print("BBB")
              break
def queshien3(r):
    maxAmuda=0
    maxShura=0
    for i in range(cols):
         if(boardArray[r][i]==1):
             maxShura+=1
         if(boardArray[r][i+1]!=1 and maxShura>=seq):
             for j in range(rows):
                   if(boardArray[r][j]==1):
                       maxAmuda+=1
    if(maxAmuda>=seq):
        print("CCC")



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
def slantTopToRighetFUN(r,c,tor,tor_1,max_o,max_x,seq):
     
    for i in range(0, seq):
             #מוודא שאין דריסה של ערך קיים
            if(slantTopToRighet[r][c] != 99 ):
                if(tor_1):
                    #בדיקה שאין ערך בטווח של תור 1 ששורף את הרצף של הטווח
                    if(slantTopToRighet[r][c] >= 0):
                     slantTopToRighet[r][c]+=1
                    else:
                      slantTopToRighet[r][c] = 99
                      #מעדכן ל-MAX
                    if(slantTopToRighet[r][c]!=99 and slantTopToRighet[r][c]>max_x):
                        max_x=heightArry[r][c]

                #בדיקה שאין ערך בטווח של תור 2 ששורף את הרצף של הטווח
                elif(tor_1 == False):
                   
                   if(slantTopToRighet[r][c] <= 0):
                    slantTopToRighet[r][c]+=(-1)
                   else:
                      slantTopToRighet[r][c] = 99

                     #מעדכן ל-MAX
                   if(slantTopToRighet[r][c]!=99 and slantTopToRighet[r][c]<max_o):
                        max_o=slantTopToRighet[r][c]
                
                r-=1
                c-=1
            # if(max_o==(seq*-1) or max_x==seq):
            #     #מדפיס ניצחון
            #     winerr()
            #     break
            #מוודא שלא תהיה גלישה
            if(r < 0 or c<0):
                   break
    print("slantTopToRighet")
    print()
    Show2DArray(slantTopToRighet)

def slantTopToLeftFUN(r,c,tor,tor_1,max_o,max_x,seq,rows):
     
    for i in range(0, seq):
             #מוודא שאין דריסה של ערך קיים
            if(slantTopToLeft[r][c] != 99 ):
                if(tor_1):
                    #בדיקה שאין ערך בטווח של תור 1 ששורף את הרצף של הטווח
                 
                    if(slantTopToLeft[r][c] >= 0 ):
                     slantTopToLeft[r][c]+=1
                    else:
                      slantTopToLeft[r][c] = 99
                      #מעדכן ל-MAX
                    if(slantTopToLeft[r][c]!=99 and slantTopToLeft[r][c]>max_x):
                        max_x=slantTopToLeft[r][c]

                #בדיקה שאין ערך בטווח של תור 2 ששורף את הרצף של הטווח
                elif(tor_1 == False):
                   
                   if(slantTopToLeft[r][c] <= 0):
                    slantTopToLeft[r][c]+=(-1)
                   else:
                      slantTopToLeft[r][c] = 99

                     #מעדכן ל-MAX
                   if(slantTopToLeft[r][c]!=99 and slantTopToLeft[r][c]<max_o):
                        max_o=slantTopToLeft[r][c]
                
                r-=1
                c+=1
            # if(max_o==(seq*-1) or max_x==seq):
            #     #מדפיס ניצחון
            #     winerr()
            #     break
            #מוודא שלא תהיה גלישה
            if(r < 0 or c>=rows):
                   break
    print("slantTopToLeft")
    print()
    Show2DArray(slantTopToLeft)
def heightFUN(r,c,tor,tor_1,max_o,max_x,seq):
     
    for i in range(0, seq):
             #מוודא שאין דריסה של ערך קיים
            if(heightArry[r][c] != 99 ):
                if(tor_1):
                    #בדיקה שאין ערך בטווח של תור 1 ששורף את הרצף של הטווח
                    if(heightArry[r][c] >= 0):
                     heightArry[r][c]+=1
                    else:
                      heightArry[r][c] = 99
                      #מעדכן ל-MAX
                    if(heightArry[r][c]!=99 and heightArry[r][c]>max_x):
                        max_x=heightArry[r][c]

                #בדיקה שאין ערך בטווח של תור 2 ששורף את הרצף של הטווח
                elif(tor_1 == False):
                   
                   if(heightArry[r][c] <= 0):
                    heightArry[r][c]+=(-1)
                   else:
                      heightArry[r][c] = 99

                     #מעדכן ל-MAX
                   if(heightArry[r][c]!=99 and heightArry[r][c]<max_o):
                        max_o=heightArry[r][c]
                
                r-=1
            # if(max_o==(seq*-1) or max_x==seq):
            #     #מדפיס ניצחון
            #     winerr()
            #     break
            #מוודא שלא תהיה גלישה
            if(r < 0):
                   break
    print("heightArry")
    print()
    Show2DArray(heightArry)
def WidthFUN(r,c,tor,tor_1,max_o,max_x,seq,rows):
     #מוודא שאין דריסה של ערך קיים
   
        boardArray[r][c]=tor
        Show2DArray(boardArray)

        for i in range(0, seq):
             #מוודא שאין דריסה של ערך קיים
            if(countersArray[r][c] != 99 ):
                if(tor_1):
                    queshien2(r,rows)
                    #בדיקה שאין ערך בטווח של תור 1 ששורף את הרצף של הטווח
                    if(countersArray[r][c] >= 0):
                     countersArray[r][c]+=1
                    else:
                      countersArray[r][c] = 99
                      #מעדכן ל-MAX
                    if(countersArray[r][c]!=99 and countersArray[r][c]>max_x):
                        max_x=countersArray[r][c]

                #בדיקה שאין ערך בטווח של תור 2 ששורף את הרצף של הטווח
                elif(tor_1 == False):
                   
                   if(countersArray[r][c] <= 0):
                    countersArray[r][c]+=(-1)
                   else:
                      countersArray[r][c] = 99

                     #מעדכן ל-MAX
                   if(countersArray[r][c]!=99 and countersArray[r][c]<max_o):
                        max_x=countersArray[r][c]
                
                c-=1
            # if(max_o==(seq*-1) or max_x==seq):
            #     #מדפיס ניצחון
            #     winerr()
            #     break
            #מוודא שלא תהיה גלישה
            if(c < 0):
                   break
        print("widthArray")
        print()
        Show2DArray(countersArray)
#                                       MAIN

rows=(int)(input("Enter rows : "))
cols=(int)(input("Enter cols : "))
seq=(int)(input("Enter sequnce : "))
#לוח האם
boardArray=DefineDynamicArray(rows, cols)
#לוח ספירה שורה
countersArray=DefineDynamicArray(rows, cols)
#לוח ספירה עמודה 
heightArry=DefineDynamicArray(rows, cols)
slantTopToRighet=DefineDynamicArray(rows, cols)
slantTopToLeft=DefineDynamicArray(rows, cols)

Show2DArray(boardArray)
Show2DArray(countersArray)
Show2DArray(heightArry)
max_o = 0
max_x = 0
r=(int)(input("Enter row : "))
c=(int)(input("Enter col : "))
tor=(int)(input("Enter 1/2 : "))

 #תור אחד = איקס = נכון. תור שני שווה עיגול לא נכון  בוליאני
tor_1 = True
while(r>=0):
    if(r%2==0 or c%2==0):
        print("AAA")
        #שאלה 4
    if(boardArray[r][c] != 0):   
        if(countersArray[r][c]==-1 or countersArray[r][c]==1):
                countersArray[r][c]=0
        if(heightArry[r][c]==-1 or heightArry[r][c]==1):
                heightArry[r][c]=0
        if(slantTopToRighet[r][c]==-1 or slantTopToRighet[r][c]==1):
                slantTopToRighet[r][c]=0
        if(slantTopToLeft[r][c]==-1 or slantTopToLeft[r][c]==1):
                slantTopToLeft[r][c]=0    

    WidthFUN(r,c,tor,tor_1,max_o,max_x,seq,rows)
    heightFUN(r,c,tor,tor_1,max_o,max_x,seq)
    slantTopToRighetFUN(r,c,tor,tor_1,max_o,max_x,seq)
    slantTopToLeftFUN(r,c,tor,tor_1,max_o,max_x,seq,rows)

    # else:
    #    print("Sorry, the place is taken")  
    #    tor_1= not tor_1
  #  if(max_o==(seq*-1) or max_x==seq):
                #מדפיס ניצחון
   # winerr(r)
 #  break
    
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

