def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    test = []
    for x in matrix:
        test += [x[::-1]]
    return test
            

    


print(mirror_matrix([[1,2,3],[4,5,6]]))
mirror_matrix([[1,2],[3,4],[5,6]])
mirror_matrix([[-1,-2],[-3,-4]])
