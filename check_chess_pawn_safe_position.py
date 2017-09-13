"""
Script checks if chess pawn has other pawn guarding its position
"""

files = ("a", "b", "c", "d", "e", "f", "g", "h")
ranks = range(1, 9)

def safe_pawns(pawns):
    result = 0
    safe_positions = []
    for pawn in pawns:
        print(pawn)
        safe_positions = get_safe_positions(pawn)
        for position in safe_positions:
            if position in pawns:
                result += 1
                break
    return result

def get_safe_positions(pawn):
    current_rank = int(pawn[1])
    safe_rank = current_rank - 1
    pawn_file_index = files.index(pawn[0])
    if pawn_file_index != 0 and pawn_file_index != 7:
        positions = [ "".join((files[pawn_file_index - 1], str(safe_rank))), "".join((files[pawn_file_index + 1], str(safe_rank)))]
    elif pawn_file_index == 0:
        positions = ["".join((files[pawn_file_index + 1], str(safe_rank)))]
    elif pawn_file_index == 7:
        positions = ["".join((files[pawn_file_index - 1], str(safe_rank)))]
    return positions

if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"}) == 7
