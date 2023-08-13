import winreg


def reg_emp():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\Valve\\Steam\\Apps\\1142710\\")
    b = winreg.QueryValueEx(key, "Running")
    if key:
        winreg.CloseKey(key)
    print(b)

    parent_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\Valve\\Steam\\Apps\\")
    num = winreg.QueryInfoKey(parent_key)
    print(num)
    i = 0
    while True:
        try:
            key = winreg.EnumKey(parent_key, i)
            print(key)
            i += 1
        except WindowsError:
            print("xxxxxxx")
            break
    print(i)


def get_running_game_id():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\Valve\\Steam\\")
    id_tuple = winreg.QueryValueEx(key, "RunningAppID")
    if key:
        winreg.CloseKey(key)
    game_id = id_tuple[0]
    except_list = [228980, 431960]
    if game_id in except_list:
        game_id = 0
    return game_id


if __name__ == '__main__':
    pass
