def print_spiral_matrix(input_array):

    # Set starting index to [0][0] (top left corner)
    starting_row_index = 0
    starting_col_index = 0

    # Set starting index to [len(a)][len(a[1])] (bottom right corner)
    ending_row_index = len(input_array)
    ending_col_index = len(input_array[1])

    while starting_row_index < ending_row_index and starting_col_index < ending_col_index:

        # Print the first row from remaining rows
        for i in range(starting_col_index, ending_col_index):
            print(input_array[starting_row_index][i], end=" ")

        starting_row_index += 1  # Just printed a row at that index so increment

        # Print the last col in remaining cols
        for i in range(starting_row_index, ending_row_index):
            print(input_array[i][ending_col_index - 1], end=" ")

        ending_col_index -= 1  # Just printed a col at that index so decrement

        # Check to see if there is another row to print
        if starting_row_index < ending_row_index:

            # Print the last row from the remaining rows
            for i in range(ending_col_index - 1, (starting_col_index - 1), -1):
                print(input_array[ending_row_index - 1][i], end=" ")

            ending_row_index -= 1  # Just printed a row at that index so decrement

        # Check to see if there is another col to print
        if starting_col_index < ending_col_index:

            # Print the first column from the remaining columns
            for i in range(ending_row_index - 1, starting_row_index - 1, -1):
                print(input_array[i][starting_col_index], end=" ")

            starting_col_index += 1  # Just printed a col at that index so increment


# Test the Function
test_matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

print_spiral_matrix(test_matrix)
