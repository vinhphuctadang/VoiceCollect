from pip._internal import main as pmain
while 1:
    s = input (">>> Pass command to pip (type 'exit' to terminate): ");
    if s == 'exit':
        break;
    pmain (s.split ())

    