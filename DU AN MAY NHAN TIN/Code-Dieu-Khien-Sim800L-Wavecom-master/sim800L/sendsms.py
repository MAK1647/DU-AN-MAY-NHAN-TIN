import serial
import sys
import time


def hello(a,b,c):
    k=1
    try:
    #print "hello and that's your sum:", a + b
        ser = serial.Serial(
                    #port = '/dev/ttyAMA0',
                    port = a,
                    baudrate = 9600,
                    
                    timeout = 2
            )
        #if ser.isOpen():
         #print(ser.name + ' is open...!!!')

        ser.write('AT'+'\r')
        #print ser.read(32)
        time.sleep(0.5)

        ser.write('AT+CMGF=1'+'\r')
        #print ser.read(32)
        time.sleep(0.5)

        ser.write(b'AT+CMGS="' + b.encode() + b'"\r')
        #print ser.read(32)
        time.sleep(0.5)

        ser.write(c.encode('UTF-8') + b"\r")
        time.sleep(0.5)

        ser.write(chr(26))
        #print ser.read(32)
        time.sleep(0.5)
    except Exception as e:
        k=0
    if(k==1):
        strr = "OK:"
        return strr
    else:
        strr1 = "ERROR:101" 
        return strr1
        
    

    #command = b #":01050004FF00F7\r\n"
    #command1 = 'AT+CMGS='+b+'\r'
    #print(command1)
    #ser.write(command1)
    #time.sleep(3)
    #s = ser.read(ser.inWaiting())
    #print(s)
    #command2 = "AT+CMGF=1\r"
    #ser.write(command2)
    #s2 = ser.read(ser.inWaiting())
    #print(s2)
    #command3 = 'AT+CMGS='+b+'\r\n'
    #print(command3)
    
    #ser.write(command3)
    #time.sleep(3)
    #ser.write(c + '\r\n')
    #time.sleep(3)
    #ser.write(chr(26))
    #time.sleep(3)
    #s3 = ser.read(ser.inWaiting())
    #print(s3)
    #ser.write('AT+CMGDA="DEL ALL"\r') # delete all
    #time.sleep(3)
    #ser.read(ser.inWaiting()) # Clear buf 
    #print(c)

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    
    kq=hello(a, b,c)
    print(kq)
    #return kq
