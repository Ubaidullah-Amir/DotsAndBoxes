from random import *
from Algorithm import *
from Board import *
from Nodes import *
import pygame


class DotsNBoxes: # A class for managing the moves made by the human and the computer
    def __init__(self, Board_Xdim, Board_Ydim, Ply_num,win):
        self.win=win
        self.mouse_position=(0,0)
        currentState = Game([], Board_Xdim, Board_Ydim,win)
        currentState.Initiate()
        self.State = Thing(currentState)
        self.Ply_num = Ply_num
        self.Score = 0
        self.AI_move="(None,None)"
        self.current_score_UI="0"
        self.someone_win=False
        self.winning_text=""
        

    def Human(self): # Defining the Human player and his actions/Choices
        running= True
        HumanX_pressed=False
        HumanY_pressed=False
        font = pygame.font.Font('freesansbold.ttf', 13)
        
        text_obj_AI_move = font.render("Move played by AI"+self.AI_move, True, GREEN)
        text_obj_current_score = font.render("Your current score"+self.current_score_UI, True, BLUE)
        
        while running:
            self.win.fill(WHITE)
            self.win.blit(text_obj_AI_move, (200,0))
            self.win.blit(text_obj_current_score, (200,50))

            text_mouse_postion=font.render("mouse position"+ str(self.mouse_position),True,GREEN)
            self.win.blit(text_mouse_postion,(200,100))
            self.State.Current.mouse_position=self.mouse_position
            
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quit")
                    running=False

                #Mouse inputs
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    loop_breaker=False
                    for i in range(5):
                        for j in range(5):
                            # print("selected result is i:",i,"j :",j)
                            if type(self.State.Current.UI_Mat[i][j]) != str:
                                # print("not str selected result is i:",i,"j :",j)
                                if self.State.Current.UI_Mat[i][j].rect.collidepoint(pygame.mouse.get_pos()):
                                    print("the mouse is colliding wiht rect")
                                    HumanX=j
                                    HumanY=i
                                    HumanX_pressed=HumanY_pressed=True
                                    loop_breaker=True
                                    break
                        if loop_breaker:
                            break
                                
                # checking if keydown event happened or not
                if event.type == pygame.KEYDOWN:
                    
                    # checking if key "0" was pressed
                    if event.key == pygame.K_KP0:
                        if not HumanX_pressed:
                            HumanX=0
                            HumanX_pressed=True
                        else:
                            HumanY=0
                            HumanY_pressed=True

                    # checking if key "1" was pressed
                    if event.key == pygame.K_KP1:
                        if not HumanX_pressed:
                            HumanX=1
                            HumanX_pressed=True
                        else:
                            HumanY=1
                            HumanY_pressed=True
                    # checking if key "2" was pressed
                    if event.key == pygame.K_KP2:
                        if not HumanX_pressed:
                            HumanX=2
                            HumanX_pressed=True
                        else:
                            HumanY=2
                            HumanY_pressed=True
                    # checking if key "3" was pressed
                    if event.key == pygame.K_KP3:
                        if not HumanX_pressed:
                            HumanX=3
                            HumanX_pressed=True
                        else:
                            HumanY=3
                            HumanY_pressed=True
                    # checking if key "4" was pressed
                    if event.key == pygame.K_KP4:
                        if not HumanX_pressed:
                            HumanX=4
                            HumanX_pressed=True
                        else:
                            HumanY=4
                            HumanY_pressed=True
                    # checking if key "5" was pressed
                    if event.key == pygame.K_KP5:
                        if not HumanX_pressed:
                            HumanX=5
                            HumanX_pressed=True
                        else:
                            HumanY=5
                            HumanY_pressed=True
                    # checking if key "6" was pressed
                    if event.key == pygame.K_KP6:
                        if not HumanX_pressed:
                            HumanX=6
                            HumanX_pressed=True
                        else:
                            HumanY=6
                            HumanY_pressed=True
            if self.someone_win:
                self.win.fill(WHITE)
                font = pygame.font.Font('freesansbold.ttf', 25)
                text_obj_winning = font.render(self.winning_text, True, GREEN)
                self.win.blit(text_obj_winning, (200,100))
                pygame.display.update()
                continue
            self.mouse_position=pygame.mouse.get_pos()
            # UI matice drawn
            # print("drawing Ui table")
            self.State.Draw(True)

            
            
            pygame.display.update()
            
            if  HumanX_pressed and HumanY_pressed:
                print("x and y given stopping the loop")
                print("x:",HumanX,"y",HumanY)
                # pygame.display.update()
                break
        
        print("now drawing the normal mat")
        # HumanX = int(input("Please enter the 'X' coordinate of your choice (an integer such as 4): "))
        # HumanY = int(input("Please enter the 'Y' coordinate of your choice (an integer such as 4): "))
        self.State.Draw(False)
        print("outside loop",HumanX,HumanY)
        if (HumanX, HumanY) not in self.State.children:
            self.State.Make(HumanX, HumanY, False)
            self.State = self.State.children[(HumanX, HumanY)]
        else:
            self.State = self.State.children[(HumanX, HumanY)]


        print("Current Score =====>> Your Score - AI Score = " + str(self.State.CurrentScore),end ="\n\n\n")

        self.Computer()

           
        

    def Computer(self): # Defining the Computer player and its actions/Choices
        self.State.Draw(False)

        move = Algo.miniMax(self.State, self.Ply_num)

        self.State = self.State.children[(move[0], move[1])]

        print("AI selected the following coordinates to play:\n" + "(" ,str(move[0]), ", " + str(move[1]), ")", end = "\n\n")
        self.AI_move=f"({move[0]},{move[1]})"
        print("Current Score =====>> Your Score - AI Score = " + str(self.State.CurrentScore), end = "\n\n\n")
        self.current_score_UI=f"{self.State.CurrentScore}"
        if len(self.State.children) == 0:
            self.State.Draw(False)
            self.Evaluation()
            return

        self.Human()

    def Evaluation(self): # Evaluation function for taking care of the final scores
        print("Stop this Madness!!!\n")
        if self.State.CurrentScore > 0:
            print("You won you crazy little unicorn!! You are the new hope for the mankind!")
            self.If_wins("human")
            # exit()
        elif self.State.CurrentScore < 0:
            print("!!! Inevitable Doom!!! You were crushed by the AI!! ")
            self.If_wins("ai")
            # exit()
        else:
            print("Draw! Well Congratulations! you are as smart as the AI!")
            self.If_wins("draw")
            # exit()
        self.Human()

    def start(self):
        self.Human()
    
    def If_wins(self,player="draw"):
        self.someone_win=True
        if player =="human":
            self.winning_text="Congratulation You have defeated the AI"
        elif player== "ai":
            self.winning_text="AI wins"
        else:
            self.winning_text="Its a Draw"
        
