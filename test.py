import sys, os


def Print(value):
    print(f"{__file__} --- {value}")


#prints the stuff
Print(f"{sys.argv[1]} if you read this the file has run")
    