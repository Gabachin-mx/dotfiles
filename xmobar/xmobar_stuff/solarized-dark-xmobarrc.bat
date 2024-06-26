-- Xmobar (http://projects.haskell.org/xmobar/)
-- This is one of the xmobar configurations for DTOS.
-- This config is packaged in the DTOS repo as 'dtos-xmobar'
-- Color scheme: Solarized Dark
-- Dependencies: 
   -- otf-font-awesome 
   -- ttf-mononoki 
   -- ttf-ubuntu-font-family
   -- htop
   -- emacs
   -- pacman (Arch Linux)
   -- trayer
   -- 'dtos-local-bin' (from dtos-core-repo)

Config { font            = "xft:Ubuntu:weight=bold:pixelsize=20:antialias=true:hinting=true, Font Awesome 6 Free-Solid:style=solid: pixelsize=20, Font    Awesome 6 Brands:pixelsize=18, Font Awesome 5 Free-Solid:style=solid:pixelsize=16"
       , additionalFonts = [ "xft:Mononoki:pixelsize=11:antialias=true:hinting=true"
                           , "xft:Font Awesome 6 Free Solid:pixelsize=18"
                           , "xft:Font Awesome 6 Brands:pixelsize=18"
                           ]
       , bgColor      = "#002b36"
       , fgColor      = "#839496"
       , alpha        = 0
       , border      = NoBorder
       , borderWidth = 0
       -- Position TopSize and BottomSize take 3 arguments:
       --   an alignment parameter (L/R/C) for Left, Right or Center.
       --   an integer for the percentage width, so 100 would be 100%.
       --   an integer for the minimum pixel height for xmobar, so 24 would force a height of at least 24 pixels.
       --   NOTE: The height should be the same as the trayer (system tray) height.
       , position       = TopSize L 100 24
       , lowerOnStart = True
       , hideOnStart  = False
       , allDesktops  = True
       , persistent   = True
       , iconRoot     = ".xmonad/xpm/"  -- default: "."
        , commands = [
                        -- Echos a "penguin" icon in front of the kernel output.
--                       Run Com "echo" ["<fn=3>\xf17c</fn>"] "penguin" 3600
                        -- Get kernel version (script found in .local/bin)
--                      , Run Com ".local/bin/kernel" [] "kernel" 36000
                       -- Cpu usage in percent
--                    , Run Cpu ["-t", "<fn=2>\xf108</fn>  cpu: (<total>%)","-H","50","--high","red"] 20
                        -- Ram used number and percent
--                    , Run Memory ["-t", "<fn=2>\xf233</fn>  mem: <used>M (<usedratio>%)"] 20
                        -- Disk space free
--                    , Run DiskU [("/", "<fn=2>\xf0c7</fn>  hdd: <free> free")] [] 60
                       -- Echos up arrow in front of temperature  
                        Run Com "echo" ["<fn=2><\xf108></fn>"] "uparrow" 3600
                        
                      -- Cpu usage in percent
                      , Run Cpu ["-t", "cpu: <total>%","-H","75","--high","red"] 20
                        
                        
                       -- CPU temperature
                      ,Run Com ".local/bin/temp" [] "temp" 100

--                    ,Run Com "echo" ["<fn=2><\xf108></fn>"] "uparrow" 3600
                       -- Fan speed
                      ,Run Com ".local/bin/fan" [] "fan" 100
                        -- Echos an "up arrow" icon in front of the uptime output.
 --                   , Run Com "echo" ["<fn=2>\xf0aa</fn>"] "uparrow" 3600
 --                       -- Uptime
 --                   , Run Uptime ["-t", "uptime: <days>d <hours>h"] 360
                        -- Echos a "bell" icon in front of the pacman updates.
                    , Run Com "echo" ["<fn=2>\xf0f3</fn>"] "bell" 3600
                        -- Check for pacman updates (script found in .local/bin)
--                    , Run Com ".local/bin/pacupdate" [] "pacupdate" 36000
                        -- Echos a "battery" icon in front of the pacman updates.
                    , Run Com "echo" ["<fn=2>\xf242</fn>"] "baticon" 3600
                        -- Battery
                    , Run BatteryP ["BAT0"] ["-t", "<acstatus><watts> <left>%"] 360
                        -- Time and date
                    , Run Date "  %A, %B %d, %Y %H:%M " "date" 50
                        -- Script that dynamically adjusts xmobar padding depending on number of trayer icons.
                    , Run Com ".config/xmobar/trayer-padding-icon.sh" [] "trayerpad" 20
                        -- Prints out the left side items such as workspaces, layout, etc.
                    , Run UnsafeStdinReader
                    ]
       , sepChar = "%"
       , alignSep = "}{"
       , template = "%UnsafeStdinReader% } <fc=#da8548>%uparrow%   <fc=#da8458><action=`alacritty -e htop`>%cpu%</action></fc>   %temp%</fc><fc=#da8548>%%  %fan%</fc>  <fc=#da8548>%baticon%  %battery%</fc>{ <fc=#46d9ff><action=`emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(dt/year-calendar))'`>%date%</action></fc> %trayerpad%"
       }
