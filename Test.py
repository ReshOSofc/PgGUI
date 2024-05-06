from PgGUI import SimpleGUI
import pygame 

# SimpleGUI module will init: pygame.init()
#                             pygame.mixer.init()
#                             pygame.font.init()

screen = pygame.display.set_mode((1000,500),pygame.RESIZABLE)
pygame.display.set_caption("pyGUI SimpleGUI")

def on_submit(e):
    global MesagePopUp,UsernameEntry,SubmitButton,PasswordEntry
    if len(UsernameEntry.text)<3 or len(PasswordEntry.text)<3:
        # Re - initialize the message popup(timer = 50ms) with text value:
        if MesagePopUp.timer==None: # if the timer has finished
            MesagePopUp = SimpleGUI.Widget(x=0,y=SubmitButton.rect.y+SubmitButton.rect.height + 50,
                                      text="Username and password must be longer than 3 characters!",
                                      font = pygame.font.SysFont("Arial",20,None),bg=(100,5,5),border=10,
                                      border_radius=25,timer=50)
    else:
        SimpleGUI.Clear() # Clear the screen of SimpleGUI widgets
        # Re - initialize the message popup(timer = 50ms) with text value:
        MesagePopUp = SimpleGUI.Widget(x=0,y=50,
                                      text=f"Username: {UsernameEntry.text}  Password: {PasswordEntry.text}",
                                      font = pygame.font.SysFont("Arial",20,None),bg=(5,100,5),border=10,
                                      border_radius=25,timer=50)
            
# Build all SimpleGUI widgets (buttons / labels / entrys and popups)
Title = SimpleGUI.Widget(x = 0,y = 50,font=pygame.font.SysFont("Arial",40,None),
                        text = "The SimpleGUI Examples:")
UsernameEntry = SimpleGUI.Widget(x = 0,y = Title.rect.y+Title.rect.height + 50,font = pygame.font.SysFont("Arial",20,None),
                        text = "",width=150,bg=(10,10,10),entry=True,
                        active_bg=(50,50,50),border=5,border_radius=25,extend_entry=False,show_entry=None)
UsernameLabel = SimpleGUI.Widget(x=0,y = Title.rect.y+Title.rect.height + 50,font = pygame.font.SysFont("Arial",20,None),
                        text = "Username :")
PasswordEntry = SimpleGUI.Widget(x = 0,y = UsernameEntry.rect.y+UsernameEntry.rect.height + 50,font = pygame.font.SysFont("Arial",20,None),
                        text = "",width=150,bg=(10,10,10),entry=True,
                        active_bg=(50,50,50),border=5,border_radius=25,extend_entry=False,show_entry="X")
PasswordLabel = SimpleGUI.Widget(x = 0,y = UsernameEntry.rect.y+UsernameEntry.rect.height + 50,font = pygame.font.SysFont("Arial",20,None),
                        text = "Password :")
SubmitButton = SimpleGUI.Widget(x=0,y = PasswordLabel.rect.y+PasswordLabel.rect.height + 50,font = pygame.font.SysFont("Arial",20,None),
                        text = "Submit",bg = (15, 2, 26),active_bg=(57, 8, 94),command=on_submit,border=10,border_radius=25)
MesagePopUp = SimpleGUI.Widget(x=0,y=SubmitButton.rect.y+SubmitButton.rect.height + 50,font = pygame.font.SysFont("Arial",20,None),
                        bg=(255,5,5),border=10,border_radius=25,timer=0)
run = True 
while run:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            SimpleGUI.MouseClick(event.pos) # Check Mouse click event with SimpleGUI
        if event.type == pygame.MOUSEMOTION:
            SimpleGUI.MouseHover(event.pos) # Check Mouse hoover over SimpleGUI Widgets
        if event.type == pygame.KEYDOWN:
            SimpleGUI.GetKeyPress(event) # Get key event and insert it in the entry widget if selected

    # Set the label position to always be relative to the middle of the screen : 
    Title.rect.x = int(pygame.display.get_window_size()[0]/2) - int(Title.rect.width/2)
    UsernameLabel.rect.x = int(pygame.display.get_window_size()[0]/2 - UsernameLabel.rect.width - 20)
    UsernameEntry.rect.x = int(pygame.display.get_window_size()[0]/2)
    PasswordLabel.rect.x = int(pygame.display.get_window_size()[0]/2 - PasswordLabel.rect.width - 20)
    PasswordEntry.rect.x = int(pygame.display.get_window_size()[0]/2)
    SubmitButton.rect.x = int(pygame.display.get_window_size()[0]/2-SubmitButton.rect.width/2)
    MesagePopUp.rect.x = int(pygame.display.get_window_size()[0]/2-MesagePopUp.rect.width/2)
    
    SimpleGUI.Draw(screen) # Draw the SimpleGUI Widgets on the pygame screen
    pygame.display.update()