import treasure_map

# function definitions go here


if __name__ == "__main__":
    # start your main program here
    size = 5
    chests = [(1,2), (0,0)]
    init_len = len(chests)
    trees = [(0,1), (2,3), (0,4)]
    global_map = []
    for i in range(size):
            for j in range(size):
                global_map.append(" .")
    have_found = 0
    pir = 0
    while(1):
        y = input("please input the ypoint which you want to search(must a integer from 0 to "+str(size-1)+"):")
        x = input("please input the xpoint which you want to search(must a integer from 0 to "+str(size-1)+"):")
        if int(y) > size - 1 or int(y) < 0 or int(x) > size - 1 or int(x) < 0 :
        	print("input error,please input a legal number")
        	continue
        pos = (int(y),int(x))

        game_map = treasure_map.TreasureMap(size, chests, trees, pos,have_found,pir,global_map,init_len)
        distances = game_map.calculate_distance(pos)
        closest_distance = game_map.closest_chest(distances)
        game_map.display_map(global_map)
        pir += 1
        residue_found =  game_map.update_map(have_found,init_len)
        have_found = residue_found[1]
        print(str(residue_found[0]) + " residue point ")
        print(str(residue_found[1]) + " have found")
        if game_map.is_hunt_over():
            print("all have found")
            break