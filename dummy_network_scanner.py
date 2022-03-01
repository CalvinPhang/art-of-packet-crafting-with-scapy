import getopt, sys
from netaddr import *
 
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
 
# Options
options = "r:e:"
 
# Long options
long_options = ["range=", "exclude="]
 
try:
    range = None
    exclude = None
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument

    for currentArgument, currentValue in arguments:

        if currentArgument in ("-r", "--range"):
            range = currentValue

        elif currentArgument in ("-e", "--exclude"):
            exclude = currentValue

    if range is None:
        print('\nPlease input range using --range argument\n')
        sys.exit()
    if exclude is None:
        print('\nPlease input exclude using --exclude argument\n')
        sys.exit()
    
    print(f"Range   => IPSet(['{range}'])")
    print(f"Exclude => IPSet(['{exclude}'])")
    
    ip = []
    for i in IPNetwork(range):
        ip.append(str(i))
    
    for i in IPNetwork(exclude):
        ip.remove(str(i))
    
    for i in ip:
        print(i)

    
          
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))