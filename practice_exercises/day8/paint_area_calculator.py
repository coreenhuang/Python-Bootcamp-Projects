# Calculate how many cans of paint to buy

def paint_calc(height, width, cover):
    num_of_cans = round((height * width) / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

# Test

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
