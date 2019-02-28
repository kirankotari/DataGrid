# Import Statements
import sys
from math import ceil
from errno import ENOENT, EACCES, EPERM
 
# Class Files
# BinarySearch Class # return True if exist else False
class BinarySearch(object):
    def __init__(self):
        pass
    def binary_search(self,lst,key):
        low = 0
        high = len(lst)-1
        while low <= high :
            mid = int((low+high)/2)
            if lst[mid]==key:
                return True
            elif lst[mid] < key:
                low = mid+1
            else:
                high = mid-1
        return False
         
# Stopwords Class # elimanating stop words from given files
class StopWords(object):
    # stop words in a list
    stopwords = [["a","a\'s","able","about","above","according","accordingly","across","actually","after","afterwards","again","against","ain\'t","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren\'t","around","as","aside","ask","asking","associated","at","available","away","awfully"],
        ["b","be","became","because","become","becomes","becoming","been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by"],
        ["c","c\'mon","c\'s","came","can","can\'t","cannot","cant","cause","causes","certain","certainly","changes","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn\'t","course","currently"],
        ["d","definitely","described","despite","did","didn\'t","different","do","does","doesn\'t","doing","don\'t","done","down","downwards","during"],
        ["e","each","edu","eg","eight","either","else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except"],
        ["f","far","few","fifth","first","five","followed","following","follows","for","former","formerly","forth","four","from","further","furthermore"],
        ["g","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings"],
        ["h","had","hadn\'t","happens","hardly","has","hasn\'t","have","haven\'t","having","he","he\'s","hello","help","hence","her","here","here\'s","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit","however"],
        ["i","i\'d","i\'ll","i\'m","i\'ve","ie","if","ignored","immediate","in","inasmuch","inc","indeed","indicate","indicated","indicates","inner","insofar","instead","into","inward","is","isn\'t","it","it\'d","it\'ll","it\'s","its","itself"],
        ["j","just"],
        ["k","keep","keeps","kept","know","known","knows"],
        ["l","last","lately","later","latter","latterly","least","less","lest","let","let\'s","like","liked","likely","little","look","looking","looks","ltd"],
        ["m","mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much","must","my","myself"],
        ["n","name","namely","nd","near","nearly","necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally","not","nothing","novel","now","nowhere"],
        ["o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only","onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own"],
        ["p","particular","particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides"],
        ["q","que","quite","qv"],
        ["r","rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right"],
        ["s","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","should","shouldn\'t","since","six","so","some","somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure"],
        ["t","t\'s","take","taken","tell","tends","th","than","thank","thanks","thanx","that","that\'s","thats","the","their","theirs","them","themselves","then","thence","there","there\'s","thereafter","thereby","therefore","therein","theres","thereupon","these","they","they\'d","they\'ll","they\'re","they\'ve","think","third","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly","try","trying","twice","two"],
        ["u","un","under","unfortunately","unless","unlikely","until","unto","up","upon","us","use","used","useful","uses","using","usually","uucp"],
        ["v","value","various","very","via","viz","vs"],
        ["w","want","wants","was","wasn\'t","way","we","we\'d","we\'ll","we\'re","we\'ve","welcome","well","went","were","weren\'t","what","what\'s","whatever","when","whence","whenever","where","where\'s","whereafter","whereas","whereby","wherein","whereupon","wherever","whether","which","while","whither","who","who\'s","whoever","whole","whom","whose","why","will","willing","wish","with","within","without","won\'t","wonder","would","would","wouldn\'t"],
        ["x"],
        ["y","yes","yet","you","you\'d","you\'ll","you\'re","you\'ve","your","yours","yourself","yourselves"],
        ["z","zero"]]
    # alphabet indexing
    alphabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,
                'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,
                'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    def __init__(self):
        pass
 
    # printing stop words member function
    def stopwords_print(self):
        print (self.stopwords)
 
    # deleting stop words from the given file member function
    def stopwords_del(self,file_name):
        self.file_name = file_name
        search = BinarySearch()
        string = []
        try:
            with open(file_name,"r") as f:
                content = (f.read()).split() # content in the file
                for i in content:
                    try:
                        index = self.alphabet[i[0].lower()]
                    except Exception as er:
                        index = 26
                    """ print (index) """
                    if index != 26:
                        if not search.binary_search(self.stopwords[index],i.lower()): # binary search
                            string.append(i.lower())
                    else:
                        string.append(i.lower())
        except IOError as err:
            if err.errno == ENOENT:
                print("%s file is missing",file_name)
            elif err.errno in (EACCES, EPERM):
                print("You are not allowed to read %s",file_name)
            else:
                raise
        """ string.sort() """ # sorted order list
        return string
 
 
# DataGrid Class # returning data grid and there respective counts
class DataGrid(StopWords):
     
    # docs,words,count
    def __init__(self,words,count):
        self.words = words
        self.count = count
 
    def counting(self,doc_index,lst,words,count):
        # handling each word in the lst ...
        for i in lst:
            # finding alphabet index ...
            try:
                index = self.alphabet[i[0].lower()]
            except Exception as er:
                index = 26
            # count the words ...
            # print ("counting words")
            if i not in words[doc_index][index]:
                words[doc_index][index].append(i)
                count[doc_index][index].append(1)
            else:
                # print (words[doc_index][index].index(i))
                count[doc_index][index][words[doc_index][index].index(i)] +=1
                 
        return words, count
 
 
# DataWarehouse Class # returning data warehouse contains all document words and there respective counts as an 2D-array..
class DataWarehouse(object):
    def __init__(self):
        pass
    def data_warehouse(self,docs,doc_len):
        try:
            # initializing variables and objects...
            words = []
            count = []
            warehouse = [[]]
            warehouse[0].append("")
            stopword_obj = StopWords()
            datagrid_add = DataGrid(words,count)
            search = BinarySearch()
 
            # calling member functions
            for i in range(0,doc_len):
                stopword_rem = stopword_obj.stopwords_del(docs[i])
                words.append([[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]])
                count.append([[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]])
                words, count = datagrid_add.counting(i,stopword_rem,words,count)
 
            # data grid warehouse # output number : 1
            # appending word to warehouse
            for x in words:
                for y in x:
                    for z in y:
                        if not search.binary_search(warehouse[0],z): # binary search
                            warehouse[0].append(z)
 
            # appending zero to documents word count
            words_len = len(warehouse[0])
            for i in range(0,doc_len):
                warehouse.append([])
                for j in range(0,words_len):
                    warehouse[i+1].append(0)
 
            # appending related word count to the respective documents
            for i in range(0,len(words)):
                for j in range(0,len(words[i])):
                    for k in range(0,len(words[i][j])):
                        warehouse[i+1][warehouse[0].index(words[i][j][k])] += count[i][j][k]
 
        except Exception as er:
            print ("Runtime Error or No Documents Passed ......")
            print (er)
 
        return warehouse
 
    def calc_warehouse(self,warehouse,doc_len):
        calc_warehouse = warehouse[:]
        try:
            for i in range(1,len(warehouse)):
                for j in range(1,len(warehouse[i])):
                    word_count = warehouse[i][j]
                    total_count = len(warehouse[i])-1
                    doc_word_count = 0
                    doc_count = 0
                    for k in range(0,doc_len):
                        doc_word_count += warehouse[k+1][j]
                        if warehouse[k+1][j] != 0 :
                            doc_count +=1
                    if doc_count == 0 or total_count == 0:
                        calc_warehouse[i][j]=0
                    else:
                        calc_warehouse[i][j] = ceil(((word_count*doc_len)/(total_count*doc_count))*1000)/1000
                        # print (word_count, doc_len, total_count, doc_count)
        except Execption as er:
            print ("Runtime Calculation Error")
            print (er)
 
        return calc_warehouse
 
# Main Defination  
def main():
    docs = sys.argv[1:]
    doc_len = len(sys.argv)-1
    data_warehouse = DataWarehouse()
    warehouse = data_warehouse.data_warehouse(docs,doc_len)
    print (warehouse,"\n")
    print (data_warehouse.calc_warehouse(warehouse,doc_len))
 
main()

