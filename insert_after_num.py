class student:
    def __init__(self,r,n):
        self.roll=r
        self.name=n
        self.nextstud=None
    def printinfo(self):
        print(self.roll,":",self.name)
        if self.nextstud is not None:
            print("next student:",self.nextstud.name)
        else:
            print("next student not set")
class singlist:
    def __init__(self):
        self.start=None
        self.last=None
    def insertnode(self,newstud):
        if(self.start==None):
            self.start=newstud
            self.last=newstud
        else:
            self.last.nextstud=newstud
            self.last=newstud
    def printlist(self):
        ptr=self.start
        while (ptr!=None):

            ptr.printinfo()
            ptr=ptr.nextstud
    def insertafter(self,new,pos):
        ptr=self.start
        while(ptr!=None):
            ptr.printinfo()
            if(ptr.roll==pos):
                new.nextstud=ptr.nextstud
                ptr.nextstud=new
                #ptr.printinfo()
            ptr=ptr.nextstud
alist=singlist()
for i in range(1,5):
    r=int(input("enter rollno."))
    n=input("enter your name:")
    nstud=student(r,n)
    alist.insertnode(nstud)
print("the linklist=")
alist.printlist()
'''\\'''
r=int(input("enter rollno."))
n=input("enter your name:") 
newstud=student(r,n)
pos=int(input("enter after what"))
alist.insertafter(newstud,pos)
