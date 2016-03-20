import subprocess

# Default path is trunk path
def getUpdate(patchLink):
    try:
        patchLink
    except NameError:
        print "The patchLink is not defined"
        usage()
        exit()
    else:
        downloadPatch(patchLink)

def usage():
    print "Usage :upgrade.py  <path to the link>"

def downloadPatch(link):
    try:
        subprocess.check_call(["curl","-O",link])
    except subprocess.CalledProcessError as e:
        print "Failed to download the patch\n"
        print e.returncode
        
    
        

# Get the version of the upgrade to 

# Validate the upgrade path validity

# Apply the upgrade 


