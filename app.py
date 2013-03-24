import mc

def main_content_left_press ():
    list_container = mc.GetActiveWindow ().GetList (90)
    index = list_container.GetFocusedItem ()

    items = list_container.GetItems ()
    num_items = len (items)

    if (index <= 0):
        index = num_items - 1
    else:
        index = index - 1

    #list_container.ScrollPageDown ()
    list_container.SetFocus ()
    list_container.SetFocusedItem (index)


def main_content_right_press ():
    list_container = mc.GetActiveWindow ().GetList (90)
    index = list_container.GetFocusedItem ()

    items = list_container.GetItems ()
    num_items = len (items)

    if (index >= num_items - 1):
        index = 0
    else:
        index = index + 1

    list_container.SetFocusedItem (index)
    mc.GetActiveWindow ().GetList (90).SetFocus ()
    mc.GetActiveWindow ().GetList (90).SetFocusedItem (index)
    #list_container.ScrollPageUp ()


def category_links_on_click ():
    current_control = mc.GetActiveWindow ().GetList (90)
    item_number = current_control.GetFocusedItem ()
    current_item = current_control.GetItem (item_number)

    if current_item.GetLabel () == "Playthroughs":
        mc.ActivateWindow (14001)

    elif current_item.GetLabel () == "Latests":
        list_control = mc.GetActiveWindow ().GetList (120)
        list_control.SetContentURL (current_item.GetPath ())
        list_control.Refresh ()
        list_control.SetFocus ()

    else:
        mc.ActivateWindow (14003)
        label_control = mc.GetWindow (14003).GetLabel (400)
        label_control.SetLabel (current_item.GetLabel ())

        list_control = mc.GetWindow (14003).GetList (420)
        list_control.SetContentURL (current_item.GetPath ())

    #mc.ShowDialogConfirm("My App", "fsfddfs you wish to play?", "No", "Yes")

def playthrough_link_on_click ():
    current_control = mc.GetActiveWindow ().GetList (220)
    item_number = current_control.GetFocusedItem ()
    current_item = current_control.GetItem (item_number)

    mc.ActivateWindow (14002)
    list_control = mc.GetWindow (14002).GetList (320)
    list_control.SetContentURL (current_item.GetPath ())
    label_control = mc.GetWindow (14002).GetLabel (300)
    label_control.SetLabel (current_item.GetLabel ());

