import sys

#Check Python path, and count them
print('path has', len(sys.path), 'members')
print('The members are:')
for member in sys.path:
    print(member)

#Print all imported modules:
print(sys.modules.keys())

#Print the platform type (linux, win32, mac, etc)
print(sys.platform)

#Check application name, and list number of passed arguments
print('The application name is:', sys.argv[0])
if len(sys.argv) > 1:
    print('You passed', len(sys.argv)-1, 'arguments. They are:')
    for arg in sys.argv[1:]:
        print(arg)
else:
    print('No arguments passed!')

#Check the Python working version
sys.version