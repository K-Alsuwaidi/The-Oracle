def GetReminders(Name):
    """
    :param Name: Name of user
    :return: returns a list of reminders if present else None
    """
    with open("Reminders.json", "r") as f:
        Dicto = f.load()
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
    with open("Reminders.json", 'w') as f:
        Dicto = f.load()
        try:
            Listo = Dicto[Name]
            Listo.append(Reminder)
            Dicto[Name] = Listo
            f.dump(Dicto)
        except:
            Listo = [Reminder]
            Dicto[Name] = Listo
            f.dump(Dicto)


def DeleteReminder(Name, Reminder):
    """
    :param Name: Name of user
    :param Reminder: Reminder in string format
    :return: Nothing
    """
    with open('Reminders.json', 'w') as f:
        Dicto = f.load()
        try:
            Listo = Dicto[Name]
            NewList = []
            for i in Listo:
                if Reminder == i:
                    pass
                else:
                    NewList.append(i)
        except:
            return None