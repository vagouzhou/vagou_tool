#!/usr/bin/python
import sys,os

def get_module_root():
    if(len(sys.argv)>1):
        return sys.argv[1]
    else:
        return os.getcwd()
    
def executeCmd(args):
    cmd_line="".join(args)
    print(cmd_line)
    os.system(cmd_line)

module_root_dir = get_module_root()
os.chdir(module_root_dir)
print("current module root dir=" + module_root_dir)

#update latest both git and svn
executeCmd("git pull origin master")
executeCmd("git svn rebase")


#get need commit count of git to svn 
commits_count = 0
if(len(sys.argv)>2):
    commits_count = int(sys.argv[2])
else:
    #get commit count from git status
    #git log --branches --not --remotes --simplify-by-decoration --decorate --oneline
    output = os.popen('git log --branches --not --remotes --simplify-by-decoration --decorate --oneline','r',-1);
    commits_count = sum(1 for _ in output) #len(output.readlines())
    
print("need to commit count = " + str(commits_count))


#commit code into svn 
for i in range(commits_count):
    executeCmd("git svn dcommit")
    executeCmd("git svn rebase")

#sync back to git
if(commits_count>0):
    executeCmd("git push origin master -f")
else:
    executeCmd("git push origin master")

