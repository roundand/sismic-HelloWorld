# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Learning from https://statecharts.dev/how-to-use-statecharts.html
# and more importantly from https://sismic.readthedocs.io/en/latest/format.html
from sismic.io import import_from_yaml
from sismic.model import Statechart

statechart = import_from_yaml(filepath='keyboard.yaml')
assert isinstance(statechart, Statechart)
print(f'statechart.name: {statechart.name}')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
