import json
def GetReminders(Name):
    """
    :param Name: Name of user
    :return: returns a list of reminders if present else None
    """
    Name = "{}".format(Name)
    with open("Reminders.json", "r") as f:
        Dicto = json.load(f)
        try:
            Reminders = Dicto[Name]
            f.close()
        except:
            return None
    return Reminders

def SetReminders(Name, Reminder):
    """
    :param Name: Name of user
    :param Reminder: Reminder in string format
    :return: Nothing
    """
    Name = "{}".format(Name)
    with open("Reminders.json", 'r') as f:
        Dicto = json.load(f)
        f.close()

    with open("Reminders.json", 'w') as f:
        try:
            Listo = Dicto[Name]
            Listo.append(Reminder)
            Dicto[Name] = Listo
            json.dump(Dicto, f)
        except:
            Listo = [Reminder]
            Dicto[Name] = Listo
            json.dump(Dicto, f)
        f.close()


def DeleteReminder(Name, Reminder):
    """
    :param Name: Name of user
    :param Reminder: Reminder in string format
    :return: Nothing
    """
    Name = "{}".format(Name)

    with open('Reminders.json', 'r') as f:
        Dicto = json.load(f)
    f.close()

    with open("Reminders.json", 'w') as f:
        try:
            Listo = Dicto[Name]
            NewList = []
            for i in Listo:
                if Reminder == i:
                    pass
                else:
                    NewList.append(i)
            Dicto[Name] = NewList
            json.dump(Dicto, f)
        except:
            return False
        f.close()