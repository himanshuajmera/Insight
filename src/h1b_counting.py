
# coding: utf-8

# In[ ]:


#Function to get top-10 most frequent words from a list
def gettop10(l):
    word_counter = {}
    res=[]
    for word in l:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    #sorting words according to number of count
    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    for i in popular_words[0:10]:
        i=i.replace("'","")
        prcnt=round(word_counter[i]*100/len(l),1)
        op=i+';'+str(word_counter[i])+';'+str(prcnt)+'%'        
        res.append(op)
    return res


# In[ ]:


def main():
    #get required packages
    import csv
    import fnmatch

    #read file 
    infile = open('./input/h1b_input.csv', encoding = 'utf8')
    csv_f = csv.DictReader(infile, delimiter=';')

    #create output file in .txt
    outfile1 = open("./output/top_10_occupations.txt","w")
    outfile2 = open("./output/top_10_states.txt","w")

    #create lists to store the data 
    occupation = []
    state = []

    #get headers from the file
    header=[]
    for row,check in zip(csv_f,range(1)):
        header.append(row)
    headers=header[0]  
    
    #creating pattern to match column name irrespective of index and different names. 
    pattern_status = '*STATUS*'
    pattern_occupation = '*SOC*NAME*'
    pattern_state = '*WORK*STATE*'
    
    #using fnmatch get column name as string
    a=fnmatch.filter(headers,pattern_status)[0]
    b=fnmatch.filter(headers,pattern_occupation)[0]
    c=fnmatch.filter(headers,pattern_state)[0]
    
    #append data in lists for certified cases only
    for row in csv_f:
        if row[a]=="CERTIFIED":
            occupation.append(row[b])
            state.append(row[c])

    #create list of top-10 required information        
    top_occ=gettop10(occupation)
    top_occ.insert(0, "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE")
    top_state=gettop10(state)
    top_state.insert(0, "TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE")

    #writing the output file as txt
    for listitem in top_occ:
        outfile1.write('%s\n' % listitem)

    for listitem in top_state:
        outfile2.write('%s\n' % listitem)

    #close the output file    
    outfile1.close()
    outfile2.close()


# In[ ]:


#creating main function
if __name__ == '__main__':
    main()

