word = "Little"
with open("file.txt","r") as f :
    content=f.read()

new_content=content.replace(word,"#"*len(word))

with open("file.txt","w") as f :
    f.write(new_content)
    


