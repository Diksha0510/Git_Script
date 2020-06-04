import os
def create():
    # os.system('git checkout practice-1')
    os.system('git init')
    #  os.system('git clone \"https://github.com/Diksha0510/Git_Script.git\"')
  # file=input("Enter the file name")
    os.system('git add .')
    os.system('git commit -m \"Initial commit\"')
    os.system('git remote add origin https://github.com/Diksha0510/Git_Script.git')
    os.system('git checkout -b practice-1')
    os.system('git pull origin practice-1 allow-unrelated-histories')
    os.system('git push --set-upstream origin practice-1')
create()
