import datastruct
import classes
import sorting

from etc import *

from code import InteractiveConsole
import rlcompleter  # modified one!
import readline

import inspect

# Backend

def start_backend(data, save):
    console = InteractiveConsole()
    
    
    backendlocals = {
        "switchDataStructure": switchDataStructure,
        "data": data,
        "save": save,
        "create": create,
    }
    
    backendlocals.update(classes.__dict__)  # add module classes to console
    backendlocals.update(datastruct.__dict__)  # add module datastruct to console
    backendlocals.update(sorting.__dict__)  # add module sorting to console
    
    console.locals = backendlocals
    
    # OMG Tab completion!!!
    readline.set_completer(rlcompleter.Completer(console.locals).complete)
    readline.parse_and_bind("tab: complete")
    # OMG own modification to rlcompleter
    #readline.set_completer_delims(' \t\n`~!@#$%^&*()-=+[{]}\\|;:\'",<>/?') # original
    readline.set_completer_delims(' \t\n`~!@#$%^&*()-=+{]}\\|;:,<>/?') # no [,' or "  in here!
    
    while True:
        # no more color for input, too much bugs
        c = input("> ")
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

#def args(T):
    ##args for T.__init__: T.__init__.__code__.co_varnames
    #args = T.__init__.__code__.co_varnames[1:]
    #print("The initializer of {} takes these arguments:\n\t{}".format(T.__name__, args))


def switchDataStructure(oldds, newT, newAttr=None):
    if newAttr == None:
        newAttr = oldds.attribute()
    newds = datastruct.createDataStructure(newT, newAttr)
    
    for element in oldds.inorder():
        newds.insert(element)
        
    return newds


def create(T):
    # helper function to create new objects easily, without having to know how the code works.
    paras = {}
    
    sig = inspect.signature(T.__init__)
    for parname in sig.parameters:
        if parname != 'self':
            if sig.parameters[parname]._default == inspect._empty:
                paras[parname] = eval(input("%s? "%parname))
            else:
                inp = input("{} [{}]? ".format(parname, sig.parameters[parname]._default))
                if inp != '':
                    paras[parname] = eval(inp)
    
    return T(**paras)


