import msvcrt
import time

fin=10
co=0
a=0

print"PRESS ENTER TO START"
raw_input()
s_time=time.time()
while(1):
	key=msvcrt.getch()
	if key=='\xe0':
		co=co+1
		print"D",
		if co==fin:
			break	

fin=10
co=0
while(1):
	key=msvcrt.getch()
	if key=='\xe0':
		co=co+1
		print"\n\t\t  S",
		if co==fin:
			break

fin=10
co=0
while(1):
	key=msvcrt.getch()
	if key=='\xe0':
		co=co+1
		print"D",
		if co==fin:
			break

print"\n"

time_elapsed=time.time()-s_time
print"\nCONGRATS YOU JUST FINISHED THE GAME!"
print"TIME ELAPSED IS %s SECS"%str(round(time_elapsed))

'''
1. Mention controls for the game.
2. The game should be lost on pressing the wrong key
3. Fix controls of the game	
'''



