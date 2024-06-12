import time
import sys


def display_text(text_list, pause_time=0.5, nested_pause_time=1.0):
    """
    Display text from a nested list with pauses between each phrase.

    :param text_list: Nested list of phrases to display
    :param pause_time: Pause time between phrases in seconds
    :param nested_pause_time: Pause time between nested lists in seconds
    """
    for item in text_list:
        if isinstance(item, list):
            display_text(item, pause_time, nested_pause_time)
            time.sleep(nested_pause_time)
        else:
            print(item)
            sys.stdout.flush()  # Ensure the text is displayed immediately
            time.sleep(pause_time)


# Example usage
dialogue = [
    "The night was dark and stormy.",
    ["A figure appeared in the distance,", "moving slowly towards the alley."],
    "A sense of dread filled the air.",
    ["The figure stopped,", "looked around,", "and then continued on its way."]
]

display_text(dialogue)