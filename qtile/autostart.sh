#! /bin/bash

# If the process doesn't exists, start one in background
run() {
	if ! pgrep $1 ; then
		$@ &
	fi
}

# Just as the above, but if the process exists, restart it
run-or-restart() {
	if ! pgrep $1 ; then
		$@ &
	else
		process-restart $@
	fi
}

# Graphical authentication agent
run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1

#run trayer							# Start system tray

run xset b on 						# Disable beep

run nitrogen --restore 				# Wallpaper
#run feh --no-fehbg --bg-scale ~/Backgrounds/mist.jpg
#run sxhkd							# Simple X HKey daemon
run dunst							# Notification daemon
#run picom							# Compositor
run picom -b --experimental-backends --backend glx

#run volumeicon 						# Volume icon
run nm-applet 						# NetworkManager icon
#run polybar

#run cbatticon						# Battery icon and command
run xscreensaver -no-splash			# Power management

#set volume to 30%
run amixer sset 'Master' 30%

#run startup sound
#run mpv --no-video ~/.config/qtile/who.mp3  
run mpv --no-video ~/.config/qtile/startup-01.mp3 

