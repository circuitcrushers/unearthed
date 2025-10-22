from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2")

# Based on the selection, run a program.
if selected == "1":
    import Mission_5_6_8
elif selected == "2":
    import Mission_10

