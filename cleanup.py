import os
path = "./"
for filename in os.listdir(path):
    f = os.path.join(path,filename)
    if os.path.isfile(f):
        if (f[len(f)-8:len(f)] != "Trim.mp4" and filename != "cleanup.py"):
            os.remove(f)
