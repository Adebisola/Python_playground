#!/usr/bin/python3
try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong when writing the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


