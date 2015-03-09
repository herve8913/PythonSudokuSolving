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

def setpeers(sudo1,item,v):
    
    row = getattr(item,"row");
    col = getattr(item,"col");
    blk = getattr(item,"blk");
    print row, col, blk;
    
    
    for con in range(1,count+1):
        
        dom = getattr(sudo1[con],"domain");
        if getattr(sudo1[con],"row")==row and getattr(sudo1[con],"col")!=col:
            
            try:
                dom.remove(v);
                setattr(sudo1[con],"domain",list(dom));
            except:
                print "~~";
        elif getattr(sudo1[con],"col")==col and getattr(sudo1[con],"row")!=row:
            
            try:
                dom.remove(v);
                setattr(sudo1[con],"domain",list(dom));
            except:
                print "~~";
        elif getattr(sudo1[con],"blk")==blk and getattr(sudo1[con],"col")!=col:
        
            try:
                dom.remove(v);
                setattr(sudo1[con],"domain",list(dom));
            except:
                print "~~";
        if len(dom)<0:
            print "dom<0"
            return {};
    return sudo1;
                
    
def getdomain(sudo2,newitem):
    domainlist=[0]*len(getattr(newitem,"domain"));
    
    do1 = getattr(newitem,"domain");
    peerlist = getpeers(sudo2,newitem);
    for domnum in range(0,len(domainlist)):
        for peer in peerlist:
            do2 = getattr(peer,"domain");
            for vl in do2:
                if vl==do1[domnum]:
                    domainlist[domnum]+=1;
                    break;
                    
    domain1 = [];
    for cont in range(0,len(domainlist)):
        tempcon=0;
        mindomain = domainlist[0];
        for con in range(0,len(domainlist)):
            if domainlist[con]< mindomain:
                mindomain = domainlist[con];
                tempcon = con;
        domain1.append(do1[tempcon]);
        domainlist[tempcon]=100000;
    return domain1;
    
                    
    
def getpeers(sudo3,item3):
    peers=[];
    row = getattr(item3,"row");
    col = getattr(item3,"col");
    blk = getattr(item3,"blk");
    for con in range(1,count+1):
        if getattr(sudo3[con],"row")==row:
            peers.append(sudo3[con]);
        elif getattr(sudo3[con],"col")==col:
            peers.append(sudo3[con]);
        elif getattr(sudo3[con],"blk")==blk:
            peers.append(sudo3[con]);
        if getattr(sudo3[con],"row")==row and getattr(sudo3[con],"col")==col:
            peers.remove(sudo3[con]);
    return peers;
    
    
                    
def Assignnew(newsudoku,item,v):    
    
    newsudoku = setpeers(newsudoku,item,v);
    
    if newsudoku=={}:
        return {};
    for con in range(1,count+1):
        if getattr(newsudoku[con],"row")==getattr(item,"row") and getattr(newsudoku[con],"col")==getattr(item,"col"):
            indexcon = con;
            break;
    
    setattr(newsudoku[indexcon],"value",v);
    print "value: ", newsudoku[indexcon].value;
    printSudoku(newsudoku);
    
    return newsudoku;
       
def getunsigned(newsudoku1):
    length = blknum+1;
    for con in range(1,count+1):
        if getattr(newsudoku1[con],"status")==1:
            if getattr(newsudoku1[con],"value")=="?":
                if len(getattr(newsudoku1[con],"domain"))<length:
                    length = len(getattr(newsudoku1[con],"domain"));
                    item = newsudoku1[con];
    return item;

def getmaxdegree(sodu3):
    deg=-1;
    for con in range(1,count+1):
        if getattr(sodu3[con],"status")==1:
            if getattr(sodu3[con],"value")=="?":
                cnt=0;
                for peer in getpeers(sodu3,sodu3[con]):
                    if getattr(peer,"value")=="?":
                        cnt+=1;
                if cnt>deg:
                    deg = cnt;
                    item = sodu3[con];
    return item;
                        
      
def CSPbacktracing(sudoku):
 
    if sudoku=={}:
        return {};
    
    checking = 1;
    for con in range(1,count+1):
        if getattr(sudoku[con],"value")=="?":
            checking=0;
    
    if test(sudoku)==0 and checking==1:
        printSudoku(sudoku);
        return sudoku;
    #get a proper unsigned item : getunsigned() or getmaxdegree()
    item = getunsigned(sudoku);
    #select a proper order for list of domain.
    domainnew = getdomain(sudoku,item);
    print domainnew;
    print sudoku[6].value;
    
    for v in domainnew:
        newsudo = copy.deepcopy(sudoku);
        rs = CSPbacktracing(Assignnew(newsudo,item, v));
        if rs!= {}:
            return rs;
        
    return {};
        
def initdomain():
    domain = range(1,blknum+1);
    for con in range(1,count+1):
        setattr(dic[con],"domain",list(domain));
        if getattr(dic[con],"value")!="?":
            dom = getattr(dic[con],"domain");
            dom.remove(getattr(dic[con],"value"));
            setattr(dic[con],"domain",list(dom));
        else:
            row = getattr(dic[con],"row");
            col = getattr(dic[con],"col");
            blk = getattr(dic[con],"blk");
            dom = getattr(dic[con],"domain");
            for con2 in range(1,count+1):
                
                if getattr(dic[con2],"row")==row and getattr(dic[con2],"col")!=col:
                    if getattr(dic[con2],"status")==0:
                        try:
                            dom.remove(getattr(dic[con2],"value"));
                            setattr(dic[con],"domain",list(dom));
                        except:
                            print "~~";
                elif getattr(dic[con2],"col")==col and getattr(dic[con2],"row")!=row:
                    if getattr(dic[con2],"status")==0:
                        try:
                            dom.remove(getattr(dic[con2],"value"));
                            setattr(dic[con],"domain",list(dom));
                        except:
                            print "~~";
                elif getattr(dic[con2],"blk")==blk and getattr(dic[con2],"col")!=col:
                    if getattr(dic[con2],"status")==0:
                        try:
                            dom.remove(getattr(dic[con2],"value"));
                            setattr(dic[con],"domain",list(dom));
                        except:
                            print "~~";
    

def solve():
    
    initdomain();
    sudopassing = copy.deepcopy(dic);
    result1 = CSPbacktracing(sudopassing);
    return result1;
    
        
    
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
    