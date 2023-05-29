import os
import cv2
path = "Pic"
images = []
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame=cv2.imread(images[0])
height,width,fps=frame.shape
out=cv2.VideoWriter("Friends.mp4",cv2.VideoWriter_fourcc(*"DIVX"),5,(width,height))

for i in range(count-1,0,-1):
    f=cv2.imread(images[i])
    out.write(f)
    
out.release()



