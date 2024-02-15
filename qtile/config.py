from libqtile import bar, layout, widget,qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.command.client import Client

from typing import List  # noqa: F401

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
alt = "mod1"
terminal = guess_terminal()
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
	#Keys for apps
	Key([mod, alt], "2",        lazy.spawn("alacritty")),
    Key([mod, alt], "1",        lazy.spawn("google-chrome-stable")),
    Key([mod, alt], "3",        lazy.spawn("thunar")),
    Key([mod, alt], "d",        lazy.spawn("rofi -show drun -dpi 1")),
    Key([mod, alt], "7",        lazy.spawn("vlc")),
    Key([mod, alt], "5",        lazy.spawn("transmission-gtk")),
    Key([mod, alt], "6",        lazy.spawn("blueman-manager")),
    Key([mod, alt], "8",        lazy.spawn("okular")),
#	Key([mod, alt], "9",        lazy.spawn("Zathura")),
	Key([mod, alt], "4",        lazy.spawn("catfish")),


# == floating and maximise
    Key([mod], "t", lazy.window.toggle_floating()),
    Key([mod, "shift"], "m", lazy.window.toggle_maximize()),

    # == opacity control
    Key([mod], "o", lazy.window.down_opacity()),
    Key([mod, "shift"], "o", lazy.window.up_opacity()),
    Key([mod, "control"], "o", lazy.window.opacity(.3)),
    Key([mod, "shift", "control"], "o", lazy.window.opacity(1)),

    # Keys for special events
#    Key([mod], "l",            lazy.spawn("xscreensaver-command -lock")),
#    Key([], "XF86AudioRaiseVolume",        lazy.spawn("amixer -c 0 -q set Master 2dB+")),
#    Key([], "XF86AudioLowerVolume",        lazy.spawn("amixer -c 0 -q set Master 2dB-")),
#    Key([], "XF86AudioMute",        lazy.spawn("amixer -c 0 -q set Master toggle")),

#Increase or decrease brightness
#	Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +2%")),
#    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 2%-")),

# Increase or decrease brightness and send notification

    Key([], "XF86MonBrightnessUp", lazy.spawn("/home/paul/.config/qtile/scripts/brightup.sh")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("/home/paul/.config/qtile/scripts/brightdown.sh")),


#Incease or decrease volume
#    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
#    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
	Key([], "XF86AudioMute",        lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle")),

#increase or decrease volume and send notification

    Key([], "XF86AudioRaiseVolume",lazy.spawn("/home/paul/.config/qtile/scripts/volup.sh")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("/home/paul/.config/qtile/scripts/voldown.sh")),

#Poweroff script
    Key([mod, alt], "p", lazy.spawn("/home/paul/.config/qtile/scripts/logout.sh")),

#add key command for scratchpad
	Key([mod], "space", lazy.group["scratchpad"].dropdown_toggle("term")),

]
        
# group_names = [("", {'layout': 'max', 'matches':[Match(wm_class=["google-chrome"])]}),
               # ("", {'layout': 'Bsp'}),
               # ("", {'layout': 'treetab', 'matches':[Match(wm_class=["thunar"])]}),
               # ("", {'layout': 'treetab', 'matches':[Match(wm_class=["catfish"])]}),
               # ("", {'layout': 'columns', 'matches':[Match(wm_class=["transmission-gtk"])]}),
               # ("", {'layout': 'columns', 'matches':[Match(wm_class=["blueman-manager"])]}),
               # ("", {'layout': 'floating', 'matches':[Match(wm_class=["vlc"])]}),
               # ("", {'layout': 'columns'}),
               # ("9", {'layout': 'columns'})]

group_names = [("www", {'layout': 'max', 'matches':[Match(wm_class=["google-chrome"])]}),
               ("alacritty", {'layout': 'Bsp'}),
               ("thunar", {'layout': 'treetab', 'matches':[Match(wm_class=["thunar"])]}),
               ("catfish", {'layout': 'treetab', 'matches':[Match(wm_class=["catfish"])]}),
               ("transmission", {'layout': 'columns', 'matches':[Match(wm_class=["transmission-gtk"])]}),
               ("bluetooth", {'layout': 'columns', 'matches':[Match(wm_class=["blueman-manager"])]}),
               ("vlc", {'layout': 'floating', 'matches':[Match(wm_class=["vlc"])]}),
               ("", {'layout': 'columns'}),
               ("9", {'layout': 'columns'})]


groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen(toggle=True)))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(
        name, switch_group=True)))  # Send current window to another group 

#Append Scratchpad to Groups list
groups.append(
	ScratchPad("scratchpad", [
#define a terminal
	DropDown("term", "alacritty", opacity=0.8, height=0.5, width=0.00),
	]),
)

layouts = [
      layout.Bsp(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin = 8),  
      layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin = 8),
      layout.Max(),
    # Try more layouts by unleashing below layouts.
 	  layout.Stack(num_stacks=2),
      #layout.Bsp(),
      layout.Matrix(),
      layout.MonadTall(),
      layout.MonadWide(),
      layout.RatioTile(),
      layout.Tile(),
      layout.TreeTab(),
      layout.VerticalTile(),
      layout.Zoomy(),
      layout.Floating()
]

#Use these colors in the widgets
colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize = 10,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/python-white.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)}
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 9,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
             widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 5
                       ),
             widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
             widget.Net(
                       interface = "enp6s0",
                       format = 'Net: {down} ↓↑ {up}',
                       foreground = colors[3],
                       background = colors[0],
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[3],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.ThermalSensor(
                       foreground = colors[4],
                       background = colors[0],
                       threshold = 90,
                       fmt = 'Temp: {}',
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[4],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "Updates: {updates} ",
                       foreground = colors[5],
                       colour_have_updates = colors[5],
                       colour_no_updates = colors[5],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       padding = 5,
                       background = colors[0],
                       decorations=[
                           BorderDecoration(
                               colour = colors[5],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.Memory(
                       foreground = colors[9],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       fmt = 'Mem: {}',
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),

              widget.Volume(
                       foreground = colors[7],
                       background = colors[0],
                       fmt = 'Vol: {}',
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[7],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),


              widget.KeyboardLayout(
                       foreground = colors[8],
                       background = colors[0],
                       fmt = 'Keyboard: {}',
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[8],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.AnalogueClock(
                       background = colors[0],
                       face_shape = "square",
                       face_background = colors[6],
                       face_border_colour = colors[6],
                       face_border_width = 4,
                       padding = 5
                       ),
              widget.Clock(
                       foreground = colors[6],
                       background = colors[0],
                       format = "%A, %B %d - %H:%M ",
                       decorations=[
                           BorderDecoration(
                               colour = colors[6],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],

                       ),

              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[9:10]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
