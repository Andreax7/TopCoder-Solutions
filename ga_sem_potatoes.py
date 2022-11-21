def convertField(field):
    newField = []
    for x in range(len(field)):
        for y in range(len(field[x])):
            string_list = list(field[x])
        newField.append(string_list)
    return newField

def solution(noP, field):
    planted = []
    newField = convertField(field)
    
    for x in range(len(field)):

            if x == 0 : 
                      # check first row for soil
                for k in range( len(field[x]) ): # range 0 - len check row element
                    if noP == 0:
                        print('all is planted \n ')
                        for i in range(len(newField)):
                            newField[i] = "".join(newField[i])
                        planted = newField
                        return planted, noP

                    if k == len(field[x]): # when it reaches last element in row 
                        if newField[x][k-1] == "." and newField[x][k-2] != "P": # checks if previous element has P (k-1 not to reach list out of range)
                            if newField[x+1][k-1] != "P": # checks if element bellow has P
                                newField[x][k-1]="P"
                                noP= noP -1
                    else:
                        if newField[x][k] == "." and newField[x][k-1] != "P": # checks if previous element has P
                            if newField[x+1][k] != "P":  # checks if element bellow has P
                                newField[x][k]="P"
                                noP= noP-1             
            if x > 0 :
                
                for k in range( len(field[x]) ): # range 0 - len
                    if noP == 0:
                        print('nula ')
                        for i in range(len(newField)):
                            newField[i] = "".join(newField[i])
                        planted = newField
                        return planted, noP

                    if k == len(field[x]): # when it reaches last element y
                        if newField[x][k-1] == "." and newField[x][k-2] != "P":
                            if newField[x+1][k-1] != "P" and newField[x+1][k-2] != "P":
                                newField[x+1][k-1]="P"
                                noP= noP-1
                    else:
                        if newField[x][k] == "." and newField[x][k-1] != "P":
                            if newField[x][k] != "P" and newField[x-1][k] != "P":
                                newField[x][k]="P"
                                noP= noP-1
             
        
    for i in range(len(newField)):
        newField[i] = "".join(newField[i])
    planted = newField

    return newField, noP
    

def main():
   
    N = int(input("number of potatoes to plant: "))# 0-2500
    field = [".........","#########",".#......#",".########",".#.....##"] # 1-50 characters inclusive
    print(field)
    result, N = solution(N, field)
    for i in result:
        print('\n', i)
    if N > 0:
        print(' no of potatoes left ', N )

    
if __name__ == "__main__":
    main()