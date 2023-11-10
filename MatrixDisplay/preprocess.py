from PIL import Image
import sys

def coords_to_num(x,y):
    pixel = y * 12
    if (y % 2 == 0):
        pixel += x
    else:
        pixel += 11 - x
    return pixel

current_image_state={}

with open("data.csv",'w') as data:
    last_painted_frame = 0
    i=1
    while(i<6362):
        try:
            img = Image.open(sys.argv[1] + r"\out"+str(i)+'.png')
            pixels_to_update = []
            for y in range(0,12):
                for x in range(0,12):
                    color = img.getpixel((x,y))
                    color2 = []
                    for c in color:
                        if c>254:
                            c=254
                        color2.append(c)
                    color=color2
                    if current_image_state.get((x,y)) != color:
                        current_image_state[(x,y)]=color
                        pixels_to_update.append((x,y,color))
            if(len(pixels_to_update)!=0):         
                delay = (i-last_painted_frame)*0.03333333333
                data.write(str(delay)+",")
                last_painted_frame=i

                for pixel in pixels_to_update:
                    data.write(str(coords_to_num(pixel[0],pixel[1]))+",")
                    for color in pixel[2]:
                        data.write(str(color)+",")
                data.write("255\n")            

        except NotImplementedError:
            print("Ignoring frame "+ str(i))    
        i+=1    

        