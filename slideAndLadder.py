def check_movement(starting_index,lst,i):
    if i == 1:
        lst[starting_index][5] = 1
    

def check_pos(pos,lst,starting_index):
    for all in pos:
        if lst[starting_index][1] ==  all[0]:
            if all[1] == 0:
                lst[starting_index][1] = all[2]
                lst[starting_index][3]+=1
            elif all[1] == 1:
                lst[starting_index][1] = all[2]
                lst[starting_index][3] +=1
            break

def check_valid(lst,starting_index,i):
    if (lst[starting_index][1]+i) > 25:
        pass
    else:
        lst[starting_index][1] +=i

def check_opponent(lst,starting_index):
    for index, all in enumerate(lst):
        if  index != starting_index:
            if all[1] == lst[starting_index][1]:
                all[1] = 1


pos=[[4,0,12],[6,0,15],[14,1,5],[18,0,23],[21,1,2],[24,1,16]]
players_count= int(input())
lst=[[input(),0,0,0,0,-1] for i in range(players_count)]
starting_player=input()
dice_count=int(input())
dice_value=[int(input()) for i in range(dice_count)]
starting_index = 0
for index, sublist in enumerate(lst):
    if sublist[0] == starting_player:
        starting_index = index
        break
for i in dice_value:
    if i > 6 or i < 0:
        break
    check_movement(starting_index,lst,i)
    if lst[starting_index][5] == 1:
        check_valid(lst,starting_index,i)
        check_pos(pos,lst,starting_index)
        lst[starting_index][2] = 25 - lst[starting_index][1]
    if lst[starting_index][1] == 25:
        break
    check_opponent(lst,starting_index)
    if i == 1 or i == 5:
        pass
    else:
        starting_index+=1
    if starting_index >= players_count:
        starting_index %=players_count