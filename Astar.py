import math
import random
import copy
class Element:
    def __init__(self, value, status):
        self.value = value;
        self.status = status;
        self.row = 0;
        self.col = 0;
        self.blk = 0;
    
def printSudoku(dictsudo):
    for con in range(1,len(dictsudo)+1):
        print getattr(dictsudo[con],"value"),;
        if con % blknum ==0:
            print "\n"    
                
def getRow(dictionary,rowDes):
        i=0;
        tempdict={};
        for con in range(1,count+1):
            elm = dictionary[con];
            if getattr(elm,"row")==rowDes:
                i+=1;
                tempdict[i]=elm;
                #print getattr(elm,"value"); 
        return tempdict;   

def getCol(dictionary,colDes):
    i=0;
    tempdict={};
    for con in range(1,count+1):
        elm = dictionary[con];
        if getattr(elm,"col")==colDes:
            i+=1;
            tempdict[i]=elm;
            #print getattr(elm,"value");
    return tempdict; 

def setRowCol():
    con=0;
    for row in range(1,blknum+1):
            for col in range(1,blknum+1):
                con+=1;
                setattr(dic[con],"row",row);
                setattr(dic[con],"col",col);
                
                if con>count:
                    break;
                

def getBlk(dictionary, blkDes):
    i=0;
    tempdict={};
    for con in range(1,count+1):
        elm = dictionary[con];
        if getattr(elm,"blk")==blkDes:
            i+=1;
            tempdict[i]=elm;
            #print getattr(elm, "value");
    return tempdict;
        

def setBlk():
    for con in range(1,count+1):
        #elm = dic[con];
        row = getattr(dic[con],"row");
        col = getattr(dic[con],"col");
        for j in range(0,blkdim):
            if row>j*blkdim and row<=(j+1)*blkdim:
                for i in range(0,blkdim):
                    if col>i*blkdim and col<=(i+1)*blkdim:
                        setattr(dic[con], "blk",j*blkdim+i+1);
                        
                

def grouptest(testdict):
    confl=0;
    for con in range(1,blknum):
        for el in range(con+1,blknum+1):
            elm1 = testdict[con];
            elm2 = testdict[el];
            if getattr(elm1,"value")==getattr(elm2,"value"):
                confl+=1;
     
    return confl;
        
def test(testdic):
    conflict = 0;
    for testgroupnum in range(1,blknum+1):
        conflict += grouptest(getRow(testdic,testgroupnum));
        conflict += grouptest(getCol(testdic,testgroupnum));
        conflict += grouptest(getBlk(testdic,testgroupnum));
    return conflict;
    

def readSoduku(filename):
    f = open(filename,"r");
    
    count=0;
    ctn=0;
    ctn1=0;
    #row=0;
    alllines = f.readlines();
    for line in alllines:
        #row+=1;
        #col=0;
        for varnum in range(0,len(line)-1):
            if ctn==1 and ctn1==1:
                ctn=0;
                ctn1=0;
                continue;
            ctn=0;
            ctn1=0;
            tempvar = line[varnum];
            if line[varnum+1]!="," and line[varnum+1]!=" " and line[varnum+1]!="\n":
                tempvar+=line[varnum+1];
                ctn=1;
            if tempvar[0]!=" " and tempvar[0]!="\n" and tempvar[0]!=",":
                ctn1=1;
                #col +=1;
                count+=1;
                if tempvar != "?":
                    tempvar = int(tempvar);
                    sta = 0;
                else:
                    sta = 1;
                elm = Element(tempvar,sta);
                dic[count] = elm;
    return count;    
    f.close();
    
def setctrlist(row):
    ctrlist = list(controlist);
    
    tempdict = getRow(dic,row);
    for con in range(1,len(tempdict)+1):
        if getattr(tempdict[con],"status")==0:
            
            ctrlist.remove(getattr(tempdict[con],"value"));
    return ctrlist
    
def assign():
    a=[];
    i=0;
    
    for con in range(1,count+1):
        if con % blknum ==1:
                i+=1;
                ctrlist = setctrlist(i);
               
        if getattr(dic[con],"status")==1:
            
            cho = random.choice(ctrlist);
            ctrlist.remove(cho);
            setattr(dic[con],"value", cho);
            
            a.append(con);
            #i+=1;
    return a;
            
def newmove(movedict):
    while True:
        indexrow = random.randrange(1,blknum+1);
        temprow = getRow(movedict,indexrow);
        i=0;
        for con in range(1,blknum+1):
            if getattr(temprow[con],"status")==1:
                i+=1;
        if i>1:
            break;
    movedict = swapwithinrow(indexrow,movedict);
    
    
    return movedict;
        
    
def swapwithinrow(row,mvdict):
    tempdic = getRow(mvdict,row);
    while True:
        index1 = random.randrange(1,blknum+1);
        if getattr(tempdic[index1],"status")==1:
            break;
    while True:
        index2 = random.randrange(1,blknum+1);
        if getattr(tempdic[index2],"status")==1 and index2 != index1:
            break;
    swapvalue = getattr(tempdic[index1],"value");
    setattr(tempdic[index1],"value", getattr(tempdic[index2],"value"));
    setattr(tempdic[index2],"value", swapvalue); 
    mvdict = setRowValue(row,tempdic,mvdict);
    return mvdict;

def setRowValue(row,newrow,newdict):  
    i=1;
    for con in range(1,count+1):
        if getattr(newdict[con],"row")==row:
            newdict[con] = newrow[getattr(newdict[con],"col")];   
            i+=1;     
    return newdict;   
     
def getallsudo(sudo,g):
    allsudo = [];
    allconflict = [];
    tempsudo=copy.deepcopy(sudo);
    for i in range(0,blknum):
        for x in range(i*blknum+1,(i+1)*blknum+1):
            for y in range(i*blknum+1, (i+1)*blknum+1):
                if x!=y and getattr(tempsudo[x],"status")==1 and getattr(tempsudo[y],"status")==1:
                    swapvalue = getattr(tempsudo[x],"value");
                    setattr(tempsudo[x],"value", getattr(tempsudo[y],"value"));
                    setattr(tempsudo[y],"value", swapvalue);
                    h = test(tempsudo);
                    f = h+g;
                    if len(allconflict)>0:
                        for j in range(0,len(allconflict)):
                            if f<allconflict[j]:
                                allconflict.insert(j,f)
                                allsudo.insert(j,tempsudo);
                                tempsudo = copy.deepcopy(sudo);
                                break;
                        else:
                            allconflict.append(f);
                            allsudo.append(tempsudo);
                            tempsudo = copy.deepcopy(sudo);
                    else:
                        allconflict.append(f);
                        allsudo.append(tempsudo);
                        tempsudo = copy.deepcopy(sudo);
    print len(allsudo), len(allconflict), allconflict[0],allconflict[len(allconflict)-1];
    return allsudo;                   
                    
    
     
def solve():
    start=1;
    
    while start==1:
        start=0;
        assign();
        print test(dic);
        g=0;
        tes=0;
        bestsudo = copy.deepcopy(dic);
        while test(bestsudo)>0:
            g+=1;
            print g;
            cot = test(bestsudo);
            sudo = copy.deepcopy(bestsudo);
            allsudo = getallsudo(sudo,g);
            print "tes:", test(bestsudo), test(allsudo[0]), test(allsudo[1]);
            
            bestsudo = copy.deepcopy(allsudo[0]);
            print "conflict: ", test(bestsudo);
            if cot==test(bestsudo):
                tes+=1;
            if tes==20 or g==80:
                start=1;
                break;
            
    return bestsudo;
        
    
#this is the main function where this script begins to execute
if __name__ == "__main__":
    dic={};
    count = readSoduku("sudoku1.txt");
    print count;
    blknum = int(math.sqrt(count));
    blkdim = int(math.sqrt(blknum));
    setRowCol();
    setBlk();
    controlist = list(range(1,blknum+1));
    print test(dic);
    result = solve();
    print test(result);
    print "Sudoku:";
    printSudoku(result);
    
    
    #print conflict;
    