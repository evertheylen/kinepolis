import datastruct
import classes
import sorting

from etc import *

from code import InteractiveConsole
import rlcompleter
import readline

# Backend

def start_backend(data, save):
    console = InteractiveConsole()
    
    backendlocals = {
        "args": args,
        "switchDataStruct": switchDataStruct,
        "data": data,
        "save": save,
    }
    
    backendlocals.update(classes.__dict__)  # add module classes to console
    backendlocals.update(datastruct.__dict__)  # add module datastruct to console
    backendlocals.update(sorting.__dict__)  # add module sorting to console
    
    console.locals = backendlocals
    
    while True:
        c = input(rgbtext("> ", green))
        if c == "q":
            return
            # exit
        else:
            try:
                if console.push(c): # console.push(c) executes the string c in the console.
                                    # if it is True, it means it expects more input (for example a function definition)
                    _input = ' '
                    totalcommand = ''
                    while _input!='':
                        _input = input('. ')
                        totalcommand += _input+'\n'
                    console.push(totalcommand)
            except Exception as e:
                print(rgbtext('Error: %s'%e))
            
        console.resetbuffer()
    
    #command = get_command()




# start of backend locals
# these functions should only be called in the backend console

def args(T):
    #args for T.__init__: T.__init__.__code__.co_varnames
    args = T.__init__.__code__.co_varnames[1:]
    print("The initializer of {} takes these arguments:\n\t{}".format(T.__name__, args))


def switchDataStruct(oldds, newT, newAttr):
    # TODO datatstruct should provide a function .attribute()
    newds = datastruct.createDataStruct(newT, oldds.attribute())
    
    for element in oldds.inorder():
        newds.insert(element)
        
    return newds