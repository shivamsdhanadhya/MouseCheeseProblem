import sys

def selectValidMaxElement(cheese_weights, cheese_eaten_map):
    """
        This method implements an algorithm for Mouse to eat max cheese
        by following provided game-rules
    """
    tmp_list = []
    for index in range(len(cheese_weights)):
        if index == 0 and cheese_eaten_map[index] == 0 and\
        (cheese_eaten_map[index+1] == 0 or cheese_eaten_map[index+1] == -1):
            tmp_list.append(cheese_weights[index])
        elif index == len(cheese_weights) - 1 and cheese_eaten_map[index] == 0 and\
        (cheese_eaten_map[index-1] == 0 or cheese_eaten_map[index-1] == -1):
            tmp_list.append(cheese_weights[index])
        elif index != 0 and index != len(cheese_weights) - 1 and cheese_eaten_map[index] == 0 and\
        (cheese_eaten_map[index+1] == 0 or cheese_eaten_map[index+1] == -1) and\
        (cheese_eaten_map[index-1] == 0 or cheese_eaten_map[index-1] == -1):
            tmp_list.append(cheese_weights[index])
    if not len(tmp_list):
        return 0
    curr_max = max(tmp_list)
    indices = []
    indices = [i for i in range(len(cheese_weights)) if cheese_weights[i] == curr_max]
    
    for entry in indices:
        if entry == 0 and (cheese_eaten_map[entry+1] == 0 or cheese_eaten_map[entry+1] == -1):
            cheese_eaten_map[entry] = 1
            return cheese_weights[entry]
        elif entry == len(cheese_weights) - 1 and (cheese_eaten_map[entry-1] == 0 or cheese_eaten_map[entry-1] == -1):
            cheese_eaten_map[entry] = 1
            return cheese_weights[entry]
        elif entry != 0 and entry != len(cheese_weights) - 1 and\
        (cheese_eaten_map[entry] == 0) and\
        (cheese_eaten_map[entry -1] == 0 or cheese_eaten_map[entry -1] == -1) and\
        (cheese_eaten_map[entry+1] == 0 or cheese_eaten_map[entry+1] == -1):
            cheese_eaten_map[entry] = 1
            return cheese_weights[entry]
        else:
            cheese_eaten_map[entry] = -1
            continue
    
def maxCheeseRatCanEat(cheese_weights):
    """ 
        Applies algorithm onto cheeese_weights
        to get Max weight mouse can eat
    """
    cheese_eaten_map = len(cheese_weights) * [0]
    cheese_eaten = 0
    while True:
        tmp_wght = selectValidMaxElement(cheese_weights, cheese_eaten_map)
        if tmp_wght > 0:
            cheese_eaten += tmp_wght
        elif not tmp_wght:
            break
    return cheese_eaten
    
def validateInputWeightCounts(cheese_weights, n):
    """
        Validates the n and weights count provided as input
    """
    wght_count_flag = True
    if len(cheese_weights) < n:
        wght_count_flag = False
        print("Invalid Input, provided weights are lesser "
              "than the earlier input weight count")
        print("Exiting....")
    elif len(cheese_weights) < n:
        wght_count_flag = False
        print("Invalid Input, provided weights are more" 
              "than the earlier input weight count %s", str(n))
        print("Exiting....")
    return wght_count_flag
        
def validateInputConstraints(T, n, cheese_weight):
    """
        Validates the input Constraints 
        and returns boolean Flag
    """
    constraint_flg = True
    if not(1<=T<=200):
        constraint_flg = False
    if not (1<=n<=1000):
        constraint_flg = False
    for entry in cheese_weight:
        if not (1<= entry <= 10000):
            constraint_flg = False
            break
    if not constraint_flg:
        print("Input Constaints not Followed, Exiting...")
    return constraint_flg

if __name__ == "__main__":
    # Following is the main driver code
    # There are no prompt messages added to get inputs,
    # user is supposed to provide input as explained in problem description
    # Get number of TCs as input
    T = int(input())
    for i in range(T):
        # get cheese pieces' count as input for every TC
        n = int(input())
        cheese_weights = input()
        cheese_weights = [int(element) for element in cheese_weights.split()]
        # Basic Input Validation for Error Out Cases
        input_wght_val_flg = validateInputWeightCounts(cheese_weights, n)
        input_constraint_val = validateInputConstraints(T, n, cheese_weights)
        if not input_wght_val_flg or not input_constraint_val:
            sys.exit(0)
        #print(cheese_weights)
        all_equal_flg = all(ele == cheese_weights[0] for ele in cheese_weights)
        # Handle special case of single cheese block
        if len(cheese_weights) == 1:
            max_cheese_weight = cheese_weights[0] 
        # Handle special case of all cheese items with exact equal weights
        elif len(cheese_weights) > 1 and all_equal_flg:
            if len(cheese_weights) % 2 == 0:
                max_cheese_weight = int(cheese_weights[0] * len(cheese_weights)/2)
            else:
                max_cheese_weight = int(cheese_weights[0] * (len(cheese_weights)+1)/2)
        else:
            max_cheese_weight = maxCheeseRatCanEat(cheese_weights)
        print(max_cheese_weight)