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
    
#this is the main function where this script begins to execute
if __name__ == "__main__":
    dic={};
    count = readSoduku("completesudo.txt");
    print count;
    blknum = int(math.sqrt(count));
    blkdim = int(math.sqrt(blknum));
    setRowCol();
    setBlk();
    controlist = list(range(1,blknum+1));
    print "Sudoku:";
    printSudoku(dic);
    if test(dic)!=0:
        print "It has conflicts of {}. It's not complete ".format(test(dic));
    else:
        print "It's a complete Sudoku with {} conflicts.".format(test(dic));
    