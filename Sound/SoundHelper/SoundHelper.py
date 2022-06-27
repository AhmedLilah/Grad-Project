import pygame

def playSound(sound,vol):
	path = 'Sound/Sounds/'+sound
	pygame.mixer.init()
	pygame.mixer.music.load(path)
	pygame.mixer.music.set_volume(vol)
	pygame.mixer.music.play()