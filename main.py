import pygame
import math
import  random
#initialize the pygame
pygame.init()


# create the screen
screen = pygame.display.set_mode((800,600))

# title
pygame.display.set_caption("Space Invaders")
playerImg =  pygame.image.load('space-invaders.png')
pygame.display.set_icon(playerImg)
enemyImg = pygame.image.load('space_enemy.png')
enemyImg = pygame.transform.scale(enemyImg,(60,60))
backgroundImg = pygame.image.load('spaceImg.png')
backgroundImg = pygame.transform.scale(backgroundImg,(800,600))
bulletImg = pygame.image.load('bullet.png')
bullet_list = ["ready","ready","ready","ready"]
bulletImg_list = [bulletImg,bulletImg,bulletImg,bulletImg]
playerX  = 370
playerY = 560
running =True
cross=0
i=0
r=150
cX=370.0
cY=240.0
velocity = 10;
vX=0;
vY=velocity
playerX = cX
playerY = 560
t=0.0
pi=3.141
X_change=0
ln=0
enemyVx=2
enemyVy=[0.2,0.01,0.05,0.3,0.04,0.1,0.2,0.4]
hieght_gap=45
playerVx=0.8
bulletVy=2.4
bulletY=[0,0,0,0]
bulletX=[0,0,0,0]
total_bullets = 4
enemy_list = ["dead","dead","dead","dead","dead","dead","dead","dead"]
enemyX = [0,0,0,0,0,0,0,0]
enemyY = [0,0,0,0,0,0,0,0]
direction_list = [0,0,0,0,0,0,0,0]
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
font2 = pygame.font.Font('freesansbold.ttf',16)
enemyImg_list = [enemyImg,enemyImg,enemyImg,enemyImg,enemyImg,enemyImg,enemyImg,enemyImg]
total_enemies = 8
loop = 1

game_over=0
# def Show_score():
#     screen.blit(score,(100 ,100))
#     screen.blit("Game over",(100,206))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg_list[i],(x,y))
    enemy_list[i] = "live"
    V=random.randint(1,5000)
    enemyVy[i]=0.0001*V

def background():
    screen.blit(backgroundImg,(0,0))


def bullet(x,y,i):
    screen.blit(bulletImg_list[i],(x,y))
    bullet_list[i]="fire"

def collision(bullet_no,enemy_no):
    if bulletX[bullet_no] >= enemyX[enemy_no]-10 and bulletX[bullet_no]<enemyX[enemy_no]+40 and bulletY[bullet_no] < enemyY[enemy_no]+60 and bulletY[bullet_no]+16>enemyY[enemy_no] :
        return True
    else:
        return False



#icon
#icon = pygame.image.load('')
#Game loop

while running:
    # time.sleep(1)
    # t+=0.01
    # if(t==(2*pi*r)/velocity):
    #     t=0
    # r+=0.01
    # if(r>200):
    #     r-=100
    screen.fill((150, 20, 180, 0.01))
    # background added
    background()
    if game_over!=1:
        for index in range(8):
            # if direction_list[index]==0:
            #     if enemy_list[index] == "live":
            #         enemyY[index]+=enemyVx
            #         # print(enemyX[index])
            # else:
            #     if enemy_list[index] == "live":
            #         enemyX[index] -= enemyVx
            #         # print(enemyX[index])
            # if enemyX[index]>750 or enemyX[index]<0:
            #     enemyY[index]+=hieght_gap
            #     direction_list[index]=1-direction_list[index]
            if enemy_list[index] == "live":
                enemyY[index]+=enemyVy[index]
                if enemyY[index] >= 600:
                    enemy_list[index]="dead"
                    enemyX[index]=0
                    enemyY[index]=0
                    cross+=1
                    if cross==3:
                        game_over=1

        for index in range(8):
            if(enemy_list[index] == "live"):
                enemy(enemyX[index],enemyY[index],index)
        # player(playerX,playerY)
        # enemy(370, 30,)

        for index in range(4):
            bulletY [index]-= bulletVy

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether left or right keystroke is pressed.
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    X_change = -playerVx
                    # print(X_change)
                if event.key == pygame.K_RIGHT:
                    X_change = playerVx
                     # print(X_change)
                if event.key == pygame.K_SPACE:
                    for index in range(4):
                        if bullet_list[index] == "ready":
                            break
                    if index <= 3:
                        bullet(playerX + 16,playerY-30,index)
                        bulletY[index] = playerY - 30
                        bulletX[index] = playerX + 16

            if event.type == pygame.KEYUP:
                pressed_keys =  pygame.key.get_pressed()
                if pressed_keys[pygame.K_RIGHT]:
                    X_change = playerVx
                elif pressed_keys[pygame.K_LEFT]:
                    X_change = -playerVx
                else:
                    X_change=0



        playerX += X_change
        if(playerX<0):
            playerX=0
        elif playerX>736:
            playerX=736
        player(playerX, playerY)

        for index in range(4):
            if bulletY[index]<=0:
                bullet_list[index]="ready"
                bulletY[index]=playerY

        for index in range(4):
            if bullet_list[index] == "fire":
                bullet(bulletX[index], bulletY[index],index)

        if loop == 1:
            for index in range(8):
                if enemy_list[index] == "dead":
                    enemyX[index] = random.randint(1, 735)
                    enemyY[index] = -60
                    enemy(enemyX[index], enemyY[index], index)

        loop = (loop+1)%1000
        # print(str(loop)+" ")
        for i in range(4):
            for j in range(8):
                if(bullet_list[i] == "fire" and enemy_list[j] == "live"):
                    if collision(i,j)==True:
                        bullet_list[i]="ready"
                        bulletY[i]=playerY
                        bulletX[i]=playerX
                        enemy_list[j]="dead"
                        direction_list[j]=0
                        score+=1
        # print("\n"+str(score)+"\n")
        text = font2.render('Score : ' + str(score), True, (255, 255, 255), (2, 3, 4))
        screen.blit(text, (650, 40))
    else:
        text = font.render('Game Over \n Your Score : ' + str(score), True, (255, 255, 255), (2, 3, 4))
        screen.blit(text,(150,225))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # show_score()

    pygame.display.update()
    # playerX = cX + r*(math.sin((velocity*t)/r))
    # playerY = cY + r*(math.cos((velocity*t)/r))
    # print(playerX)
    # print(playerY)
    # playerX= cX + r*(1-math.cos((2*3.14*i)/100))
    #
    # # if playerX>cX+r and flag ==0:
    # if flag==0:
    #     # playerX+=0.1
    #     playerY = cY + math.sqrt(abs(r*r-((playerX - cX)*(playerX - cX))))
    #     flag=1
    # elif flag==1:
    #     # playerX+=0.1
    #     playerY = cY + math.sqrt(abs(r*r-((playerX-cX)*(playerX-cX))))
    # elif playerX<cX-r and flag==1:
    #     # playerX+=0.1
    #     playerY = cY  + math.sqrt(abs(r*r-((playerX-cX)*(playerX-cX))))
    #     flag=0
    # elif flag==1:
    #     # playerX-=0.1
    #     playerY = cY+math.sqrt(abs(r*r-((playerX-cX)*(playerX-cX))))

