
def print_block_letters(text):
    # Define the block letter patterns for each character
    block_letters = {
        'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        'C': [" CCC ", "C   C", "C    ", "C   C", " CCC "],
        'D': ["DDD  ", "D  D ", "D   D", "D  D ", "DDD  "],
        'E': ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"],
        'F': ["FFFFF", "F    ", "FFFF ", "F    ", "F    "],
        'G': [" GGG ", "G    ", "G  GG", "G   G", " GGG "],
        'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        'I': [" III ", "  I  ", "  I  ", "  I  ", " III "],
        'J': ["  JJJ", "   J ", "   J ", "J  J ", " JJ  "],
        'K': ["K  K ", "K K  ", "KK   ", "K K  ", "K  K "],
        'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
        'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
        'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
        'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        'Q': [" QQQ ", "Q   Q", "Q   Q", "Q  QQ", " QQQQ"],
        'R': ["RRRR ", "R   R", "RRRR ", "R R  ", "R  RR"],
        'S': [" SSS ", "S    ", " SSS ", "    S", " SSS "],
        'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
        'V': ["V   V", "V   V", " V V ", " V V ", "  V  "],
        'W': ["W   W", "W   W", "W W W", "W W W", " W W "],
        'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
        ' ': ["     ", "     ", "     ", "     ", "     "]  # Space
    }
    
    # Convert the text to upper case
    text = text.upper()
    
    # Initialize a list to hold each line of the block letters
    lines = ["", "", "", "", ""]
    
    # Build the block letters line by line
    for char in text:
        if char in block_letters:
            char_lines = block_letters[char]
            for i in range(5):
                lines[i] += char_lines[i] + "  "
    
    # Print the block letters
    for line in lines:
        print(line)

# Example usage
print_block_letters("Salome miller")