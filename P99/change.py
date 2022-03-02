import os
import shutil
files = os.listdir('C:/Users/Minho/OneDrive/바탕 화면/python/P99/dummy')
for i in files:
    root, ext = os.path.splitext(
        'C:/Users/Minho/OneDrive/바탕 화면/python/P99/dummy/'+i)
    isexist = os.path.exists(
        'C:/Users/Minho/OneDrive/바탕 화면/python/P99/dummy/'+ext)
    if(isexist == True):
        shutil.move('C:/Users/Minho/OneDrive/바탕 화면/python/P99/dummy/'+i,
                    'C:/Users/Minho/OneDrive/바탕 화면/python/P99/dummy/'+ext)
    elif(isexist != True):
        os.mkdir('C:/Users/Minho/OneDrive/바탕 화면/python/P99/dummy/'+ext)
        shutil.move('C:/Users/Minho/OneDrive/바탕 화면/python/P99/dummy/'+i,
                    'C:/Users/Minho/OneDrive/바탕 화면/python/P99/dummy/'+ext)
