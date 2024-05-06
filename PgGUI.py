import pygame

class SimpleGUI:
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    Widgets = []
    Selection = None
    class Widget():
        def __init__(self,x=0,y=0,width=None,height=None,min_width = None,min_height = None,
                     max_width = None,max_height = None,text="",font = pygame.font.SysFont("Arial",20,None),
                     fg=(255,255,255,0),bg=None,image=None,image_size=(None,None),anchor = "C",
                     border=0, border_radius = 0, border_color = None,
                     command=None,on_hover=None, active_fg=None,
                     entry = False,extend_entry=True,show_entry=None, active_bg=None,
                     timer = None,on_timer_tick = None,on_timer_end = None):
            self.min_width = min_width 
            self.min_height = min_height 
            self.max_width = max_width 
            self.min_height = max_height
            self.anchor = anchor
            self.on_timer_tick = on_timer_tick
            if on_timer_end!=None:
                self.on_timer_end = on_timer_end
            else:
                self.on_timer_end = self.Destroy
            if timer!=None:
                self.timer = timer*100 
            else:
                self.timer = None
            self.entry = entry
            self.show_entry = show_entry
            self.extend_entry = extend_entry
            self.font = font 
            self.fg = fg 
            self.bg = bg 
            self.widget_image = None 
            self.widget_text = None
            self.image_size = image_size
            if image!=None:
                self.image = image 
                self.widget_image = pygame.image.load(self.image)
                if self.image_size!=(None,None):
                    self.widget_image = pygame.transform.scale(self.widget_image,self.image_size)
            else:
                self.image = None 
            if text!=None:
                self.text = text 
                if self.entry == True and self.show_entry!=None:
                    if self.bg!=None:
                        self.widget_text = self.font.render(self.show_entry*len(self.text),True,self.fg,self.bg)
                    else:
                        self.widget_text = self.font.render(self.show_entry*len(self.text),True,self.fg)
                else:
                    if self.bg!=None:
                        self.widget_text = self.font.render(self.text,True,self.fg,self.bg)
                    else:
                        self.widget_text = self.font.render(self.text,True,self.fg)
            else:
                self.text = None

            if self.widget_image!= None and self.widget_text!=None:
                if self.widget_image.get_rect().width*self.widget_image.get_rect().height>self.widget_text.get_rect().width*self.widget_text.get_rect().height:
                    self.rect = self.widget_image.get_rect()
                else:
                    self.rect = self.widget_text.get_rect()
            elif self.widget_image!=None:
                self.rect = self.widget_image.get_rect()
            elif self.widget_text!=None:
                self.rect = self.widget_text.get_rect()

            if self.image!=None and image_size==(None,None):
                self.widget_image = pygame.transform.scale(self.widget_image,(self.rect.width,self.rect.height))

            self.rect.x = x 
            self.rect.y = y
            if width!=None:
                self.rect.width = width
                if self.min_width == None:
                    self.min_width = width
            if height!=None:
                self.rect.height = height  
                if self.min_height == None:
                    self.min_height = height

            self.border = border 
            if border_color!=None:
                self.border_color = border_color 
            else:
                if self.bg!=None:
                    self.border_color = self.bg 
                else:
                    self.border_color = (50,50,50)
            self.border_radius = border_radius 
            
            self.on_hover = on_hover
            self.command = command 
            if active_fg==None:
                self.active_fg = fg 
            else:
                self.active_fg = active_fg
            if active_bg == None:
                if self.bg!=None:
                    self.active_bg = self.bg
                else:
                    self.active_bg = (50,50,50)
            else:
                self.active_bg = active_bg

            self.SavedColors = [self.bg,self.fg,self.border_color]
            
            SimpleGUI.Widgets.append(self)

        def Update(L):
            if L.image!=None:
                L.widget_image = pygame.image.load(L.image)
                if L.image_size!=(None,None):
                    L.widget_image = pygame.transform.scale(L.widget_image,L.image_size)
            if L.text!=None:
                if L.show_entry !=None:
                    L.widget_text = L.font.render(L.show_entry*len(L.text),True,L.fg)
                else:
                    L.widget_text = L.font.render(L.text,True,L.fg)
            
            if L.widget_image!= None and L.widget_text!=None:
                if L.widget_image.get_rect().width*L.widget_image.get_rect().height>L.widget_text.get_rect().width*L.widget_text.get_rect().height:
                    if L.extend_entry == True:
                        L.rect.width = L.widget_image.get_rect().width
                    L.rect.height = L.widget_image.get_rect().height
                else:
                    if L.extend_entry == True:
                        L.rect.width = L.widget_text.get_rect().width
                    L.rect.height = L.widget_text.get_rect().height
            elif L.widget_image!=None:
                if L.extend_entry == True:
                    L.rect.width = L.widget_image.get_rect().width
                L.rect.height = L.widget_image.get_rect().height
            elif L.widget_text!=None:
                if L.extend_entry == True:
                    if L.min_width!=None:
                        L.rect.width = max([L.min_width,L.widget_text.get_rect().width])  
                L.rect.height = L.widget_text.get_rect().height

            if L.image!=None and L.image_size==(None,None):
                L.widget_image = pygame.transform.scale(L.widget_image,(L.rect.width,L.rect.height))
        def Destroy(self):
            SimpleGUI.Widgets.remove(self)
    def Draw(screen):
        for L in SimpleGUI.Widgets:
            if L.bg!=None:
                pygame.draw.rect(screen,L.bg,pygame.rect.Rect(L.rect.x-L.border,L.rect.y-L.border,L.rect.width+L.border*2,L.rect.height+L.border*2),0,L.border_radius)
            if L.border>0:
                pygame.draw.rect(screen,L.border_color,pygame.rect.Rect(L.rect.x-L.border,L.rect.y-L.border,L.rect.width+L.border*2,L.rect.height+L.border*2),L.border,L.border_radius)
            if L.image!=None:
                if L.anchor == "NW":
                    screen.blit(L.widget_image,L.rect)
                if L.anchor == "W":
                    screen.blit(L.widget_image,(L.rect.x,L.rect.y+int(L.rect.height/2)-int(L.widget_image.get_rect().height/2)))
                if L.anchor == "SW":
                    screen.blit(L.widget_image,(L.rect.x,L.rect.y+int(L.rect.height)-int(L.widget_image.get_rect().height)))
                if L.anchor == "S":
                    screen.blit(L.widget_image,(L.rect.x+int(L.rect.width/2)-int(L.widget_image.get_rect().width/2),L.rect.y+int(L.rect.height-L.widget_image.get_rect().height)))
                if L.anchor == "SE":
                    screen.blit(L.widget_image,(L.rect.x+L.rect.width-L.widget_image.get_rect().width,L.rect.y+int(L.rect.height)-int(L.widget_image.get_rect().height)))
                if L.anchor == "E":
                    screen.blit(L.widget_image,(L.rect.x+L.rect.width-L.widget_image.get_rect().width,L.rect.y+int(L.rect.height/2)-int(L.widget_image.get_rect().height/2)))
                if L.anchor == "NE":
                    screen.blit(L.widget_image,(L.rect.x+L.rect.width-L.widget_image.get_rect().width,L.rect.y))
                if L.anchor == "N":
                    screen.blit(L.widget_image,(L.rect.x+int(L.rect.width/2)-int(L.widget_image.get_rect().width/2),L.rect.y))
                if L.anchor == "C":
                    screen.blit(L.widget_image,(L.rect.x+int(L.rect.width/2)-int(L.widget_image.get_rect().width/2),L.rect.y+int(L.rect.height/2)-int(L.widget_image.get_rect().height/2)))

            if L.text!=None:
                if L.anchor == "NW":
                    screen.blit(L.widget_text,L.rect)
                if L.anchor == "W":
                    screen.blit(L.widget_text,(L.rect.x,L.rect.y+int(L.rect.height/2)-int(L.widget_text.get_rect().height/2)))
                if L.anchor == "SW":
                    screen.blit(L.widget_text,(L.rect.x,L.rect.y+int(L.rect.height)-int(L.widget_text.get_rect().height)))
                if L.anchor == "S":
                    screen.blit(L.widget_text,(L.rect.x+int(L.rect.width/2)-int(L.widget_text.get_rect().width/2),L.rect.y+int(L.rect.height-L.widget_text.get_rect().height)))
                if L.anchor == "SE":
                    screen.blit(L.widget_text,(L.rect.x+L.rect.width-L.widget_text.get_rect().width,L.rect.y+int(L.rect.height)-int(L.widget_text.get_rect().height)))
                if L.anchor == "E":
                    screen.blit(L.widget_text,(L.rect.x+L.rect.width-L.widget_text.get_rect().width,L.rect.y+int(L.rect.height/2)-int(L.widget_text.get_rect().height/2)))
                if L.anchor == "NE":
                    screen.blit(L.widget_text,(L.rect.x+L.rect.width-L.widget_text.get_rect().width,L.rect.y))
                if L.anchor == "N":
                    screen.blit(L.widget_text,(L.rect.x+int(L.rect.width/2)-int(L.widget_text.get_rect().width/2),L.rect.y))
                if L.anchor == "C":
                    screen.blit(L.widget_text,(L.rect.x+int(L.rect.width/2)-int(L.widget_text.get_rect().width/2),L.rect.y+int(L.rect.height/2)-int(L.widget_text.get_rect().height/2)))
            if L.timer!=None:
                if L.timer>0:
                    if L.on_timer_tick!=None:
                        L.on_timer_tick(L)
                    L.timer-=1
                elif L.timer==0:
                    L.timer = None
                    L.on_timer_end()
    def Clear():
        SimpleGUI.Widgets = []
    def MouseClick(pos=(None,None)):
        if pos!=(None,None):
            for L in SimpleGUI.Widgets:
                if L.rect.collidepoint(pos):
                    if L.command!=None:
                        L.command(L)
                    if L.entry == True:
                        # make auto clear on focus system:
                        SimpleGUI.Selection = L
    def MouseHover(pos=(None,None)):
        for L in SimpleGUI.Widgets:
                if L.rect.collidepoint(pos) and ((L.widget_text!=None and (L.command!=None or L.entry==True)) or L==SimpleGUI.Selection):
                    if L.entry == True and L.show_entry!=None:
                        L.widget_text = L.font.render(L.show_entry*len(L.text),True,L.active_fg)
                        L.bg = L.active_bg
                        L.border_color = L.active_bg
                    else:
                        L.widget_text = L.font.render(L.text,True,L.active_fg)
                        L.bg = L.active_bg
                        L.border_color = L.active_bg
                else:
                    if L.entry == True and L.show_entry!=None:
                        L.widget_text = L.font.render(L.show_entry*len(L.text),True,L.fg)
                        L.bg = L.SavedColors[0]
                        L.border_color = L.SavedColors[2]
                    else:
                        L.widget_text = L.font.render(L.text,True,L.fg)
                        L.bg = L.SavedColors[0]
                        L.border_color = L.SavedColors[2]
                if L.rect.collidepoint(pos) and L.on_hover!=None:
                    L.on_hover(L)
                
    def GetKeyPress(key = pygame.event.get()):
        if SimpleGUI.Selection != None:
            for E in SimpleGUI.Widgets:
                if E == SimpleGUI.Selection:
                    if key.unicode == "\x08":
                        E.text = E.text[:-1]
                    else:
                        if E.extend_entry == False:
                            if E.widget_text.get_rect().width<E.rect.width-E.border:
                                E.text += f"{key.unicode}"
                        elif E.max_width!=None:
                            if E.widget_text.get_rect().width<E.max_width:
                                E.text += f"{key.unicode}"
                        else:
                            E.text += f"{key.unicode}"
                    E.Update()
