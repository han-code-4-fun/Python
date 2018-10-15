# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for key in index:
        if (key[0] == keyword):
            for ele in key[1]:
                if(ele == url):   #if there is already a url in the list of url
                    return index
            key[1].append(url)
            return index
    #if key[0] != keyword
    index.append([keyword,[url]])
    return index

def add_page_to_index(index,url,content):
    contentList = content.split()
    
    for element in contentList:
        for entry in index: #nested loop to check every element with every entry
        #if element equal entry[0], check if url is in entry[1] list
            if(element == entry[0]):
                for urlInEntry in entry[1]:
                    if urlInEntry == url: #if current element and url in current entry, check next entry
                        break #check next element
                #if url is not in current entry's url list
                entry[1].append(url) #add url to current entry, and go to next entry
                break
                
        #if element not equal any of the entry[0], add element and url
        index.append([element,[url]])
           
    return index




add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


