from typing import List
import numpy as np

class Vector():

    """
    Data model to store coordinates.
    """

    def __init__(self,coord_tuple:tuple):

        self.x_value = coord_tuple[0]
        self.y_value = coord_tuple[1]
        self.tuple = coord_tuple




def clockwise_turn_right(direction:Vector)->Vector:

    """
    Function that performs a matrix transformation on vector to rotate it 90 degrees.
    """

    rotation_matrix = [[0,-1],[1,0]]
    image = np.dot(rotation_matrix,direction.tuple)

    return Vector((image[0],image[1]))

def traverse(array:List[List], direction:Vector, array_last_point:Vector)-> (int,Vector):

    next_x_point = direction.x_value + array_last_point.x_value
    next_y_point = direction.y_value + array_last_point.y_value

    return array[next_y_point][next_x_point] , Vector((next_x_point,next_y_point))


def make_array(n:int)->np.array:
    """ 
    Function to create an n x n array.
    """

    array = np.arange(n**2).reshape((n,n))

    return array




def generate_target_sequence(n:int)->List[int]:
    """
    Generate a target sequence based on the input value 'n'.

    Args:
    n (int): The input value.

    Returns:
    list: The generated target sequence.
    """
    if n <= 1:
        return []

    target = []
    for i in range(2,n+1):
        if i == n:
            target.extend([i] * 3)
        else:
            target.extend([i]*2)

        
    return sorted(target,reverse=True)


def snail_crawl(n:int,direction:Vector,point:Vector)->(List[int],np.array):

    """  
    Function that takes a n x n numpy array and walks around the array 
    in a 'snail like' fashion, spiralling towards the centre of the array
    and finishing at the centre. Values are appended to a list sequentially 
    and outputted by the function.
    
    """

    sequence = generate_target_sequence(n)
    n_array = make_array(n)

    my_list = []  #empty list to append to

    for i in sequence: #hop through each value
        for b in range(i-1): #number of hops to make per each value
            value,point = traverse(n_array,direction,point) #function to traverse array
            my_list.append(value)
        direction = clockwise_turn_right(direction)
    my_list.insert(0,n_array[0][0]) #final insert to include first array value

    return my_list,n_array



if __name__ == '__main__':

    my_input = 4
    direction = Vector((1,0))
    point = Vector((0,0))
    output_list , my_array = snail_crawl(my_input,direction,point)
    print(output_list)
    print(my_array)