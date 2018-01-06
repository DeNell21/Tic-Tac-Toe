l = [["","",""],["","",""],["","",""]]

print(                 )
print("     0   1   2 ")
print("  0    |   |   ")
print("    ---|---|---")
print("  1    |   |   ")
print("    ---|---|---")
print("  2    |   |   ")
print("               ")
print(" Choose a space on the board.")

full = False
win = False

count = 1
x = input("Would you like to begin? (Press Enter)")

while full == False and win == False and x != "q":
    count3 = 0
    if count % 2 == 1:
        try:
            print(" ")
            print("Enter 'q' to quit")
            
            x = input ("Choose a space (X): ")

            first_x = x[0]
            second_x = x[1]
    
            if l[int(first_x)][int(second_x)] == "X" or l[int(first_x)][int(second_x)] == "O":
                print("That space is already taken!")
                print("Pick again.")
                
            else:
                l[int(first_x)][int(second_x)] = "X"
                count += 1
                
                count1 = 0
                for lis in l:
                    count2 = 0
                    count1 += 1
                    for i in lis:
                        count2 += 1
                        if count2 <= 2:
                            if i == "":
                                print(" "," | ",end = "")
                            else:
                                print(i," | ",end = "")
                        else:
                            if i == "":
                                print(" ")
                            else: 
                                print(i)
                    if count1 <= 2:
                        print("------------")
                        
                if l[0][0] == "X" and l[1][1] == "X" and l[2][2] == "X":
                    print("X is the winner!!!!!")
                    break
                if l[0][2] == "X" and l[1][1] == "X" and l[2][0] == "X":
                    print("X is the winner!!!!!")
                    break
                if l[0][0] == "X" and l[0][1] == "X" and l[0][2] == "X":
                    print("X is the winner!!!!!")
                    break
                if l[1][0] == "X" and l[1][1] == "X" and l[1][2] == "X":
                    print("X is the winner!!!!!")
                    break
                if l[2][0] == "X" and l[2][1] == "X" and l[2][2] == "X":
                    print("X is the winner!!!!!")
                    break
                if l[0][0] == "X" and l[1][0] == "X" and l[2][0] == "X":
                    print("X is the winner!!!!!")
                    break
                if l[0][1] == "X" and l[1][1] == "X" and l[2][1] == "X":
                    print("X is the winner!!!!!")
                    break
                if l[0][2] == "X" and l[1][2] == "X" and l[2][2] == "X":
                    print("X is the winner!!!!!")
                    break
                
                for lis in l:
                    for i in lis:
                        if i != "":
                            continue
                        else:
                            count3 += 1
                if count == 10:
                    print("Cat Game!!! No Winner!!!")
                    break
                    
        except IndexError:
            print("Make a pick ON the board!")
            continue
        
    if count % 2 == 0:
        try:
            print(" ")
            print("Enter 'q' to quit")
            x = input("Choose a space (O): ")
            
            first_o = x[0]
            second_o = x[1]
    
            if l[int(first_o)][int(second_o)] == "X" or l[int(first_o)][int(second_o)] ==  "O":
                print("That space is already taken!")
                print("Pick again.")
                
            else:
                l[int(first_o)][int(second_o)] = "O"
                count += 1
                
                count1 = 0
                for lis in l:
                    count2 = 0
                    count1 += 1
                    for i in lis:
                        count2 += 1
                        if count2 <= 2:
                            if i == "":
                                print(" "," | ",end = "")
                            else:
                                print(i," | ",end = "")
                        else:
                            if i == "":
                                print(" ")
                            else: 
                                print(i)
                    if count1 <= 2:
                        print("------------")
                
                if l[0][0] == "O" and l[1][1] == "O" and l[2][2] == "O":
                    print("O is the winner!!!!!")
                    break
                if l[0][2] == "O" and l[1][1] == "O" and l[2][0] == "O":
                    print("O is the winner!!!!!")
                    break
                if l[0][0] == "O" and l[0][1] == "O" and l[0][2] == "O":
                    print("O is the winner!!!!!")
                    break
                if l[1][0] == "O" and l[1][1] == "O" and l[1][2] == "O":
                    print("O is the winner!!!!!")
                    break
                if l[2][0] == "O" and l[2][1] == "O" and l[2][2] == "O":
                    print("O is the winner!!!!!")
                    break
                if l[0][0] == "O" and l[1][0] == "O" and l[2][0] == "O":
                    print("O is the winner!!!!!")
                    break
                if l[0][1] == "O" and l[1][1] == "O" and l[2][1] == "O":
                    print("O is the winner!!!!!")
                    break
                if l[0][2] == "O" and l[1][2] == "O" and l[2][2] == "O":
                    print("O is the winner!!!!!")
                    break
                
                for lis in l:
                    for i in lis:
                        if i != "":
                            continue
                        else:
                            count3 += 1
                if count == 10:
                    print("Cat Game!!! No Winner!!!")
                    break
                
        except IndexError:
            print("Make a pick ON the board!")
            continue