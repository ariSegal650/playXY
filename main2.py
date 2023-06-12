import turtle
boardArray=[]
Height_Array = []
Width_Array = []
slant_to_left_Array = []
slant_to_right_Array = []
countMoves = 0
queshin3=0

def clickMe(x,y):
    global countMoves, boardArray, rowPressed,colPressed
    rowPressed=(int)(abs(topLeftY-y)//rowHeight)  
    colPressed=(int)(abs(topLeftX-x)//colWidth)
   
    squareTopLeftY=topLeftY - rowPressed*rowHeight
    squareTopLeftX=topLeftX + colPressed*colWidth
    if(rowPressed %2==0 or colPressed%2==0):
        print("AAA 1")
    if(boardArray[rowPressed][colPressed] != 0):
        print ("Sorry, someone clicked on me before you")
        clean(squareTopLeftX,squareTopLeftY)
     
    if(countMoves%2==0 ):
        boardArray[rowPressed][colPressed]=2
        test_Width(True)
        test_Height(True)
        test_slant_to_left_Array(True)
        test_slant_to_right_Array(True)
        player.color("orange")
        player.penup()
        player.goto(squareTopLeftX+8,squareTopLeftY-8)
        player.pendown()
        player.goto(squareTopLeftX+colWidth-8, squareTopLeftY-8)
        player.goto(squareTopLeftX+colWidth-8, squareTopLeftY-rowHeight+8)
        player.goto(squareTopLeftX+8, squareTopLeftY-rowHeight+8)
        player.goto(squareTopLeftX+8, squareTopLeftY-8)
    else:    
        boardArray[rowPressed][colPressed]=1     
        test_Width(False)
        test_Height(False)
        test_slant_to_left_Array(False)
        test_slant_to_right_Array(False)
        player.color("green")
        player.penup()
        player.goto(squareTopLeftX+8,squareTopLeftY-8)
        player.pendown()
        player.goto(squareTopLeftX+colWidth-8, squareTopLeftY-rowHeight+8)
        player.penup()
        player.goto(squareTopLeftX+colWidth-8 ,squareTopLeftY-8)
        player.pendown()
        player.goto(squareTopLeftX+8, squareTopLeftY-rowHeight+8)
    print("boardArray")
    printBoard(boardArray)
    print()
    print("Height_Array")
    printBoard(Height_Array)
    print()
    print("Width_Array")
    printBoard(Width_Array)
    print()
    print("slant_to_left_Array")      
    printBoard(slant_to_left_Array)
    print()
    print("slant_to_right_Array")
    printBoard(slant_to_right_Array)
    countMoves+=1

def DrawRows(rows, rowLen, space, xLocation, yLocation):
    while(rows>0):
        player.penup()
        player.goto(xLocation, yLocation)
        player.pendown()
        player.goto(xLocation+rowLen, yLocation)
        yLocation-=space;
        rows-=1
def DrawCols(cols, colLen, space, xLocation, yLocation):
    while(cols>0):
        player.penup()
        player.goto(xLocation, yLocation)
        player.pendown()
        player.goto(xLocation, yLocation-colLen)
        xLocation+=space;
        cols-=1
def createEmptyArray(rows, cols):
    arr=[]
    for r in range(rows):
        newRow=[]
        for c in range(cols):
            newRow.append(0)
        arr.append(newRow)
    return arr
def printBoard(arr):
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            print(arr[r][c], end=" ")
        print()
    print()


def test_Height(tor_1):
    global rowPressed , colPressed,queshin3
    r=rowPressed
    c=colPressed

    for i in range(0,seq):

        if(Height_Array[r][c] != 99 ):
                if(tor_1):
                    #בדיקה שאין ערך בטווח של תור 1 ששורף את הרצף של הטווח
                    if(Height_Array[r][c] >= 0):
                     Height_Array[r][c]+=1
                    else:
                      Height_Array[r][c] = 99

                elif(tor_1 == False):
                   
                   if(Height_Array[r][c] <= 0):
                    Height_Array[r][c]+=(-1)
                   else:
                      Height_Array[r][c] = 99

        if(Height_Array[r][c]==seq):
            print("the winner is y")
        elif(Height_Array[r][c]==(seq*-1)):
            print("the winner is x")
            queshin3+=1
            test_queshin3()

        r-=1
               
                #מוודא שלא תהיה גלישה
        if(r < 0 ):
            break
           
def test_Width(tor_1):
    global rowPressed , colPressed ,queshin3
    r=rowPressed
    c=colPressed

    for i in range(0,seq):

        if(Width_Array[r][c] != 99 ):
                if(tor_1):
                    #בדיקה שאין ערך בטווח של תור 1 ששורף את הרצף של הטווח
                    if(Width_Array[r][c] >= 0):
                     Width_Array[r][c]+=1
                    else:
                      Width_Array[r][c] = 99

                elif(tor_1 == False):
                   
                   if(Width_Array[r][c] <= 0):
                    Width_Array[r][c]+=(-1)
                   else:
                      Width_Array[r][c] = 99


        if(Width_Array[r][c]==seq):
            print("the winner is y")
        elif(Width_Array[r][c]==(seq*-1)):
            print("the winner is x")
            queshin3+=1
            test_queshin3()
        c-=1
               
                #מוודא שלא תהיה גלישה
        if(c < 0):
            break

    # queshin 2
    c=colPressed
    tempx=0
    tempy=0
    for i in range(0,colPressed):
        if(Width_Array[r][c] > 0):
            tempx+=1
        elif(Width_Array[r][c] < 0):
            tempy+=1
        
        if(tempx>0 and tempy>0):
            print("BBB")
            break
        c-=1

def test_slant_to_right_Array(tor_1):
    global rowPressed , colPressed
    r=rowPressed
    c=colPressed

    for i in range(0,seq):

        if(slant_to_right_Array[r][c] != 99 ):
                if(tor_1):
                    #בדיקה שאין ערך בטווח של תור 1 ששורף את הרצף של הטווח
                    if(slant_to_right_Array[r][c] >= 0):
                     slant_to_right_Array[r][c]+=1
                    else:
                      slant_to_right_Array[r][c] = 99

                elif(tor_1 == False):
                   
                   if(slant_to_right_Array[r][c] <= 0):
                    slant_to_right_Array[r][c]+=(-1)
                   else:
                      slant_to_right_Array[r][c] = 99


        if(slant_to_right_Array[r][c]==seq):
            print("the winner is y")
        elif(slant_to_right_Array[r][c]==(seq*-1)):
            print("the winner is x")
        r-=1
        c-=1
               
                #מוודא שלא תהיה גלישה
        if(r < 0 or c<0):
            break
   
def test_slant_to_left_Array(tor_1):
    global rowPressed , colPressed
    r=rowPressed
    c=colPressed

    for i in range(0,seq):

        if(slant_to_left_Array[r][c] != 99 ):
                if(tor_1):
                    #בדיקה שאין ערך בטווח של תור 1 ששורף את הרצף של הטווח
                    if(slant_to_left_Array[r][c] >= 0):
                     slant_to_left_Array[r][c]+=1
                    else:
                      slant_to_left_Array[r][c] = 99

                elif(tor_1 == False):
                   
                   if(slant_to_left_Array[r][c] <= 0):
                    slant_to_left_Array[r][c]+=(-1)
                   else:
                      slant_to_left_Array[r][c] = 99


        if(slant_to_left_Array[r][c]==seq):
            print("the winner is y")
        elif(slant_to_left_Array[r][c]==(seq*-1)):
            print("the winner is x")
        r-=1
        c+=1
               
                #מוודא שלא תהיה גלישה
        if(r < 0 or c>=cols):
            break

def test_queshin3():
    global queshin3
    if(queshin3>1):
        print("CCC")

def clean(squareTopLeftX,squareTopLeftY):
    global rowPressed , colPressed
    r=rowPressed
    c=colPressed
    if(countMoves%2!=0 ):
        player.color("white")
        player.penup()
        player.goto(squareTopLeftX+8,squareTopLeftY-8)
        player.pendown()
        player.goto(squareTopLeftX+colWidth-8, squareTopLeftY-8)
        player.goto(squareTopLeftX+colWidth-8, squareTopLeftY-rowHeight+8)
        player.goto(squareTopLeftX+8, squareTopLeftY-rowHeight+8)
        player.goto(squareTopLeftX+8, squareTopLeftY-8)

      
    else:    
        boardArray[rowPressed][colPressed]=1     
        player.color("white")
        player.penup()
        player.goto(squareTopLeftX+8,squareTopLeftY-8)
        player.pendown()
        player.goto(squareTopLeftX+colWidth-8, squareTopLeftY-rowHeight+8)
        player.penup()
        player.goto(squareTopLeftX+colWidth-8 ,squareTopLeftY-8)
        player.pendown()
        player.goto(squareTopLeftX+8, squareTopLeftY-rowHeight+8) 

        for i in range(0,seq):
             Width_Array[r][c]+=1
             if( Width_Array[r][c+1]>0):
                   Width_Array[r][c]= Width_Array[r][c+1]
             else:
                 Width_Array[r][c]=0
             c-=1
             print("5555555555555555555")

#def test_Height()
# taking input from user regarding rows and columns
rows=(int)(input("Enter rows : "))
cols=(int)(input("Enter cols : "))
seq = (int)(input("Enter sec : "))
# default setting for showing the screen and also the with of lines
screen = turtle.Screen()
player = turtle.Turtle()
player.width(5)    
player.speed(9)
rowPressed=0
colPressed=0
boardArray=createEmptyArray(rows, cols)
Height_Array = createEmptyArray(rows, cols)
Width_Array = createEmptyArray(rows, cols)
slant_to_left_Array = createEmptyArray(rows, cols)
slant_to_right_Array = createEmptyArray(rows, cols)
printBoard(boardArray)
rowHeight=70
colWidth=70
lineRowLen=cols*colWidth
lineColLen=rows*rowHeight
topLeftX=-lineRowLen//2
topLeftY=lineColLen//2
DrawRows(rows+1, lineRowLen, rowHeight, topLeftX, topLeftY)
DrawCols(cols+1, lineColLen, colWidth, topLeftX, topLeftY)
screen.onclick(clickMe)
turtle.mainloop()