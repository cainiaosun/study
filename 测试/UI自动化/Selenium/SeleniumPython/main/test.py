import sys
def add_path(paths):
    for path in sys.path:
        if path.count('site-packages') and path.count('Users')==0:
            mypath=path+'/mypath.pth'
            with open(mypath,'a',encoding='utf-8') as fp:
                pass