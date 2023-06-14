import png, array
from PIL import Image

THREE_PLAYER_BOUNDS = (933, 110, 1805, 1020)




def find_good_bounds(input_path):
    bounds = (930, 110, 1820, 1020)
    d = {'l': 0, 't': 1, 'r': 2, 'b': 3}
    while True:
        with Image.open(input_path) as im:
            im.crop(bounds).show()
        next = input(f'shift bounds from {bounds}? ')
        if next == 'done':
            break
        elif next in d:
            shift = int(input('shift by: '))
            index = d[next]
            bounds_list = list(bounds)
            bounds_list[index] = bounds_list[index] + shift
            bounds = tuple(bounds_list)
            print(f'now cropping using {bounds}')

def crop_screenshot(bounds, input_file, output_file):
    pass        


if __name__ == "__main__":
    find_good_bounds("input_files/1.png")