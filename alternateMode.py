#!/usr/bin/env python3

import os
from i3ipc import Connection

def find_parent(i3, window_id):
    def finder(con, parent):
        if con.id == window_id:
            return parent
        for node in con.nodes:
            res = finder(node, con)
            if res:
                return res
        return None

    return finder(i3.get_tree(), None)

def set_alternate_layout(i3):
    win = i3.get_tree().find_focused()
    parent = find_parent(i3, win.id)

    if (parent and parent.layout != 'tabbed'
            and parent.layout != 'stacked'):

        if parent.orientation == 'horizontal':
            i3.command('split v')
        else:
            i3.command('split h')

def main():
    i3 = Connection()
    set_alternate_layout(i3)

if __name__ == "__main__":
    main()
