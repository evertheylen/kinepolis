
origlocals = locals()  # used for suff like __name__ etc (see below)
backendlocals = {}

import datastruct
import classes
import sorting

from etc import *

from example_init import example_cinema

from code import InteractiveConsole
import rlcompleter  # modified one!
import readline

import inspect

# Backend

def start_backend(data, save):
    # this will modify the backendlocals to contain the actual backendlocals.
    # it is used in create(T), to eval() stuff like 'data["kinepolis"]...'
    global backendlocals
    
    console = InteractiveConsole()
    
    backendlocals = {
        "switchDataStructure": switchDataStructure,
        "data": data,
        "save": save,
        "create": create,
        "example_cinema": example_cinema,
    }
    
    backendlocals.update(classes.__dict__)  # add module classes to console
    backendlocals.update(datastruct.__dict__)  # add module datastruct to console
    backendlocals.update(sorting.__dict__)  # add module sorting to console
    backendlocals.update(origlocals)  # reset the stuff that might otherwise be modifed by importing other modules (like __package__ and __name__)
    
    console.locals = backendlocals
    
    console.locals['credits'] = type(credits)("credits",
        "\n\n"+fancytext("Anthony")+"\n\n"+fancytext("Pieter")+"\n\n"+fancytext("Stijn")+"\n\n"+fancytext("Evert"))
    
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
        backendlocals = console.locals  # again for create(T)
    
    #command = get_command()




# start of backend locals
# these functions should only be called in the backend console

#def args(T):
    ##args for T.__init__: T.__init__.__code__.co_varnames
    #args = T.__init__.__code__.co_varnames[1:]
    #print("The initializer of {} takes these arguments:\n\t{}".format(T.__name__, args))


def switchDataStructure(oldds, newT, newAttr=None, **kwargs):
    if newAttr == None:
        newAttr = oldds.attribute()
    newds = datastruct.createDataStructure(newT, newAttr, **kwargs)
    
    
    if type(newds) == datastruct.structures.BinTree:
        # instead of adding inorder, we'll add all elements to a redblacktree, which
        # is then converted to a binary tree. this will make the binary tree start
        # as a balanced one, instead of largely imbalanced due to inorder adding.
        
        rb = None
        if type(oldds) == datastruct.structures.RedBlackTree:
            # of course, if the old datastructure was a RBT already, we don't need to
            # convert it.
            rb = oldds
        else:
            rb = createDataStructure(datastruct.structures.RedBlackTree, newAttr)
            for element in oldds.inorder():
                rb.insert(element)
        
        # at this point, rb is a RBT with all data in it. We'll now add elements from
        # it in the Binary tree in preorder, so the binary tree will be balanced too.
        
        for element in rb.preorder():
            newds.insert(element)
    else:
        # this is the default case. just add elements to the new datastructure.
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
                paras[parname] = eval(input("%s? "%parname), backendlocals)
            else:
                inp = input("{} [{}]? ".format(parname, sig.parameters[parname]._default))
                if inp != '':
                    paras[parname] = eval(inp, backendlocals)
    
    return T(**paras)

# also example_cinema from example_init.py
