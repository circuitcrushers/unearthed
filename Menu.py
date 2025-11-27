from pybricks.tools import hub_menu

# Menu selection
selected = hub_menu("1", "2", "3", "4", "5")

# Based on the selection, run a program.
if selected == "1":
    import Mission_5_6_7_8
elif selected == "2":
    import Mission_9_10
elif selected == "3":
    import Mission_12
elif selected == "4":
    import Mission_2
elif selected == "5":
    import Mission_4    

