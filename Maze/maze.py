import pygame
import os


#IMPORTANT PYGAME/GENERAL CONCEPTS:
#SURFACE OBJECTS - a surface of set width and height which can have things drawn onto it, then drawn onto other surfaces or the screen
#RECT OBJECTS - an object defining a rectangular area, x and y coordinates of rect object and width and height of rect object required
#PYGAME.DISPLAY.FLIP() - updates the entire display
#FONT OBJECTS - Object specifically for making text using specific fonts
#BLIT - Draws one surface onto another surface
#ANTIALIASING - 'smoothing down' jagged edges on images. Reduces program speed.
#EVENTS - events are for getting the os events/queues such as if keys are pressed/if the mouse is clicked.
#CLOCK OBJECTS - monitors time within the game.

# MISC ATTRIBUTES

class colours:  # library of colours in rgb
    white = [255, 255, 255]
    black = [0, 0, 0]
    buttonBlue = [124, 176, 255]
    buttonDarkC = [89, 103, 181]
    space = [29, 41, 81]
    crimson = [220,20,60]


# END OF MISC ATTRIBUTES

# BASIC DISPLAY ATTRIBUTES

class mainDisplay:  # defines the mainDisplay

    def __init__(self):             #initialize self
        self.screenDisplay = pygame.display.set_mode(
            [1200, 720])  # creates the game window as a 1200x720px surface object
        pygame.display.set_caption("Maze")  # set window name as 'maze'
        self.edges = self.screenDisplay.get_rect() #sets the class variable 'edges' as the rect object created from the screenDisplay surface

class button:   #class for drawing a rectangle with text in the centre
    def __init__(self, x, y, width, height, text, fontSize, buttonColour, borderColour, fontColour,textX,textY):           #Initialize button with parameters x,y,width,height,text,font,fontSize,buttonColour,borderColour,fontColour,Display
                                            #(display surface to be drawn onto),xratio and yratio (ratios of text to centre - inefficient but explained later)

        #SETS INITIAL ATTRIBUTES
        self.x = x                                  #sets class attribute 'x' as the x input when button is initialized
        self.y = y                                  #sets class attribute 'y' as the y input when button is initialized
        self.width = width                          #sets class attribute 'width' as the width input when the button is initialized
        self.height = height                        #sets class attribute 'height' as the height input when the button is initialized
        #SETS BORDER OF BUTTON
        self.buttonBorder = pygame.Rect(self.x, self.y, self.width, self.height)            #defines the button border as a rect object with the predefined x,y,
                                                                                            #width and height attributes
        self.colour = buttonColour                                                          #defines colour attribute
        self.bordercolour = borderColour                                                    #and border colour attribute
        self.textx = textX                                                                  #sets buttons text coordinates
        self.texty = textY
        #SETS TEXT SURFACE IN BOX
        textFont = pygame.font.SysFont('Candara', fontSize)                              #sets the font of the text to the font established at definition of initialisation
        self.textSurface = textFont.render(text, False, fontColour,                      #Creates a font object using the font, font colour and text established
                                      None)                                         #Sets antialiasing to false and gives no background to text
    def drawButton(self,Display):
        pygame.draw.rect(Display.screenDisplay, self.colour, self.buttonBorder,
                         0)                                                         # draws the buttonBorder as a filled in rectangle onto the
                                                                                    # screenDisplay surface of the Display parameter passed on initialisation
                                                                                    # with button colour defined at initialisation
        pygame.draw.rect(Display.screenDisplay, self.bordercolour, self.buttonBorder,
                         10)                                                        # draws the buttonBorder as a border with a width of 10px and the
                                                                                    # border colour defined at intialisation definition
        Display.screenDisplay.blit(self.textSurface, (self.textx,self.texty))      # blits text onto screen
        pygame.display.flip()  # updates entire display

class text:                                                                         #creates text class for creating and blitting text to screen
    def __init__(self, x, y,  fontSize, fontColour, text, Display):            #Initialize text class with x coordinate, y coordinate, font, fontSize, fontColour,text used and
                                                                                    #Display to blit
        textFont = pygame.font.SysFont('Candara', fontSize)                              #defines font of text as a system font with font and fontSize as defined upon initialisation passing
        textSurface = textFont.render(text, False, fontColour, None)                #creates surface of text with text defined previously, font defined previously and font colour defined
                                                                                    #previously. antialiasing is set to false and there is no background for text
        Display.screenDisplay.blit(textSurface, (x, y))                             #blits text onto screenDisplay using predefined x and y coordinates
        pygame.display.flip()                                                       #updates full display


# END OF BASIC DISPLAY ATTRIBUTES

# FIRST SCREEN CODE


def firstScreen(Display):                                                                                         #Function to create the 'look' of the main menu, using Display parameter
    Display.screenDisplay.fill(colours.black)                                                                     #Clear display by setting display to black
    title = text((1200/24)*10, ((720 / 20) * 2), 96, colours.buttonDarkC, 'Maze', Display)                   #title becomes a 'text' object, with x coordinate 10/24 of screen
                                                                                                                        #y coordinate 2/20 of screen, font 'Candara', font size 96px,
                                                                                                                        #font colour is dark blue, text is 'Maze' and Display parameter used

    startButton = button(((1200 / 24) * 4), ((720 / 20) * 5), ((1200 / 24) * 16), (720 / 20)*2, "START", 48,    #startButton becomes a 'button' object with x coordinate 2/12 of screen
                         colours.buttonBlue, colours.buttonBlue, colours.buttonDarkC,                      #y coordinate is 5/20 of screen. width is 8/12 of screen, height is
                         (1200/48)*21,(720/40)*11)                                                           #1/10 of screen, text is 'START', font is 'Candara', font size is
    startButton.drawButton(Display)                                                                          #48px, colours defined by blue, blue and dark blue. text is centred

    continueButton = button(((1200 / 24) * 6), ((720 / 20) * 8), ((1200 / 24) * 12), (720 / 10), "Continue",  #continueButton becomes a 'button' object with x coordinate 3/12 of
                            36, colours.buttonBlue, colours.buttonBlue, colours.buttonDarkC,
                            (1200/48)*21,(720/40)*17)                                                          #screen, y coordinate 8/20 of screen, same height width and font
    continueButton.drawButton(Display)                                                                       #as start button
                                                                                                                        #text = 'continue', font size is 36px
                                                                                                                        #colours are blue, blue and dark blue, text is centred

    quitButton = button(((1200 / 12) * 3), ((720 / 20) * 11), ((1200 / 12) * 6), (720 / 10), "Quit", 36,     #quitButton becomes a 'button' object with same x coordinate,
                        colours.buttonBlue, colours.buttonBlue, colours.buttonDarkC, (1200/48)*22,(720/40)*23)         #width, height, font, font size and colours as continue button.
    quitButton.drawButton(Display)
                                                                                                                        #x ratio is 0.97 and y ratio is 0.95

    mainMenu(quitButton, startButton, continueButton, Display)                                                          #calls the main menu function with quitButton, startButton,
                                                                                                                        #continueButton, Display parameter. This makes the above buttons
                                                                                                                        #clickable to start the game, continue a previous save or quit.


def mainMenu(quit_button, start_button, continue_button,Display):                                                       #mainMenu makes menu clickable to star game, quit game or continue game
    mainMenu = True                                                                                                     #sets mainMenu to true to start while loop
    while mainMenu:                                                                                                     #while mainMenu is true
        for evento in pygame.event.get():                                                                               #for every 'event' that happens
            if evento.type == pygame.MOUSEBUTTONDOWN:                                                                   #if the event is the mouse being clicked
                if quit_button.buttonBorder.collidepoint(pygame.mouse.get_pos()):                                       #and if the mouse pointer is within the border of the quit button
                    pygame.quit()                                                                                       #quit the game
                    quit()
                elif start_button.buttonBorder.collidepoint(pygame.mouse.get_pos()):                                    #or if the mouse pointer is within the border of the start button
                    mainMenu = False                                                                                    #stop the main menu loop
                    player = mainSprite(1)                                                                              #set the player to a mainSprite object, the maze being used is the
                                                                                                                        #first maze, hence 1
                    mainGame(Display,1,player,False,SpriteClock)                                                        #start mainGame function with Display, first maze is 1, player is
                                                                                                                        #player object, loading is False (game is not loading), use spriteClock
                                                                                                                        #to track time. This starts the main Game (see L305)

                elif continue_button.buttonBorder.collidepoint(pygame.mouse.get_pos()):                                 #or if the mouse pointer is within the border of the continue button
                    if os.path.isfile('./sav.txt'):                                                                     #if sav.txt exists within the current folder of the program
                        loadGame(Display)                                                                               #call load game function with Display (see L342)
                        mainMenu = False                                                                                #set mainMenu to false to stop menu loop and move onto game
                    else:                                                                                               #if save file does not exist
                        errorMessage = button((1200 / 20) * 4, (720 / 20) * 8, (1200 / 20) * 12, (720 / 20) * 2,        #produce an error message which says 'No save file available'
                                              'No Save file available', 36, colours.buttonDarkC,             #in front of the continue button
                                              colours.space, colours.space,(1200/20)*7,(720/40)*17)
                        errorMessage.drawButton(Display)

#END OF FIRST SCREEN


#MAZE GENERATOR


class maze:                                         #defines class 'maze'
    def __init__(self,row,column,mazeID):           #defines initialisation with number of rows, columns and the mazeID
        self.mazeNo = mazeID                        #defines mazeNo of maze class as given mazeID parameter
        self.rows = row                             #defines rows of maze class as given row parameter
        self.columns = column                       #defines columns of maze class as given column parameter
        self.boxWidth = 1200/self.columns           #defines boxWidth for maze class as the width of the screen divided by number of columns
        self.boxHeight = 720/self.rows              #defines boxHeight for maze class as the height of the screen divided by number of rows
        self.unrendered = [[]]                      #defines unrendered for maze class as an empty 2D array, in future to be defined as the unrendered map of boxes for the maze.

    def drawMaze(self,Display):                                                                         #defines method 'drawMaze' with parameter 'Display'
        bx = 0                                                                                          #defines box x coordinate initially as 0
        by = 0                                                                                          #defines box y coordinate as initially 0
        Display.screenDisplay.fill(colours.black)                                                       #fills screen with black
        self.boxList = []                                                                               #creates an empty box list attribute for maze
        for i in range(0,len(self.unrendered)):                                                         #for every index between 0 and the length of the unrendered
            for index in range(0,len(self.unrendered[i])):                                              #for every index between 0 and the length of the current element in 2D array
                                                                                                        #defined above
                if self.unrendered[i][index] == 1:                                                      #if the current element is equal to '1'
                    self.currentBox = pygame.Rect(bx,by,self.boxWidth,self.boxHeight)                   #define a Rect object with the current box x coordinate, y coordinate and boxWidth
                                                                                                        # /height
                    self.boxList.append(self.currentBox)                                                #append the currentBox rect object to the boxlist in order to create a list of
                                                                                                        #where boxes are and their details.
                    pygame.draw.rect(Display.screenDisplay, colours.buttonBlue, self.currentBox, 0)     #draw the currentBox in blue onto the screen
                    pygame.draw.rect(Display.screenDisplay,colours.buttonDarkC,self.currentBox,5)       #draw a 5px border on the currentBox
                bx += self.boxWidth                                                                     #updates current box x coordinate to the coordinate of the next 'column' of boxes.
            bx = 0                                                                                      #when moving onto next element, reset current box x coordinate to zero
            by += self.boxHeight                                                                        #and update y coordinate to the coordinate of the next 'row' of boxes
        pygame.display.flip()                                                                           #Once maze has been rendered, update entire display
#END OF MAZE GENERATOR


#PLAYER CODE
class mainSprite:           #defines class of 'mainSprite' for main player
    def __init__(self,mazeno):          #defines initialisation and uses mazeno parameter to define the maze number sprite will spawn in
        self.x = 0                      #defines sprites x coordinate as initially 0
        self.y = 0                      #defines sprites y coordinate as initially 0
        self.mazeused = ''              #defines mazeused as empty, as it will be defined after an instance of mainSprite has been created
        self.mazeno = mazeno            #defines sprites mazeno as passed mazeno
        self.speedX = 10                #defines the speed of the sprite in the x direction as 10px
        self.speedY = (720/10)/8        #defines the speed of the sprite in the y direction as the height of the screen divided by 10 divided by 8
        self.spawnX = 0                 #defines the spawn x coordinate as initially 0
        self.spawnY = 0                 #defines the spawn y coordinate as initially 0
        self.currentX = 0               #'current' x and y coordinates are defined for the purposes of recursion later. Current X really means the current box the sprite is in
        self.currentY = 0               #current Y really means the current box the sprite is in. ACTUAL current 'x' and 'y' coordinates are defined in the sprites 'x' and 'y' attributes

    def collisionDetection(self,expectedX,expectedY,mazeused):                  #defines a function which will return true if it collides with something and false if it doesnt
        temporaryRect = pygame.Rect(expectedX,expectedY,self.width,self.height) #creates a temporary rect for the expected location of the sprite
        if temporaryRect.collidelistall(mazeused.boxList) == []:                #if the temporary rect doesnt collide with any of the boxes on the current maze
            return False                                                        #return false
        else:                                                                   #if it does collide with anything
            return True                                                         #return True

    def win(self,screenRectangle):                                              #defines the function for the sprite winning
        if screenRectangle.contains(self.playerRect) == False:                  #if the sprite touches the edge of the screen
            return True                                                         #return True

    def rectAnimate(self,clock,Display):                                        #Defines animation of the sprite, using a clock object and screen Display
        pygame.draw.rect(Display.screenDisplay,colours.black,self.playerRect)   #fills in the current player rect object with black to prevent the new frame of sprite animation
                                                                                #overlapping the old one
        self.playerRect = pygame.Rect(self.x,self.y,self.width,self.height)     #defines new player rect as the current x coordinate, y coordinate, width and height
        pygame.draw.rect(Display.screenDisplay,colours.crimson,self.playerRect) #draw the new frame of sprite animation in crimson onto screen
        pygame.display.flip()                                                   #update the full screen display
        currentTime = pygame.time.get_ticks()                                   #get current ticks of the clock passed to the function
        clock.tick(10)                                                          #update the number of ticks by 10, to wait for 10ms.

    def moveRight(self,expected,mazeused,Display):                                          #defines the way the sprite moves right
        if self.collisionDetection(expected,self.y,mazeused) == False:                      #if the sprite does not collide with any of the boxes in the maze used
            self.x = self.x + self.speedX                                                   #update the sprites x coordinate to 10px further than current x coordinate
            self.rectAnimate(SpriteClock,Display)                                           #animate the sprite so you can see this x coordinate update on the screen
            if self.x != expected:                                                          #if the x coordinate is not yet what was expected
                self.moveRight((self.currentX+(1200/mazeused.columns)),mazeused,Display)    #recur the function, passing the expected x value as being the currentX + the boxwidth of the maze
            else:                                                                           #otherwise
                self.currentX = self.x                                                      #set the current x to the current x coordinate and stop the sprite moving.

    def moveLeft(self,expected,mazeused,Display):                                           #defines the way the sprite moves left
        if self.collisionDetection(expected,self.y,mazeused) == False:                      #this function works the same as the moveRight function, except expected x coordinate is
            self.x = self.x-self.speedX                                                     #currentX - the boxWidth and x coordinate is updated to x coordinate - the speed of the sprite
            self.rectAnimate(SpriteClock,Display)
            if self.x != expected:
                self.moveLeft((self.currentX-(1200/mazeused.columns)),mazeused,Display)
            else:
                self.currentX = self.x

    def moveUp(self,expected,mazeused,Display):                                             #defines the way the sprite moves up
        if self.collisionDetection(self.x,expected,mazeused) == False:                      #collision works the same as previous movement functions
            self.y = self.y-self.speedY                                                     #update y coordinate to y coordinate - speed of sprite
            self.rectAnimate(SpriteClock,Display)                                           #movement works the same as other movement functions except with y coordinates
            if self.y != expected:
                self.moveUp((self.currentY-(720/mazeused.rows)),mazeused,Display)
            else:
                self.currentY = self.y

    def moveDown(self,expected,mazeused,Display):                                           #defines the way the sprite moves down
        if self.collisionDetection(self.x,expected,mazeused) == False:                      #movement works the same as moveUp except y coordinate updates by +speed not -speed
            self.y = self.y +self.speedY
            self.rectAnimate(SpriteClock,Display)
            if self.y != expected:
                self.moveDown(self.currentY+(720/mazeused.rows),mazeused,Display)
            else:
                self.currentY = self.y

    def spawn(self,Display):                                                        #defines spawning the sprite
        self.width = self.mazeused.boxWidth-20                                      #defines the width of the sprite as the width of the maze boxes -20
        self.height = self.mazeused.boxHeight -20                                   #defines the height of the sprite as the height of the maze boxes -20
        self.currentX = self.x                                                      #defines currentX as the x coordinate of the sprite
        self.currentY = self.y                                                      #defines currentY as the y coordinate of the sprite
        self.playerRect = pygame.Rect(self.x, self.y, self.width, self.height)      #creates the playerRect as a rect object with x coordinate, y coordinate, width and height
        pygame.draw.rect(Display.screenDisplay, colours.crimson, self.playerRect)   #draw the playerRect onto the screenDisplay
        pygame.display.flip()                                                       #update entire screen


#END OF PLAYER CODE

class mazeone(maze):                                                                #defines a subclass of the maze class called 'mazeone'
    def __init__(self):                                                             #initialize self
        super().__init__(10,10,1)                                                   #initializes superclass with 10 rows, 10 columns and the ID of 1
        self.unrendered = [[1,1,1,1,1,1,1,1,1,1],                                   #defines unrendered as a 10 by 10  2D array
                           [1,0,0,0,0,0,0,0,1,1],
                           [1,0,1,1,1,0,1,0,1,1],
                           [1,0,1,0,0,0,1,0,0,1],
                           [1,0,0,1,0,1,1,1,1,1],
                           [1,1,1,1,0,0,0,0,0,1],
                           [1,0,0,0,1,1,1,0,1,1],
                           [1,0,1,0,1,1,1,0,1,1],
                           [1,0,1,0,0,0,0,0,0,1],
                           [1,0,1,1,1,1,1,1,1,1]]

#START OF MAIN GAME


SpriteClock = pygame.time.Clock()                                                  #creates a clock called 'SpriteClock'


def keys(Display,mazeused,playerused,menuused):                                                     #define the keys function in order to define events that happen when certain keys are
                                                                                                    #pressed, with parameters of a maze, player and menu
    for event2 in pygame.event.get():                                                               #for every event that happens
        if event2.type == pygame.KEYDOWN:                                                           #if the event is that a key is pressed
            if event2.key == pygame.K_RIGHT:                                                        #if the key is the right arrow key
                playerused.moveRight(playerused.currentX+(1200/mazeused.columns),mazeused,Display)  #have the player move right by one square
            elif event2.key == pygame.K_LEFT:                                                       #else if the key pressed is the left arrow key
                playerused.moveLeft(playerused.currentX-(1200/mazeused.columns),mazeused,Display)   #have the player move left by one square
            elif event2.key == pygame.K_UP:                                                         #else if the key pressed is the up arrow key
                playerused.moveUp(playerused.currentY-(720/mazeused.rows),mazeused,Display)         #have the player move up by one square
            elif event2.key == pygame.K_DOWN:                                                       #else if the key pressed is the down arrow key
                playerused.moveDown(playerused.currentY+(720/mazeused.rows),mazeused,Display)       #have the player move down by one square
            elif event2.key == pygame.K_ESCAPE:                                                     #else if the key pressed is the escape key
                    menuused.open(Display)                                                          #open the esc menu
    while menuused.escMenu == True:                                                                 #while the menu is open
        for event3 in pygame.event.get():                                                           #for every event that happens
            if event3.type == pygame.KEYDOWN:                                                       # if the escape key is pressed
                if event3.key == pygame.K_ESCAPE:
                    menuused.close(Display,mazeused,playerused)                                     #close the menu
            elif event3.type == pygame.MOUSEBUTTONDOWN:                                             #if the mouse is clicked
                if menuused.quitButton2.buttonBorder.collidepoint(pygame.mouse.get_pos()):          #if the quit button is clicked, go back to first screen
                    firstScreen(Display)
                elif menuused.saveButton.buttonBorder.collidepoint(pygame.mouse.get_pos()):         #if the save button is clicked, save the game
                    saveGame(mazeused,playerused)


def mainGame(display,currentMaze,currentPlayer,loading,clock):          #combines the maze and player to create a game
    menu = inGameMenu()                                                 #creates an object called menu which is an inGameMenu
    Maze1 = mazeone()                                                   #makes Maze1, which is a mazeone object
    maze1bool = False                                                   #sets maze1bool to False initially

    if loading == True:                                                 #if the game has been loaded using a save file
        if currentMaze == 1:                                            #if the currentMaze Id is 1
            maze1bool = True                                            #set the maze1bool to true to let the program know the current maze being used is the first
            currentPlayer.mazeused = Maze1                              #set the mazeused by the player to Maze1
            Maze1.drawMaze(display)                                     #draw maze 1
            currentPlayer.spawn(display)                                #spawn the player into the maze

    elif loading == False:                                              #else if the game has not been loaded using a save file
        maze1bool = True                                                #set maze1bool to true for same reason as before
        currentPlayer.x = ((1200/10)*1)+10                              #set the players coordinates to the first empty space in maze 1
        currentPlayer.y = ((720/10)*1)+10
        currentPlayer.mazeused = Maze1                                  #set mazeused by the player to Maze1
        Maze1.drawMaze(display)                                         #draw maze1
        currentPlayer.spawn(display)                                    #spawn the player into the maze

    while maze1bool:                                                    #while the maze1bool is set to true
        keys(display,Maze1,currentPlayer,menu)                          #set the keys and the events associated with those keys
        if currentPlayer.win(display.edges):                            #if the player wins (touches the edge)
            display.screenDisplay.fill(colours.black)                   #fill the display with black
            winningText = text((1200/25)*10, (720/20)*9,76, colours.white, "You win!", display)  #put a text saying you win! on the screen
            currentTime = pygame.time.get_ticks()                       #get the current time
            clock.tick(1)                                               #wait for a few seconds
            maze1bool = False                                           #break the loop
            firstScreen(display)                                        #bring back to the firstScreen


#SAVE GAME


def saveGame(mazeused,playerused):                                                      #define function to save the game by collecting data from the current maze and current player
    saveFile = open('sav.txt','w')                                                      #open the new save file called 'sav.txt'. If there is another save file, this replaces it
    saveFile.writelines([str(mazeused.mazeNo)+"\n",str(playerused.x)+"\n",str(playerused.y)+"\n"])  #write the maze ID and player coordinates to the file
    saveFile.close()    #close the file


#LOAD GAME


def loadGame(Display):                                                                  #define function to load the game by reading 'sav.txt'
    saveFile = open('sav.txt','r')                                                      #open sav.txt
    data = []                                                                           #create an empty array called 'data'
    for line in saveFile.readlines():                                                   #append each line of data in the sav.txt array
        data.append(line)
    for number in range(len(data)):                                                     #remove the formatting ('\n') from each element of data
        data[number] = data[number].replace('\n','')
    playerL = mainSprite(int(data[0]))                                                  #create a player object which uses the maze ID supplied by the save data
    playerL.x = float(data[1])                                                          #coordinate of player object is the x and y coordinate supplied by the save data
    playerL.y = float(data[2])
    saveFile.close()                                                                    #close the file
    mainGame(Display,int(data[0]),playerL,True,SpriteClock)                             #start the main game with the new data transferred to the player and the maze, with loading = True


class inGameMenu:                                                                       #creates an ingame menu class
    def __init__(self):                                                                 # initialisation
        self.MenuBorder = pygame.Rect((1200/25)*9, (720/20)*7, (1200/25)*7, (720/20)*7) #creates a rect object with x coordinate = 9/25 of the screen, y coordinate = 7/20 of the screen
                                                                                        #width = 7/25 of the screen, height = 7/20 of the screen
        self.escMenu = False                                                            #set escMenu to initially false

    def open(self,Display):                                                             #define method 'open' to open the esc menu
        self.escMenu = True                                                             #set escMenu to True to define the esc menu as opening
        pygame.draw.rect(Display.screenDisplay,colours.buttonDarkC,self.MenuBorder)     #draws the menu border and menu fill onto screen
        pygame.draw.rect(Display.screenDisplay,colours.space,self.MenuBorder,5)
        self.saveButton = button((1200/25)*10, (720/20)*8, (1200/25)*5, (720/20)*2,"SAVE" , 38, colours.buttonBlue,  #creates the save and quit button on the menu
                                 colours.space, colours.buttonDarkC,(1200/48)*22,(720/40)*17)
        self.saveButton.drawButton(Display)
        self.quitButton2 =  button((1200/25)*10,(720/20)*11,(1200/25)*5,(720/20)*2,"QUIT",38,colours.buttonBlue,colours.space,colours.buttonDarkC,(1200/48)*22,(720/40)*23)
        self.quitButton2.drawButton(Display)
        pygame.display.flip()   #update the display fully

    def close(self,Display,mazeused,playerused):                                        #define method 'close' to close the esc menu
        self.escMenu = False                                                            #set escMenu to false to define the esc menu as closing
        pygame.draw.rect(Display.screenDisplay,colours.black,self.MenuBorder)           #cover over the menu with black
        pygame.draw.rect(Display.screenDisplay,colours.black,self.MenuBorder,5)
        mazeused.drawMaze(Display)                                                      #draw the maze over the black
        pygame.draw.rect(Display.screenDisplay,colours.crimson,playerused.playerRect)   #draw the playerRect over the black
        pygame.display.flip()                                                           #update the display


#START FUNCTION
def main():                 #define main function to start game when program is opened
    pygame.init()           #initialize pygame
    display = mainDisplay() #create the display by making display an instance of mainDisplay
    firstScreen(display)    #opens the first menu on the screen
    while True:             #while loop is not broken
        for event in pygame.event.get():  # for every event that happens in queue
            if event.type == pygame.QUIT:  # if event type is uninitialize pygame
                pygame.quit()               # quit pygame
                quit()                      # quit python

#END OF START FUNCTION


main()              #start the main function to start entire game.
