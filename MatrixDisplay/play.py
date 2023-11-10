import serial,time
if __name__ == '__main__':
    data = open("data.csv","r")
    
    with serial.Serial("COM6", 138000 , timeout=1) as arduino:
        lines = data.read().splitlines()
        for line in lines:
            line = line.split(',')
            time.sleep(float(line[0])/1.5)
            for pixel_change in line[1:len(line)]:
                arduino.write(int(pixel_change).to_bytes())
