
import sys

filename = sys.argv[1];
title =  input("Titel:");
outfile = input("Output filename:") +".xml";

voc = [];

with open(filename, 'r', -1 , "UTF-8") as f:
    for line in f:
        words = line.split(';')
        voc.append(words)

with open(outfile, 'w', -1, "UTF-8") as outF:
    outF.write("<?xml version='1.0' encoding='UTF-16' standalone='yes' ?>")
    outF.write("<units><unit><title>"+title+"</title><vocables>")
    for translation in voc:
        firstMeaning = ""
        secondMeaning = ""
        for i in range(len(translation)-1):
            if i == 0:
                secondMeaning +="<value>"+translation[i]+"</value>\n"
            else:
                firstMeaning += "<value>"+translation[i]+"</value>\n"
        
        outF.write(
            """<vocable>
            <first_meaning>\n"""+firstMeaning+                    
            """</first_meaning>
            <second_meaning>\n"""+secondMeaning+
            """</second_meaning>
            </vocable>"""        
        )
    outF.write("</vocables></unit></units>")
            
            


   

