import os
import os.path
import stat
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from getpass import getpass as passw
import zipfile
import pwd
import smtplib
yvals=[]
zvals=[]
kvals=[]
aray=""
array=[]
k=[0]

f=open("input.txt","r")
f4=open("input2.txt","r")
if os.path.isfile("itws.txt")==False:
    f1=open("itws.txt","w")
if os.path.isfile("co.txt")==False:
    f2=open("co.txt","w")
os.chmod("itws.txt", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH|stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH|stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
os.chmod("co.txt", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH|stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH|stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

f1=open("itws.txt","w")
f2=open("co.txt","w")
#os.system("chmod 777 itws.txt")
aray=open("input.txt").read().split()
aray2=open("input2.txt").read().split()
f.close()

class Node:
    def __init__(self):
        self.rollno=None
        self.name=None
        self.mid1=None
        self.mid2=None
        self.end=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.cur_node = None
    def add_node(self,rollno,name,mid1,mid2,end):
        new_node = Node()
        for i in range(0,len(aray),5):
          new_node.rollno=rollno
          new_node.name=name
          new_node.mid1=mid1
          new_node.mid2=mid2
          new_node.end=end
        new_node.next=None
        
        new_node.next=self.cur_node
        self.cur_node=new_node
                
    def print_list(self,f,f1):
        Node = self.cur_node
        count=0
        while Node:
            if(Node.rollno==data):
                count=count+1
                f1.write("ROLLNO : ",)
                f1.write(str(Node.rollno))
                f1.write("\n")
                f1.write("NAME : ",)
                f1.write(str(Node.name))
                f1.write("\n")
                f1.write("MID1 MARKS : ",)
                f1.write(str( Node.mid1))
                f1.write("\n")
                f1.write("MID2 MARKS : ",)
                f1.write(str(Node.mid2))
                f1.write("\n")
                f1.write("ENDSEM MARKS : "+str(Node.end)+"\n")
                k=int(Node.mid1)*(0.25)
                q=int(Node.mid2)*(0.25)
                r=int(Node.end)*(0.50)
                l=k+q+r
                f1.write("Grade : ",)
                if(l>=90):
                    f1.write("A")
                elif(l<90 and l>=80):
                    f1.write("A-")
                elif(l>=70 and l<80):
                    f1.write("B")
                elif(l>=60 and l<70):
                    f1.write("B-")
                elif(l>=50 and l<60):
                    f1.write("C")
                elif(l>=40 and l<50):
                    f1.write("C-")
                elif(l>=30 and l<40):
                    f1.write("D")
                else:
                    f1.write("F")
                f1.write("\n")
                objects = ('mid1', 'mid2','end')
                y_pos = np.arange(len(objects))
                performance = [Node.mid1,Node.mid2,Node.end]
 
                plt.bar(y_pos, performance, align='center', alpha=0.25)
                plt.xticks(y_pos, objects)
                plt.ylabel('marks')
                plt.title('performance')
    
                plt.savefig("foo.pdf")        
    
            Node=Node.next
        if(count==0):
            print("your login id is invalid please check it once") 
    
    def print_list2(self,f,f1):
        Node = self.cur_node
        while Node:
             if(data=="itws"or data=="co"):
               # f1.write("ROLLNO : ",)
                f1.write("ROLLNO : "+str(Node.rollno)+"\n")
                #f1.write("\n")
                f1.write("NAME : ",)
                f1.write(str(Node.name))
                f1.write("\n")
                f1.write("MID1 MARKS : ",)
                f1.write(str( Node.mid1))
                f1.write("\n")
                f1.write("MID2 MARKS : ",)
                f1.write(str(Node.mid2))
                f1.write("\n")
                f1.write("END SEMMARKS : "+str(Node.end)+"\n")
                k=int(Node.mid1)*(0.25)
                q=int(Node.mid2)*(0.25)
                r=int(Node.end)*(0.50)
                l=k+q+r
                f1.write("Grade : ",)
                if(l>=90):
                   f1.write("A")
                elif(l<90 and l>=80):
                   f1.write("A-")
                elif(l>=70 and l<80):
                   f1.write("B")
                elif(l>=60 and l<70):
                   f1.write("B-")
                elif(l>=50 and l<60):
                   f1.write("C")
                elif(l>=40 and l<50):
                   f1.write("C-")
                elif(l>=30 and l<40):
                   f1.write("D")
                else:
                   f1.write("F")
                f1.write("\n")
                f1.write("\n")
                f1.write("\n")
                

               
             Node=Node.next
        if(data!="itws"and data!="co"):
             print "invalid login id" 
    
ll = LinkedList()
ll2=LinkedList()
def graph(aray):  
    import numpy as np
    import matplotlib.pyplot as plt    
    N = 6
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27      # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(0,len(aray),5):

        yvals.append(int(aray[2+i])) 
    rects1 = ax.bar(ind, yvals, width, color='r')
    #zvals = [aray[3],aray[8],aray[13],aray[18]]
    for i in range(0,len(aray),5):

        zvals.append(int(aray[3+i])) 
    rects2 = ax.bar(ind+width, zvals, width, color='g')
    #kvals = [aray[4],aray[9],aray[14],aray[19]]
    for i in range(0,len(aray),5):

        kvals.append(int(aray[4+i]))
    rects3 = ax.bar(ind+width*2, kvals, width, color='b')

    ax.set_ylabel('Scores')
    ax.set_xticks(ind+width)
    for i in range(0,len(aray),5):
         array.append(int(aray[i])%1000)
         #array.append(" ")
    ax.set_xticklabels( (array) )
    ax.legend( (rects1[0], rects2[0], rects3[0]), ('mid1', 'mid2', 'end') )

    def autolabel(rects):
        for rect in rects:
             h = rect.get_height()
             ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
             ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.savefig("foo.pdf")




print("please select ur option")
print("1.student")
print("2.faculty")
#data=raw_input()
#some_value =input()

# this while loop block simulates a case block
for i in range(0,len(aray),5):
    ll.add_node(aray[0+i],aray[1+i],aray[2+i],aray[3+i],aray[4+i])
for i in range(0,len(aray),5):
    ll2.add_node(aray2[0+i],aray2[1+i],aray2[2+i],aray2[3+i],aray2[4+i])

#ll.print_list()

# case

some_value=input()   
while True:

    # case 1
    if some_value==1:
        print("enter subject to know ur marks")
       
        print("1.itws")
        print("2.co")
        data3=input()
        print("enter your login id")
        data=raw_input()
        if(data3==1):
            ll.print_list(f,f1)
            #zipitws()
            os.chmod("itws.txt", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        else:
            ll2.print_list(f4,f2)
            #zipco()
            
        #data2=passw()
        #os.system("chmod 111 itws.txt")
        
        os.chmod("co.txt", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
       
        os.chmod("itws.txt", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        break

    # case 2
    else:
        print("enter subject to know ur marks")
        
        print("1.itws")
        print("2.co")
        data3=input()
        print("enter your login id")
        data=raw_input()
        
        if(data3==1):
            ll.print_list2(f,f1)
            #zipitws()
            graph(aray)
            '''z = zipfile.ZipFile("itws.zip", "w")

            z.write("foo.pdf")
            z.write("itws.txt")'''
        else:
            ll2.print_list2(f4,f2)
            #zipco()
            graph(aray2)
            '''z = zipfile.ZipFile("co.zip", "w")

            z.write("foo.pdf")
            z.write("co.txt")'''
        
      
        
        data2=passw()
        os.system("chmod 777 itws.txt")
        os.system("chmod 777 co.txt")
                
        break

f1.close()
f2.close()

if(data3==1):
    z = zipfile.ZipFile("itws.zip", "w")

    z.write("foo.pdf")
    z.write("itws.txt")
else:
    z = zipfile.ZipFile("co.zip", "w")


    z.write("foo.pdf")
    z.write("co.txt")


