
import pygame
import pyganim
from random import randrange


gameIcon = pygame.image.load('bloco.png')
pygame.display.set_icon(gameIcon)
#constantes
aquarios = 0
avisos = 3
contador = 0
lista_blocos = []
lista_recorde=[]
surgir = False
caindo = False
# ===============      CLASSES      ===============
class Bloco(pygame.sprite.Sprite):
  
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.x < 0 or self.rect.x > 580:
            self.vx = - self.vx
                
    def cair(self, camera_pos):
        posx,posy = camera_pos
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.vx = 0
            self.vy = 4 
            if contador > 1 and self.rect.x in range(lista_blocos[contador-1][0]-50,lista_blocos[contador-1][0]+50):
                posy += 1.5
        return (posx,posy)

###########################################################

pygame.init()
#configurações iniciais
tela = pygame.display.set_mode((700,700), 0, 32)
pygame.display.set_caption("Shut Up n' Build")
musica=pygame.mixer.music.load("Jazzy Elevator Music.wav")
acerto = pygame.mixer.Sound("NFF-woody-02.wav")
encaixe = pygame.mixer.Sound("acerto.wav")
destruicao_shh = pygame.mixer.Sound("destruicao+shh.wav")
destruicao = pygame.mixer.Sound("destruicao.wav")
fundo = pygame.image.load("Background jogo.png").convert()
novo_recorde= pygame.image.load("novorecorde.png")

#cria bloco
bloco = Bloco("bloco.png", randrange(500),randrange(30,100),4, 0)
bloco_group = pygame.sprite.Group()
bloco_group.add(bloco)

#tela
tela.fill((0,0,0))
myfont = pygame.font.SysFont('Gadugi',25)
aquarios_imagem = pygame.image.load('aquarios.png')
recorde_imagem=pygame.image.load('recorde.png')
avisos_imagem = pygame.image.load('avisos.png')
tia1=pygame.image.load('tia1.png')
tia2=pygame.image.load('tia2.png')
score_texto = myfont.render(str(aquarios),1,(0,0,0))
avisos_texto = myfont.render(str(avisos),1,(0,0,0))
myfont2 = pygame.font.Font('game_over.ttf',100)
myfont3 = pygame.font.Font('game_over.ttf',80)
camera_pos = (0,-13260)
#constantes
rodando = False
configuracao = False
menu = True
pausa = False
errou= False
game_over = False
musicajogo = True
JAJA = 0 
#animação
animObj = pyganim.PygAnimation([('menulogo1.png', 800), ('menulogo2.png', 800)])
animObj.play()
mainclock=pygame.time.Clock()

#menu inicial
while menu:
 
    animObj.blit(tela, (0,0))
    mainclock.tick(30)
    keys = pygame.key.get_pressed()
    pygame.display.update()
    
    
        
    if keys[pygame.K_RETURN]:
        menu = False
        rodando = True
        
    if menu == False:
        animObj.stop()
        
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            menu = False
            rodando = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        menu = False
        configuracao = True
    
    #### musica para
    if keys[pygame.K_F2]:
        musicajogo = False
        
    while configuracao:
        conf1 = pygame.image.load('menu ajuda.png').convert()
        conf2 = pygame.transform.scale(conf1, (700, 700))
        tela.blit(conf2, (0,0))
        
        keys = pygame.key.get_pressed()
        pygame.display.update()
        if keys[pygame.K_LEFT]:
            menu = True
            configuracao = False
        
        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                menu = False
                configuracao = False
   
#Looping principal
if musicajogo == True:
    pygame.mixer.music.play(loops=-1, start=0.0)

while rodando:
  #move o bloco pela tela
    bloco.move()
    camera_pos = bloco.cair(camera_pos)
    if contador == 0:
        if bloco.rect.y >= 570.5 and bloco.rect.x in range(110,475):
            bloco.vy = 0
            bloco.vx = 0
            aquarios+=1
            if musicajogo == True:
                acerto.set_volume(0.5)
                acerto.play(loops=0, maxtime=0, fade_ms=10)
            surgir = True

            
        elif bloco.rect.y >= 700:
            errou = True
            avisos -= 1
            bloco.vx=0
            bloco.vy=0
            surgir = True
            contador-=1
            JAJA = 720
            if musicajogo == True:
                destruicao_shh.set_volume(1)
                destruicao_shh.play(loops=0, maxtime=0, fade_ms=10)
                       
    else:  #contador != 0
        
        if bloco.rect.y >= (lista_blocos[contador-1][1]-115) and bloco.rect.x in range(lista_blocos[contador-1][0]-2,lista_blocos[contador-1][0]+2):
               aquarios +=1
               surgir = True
               bloco.vx=0
               bloco.vy=0
               avisos += 1
               if musicajogo == True:
                   encaixe.set_volume(0.5)
                   encaixe.play(loops=0, maxtime=0, fade_ms=10)
               
        elif bloco.rect.y >= (lista_blocos[contador-1][1]-115) and bloco.rect.x in range(lista_blocos[contador-1][0]-57,lista_blocos[contador-1][0]+57):
                aquarios +=1
                surgir = True
                bloco.vx=0
                bloco.vy=0
                if musicajogo == True:
                    acerto.set_volume(0.5)
                    acerto.play(loops=0, maxtime=0, fade_ms=10)
                #for i in lista_blocos:
                #    i[1]+=115
        
        elif bloco.rect.y >= 700:
            errou = True
            avisos -= 1
            bloco.vx=0
            bloco.vy=0
            surgir = True
            contador-=1
            JAJA = 720
            if musicajogo == True:
                destruicao_shh.set_volume(1)
                destruicao_shh.play(loops=0, maxtime=0, fade_ms=10)
            
    if contador ==2 and surgir == True and errou == False:       
        for bloco in bloco_group:
            bloco.rect.y+=110
            for i in lista_blocos:
                i[1]+=110
            bloco_group.draw(tela)
            pygame.display.update()   
        
    if contador >2 and surgir == True and errou == False:       
        for bloco in bloco_group:
            bloco.rect.y+=113
            for i in lista_blocos:
                i[1]+=113
            bloco_group.draw(tela)
            pygame.display.update()  
            
    if avisos < 0:
        surgir = False
                            
    if surgir == True:
        if errou == True:
            contador+=1
            if contador%2==0:
                bloco = Bloco("bloco.png", randrange(500),randrange(30,40),4, 0)
                bloco_group.add(bloco)
            else:
                bloco = Bloco("bloco2.png", randrange(500),randrange(30,40),4, 0)
                bloco_group.add(bloco)
            
            errou = False
        else:
            listinha = []
            listinha.append(bloco.rect.x)
            listinha.append(bloco.rect.y)
            lista_blocos.append(listinha)
            contador+=1
            if contador%2==0:
                bloco = Bloco("bloco.png", randrange(500),randrange(30,40),4, 0)
                bloco_group.add(bloco)
            else:
                bloco = Bloco("bloco2.png", randrange(500),randrange(30,40),4, 0)
                bloco_group.add(bloco)
            
            
        
        surgir = False  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            rodando = False
        if event.type == "QUIT":
            pygame.mixer.quit()
            menu = False
            rodando = False
    
    #atualização da tela    
    
    tela.blit(fundo,camera_pos)
    bloco_group.draw(tela)
    score_texto = myfont.render(str(aquarios),1,(0,0,0))
    if avisos >= 0 :
        avisos_texto = myfont.render(str(avisos),1,(0,0,0))
    else:
        avisos_texto = myfont.render(str(0),1,(0,0,0))
    if JAJA < 350 and JAJA > 1:
        if avisos%2==0:
            tela.blit(tia1,(0,300))
        else:
            tela.blit(tia2,(550,300))
    tela.blit(aquarios_imagem,(20,10))
    tela.blit(avisos_imagem,(500,10))
    tela.blit(score_texto,(140,10))
    tela.blit(avisos_texto,(660,10))
    pygame.display.update()
    JAJA -=1
    
    if avisos < 0:
        lista_recorde.append(aquarios)
        game_over = True
        rodando = False
        pygame.time.delay(200)
        pygame.mixer.music.stop()
        if aquarios <=300:
            if musicajogo == True:
                musicagameover=pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.play(loops=0,start=0.0)
                pygame.mixer.music.set_volume(0.7)
        else:
            if musicajogo == True:
                musicagameover=pygame.mixer.music.load('musicaparabens.wav')
                pygame.mixer.music.play(loops=0,start=0.0)
                pygame.mixer.music.set_volume(0.7)                 
        
    while game_over:
        numero_final = myfont2.render(str(aquarios),1,(0,0,0))
        recorde_numero=max(lista_recorde)
        recorde = myfont3.render(str(recorde_numero),1,(0,0,0))
        
        if aquarios >=300:
            conf3 = pygame.image.load('parabens.png').convert()
            conf4 = pygame.transform.scale(conf3, (700, 700))
            tela.blit(conf4, (0,0))
            tela.blit(numero_final,(370,374))
            tela.blit(recorde_imagem,(250,10))
            tela.blit(recorde, (440,14))
            if aquarios>=int(recorde_numero):
                tela.blit(novo_recorde,(428,46))
                
        else:
            if aquarios < 10:
                conf3 = pygame.image.load('gameover.png').convert()
                conf4 = pygame.transform.scale(conf3, (700, 700))
                tela.blit(conf4, (0,0))
                tela.blit(numero_final,(380,365))
                tela.blit(recorde_imagem,(250,10))
                tela.blit(recorde, (440,14))
                if aquarios>=int(recorde_numero):
                    tela.blit(novo_recorde,(425,46))
                    
            elif aquarios >= 10 and aquarios < 100:
                conf3 = pygame.image.load('gameover.png').convert()
                conf4 = pygame.transform.scale(conf3, (700, 700))
                tela.blit(conf4, (0,0))
                tela.blit(numero_final,(375,365))
                tela.blit(recorde_imagem,(250,10))
                tela.blit(recorde, (440,14))
                if aquarios>=int(recorde_numero):
                    tela.blit(novo_recorde,(425,46))
                    
            elif aquarios >= 10 and aquarios < 300:
                conf3 = pygame.image.load('gameover.png').convert()
                conf4 = pygame.transform.scale(conf3, (700, 700))
                tela.blit(conf4, (0,0))
                tela.blit(numero_final,(370,374))
                tela.blit(recorde_imagem,(250,10))
                tela.blit(recorde, (440,14))
                if aquarios>=int(recorde_numero):
                    tela.blit(novo_recorde,(425,46))
            
            
                

            
        
        bloco_group.empty()
        pygame.display.update()    
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_F2]:
            musicajogo = False
            pygame.mixer.music.pause()            
        if keys[pygame.K_F3]:
            musicajogo = True
            pygame.mixer.music.play()
        
        if keys[pygame.K_UP]:
            rodando = True
            errou= False
            game_over = False
            aquarios = 0
            avisos = 3
            contador = 0
            lista_blocos = []
            surgir = False
            caindo = False
            JAJA = 0
            camera_pos = (0,-13260)
            if musicajogo == True:
                pygame.mixer.music.stop()
                musica=pygame.mixer.music.load("Jazzy Elevator Music.wav")
                pygame.mixer.music.play(loops=-1, start=0.0)
            tela.fill((0,0,0))
            pygame.display.flip()
            pygame.display.update()
            bloco = Bloco("bloco.png", randrange(500),randrange(30,100),4, 0)
            bloco_group = pygame.sprite.Group()
            bloco_group.add(bloco)
            pygame.display.update()   
            if musicajogo == False:
               pygame.mixer.music.stop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            
 #sair do jogo   
pygame.mixer.music.stop()
pygame.display.quit()
