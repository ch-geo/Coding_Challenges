'''
You're given a string which represents a road with some potholes. 
Write a function that patches the potholes of the road by adding cement in three consecutive segments.
Return the minimum number of patches required.
'''

def solution(road):
    count = 0
    end_index = len(road) - 1

    # Printing statement in order to check algorithm correctness
    #print(road)
    
    # Find the indexes of the potholes
    road_map = []
    for index, segment in enumerate(road):
        if segment == 'x':
            road_map.append(index)

    
    past_hole = -3
    for hole in road_map:
        
        # Check if current hole is already fixed by
        # checking if it's near a previous fixed hole
        if hole in [past_hole + 1, past_hole + 2]:
            continue
        
        # If current hole is the appropriate distance
        # from the end of the road, proceed in fixing it
        if hole <= end_index - 2:
            
            # Alterate road in order to check algorithm correctness
            #road = road[:hole] + "..." + road[hole+3:] 
            
            count += 1
            past_hole = hole

        # If current hole in the last three segments of the road           
        else:
            
            # Alterate road in order to check algorithm correctness 
            #road = road[:-3] + "..."
            
            count += 1
            break


    # Printing statement in order to check algorithm correctness
    #print(road)
    return count