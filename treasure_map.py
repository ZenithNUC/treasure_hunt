import math
import sys

class TreasureMap:
    
    TREE_CHAR = " |"           # represents tree
    UNSEARCHED_CHAR = " ."     # represents unsearched location

    def __init__(self,size, chests, trees, pos , have_found,pir,global_map,init_len):
        '''
        Initialize treasure map.
        
        Parameters:
            - size (int): 
                Treasure map is square (size rows by size columns); 
                can assume that size is always a positive integer      
            - chests (list): 
                List of tuples (row, col) describing treasure chest locations     
            - trees (list): 
                List of tuples (row, col) describing tree locations
        
        Returns: None
        '''

        self.__treasure_map = size
        self.__chest_positions = chests
        self.__tree_positions = trees
        self.__num_chests_found = len(chests)
        self.__pos = pos
        self.__have_found = have_found
        self.__init_len = init_len
        self.__global_map = global_map
        self.__pir = pir
        # complete the rest of this method
        
   
    def display_map(self,global_map):
        '''
        Print treasure map in grid format, along with column and row indices.
        
        Parameters: None
        
        Returns: None
        '''
        # delete pass and complete this method
        chest_key_list = []
        unsearch_list = []
        for ypoint in range(self.__treasure_map):
            # add all tuples of point into maplist
            for xpoint in range(self.__treasure_map):
                unsearch_list.append((ypoint,xpoint))

        tree_list = self.__tree_positions
        chest_list = self.__chest_positions

        for chest in chest_list:
            chest_key_list.append(chest[0]*5 + chest[1])

        for tree in tree_list:
            # add the tree into map
            global_map[tree[0]*5+tree[1]] = " |"
        search_status = self.is_position_valid(self.__pos ,global_map,chest_key_list)
        self.auto_pirate(self.__pir,chest_key_list,chest_list)
        k = 0
        for point in global_map:
            # print the map
            print(point, end = "")
            if k % 5 == 4:
                print("\n")
            k += 1
        if search_status[1] == 0:
            print("this point is unvalid")
        print(search_status[0])
        

    def is_position_valid(self, pos, global_map,chest_key_list):
        '''
        Checks if position is a searchable location on the treasure map.
        
        Parameters:
            - position (tuple or list): 
                Valid position has values, the row and column
        
        Returns: (Boolean, string)
            - Boolean:
                True if position is valid; 
                False if position has already been searched or contains a tree
            - string:
                Message describing why position is valid or not
        '''        
        # assertion statement(s) here
        # complete the rest of this method
        posy = int(pos[0])
        posx = int(pos[1])
        try:
            is_exist = chest_key_list.index(posy*5 + posx) + 1
        except:
            is_exist = 0
        if global_map[posy * 5 + posx] == " .":
            if is_exist:
                search_valid = 1
                tip = "Congratulate!You find a treasure."
                global_map[posy * 5 + posx] = " T"
                self.__chest_positions.remove(pos)

            else:
                search_valid = 1
                self.__global_map[posy * 5 + posx] = " "+str(self.closest_chest(self.calculate_distance(pos)))
                tip = "this point can be searched"
        else:
            search_valid = 0
            if global_map[posy * 5 + posx] == " |":
                tip = "This point can't be searched,because it is a tree!"
            else:
                tip = "This point has been searched"
        return [tip,search_valid]
        
    def calculate_distance(self, pos):
        '''
        Calculate distances between searching position and all treasure chests, according to Pythagorean theorem.
        
        Parameters:
            - pos (tuple of two int): 
                Searching location (row, column)
        
        Returns: container of distances, all rounded to nearest integer
        '''        
        # delete pass and complete this method
        chest_list = self.__chest_positions
        distance_list = []
        for chest in chest_list:
            distance = math.sqrt((pos[0] - chest[0]) * (pos[0] - chest[0]) + (pos[1] - chest[1]) * (pos[1] - chest[1]) )
            dis_sub = distance - int(distance)
            if dis_sub < 0.5:
                distance_list.append(int(distance))
            else:
                distance_list.append(int(distance) + 1)
        return distance_list
    
    def closest_chest(self, distances):
        '''
        Determines the distance to the closest treasure chest, and if that
        distance is within reportable range of the current search position.
        
        Parameters:
            - distances (container of integers):
                Distances between current searching position and all chests
                
        Returns: (Boolean, int)
            - Boolean:
                True if distance to closest chest is not greater than half the number of columns in treasure map;
                False otherwise 
            - int:
                Distance to closest chest
        '''        
        # delete pass and complete this method
        closest_distance = min(distances)
        return closest_distance
    
    def update_map(self,have_found,init_len):
        '''
        Update treasure map with an 'X' if treasure is found at searching
        position, or a hint as to how far the closest treasure chest is from
        searching position.
        
        Parameters:
            - pos (tuple of ints): 
                Current searching location (row, column)      
            - player (int)
                Even number indicates that it's currently the player's turn; 
                Odd number indicates that it's currently the pirate's turn.     
        
        Returns: (int)
            - number of treasure chests found at current position (1 or 0)
        '''        
        # delete pass and complete this method
        
        residue = len(self.__chest_positions)
        have_found = init_len - residue
        return [residue,have_found]
            
             
    def auto_pirate(self,pir,chest_key_list,chest_list):
        '''
        Find the first searchable position, starting at position (0, 0) and
        searching each column, then moving down a row and searching each column,
        etc.  
        
        Parameters: None
        
        Returns: (tuple)
            - tuple of 2 integers, representing the first valid position for
              the pirate to search (row, column)
        '''        
        # delete pass and complete this method
        try:
            is_exist = chest_key_list.index(pir) + 1
        except:
            is_exist = 0
        if self.__global_map[pir] == " .":
            if is_exist:
                
                self.__global_map[pir] = "PT"
                x = pir % 5
                y = (pir - x) / 5
                chest_list.remove((y,x))
                print("pirate have found a treasure.")
            else:
                search_valid = 1
                self.__global_map[pir] = " P"
                tip = " "
        else:
            self.auto_pirate(pir+1,chest_key_list,chest_list)
        


    def is_hunt_over(self):
        '''
        Treasure hunt is over when all treasure chests have been found.
        
        Parameters: None
        
        Returns: Boolean
            - Boolean: True if all chests have been found; False otherwise
        '''        
        # delete pass and complete this method
        residue_found =  self.update_map(self.__have_found,self.__init_len)
        if residue_found[0] == 0:
            return 1
        else:
            return 0
    
    
    
if __name__ == "__main__":
    
    # test init and display_map methods: should match sample output in assignment description.
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
        y = input("please input the ypoint which you want to search:")
        x = input("please input the xpoint which you want to search:")
        pos = (int(y),int(x))

        game_map = TreasureMap(size, chests, trees, pos,have_found,pir)
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
    
    # test update map: does it work correctly when treasure chest location is guessed by player
    
    #assert found == 1, "Failed test 1: Incorrect value returned from update_map."
    
    # test update map: does it work correctly when player searches close to treasure chest location
    
    # test update map: does it work correctly when player searches far from treasure chest location
    
    # same update map tests as above, but for pirate: Do you get what you expect?
    
    # additional tests for the rest of the methods: what do you expect for each test?