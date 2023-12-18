import pyautogui
import time
import random



while True:
    time.sleep(5)
    # Replace 'start_image.png' with the path to your starting PNG image
    start_image_path = 'play.png'

    # Replace 'different_image.png' with the path to the different PNG image you're looking for
    different_image_path = 'end.png'
    def find_image(image_path):
        try:
            location = pyautogui.locateOnScreen(image_path)
            if location:
                center_x, center_y = pyautogui.center(location)
                return center_x, center_y
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def move_to_image(image_path):
        result = find_image(image_path)
        if result:
            x, y = result
            pyautogui.click(x, y)
            print(f"Mouse moved to image at coordinates: {result}")
            return True
        else:
            return False
        
    move_to_image(start_image_path)

    time.sleep(10)

    while True:
        def place():
            coord_list = [(812, 522), (1103, 515)]
            x, y = random.choice(coord_list)
            # Generate random values to add or subtract between 0 and 25 pixels
            x_offset = random.randint(-25, 25)
            y_offset = random.randint(-120, 25)

            # Add the offsets to the coordinates
            new_x = x + x_offset
            new_y = y + y_offset

            return new_x, new_y

        def offset():
            coord_list = [(847, 909), (959, 911), (1061, 911), (1168, 915)]
            x, y = random.choice(coord_list)

            # Generate random values to add or subtract between 0 and 25 pixels
            x_offset = random.randint(-25, 25)
            y_offset = random.randint(-25, 25)

            # Add the offsets to the coordinates
            new_x = x + x_offset
            new_y = y + y_offset

            return new_x, new_y
        def timer(time):
            # Adding 10-30% to the original time variable
            extra_time = time * (0.1 + (0.2 * random.random()))  # Randomly selecting between 10% and 30%
            return time + extra_time

        
        pyautogui.click(offset())
        time.sleep(timer(0.25))
        pyautogui.click(place())
        if move_to_image(different_image_path):
            break
        time.sleep(timer(5))
        


