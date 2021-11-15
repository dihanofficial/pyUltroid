# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

from .. import udB


def get_stuff():
    a = udB.get_key("PMPERMIT")
    if not a:
        return []
    try:
        return eval(a)
    except BaseException:
        try:
            # Transferring stuff From old format to new
            x, y = [], udB.get_key("PMPERMIT").split()
            for z in y:
                x.append(int(z))
            udB.set_key("PMPERMIT", str(x))
            return x
        except BaseException:
            pass
    return []


def get_approved():
    return get_stuff()


def approve_user(id):
    ok = get_approved()
    if id in ok:
        return True
    ok.append(id)
    return udB.set_key("PMPERMIT", ok)


def disapprove_user(id):
    ok = get_approved()
    if id in ok:
        ok.remove(id)
        return udB.set_key("PMPERMIT", ok)


def is_approved(id):
    return id in get_approved()
