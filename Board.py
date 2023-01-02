
from Rect import *
import pygame
WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)
GREY = (164, 162,162)


class Game: #A class for managing different situations and states happening in the game and on the board
    def __init__(self, Mat, dimX, dimY,win):
        self.Mat = Mat
        self.dimX = dimX
        self.dimY = dimY
        self.win=win
        self.UI_Mat=[]
        self.mouse_position=(0,0)

    def Initiate(self): #initiating the game board with X and Y dimensions
        for i in range(0, self.dimY):
            R = []
            for j in range (0, self.dimX):
                if i % 2 == 1 and j % 2 == 1:
                    R.append(5)  # Assigning a random number from 1 to 9 to the spots in the board as the points
                elif i % 2 == 0 and j % 2 == 0:
                    R.append('*') # printing asterisks as the dots in the board
                else:
                    R.append(' ') # adding extra space for actions in the game
            
            self.Mat.append(R)

    def Get_matrix(self): # Board matrix
        ans = []
        for i in range(0, self.dimY):
            R = []
            for j in range(0, self.dimX):
                R.append(self.Mat[i][j])
            ans.append(R)
        return ans

    def Draw_mat(self): # Drawing the board marix as dots and lines
        
        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX):
            print(str(i), end='  ')
        print()

        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX + 1):
            print("____", end='')
        print()
        for j in range(self.dimY):
            if self.dimX > 9 and j < 10:
                print(" ", end='')
            print(str(j) + "| ", end='')
            for z in range(self.dimX):
                print(str(self.Mat[j][z]), end='  ')
            print()
        print("   _________________________\n")
        self.Draw_mat2()

    def Draw_mat2(self): # UI board

        circle_x,circle_y=30,30
        rect_x,rect_y=30,30
        self.UI_Mat=[]
        for i in range(self.dimY):
            temp_row=[]
            
            for j in range(self.dimX):
                if self.Mat[i][j] == "*" :
                    pygame.draw.circle(self.win,RED,(circle_x,circle_y),5,2)
                    temp_row.append("*")
                    # circle postion change row-wise
                    circle_x+=35
                if self.Mat[i][j] == 5:
                    temp_row.append("5")
                if i%2==1 and self.Mat[i][j]==" ":
                    
                    obj=Rect(rect_x,rect_y,3,35)
                    
                    temp_row.append(obj)

                    obj.draw(self.win,GREY)
                    obj.if_hit(self.win,self.mouse_position)
                    rect_x+=35

                if i%2==1 and self.Mat[i][j]=="|":
                    
                    obj=Rect(rect_x,rect_y,3,35)
                    
                    temp_row.append(obj)

                    obj.draw(self.win,BLACK)
                    obj.if_hit(self.win,self.mouse_position)
                    rect_x+=35
                if i%2==0 and self.Mat[i][j]==" ":
                    obj=Rect(rect_x,rect_y,35,3)
                    
                    temp_row.append(obj)
                    obj.draw(self.win,GREY)
                    obj.if_hit(self.win,self.mouse_position)
                    rect_x+=35
                if i%2==0 and self.Mat[i][j]=="-":
                    obj=Rect(rect_x,rect_y,35,3)
                    
                    temp_row.append(obj)
                    obj.draw(self.win,BLACK)
                    rect_x+=35
            self.UI_Mat.append(temp_row)  
            
            if i%2==0:
                circle_y+=35
            else:
                rect_y+=35
            circle_x=rect_x=30
        # print("UI Mat=",self.UI_Mat)
        # print("Mat=",self.Mat)


    def Get_currentState(self):
        return Game(self.Get_matrix(), self.dimX, self.dimY,self.win)

    def action(self, i, j,player): # Applying the actions made by the human or the computer
        # print(f"selfMat[{j}][{i}] =")
        # print("UI mat=",self.UI_Mat)
        # print("mat",self.Mat)
        # # For UI
        # rect_obj=self.UI_Mat[j][i] 
        # print("current_rect_obj",rect_obj)
        # print("UI mat",self.UI_Mat)
        # print("mat",self.Mat)
        # if player:
        #     rect_obj.draw(self.win,GREEN)
        # else:
        #     rect_obj.draw(self.win,RED)
        
        Sum = 0

        if j % 2 == 0 and i % 2 == 1:
            self.Mat[j][i] = '-'
            if j < self.dimY - 1:
                if self.Mat[j+2][i] == '-' and self.Mat[j+1][i+1] == '|' and self.Mat[j+1][i-1] == '|':
                    Sum += self.Mat[j+1][i]
            if j > 0:
                if self.Mat[j-2][i] == '-' and self.Mat[j-1][i+1] == '|' and self.Mat[j-1][i-1] == '|':
                    Sum += self.Mat[j-1][i]

        else:
            self.Mat[j][i] = '|'
            if i < self.dimX - 1:
                if self.Mat[j][i+2] == '|' and self.Mat[j+1][i+1] == '-' and self.Mat[j-1][i+1] == '-':
                    Sum += self.Mat[j][i+1]
            if i > 0:
                if self.Mat[j][i-2] == '|' and self.Mat[j+1][i-1] == '-' and self.Mat[j-1][i-1] == '-':
                    Sum += self.Mat[j][i-1]

        return Sum
