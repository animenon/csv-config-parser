#!/usr/bin/env python3
contents=['# Specify configurations as follows -\n', '# header1, name1:val1, name2:val2\n', '# ...\n', '# each line is a config\n', '\n', 'test, column1 = type1, column2 = type2\n', 'test1, column1 = type11, column2 = type22\n', 'test3, column1 = type111, column2 = type222\n']

contents2=[x.strip() for x in contents if(x[0]!=";" and x[0]!="#")]  ## remove comments
contents2 = filter(None,contents2)

dict={}
for x in contents2:
    lst=x.split(",")    ## lst=[incubating.test, column1 = type1, column2 = type2]
    header=lst.pop(0)       ## header = incubating.test ;;;; lst=['column1 = type1', 'column2 = type2']
    while(len(lst)>0):
        l=lst[0]
        print(header, l)
        if("=" in l):
            pair=l.split("=")
            if(header not in dict):
                dict[header]={}
            dict[header][pair[0].strip()] = pair[1].strip()
            key=pair[0].strip()
            val=pair[1].strip()
            print("dict[{}][{}] = {}".format(header,key,val))
        lst.pop(0)
