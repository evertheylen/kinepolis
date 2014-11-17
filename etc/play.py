# Play the star wars movie!
# By Evert Heylen

import time

def framePrint(frame):
    print()
    print('   ########################################################################   ')
    print('   #                                                                      #   ')
    
    for l in frame:
        print('   # {0: <68} #   '.format(l))
    
    print('   #                                                                      #   ')
    print('   ########################################################################   ')
    print()

f = open('starwars.txt')

line = 'START'

while line != '':
    pause = int(f.readline())
    frame = []
    for i in range(13):
        line = f.readline()
        frame.append(line[:len(line)-1])
    
    
    framePrint(frame)
    
    time.sleep(0.01*pause)

print('THE END')