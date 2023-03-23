import pygame
pygame.init()

W, H = 500, 300
sc = pygame.display.set_mode((W, H))

song2 = r'C:\Users\ASER\Desktop\pp2\week7\zvuk-okeana-3d-zvuk-okeana.mp3'
song1 = r'C:\Users\ASER\Desktop\pp2\week7\heavy-rain-nature-sounds-8186.mp3'
song3 = r'C:\Users\ASER\Desktop\pp2\week7\Beauty.mp3'

playList=[]
playList.append(song1)
playList.append(song2)
playList.append(song3)


pygame.mixer.music.load(playList[1])
pygame.mixer.music.play()

clock = pygame.time.Clock()
FPS = 60
flPause = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_d:
                 pygame.mixer.music.load(playList[1])
                 pygame.mixer.music.play()
                
            elif event.key == pygame.K_a:
                pygame.mixer.music.load(playList[0])
                pygame.mixer.music.play()
            elif event.key == pygame.K_RSHIFT:
                pygame.mixer.music.stop()
 
    clock.tick(FPS)
    pygame.display.update()
