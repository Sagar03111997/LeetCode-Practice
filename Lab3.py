import math
def find_minimum_in_range(num_list,i,j):
    number_of_elements=round(math.sqrt(len(num_list)))
    querylist=[]
    ql=[]
    index_list=[]
    index=0
    right_elements=[]
    left_elements=[]
    query_elements=[]
    for m in range (0,number_of_elements):
        ql.append(num_list[index:index+number_of_elements])
        querylist.append(min(num_list[index:index+number_of_elements]))
        index=index+number_of_elements
    w=int(i/number_of_elements)
    v=int(j/number_of_elements)
    for z in range(w,v+1):
        if z==w and ql[w][0]==num_list[i]:
                index_list.append(querylist[w])
                query_elements.append(querylist[w])
        elif z==w and ql[w][0]!=num_list[i]:
                index_list.append(min(ql[z][i%number_of_elements:]))
                left_elements.append(ql[z][i%number_of_elements:])
        elif z==v and ql[v][-1]==num_list[j]:
                index_list.append(querylist[v])
                query_elements.append(querylist[v])
        elif z==v and ql[v][-1]!=num_list[j]:
                index_list.append(min(ql[z][0:((j+1)%number_of_elements)]))
                right_elements.append(ql[z][0:((j+1)%number_of_elements)])
        else:
            index_list.append(querylist[z])
            query_elements.append(querylist[z])
    print(index_list)
    print("Left Side of the elements are:",left_elements)
    print("Query List Elements are:",query_elements)
    print("Right Side Elements are:",right_elements)
    print("Minimum Value:",min(index_list))
    return

print(find_minimum_in_range([70,78,69,96,19,68,54,60,15,267],1,5))