import serial
import sys
import time

def hello(a,b,c):
    #print "hello and that's your sum:", a + b
    ser = serial.Serial(
                #port = '/dev/ttyAMA0',
                port = a,
                baudrate = 9600,
                
                timeout = 5
        )
    if ser.isOpen():
     print(ser.name + ' is open...!!!')

    ser.write('AT'+'\r')
    print ser.read(32)
    time.sleep(2)

    ser.write('AT+CMGF=1'+'\r')
    print ser.read(32)
    time.sleep(2)

    ser.write(b'AT+CMGS="' + b.encode() + b'"\r')
    #print ser.read(32)
    time.sleep(2)

    ser.write(c.encode() + b"\r")
    time.sleep(2)

    ser.write(chr(26))
    print ser.read(32)
    time.sleep(2)
    

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

def incall(a,b):
    k=1
    try:
        
        ser = serial.Serial(
                    #port = '/dev/ttyAMA0',
                    port = a,
                    baudrate = 9600,
                    
                    timeout = 5
            )
        ser.write(b'ATD' + b.encode() + b';\r')
        #ser.print (b);
        #ser.print(F(";\r\n"))
    except Exception as e:
        k=0
        #err=e
    if(k==1):
        strr = "OK:"
        return strr
    else:
        strr1 = "ERROR:102"
        return strr1


        

if __name__ == "__main__":
    a = sys.argv[1]#com
    b = sys.argv[2]#number
    #c = sys.argv[3]
    
    kq=incall(a, b)
    print(kq)
