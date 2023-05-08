import os
file_dir = "./_posts/"
def modify(path,filename):
    data = "---\n"
    data += "title: " + os.path.splitext(filename)[0] +"\n"

    tmp = path 
    li = tmp.split("/")
    if (len(li) != 1 ):
        data += "categories:\n"
    for categories in li:
        if (categories != "." and categories != "_posts" ):
            data += "  - "+ categories+" \n" 
    
    data +="---\n\n"

    with open(path+"/"+filename, "rb+") as f:
        old  = f.read()
        f.seek(0)
        f.write(data.encode())
        f.write(old)

    print(path , "/", filename )

#print("begin")
for folder, subFolder, filenames in os.walk(file_dir):
    #print("floder:",folder)
    for filename in filenames:
        #print(filename)
        if os.path.splitext(filename)[1] == '.md':
            modify(folder,filename)
#print("end")
