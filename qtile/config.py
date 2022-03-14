# Imports
from typing import List  # noqa: F401
from datetime import datetime
import os

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

import subprocess
@hook.subscribe.startup
def autostart():
    subprocess.call("/home/naepho/.config/qtile/autostart.sh", shell=True)

mod = "mod4"
terminal = 'sakura'

#sink = os.system("pactl list short sinks | grep RUNNING | cut -c1")

keys = [
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down in stack pane"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in stack pane"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down in current stack "),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up in current stack "),
    Key([mod, "shift"], "h", lazy.layout.swap_left(), desc="Move window left"),
    Key([mod, "shift"], "l", lazy.layout.swap_right(), desc="Move window right"),
    Key([mod], "Tab", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),
    Key([mod, "control"], "Tab", lazy.layout.client_to_next(), desc="Move window to next stack"),
    Key([mod, "shift"], "Tab", lazy.layout.rotate(), desc="Swap panes of split stack"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill window"),

    Key([mod], "c", lazy.spawn("sakura 'htop task manager' -e htop"), desc="htop"),
    Key([mod], "r", lazy.spawn("rofi-theme-selector"), desc="Rofi theme selector"),
    Key([], "F12", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    Key([mod], "F1", lazy.spawn("firefox")),
    Key([mod], "F2", lazy.spawn("notepadqq")),
    Key([mod], "F3", lazy.spawn("code")),
#    Key([mod], "F3", lazy.spawn("inskcape")),
#    Key([mod], "F4", lazy.spawn("krita")),
#    Key([mod], "F5", lazy.spawn("meld")),
#    Key([mod], "F7", lazy.spawn("virtualbox")),
    Key([mod], "F8", lazy.spawn("pcmanfm")),
#    Key([mod], "F11", lazy.spawn("firefox --private-window")),
    Key([mod], "F12", lazy.spawn("rofi -show run"), desc="rofi"),

    Key([mod, "shift"], "p", lazy.spawn("poweroff"), desc="power menu"),
    Key([mod, "shift"], "o", lazy.spawn("reboot"), desc="power menu"),

    Key(["mod1"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "x", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "x", lazy.spawn("betterlockscreen -l dim"), desc="Lock screen"),

    Key([], "Print", lazy.spawn("shutter")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
#    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 5")),
#    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 5")),
    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

]

groups = [
    Group("www"),
    Group("sys"),
    Group("dev"),
    Group("zen"),
    Group("misc"),
]

keys.extend([
    Key([mod], "ampersand", lazy.group["www"].toscreen()),
    Key([mod], "eacute", lazy.group["sys"].toscreen()),
    Key([mod], "quotedbl", lazy.group["dev"].toscreen()),
    Key([mod], "apostrophe", lazy.group["zen"].toscreen()),
    Key([mod], "parenleft", lazy.group["misc"].toscreen()),

    Key([mod, "shift"], "ampersand", lazy.window.togroup("www", switch_group=True)),
    Key([mod, "shift"], "eacute", lazy.window.togroup("sys", switch_group=True)),
    Key([mod, "shift"], "quotedbl", lazy.window.togroup("dev", switch_group=True)),
    Key([mod, "shift"], "apostrophe", lazy.window.togroup("zen", switch_group=True)),
    Key([mod, "shift"], "parenleft", lazy.window.togroup("misc", switch_group=True)),
])

colors = [
    "#050716", #0
    "#0B2EA3", #1
    "#30479E", #2
    "#6360A4", #3
    "#0337CF", #4
    "#1D55DE", #5
    "#5E67D5", #6
    "#c1afcd", #7
    "#877a8f", #8
    "#0B2EA3", #9
    "#30479E", #10
    "#6360A4", #11
    "#0337CF", #12
    "#1D55DE", #13
    "#5E67D5", #14
    "#c1afcd", #15
]

layouts = [
    layout.MonadTall(border_focus=colors[12],
                    border_normal=colors[0],
                    border_width=2,
                    margin=5,
                    single_border_width=2,
                    single_margin=5,
                    name="Monad Tall"),
    layout.Max(name="Max"),
    layout.Floating(border_focus=colors[12],
                    border_normal=colors[0],
                    border_width=2,
                    margin=0,
                    single_border_width=2,
                    single_margin=0,
                    fullscreen_border_width=2,
                    max_border_width=2,
                    name="Floating"),
    layout.RatioTile(border_focus=colors[12],
                    border_normal=colors[0],
                    border_width=2,
                    margin=5,
                    name="Ratio Tile"),
    layout.Stack(border_focus=colors[12],
                 border_normal=colors[0],
                 border_width=2,
                 margin=5,
                 num_stacks=2,
                 name="Stack"),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(highlight_method='line',
                                highlight_color=[colors[0], colors[0]],
                                active=colors[8],
                                foreground=colors[7],
                                inactive=colors[7],
                                margin=3,
                                rounded=False,
                                this_current_screen_border=colors[12],
                                this_screen_border=colors[12],
                                other_current_screen_border=colors[11],
                                other_screen_border=colors[11],
                                background=colors[0],
                                ),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.CurrentLayout(foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Prompt(foreground=colors[7], prompt='Exec: ', fmt='{} /\\/\\/\\'),
                widget.WindowName(empty_group_string='Desktop', foreground=colors[7],),
                widget.Spacer(),
                widget.Countdown(date=datetime(2022, 4, 23, 00, 00, 00), foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.ThermalSensor(foreground=colors[7], threshold=85),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Memory(format='Mem : {MemUsed}M', foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.CPU(format='CPU : {load_percent}%', foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Volume(foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Battery(format='{percent:2.0%}', foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Wlan(disconnected_message='Offline', format='{essid}', interface='wlo1', foreground=colors[7],),
                widget.Net(foreground=colors[7], format='{down} / {up}',),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Clock(format='%a %H:%M ', foreground=colors[7],),
            ],
            20,
            background=colors[0],
            opacity=0.80,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(highlight_method='line',
                                highlight_color=[colors[0], colors[0]],
                                active=colors[8],
                                foreground=colors[7],
                                inactive=colors[7],
                                margin=3,
                                rounded=False,
                                this_current_screen_border=colors[12],
                                this_screen_border=colors[12],
                                other_current_screen_border=colors[11],
                                other_screen_border=colors[11],
                                background=colors[0],
                                ),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.CurrentLayout(foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Prompt(foreground=colors[7], prompt='Exec: '),
                widget.WindowName(empty_group_string='Desktop', foreground=colors[7],),
                widget.Spacer(),
                widget.Countdown(date=datetime(2022, 4, 23, 00, 00, 00), foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.ThermalSensor(foreground=colors[7], threshold=85),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Memory(format='Mem : {MemUsed}M', foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.CPU(format='CPU : {load_percent}%', foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Volume(foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Battery(format='{percent:2.0%}', foreground=colors[7],),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Wlan(disconnected_message='Offline', format='{essid}', interface='wlo1', foreground=colors[7],),
                widget.Net(foreground=colors[7], format='{down} / {up}',),
                widget.TextBox(text="|", foreground=colors[7], fontsize=25),
                widget.Clock(format='%a %H:%M ', foreground=colors[7],),
            ],
            20,
            background=colors[0],
            opacity=0.80,
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

follow_mouse_focus = True
bring_front_click = False

loating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
