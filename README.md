# buttonboard

![ButtonBoard](/images/Button_Board_on_Wall.jpeg)

An interactive sound board that integrates lightshowpi to make LEDs dance to music.

## Install Instructions

```
git clone https://github.com/jarettrude/buttonboard.git
cd buttonboard
git submodule init
git submodule update
```

### Configure ligthshowpi

If you are running Rasbian Buster - use python3 branch.

```
cd lightshowpi
git checkout python3
```

Using the default install script wreaked havoc on my pi due to overwriting symbolic links for Python3\. Your mileage may vary. They acknowledge this in their install script:

> Note that this may (intentionally) clobber Python 3 symlinks in newer OS's

I would rather manually call python3 and define python3 environment.

Manual Override for Python3 (use in lightshowpi directory)

- First line copies a modified install script that comments out the symlink modifications.
- Second line updates all files that define the environment from python to python3.

  ```
  cp ../lightshowpiMods/install.sh install.sh
  sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|g' $(git ls-files)
  ```

Second set of modifications are to the config file that defines gpio pins and settings.

This line copies proper config file to ligthshowpi directory.

```
  cp ../lightshowpiMods/overrides.cfg ./config/overrides.cfg
```

Third customization is the python script that synchronizes the lights to sound. The default behavior is to turn off all gpio pins after a song plays. This locks us out from controlling the LEDs between button presses and songs.

The line below copies a modified synchronized_lights file to the lightshowpi directory.

```
  cp ../lightshowpiMods/synchronized_lights.py ./py/synchronized_lights.py
```
## Run the Install Script

While in the lightshowpi directory run the following to install all the dependencies needed to make the program work.
```
sudo ./install.sh
```
## Add Sound Files
Add your desired sound effects or music to their respective folders within the sounds directory. The folders are currently named in relation to the physical color of the buttons I used for this project. If you want to change them be sure to update their names in the buttonboard.py file.
```
## Final Housekeeping

Lightshowpi requires setting a defined environment for their program to operate correctly. They recommend doing this through the root user's crontab.

```
sudo crontab -e
```

Add the line below to the root user's crontab.

```
SYNCHRONIZED_LIGHTS_HOME=/home/pi/buttonboard/lightshowpi
```

While you're there, we need our project to start at system startup by adding the line below the crontab.

```
@reboot python3 /home/pi/buttonboard/buttonboard.py &
```
## Reboot System

Give the system a reboot and test all the buttons function as desired.

Enjoy!
