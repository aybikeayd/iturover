#!/usr/bin/env python

import rospy
from std_msgs.msg import String


class CallBack():
    def __init__(self):  
        rospy.init_node('subs', anonymous=True)
        self.pub_16 = rospy.Publisher('/position/drive', String, queue_size = 10)
        self.pub_24 = rospy.Publisher('/position/robotic_arm', String, queue_size = 10)
        rospy.Subscriber('/serial/drive', String, self.callback1)
        rospy.Subscriber('/serial/robotic_arm', String, self.callback1)
        self.dongu()

    def callback1(self,data):
        n_data=data.data
        s_data=n_data[1:-1] #harflerin cikarilmasi
        bos=[]
        bos.append([s_data[i:i+4] for i in range (0,len(s_data),4)]) #sayi verilerinin dort basamaktan olusan parcalara bolunmesi ve bos listeye atanmasi
        self.listtostr = " ".join(map(str,bos))  

        while len(self.listtostr) < 33: #veriler 18 basamak ise kullanilacak dongu
            a = int(self.listtostr[2:6]) #ilk dort basamak
            if a > 1255:
                a = 1255
            elif a > 255 and a < 1000:
                a=255
            else:
                a=a
            if a < 10:
                a="000" + str(a)
            elif a < 100:
                a = "00" + str(a)
            elif a < 1000:
                a = "0" +str(a)

            b = int(self.listtostr[10:14]) #ikinci dort basamak
            if b > 1255:
                b = 1255
            elif b > 255 and b < 1000:
                b=255
            else:
                b=b
            if b < 10:
                b= "000" + str(b)
            elif b < 100:
                b = "00" + str(b)
            elif b < 1000:
                b = "0" + str(b)

            c = int(self.listtostr[18:22]) #ucuncu dort basamak
            if c > 1255:
                c = 1255
            elif c > 255 and c < 1000:
                c=255
            else:
                c=c
            if c < 10:
                c = "000" + str(c)
            elif c < 100:
                c = "00" + str(c)
            elif c < 1000:
                c = "0" +str(c)

            d = int(self.listtostr[26:30]) #dorduncu dort basamak
            if d > 1255:
                d = 1255
            elif d > 255 and d < 1000:
                d=255
            else:
                d=d
            if d < 10:
                d = "000" + str(d)
            elif d < 100:
                d = "00" + str(d)
            elif d < 1000:
                d = "0" + str(d)
            son_16 = "A" + str(a) + str(b) + str(c) + str(d) + "B"

            rospy.loginfo(son_16)

            return self.pub_16.publish(son_16)


        while len(self.listtostr) > 33: #veriler 26 karaker ise kullanilacak dongu

            a = int(self.listtostr[2:6])#ilk dort basamak
            if a > 1255:
                a = 1255
            elif a > 255 and a < 1000:
                a=255
            else:
                a=a
            if a < 10:
                a="000" + str(a)
            elif a < 100:
                a = "00" + str(a)
            elif a < 1000:
                a = "0" +str(a)

            b = int(self.listtostr[10:14]) #ikinci dort basamak
            if b > 1255:
                b = 1255
            elif b > 255 and b < 1000:
                b=255
            else:
                b=b
            if b < 10:
                b= "000" + str(b)
            elif b < 100:
                b = "00" + str(b)
            elif b < 1000:
                b = "0" + str(b)

            c = int(self.listtostr[18:22]) #ucuncu dort basamak
            if c > 1255:
                c = 1255
            elif c > 255 and c < 1000:
                c=255
            else:
                c=c
            if c < 10:
                c = "000" + str(c)
            elif c < 100:
                c = "00" + str(c)
            elif c < 1000:
                c = "0" +str(c)

            d = int(self.listtostr[26:30]) #dorduncu dort basamak
            if d > 1255:
                d = 1255
            elif d > 255 and d < 1000:
                d=255
            else:
                d=d
            if d < 10:
                d = "000" + str(d)
            elif d < 100:
                d = "00" + str(d)
            elif d < 1000:
                d = "0" + str(d)

            e = int(self.listtostr[34:38]) #besinci dort basamak
            if e > 1255:
                e = 1255
            elif e > 255 and e < 1000:
                e=255
            else:
                e=e
            if e < 10:
                e = "000" + str(e)
            elif e < 100:
                e = "00" + str(e)
            elif e < 1000:
                e = "0" + str(e)

            f = int(self.listtostr[42:46]) #altinci dort basamak
            if f > 1255:
                f = 1255
            elif f > 255 and f < 1000:
                f=255
            else:
                f=f
            if f < 10:
                f = "000" + str(f)
            elif f < 100:
                f = "00" + str(f)
            elif f < 1000:
                f = "0" +str(f)


            son_24 = "A" + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + "B"

            rospy.loginfo(son_24)

            return self.pub_24.publish(son_24)


    def dongu(self):
        while not rospy.is_shutdown():
            rospy.spin()


if __name__ == '__main__':
    CallBack()
