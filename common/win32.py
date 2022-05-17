# -*- coding: UTF-8 -*-
"""
@author:crow
@file:win32.py
@time:2022/05/05
"""

import win32gui
import win32con


# 获取所有窗口句柄
def get_all_windows() -> list:
    hwnd_list = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), hwnd_list)
    return hwnd_list


# 获取窗口的子窗口句柄
def get_son_windows(parent):
    hwnd_child_list = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), hwnd_child_list)
    return hwnd_child_list


# 获取窗口标题
def get_title(hwnd):
    title = win32gui.GetWindowText(hwnd)
    print('窗口标题:%s' % (title))
    return title


# 获取窗口类名
def get_clasname(hwnd):
    clasname = win32gui.GetClassName(hwnd)
    print('窗口类名:%s' % (clasname))
    return clasname


# 窗口置顶
def set_top(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)


# 取消窗口置顶
def set_down(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                          win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)


# 根据窗口名称获取句柄
def get_hwnd_from_name(name):
    hwnd_list = get_all_windows()
    for hwd in hwnd_list:
        title = get_title(hwd)
        if name in title:
            return hwd


# 通过句柄将窗口放到最前
def show_window(name):
    handel = get_hwnd_from_name(name)
    win32gui.ShowWindow(handel, win32con.SW_SHOWMAXIMIZED)
    win32gui.SetForegroundWindow(handel)


def hide_window(name):
    hwd = get_hwnd_from_name(name)
    win32gui.ShowWindow(hwd, win32con.SW_HIDE)
