from typing import Iterable, Tuple, List, Union
TicTacToeRow = List[str]
TicTacToeBoard = Tuple[TicTacToeRow, TicTacToeRow, TicTacToeRow]

#My idea is to look at each list within the tuple, if it does not need to be updated,
#return it to a new board I am concatenating.
def tic_tac_toe_finish(board: TicTacToeBoard, pos_y: int, pos_x: int, symbol: str) -> None:

    new_board = tuple()
    for y in range(0,3):
        if y != pos_y:
            new_board = new_board + (board[y],)
        # if the list in question needs to be modified, switching a new line for the old and concatanating.
        else:
            row = board[y]
            row[pos_x] = symbol
            new_board += (row,)
            #Switching the new board in for the tuple that was there.
    board = new_board


def count_instances(collection: Tuple, instance: Union[int, str]) -> int:
    count = 0
    for item in collection:
        if item == instance:
            count += 1
    return count


def print_indexes_and_entries(indexes: Iterable, entries: Iterable) -> None:
    for pair in zip(indexes, entries):
        print(("Index: " + pair[0]).ljust(18) + "Entry: " + pair[1])



def print_items_with_index(items: Iterable):
    new_list = []
    index = 1
    while index < len(items)+ 1:
        new_list.append(index)
        index += 1
    for pair in zip(new_list, items):
        print(str(pair[0]) + ": " + pair[1])

