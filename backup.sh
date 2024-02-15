#!/bin/bash


# check to see is git command line installed in this machine
IS_GIT_AVAILABLE="$(git --version)"
if [[ $IS_GIT_AVAILABLE == *"version"* ]]; then
  echo "Git is Available"
else
  echo "Git is not installed"
  exit 1
fi


# copy other dot files
cp $HOME/.zshrc .
cp $HOME/.Xresources .
cp $HOME/.tmux.conf .
cp $HOME/.vimrc .
cp $HOME/.zshrc .
cp $HOME/.bashrc .
cp $HOME/.config/pavucontrol.ini .
cp $HOME/.config/picom.conf .
cp $HOME/.config/starship.toml .

# copy directories
cp -r $HOME/.local/bin .
cp -r $HOME/.tmux .
cp -r $HOME/.vifm .
cp -r $HOME/.vim .
cp -r $HOME/.w3m .
cp -r $HOME/.zsh .
cp -r $HOME/.config/dunst .
cp -r $HOME/.config/alacritty .
cp -r $HOME/.config/bytop .
cp -r $HOME/.config/broot .
cp -r $HOME/.config/copyq .
cp -r $HOME/.config/fastfetch .
cp -r $HOME/.config/fish .
cp -r $HOME/.config/foot .
cp -r $HOME/.config/flameshot .
cp -r $HOME/.config/geany .
cp -r $HOME/.config/gtk-2.0 .
cp -r $HOME/.config/gtk-3.0 .
cp -r $HOME/.config/gtk-4.0 .
cp -r $HOME/.config/htop .
cp -r $HOME/.config/hypr .
cp -r $HOME/.config/i3 .
cp -r $HOME/.config/mako .
cp -r $HOME/.config/micro .
cp -r $HOME/.config/mpv .
cp -r $HOME/.config/nitrogen .
cp -r $HOME/.config/nwg-look .
cp -r $HOME/.config/polybar .
cp -r $HOME/.config/pulse .
cp -r $HOME/.config/qbittorrent .
cp -r $HOME/.config/qpdfview .
cp -r $HOME/.config/qt5ct .
cp -r $HOME/.config/qtile .
cp -r $HOME/.config/ranger .
cp -r $HOME/.config/rofi .
cp -r $HOME/.config/sxhkd .
cp -r $HOME/.config/terminology .
cp -r $HOME/.config/vifm .
cp -r $HOME/.config/vlc .
cp -r $HOME/.config/waybar .
cp -r $HOME/.config/wezterm .
cp -r $HOME/.config/wlogout .
cp -r $HOME/.config/wofi .
cp -r $HOME/.config/xmobar .
cp -r $HOME/.config/xmonad .
cp -r $HOME/.config/ytfzf .

# Check git status
gs="$(git status | grep -i "modified")"
# echo "${gs}"

# If there is a new change
if [[ $gs == *"modified"* ]]; then
  echo "push"
fi


# push to Github
git add .;
git commit -m "New backup `date +'%Y-%m-%d %H:%M:%S'`";
git push origin main
