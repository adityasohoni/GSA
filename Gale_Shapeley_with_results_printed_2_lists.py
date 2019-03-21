class student:
    def __init__(self, rno, name ,main_rank, adv_rank, cat,pref):
#preferences is a list of numbers corresponding to a course
#in cat 0-General, 1-OBC, 2-SC, 3- ST 
        self.rno=rno
        self.name=name
        self.main_rank=main_rank
        self.adv_rank=adv_rank
        self.cat=cat
       
        self.pref=pref
        self.tba=0
        
class batch:
    def __init__(self, vac_seats, ids):
        self.vac_seats=vac_seats
        self.ids=ids
    
    


        
    
#add student details to this list
stl=[]
#To Add A Student do-



#FIRST DIGIT
#IIT Bombay is 0
#IIT Delhi is 1
#IIT Madras is 2
#IIT Kanpur is 3
#IIT Kharagpur is 4
#NIT Trichy is 5
#NIT Warnagal is 6
#NITK Surathkal is 7

#SECOND DIGIT
#Computer Science Engineering is 0
#Electrical Engineering is 1
#Mechanical Engineering is 2
#Civil Engineering is 3
#Chemical Engineering is 4
#Aerospace Engineering is 5
#Engineering Physics is 6
#Metallurgical Engineering and Materials Science is 7

#For eg a preference10 can be [2,3] i.e., IIT Madras Civil
for x in range(0, 1000):
    stl.append(student(x,"XYZ",x+1,x%4,(x+1)%4,[[0,0],[1,0],[2,0],[3,0],[4,0],[0,1],[-1,-1]]))
#[-1,-1] signifies "NO ALLOTMENT" and should always be added at the end

seats = [[batch([50,26,16,8],[[],[],[],[]]) for j in range(11)] for i in range(11)]    

#nit_seats = [[nit_batch([25,13,8,4,25,13,8,4],[[],[],[],[],[],[],[],[]]) for j in range(11)] for i in range(11)]

def allot(i):
    if stl[i].pref[stl[i].tba][0]==-1:
        return
#trying to get in thru general
    if not seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[1].tba][2]].ids[0]:
        seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0].append(i)
    else :
        j=0
        flag=0
        for x in seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0] :
            if stl[x].main_rank>stl[i].main_rank:
                seats[stl[i].pref[stl[i].tba][1]][stl[i].pref[stl[i].tba][2]].ids[0].insert(j, i)
                flag=1
                break
            j+=1
        if flag==0:
            seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0].append(i)
    seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[0]-=1
                
    if seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[0]==-1:
        seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[0]=0
        ko=seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0][-1]
        if stl[ko].cat==0:
            tba+=1
        if ko!=i:
            allot(ko)
#trying to get thru category
    if stl[i].cat!=0:
        if not seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat]:
            seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat].append(i)
        else :
            j=0
            flag=0
            for x in seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat]:
                if stl[x].main_rank>stl[i].main_rank:
                    seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat].insert(j, i)
                    flag=1
                    break
                j+=1
            if flag==0:
                seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat].append(i)
        seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[stl[i].cat]-=1
                
        if seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[stl[i].cat]==-1:
            seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[stl[i].cat]=0
            ko=seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat][-1]
                
            tba+=1
            allot(ko)
            
        
l=len(stl)
for i in range(l):
    allot(i)
    
for i in range(l):
    print(stl[i].pref[stl[i].tba])
    
        
        
        
        
        
            
                
            
    
        
                
            
    
    
  



 
    
    





        
            
            
            
            
                
                
                
        
    
    
  

    
    




    
    

        