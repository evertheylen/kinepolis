import curses
import threading
import time



def framePrint(scr, frame):
    scr.clear()
    scr.addstr(frame)
    scr.refresh()


def main(scr):
    f = open('starwars.txt')
    
    line = 'START'
    
    curses.noecho()
    curses.cbreak()
    scr.keypad(True)
    
    while line != '':
        try:
            pause = int(f.readline())
        except:
            pass
            #print('THE END')
        
        frame =  '\n  ########################################################################'
        frame += '\n  #                                                                      #\n'
        
        for i in range(13):
            line = f.readline()
            frame += "  # {0: <68} #\n".format(line[:len(line)-1])
        
        frame += '  #                                                                      #\n'
        frame += '  ########################################################################\n'
        
        framePrint(scr, frame)
        
        time.sleep(0.04*pause)
    
    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()
    


if __name__ == '__main__':
    try:
        scr = curses.initscr()
        main(scr)
    except:
        curses.nocbreak()
        scr.keypad(False)
        curses.echo()
        curses.endwin()
