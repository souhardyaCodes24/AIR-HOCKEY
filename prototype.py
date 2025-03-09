# ALL IMPORTS
import pygame
pygame.font.init()


# CONSTANTS
HEIGHT,WIDTH=700,700

# SETTING UP REQUIREMENTS
w=pygame.display.set_mode((WIDTH,HEIGHT))
c=pygame.time.Clock()

# BOARD COLOR
board_color="cyan"



# DRAW GAME BOARD
def draw_board():
    

    
    pygame.display.update()

# PLUCK
ball_diameter=45
ball_spawn=350
stepx=9.5
stepy=9.5

wall=650

b=pygame.image.load("b1.png")
ball=pygame.transform.scale(b,(ball_diameter,ball_diameter))
puck=pygame.Rect(ball_spawn,ball_spawn,ball_diameter,ball_diameter)



    
    

def move_puck(puck):
    global stepx
    global stepy
    puck.x+=stepx
    puck.y+=stepy
    if puck.y>wall :
        puck.y=wall
        stepy=stepy*(-1)
    if puck.y<0:
        puck.y=0
        stepy=stepy*(-1)
    if puck.x>=wall:
        puck.x=wall
        stepx=stepx*(-1)
    if puck.x<0:
        puck.x=0
        stepx=stepx*(-1)

    


    pass






# PLAYER 1

player_spawn_x=350
player_spawn_y=540
player_height=70
player_width=70



player_1=pygame.Rect(player_spawn_x,player_spawn_y,player_height,player_width)
striker1=pygame.image.load("p1.png")
striker_1=pygame.transform.scale(striker1,(player_height,player_width))




# PLAYER 2

player_2=pygame.Rect(player_spawn_x,160,player_height,player_width)
striker2=pygame.image.load("p2.png")
striker_2=pygame.transform.scale(striker2,(player_height,player_width))




def move_stricker(grab1,grab2):
  
    if grab1 :
        mx,my=pygame.mouse.get_pos()
        player_1.x=mx
        player_1.y=my
        if  player_1.x+player_height>700 :
            player_1.x=700-player_height
        if player_1.y+player_height>700:
            player_1.y=700-player_height
        if player_1.x<0:
            player_1.x=0
        if player_1.y<0:
            player_1.y=0

            
    if grab2 :
        mx,my=pygame.mouse.get_pos()
        player_2.x=mx
        player_2.y=my
        if  player_2.x+player_height>700 :
            player_2.x=700-player_height
        if player_2.y+player_height>700:
            player_2.y=700-player_height
        if player_2.x<0:
            player_2.x=0
        if player_2.y<0:
            player_2.y=0


    






# CHECK FOR COLLISION

def check_hit(player,puck):
    global stepx
    global stepy
    if player.colliderect(puck):
        
  

        
        stepy=stepy*(-1)

# failed fucntion
def check_collision(player,puck):
    global stepx
    global stepy
    if puck.y+ball_diameter == player.y and player.x<puck.x<player.x+player_height: #ok
        stepy=stepy*(-1)
    if puck.y+ball_diameter==player.y and player.x<puck.x+ball_diameter<player.x+player_height: #ok
        stepy=stepy*(-1)
    if puck.x==player.x+player_height and player.y< puck.y<player.y+player_height:#ok
        stepx=stepx*(-1)
    if puck.x==player.x+player_height and player.y+player_height<puck.y+ball_diameter<player.y+player_height:#ok
        stepx=stepx*(-1)
    if puck.x+ball_diameter==player.x and player.y<puck.y+ball_diameter<player.y+player_height: #ok
        stepx=stepx*(-1)
    if puck.x+ball_diameter==player.x and player.y<puck.y+ball_diameter<player.y+player_height:#ok
        stepx=stepx*(-1)
    if puck.y==player.y+player_height and player.x<puck.x+ball_diameter<player.x+player_height:#ok
        stepy=stepy*(-1)
    if puck.y==player.y+player_height and player.x<puck.x<player.x+player_height:#ok
        stepy=stepy*(-1)


# UPDATE SCORE

SCORE_FONT= pygame.font.SysFont("comicsans",20,"bold")
score_colour1="magenta"
score_colour2="green"




# MAIN GAME LOOP
def main():
    grab1=False
    grab2=False
    player_1_score=0
    player_2_score=0
    PAUSED=False
 
    
    FPS=24
    run=True
    

    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                break
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    grab1=True
                    grab2=False
                if event.key==pygame.K_2:
                    grab2=True
                    grab1=False
                if event.key==pygame.K_SPACE:
                    PAUSED=True
        while PAUSED:
            pygame.display.update()
            pygame.time.delay(4)
            pause_text=SCORE_FONT.render(f"GAME PAUSED",1,"yellow")
            w.blit(pause_text,(350,310))
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                
                    if event.key==pygame.K_SPACE:
                        PAUSED=False

        w.fill("black")
        

        # MAKING THE BOARD
        middle_line=pygame.Rect(0,HEIGHT//2,WIDTH,2)
        pygame.draw.rect(w,board_color,middle_line)

        p1_goal1=pygame.Rect(250,0,2,50)
        pygame.draw.rect(w,board_color,p1_goal1)

        p1_goal2=pygame.Rect(450,0,2,50)
        pygame.draw.rect(w,board_color,p1_goal2)

        p1_goal3=pygame.Rect(250,50,200,2)
        pygame.draw.rect(w,board_color,p1_goal3)

        p2_goal1=pygame.Rect(250,650,2,50)
        pygame.draw.rect(w,board_color,p2_goal1)

        p2_goal2=pygame.Rect(450,650,2,50)
        pygame.draw.rect(w,board_color,p2_goal2)

        p2_goal3=pygame.Rect(250,650,200,2)
        pygame.draw.rect(w,board_color,p2_goal3)



        w.blit(striker_1,(player_1.x,player_1.y))
        w.blit(striker_2,(player_2.x,player_2.y))
        move_stricker(grab1,grab2)
      
        

        
        
        
        check_hit(player_1,puck)
        check_hit(player_2,puck)
        move_puck(puck)
        w.blit(ball,(puck.x,puck.y))
    
        #SCORE OF PLAYER 1
        score_actual=SCORE_FONT.render(f"SCORE : {int(player_1_score)}",1,score_colour1)
        w.blit(score_actual,(20,20))
        if puck.y==0 and 250<puck.x<450:
            player_1_score+=1

        # SCORE OF PLAYER 2
        score_actual_2=SCORE_FONT.render(f"SCORE : {int(player_2_score)}",1,score_colour2)
        w.blit(score_actual_2,(20,650))
        
        if puck.y==wall and 250<puck.x<450:
            player_2_score+=1
            print("FUKCC")
        

        

        
        
        
        
        
        

        
        
     
       

        pygame.display.update()
        c.tick(FPS)
        
        


main()
