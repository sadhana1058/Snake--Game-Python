import tkinter
import random

#initilizing the number of rows and columns and size of each block in our game
rows,cols,tile_size = 25,25,25

# setting the dimensions of the game
wwidth,hheight = tile_size*rows,tile_size*cols

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = tkinter.Tk()
window.title("snake")
window.resizable(False,False)

#setting up a canvas board
canvas = tkinter.Canvas(window,bg="black",width = wwidth,height=hheight)
canvas.pack()

#updating that the frame ith black bg is set
window.update()

#let us get the mac dimensions nd then place the window in center
game_width ,game_height= window.winfo_width(),window.winfo_height()
mac_width ,mac_height = window.winfo_screenwidth(),window.winfo_screenheight()

#after getting dimensions we are dividing half of screen width and screen hight
# to get screen center then we try to to top left corner
window_x = int((mac_width/2)-(game_width/2))
window_y = int((mac_height/2)-(game_height/2))


window.geometry(f"{game_width}x{game_height}+{window_x}+{window_y}")


# initializing the game 
# 5*tile_size indicates that 5th row and 5 th column in the the game board
# for better understanding try replace the 5 wiith 6 or 7 or 8 the position keeps changing 
snake =  Tile(5*tile_size,5*tile_size)
food = Tile(15*tile_size,15*tile_size)

#to store the bodyparts of snake
snake_body = []

#snake should move in x,y direction at a certain spped
velocityX ,velocityY =0,0

game_over = False
score = 0

def change_direction(e): #e = event

    global velocityY,velocityX,game_over,score
    # print(e) -><KeyRelease event state=Lock|Mod3|Mod4 keysym=Left keycode=2063660802 x=177 y=119>
    # print(e.keysym)#symbol of key

    if e.keysym == "Up"  and velocityY !=1:
        velocityX=0
        velocityY= -1

    elif e.keysym == "Down" and velocityY !=-1:
        velocityX=0
        velocityY= 1

    elif e.keysym == "Right" and velocityX !=-1:
        velocityX= 1
        velocityY= 0

    elif e.keysym == "Left" and velocityX!=1:
        velocityX=-1
        velocityY=0

def move():
    global snake,food,snake_body,game_over,score

    if (game_over):
        return 
    
    if (snake.x<0 or snake.y<0 or snake.x>= wwidth or snake.y>=hheight):
        game_over = True
        return

    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over=True
            return


    #checking if the snake collides the food then the body gets updated
    if(snake.x==food.x and snake.y ==food.y):
        snake_body.append(Tile(food.x,food.y))
        food.x = random.randint(0,cols-1)*tile_size
        food.y = random.randint(0,rows-1)*tile_size
        score += 1




    #updating the snake body
    for i in range(len(snake_body)-1,-1,-1):
        tile = snake_body[i]
        if i==0:
            tile.x,tile.y=snake.x,snake.y
        else:
            prev_tile = snake_body[i-1] 
            tile.x,tile.y=prev_tile.x,prev_tile.y
    

    #if we dont multiply into tole sixe then this will move one pixewl only
    snake.x += velocityX*tile_size
    snake.y += velocityY*tile_size
   
    
def draw():
    global snake,food,snake_body,game_over,score

    move()
    #usin
    #drawing snake alone without clearing the old frame along with move wil cause  the snake to grow infinitely without foood 
    #clearing the framne each tiume
    canvas.delete("all")



    canvas.create_rectangle(food.x,food.y,food.x+tile_size,food.y+tile_size,fill = 'yellow')
    
    #we should take care of right and left reversal as
    # in game we cant allow reverse in same direction
    #  we can allow left the up or dow n then left or right that can be taken care of in move function if block by adding and


    canvas.create_rectangle(snake.x,snake.y,snake.x+tile_size,snake.y+tile_size,fill = 'green')
    
    #just body is moving but head as to get attached to head and rest of the body
    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y,tile.x +tile_size,tile.y+tile_size,fill="lime green")

    if (game_over):
        canvas.create_text(wwidth/2, hheight/2, font = "Arial 20", text = f"Game Over: {score}", fill = "white")
    else:
        canvas.create_text(30, 20, font = "Arial 10", text = f"Score: {score}", fill = "white")
    
    window.after(100,draw)#100ms  is 1/10th of sec 10 frames per second
draw()

#let us associate the release of the key with start of the game with the help of below functioon
window.bind("<KeyRelease>", change_direction)



window.mainloop()