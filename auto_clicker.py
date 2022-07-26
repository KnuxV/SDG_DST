import pyautogui as pgui
import time
import pyperclip


def workaround_write(text):
    """
    This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
    It copies the text to clipboard and pastes it, instead of typing it.
    """
    pyperclip.copy(text)
    pgui.hotkey('ctrl', 'v')
    pyperclip.copy('')


# pgui.PAUSE = 2.5
pgui.FAILSAFE = True

# positional variables // TO BE CHANGED IF REUSED, using mouse_pos.py
export_position = 864, 545
tab_delimited_file_position = 886, 819
records_from_button_position = 710, 665
records_from_button_position_first_box = 861, 665
records_from_button_position_second_box = 949, 665
record_content = 899, 786
full_record = 794, 858
full_record_w_citations = 876, 873
export = 739, 846
above_save_button = 1270, 931
ok = 1222, 833
text_box = 1054, 175
save_button = 1469, 948

# To be changed if we don't start downloading from 1
record_from = 1
record_to = 1000
# text_file_name
root_file_name = 1
end_file_name = ".txt"

if __name__ == "__main__":
    total_number_pub = int(input("enter total number of publications :\n"))
    root_file_name = int(input("enter first title, 1 or whatever after the first bunch of download : \n"))
    while record_from <= total_number_pub:  # To be updated every chunk
        # 1st step : click export + tab delimited file
        time.sleep(1)
        pgui.click(export_position, interval=0.5)
        # time.sleep(2)
        pgui.click(tab_delimited_file_position, interval=0.5, button='left')
        # time.sleep(2)
        pgui.click(records_from_button_position)
        time.sleep(0.1)
        # First box
        pgui.click(records_from_button_position_first_box)
        time.sleep(0.1)
        # First, we need to empty the box from text
        for i in range(10):
            pgui.press("backspace", interval=0.1)
        # Then, we write the number
        # pgui.keyDown('shift')
        # pgui.write(str(record_from))
        # pgui.keyUp('shift')
        workaround_write(record_from)

        # Second box
        pgui.click(records_from_button_position_second_box)
        for i in range(10):
            pgui.press("backspace", interval=0.1)
        # pgui.keyDown('shift')
        # pgui.write(str(record_to))
        # pgui.keyUp('shift')
        workaround_write(record_to)

        time.sleep(1)
        pgui.click(record_content)
        time.sleep(1)
        pgui.click(full_record)
        time.sleep(1)
        pgui.click(export)
        time.sleep(20)

        # need to click above the save button and wait a bit
        pgui.click(above_save_button)
        # time.sleep(1)
        # pgui.click(ok)

        # click on the text box, erase, and write new file name
        pgui.click(text_box)
        pgui.hotkey('ctrl', 'a')
        pgui.press('backspace')
        pgui.keyDown('shift')
        pgui.write(str(root_file_name))
        pgui.write(end_file_name)
        pgui.keyUp('shift')
        pgui.click(save_button)

        # Update variable
        record_from += 1000
        record_to += 1000
        # Update this to handle the last thousand elements
        if record_to > total_number_pub:
            record_to = total_number_pub
        print(record_to)
        root_file_name += 1
