# buttonboard

An interactive sound board that integrates lightshowpi to make LED dance to music.

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
- Third line copies a custom config file for ligthshowpi to config directory.
- Fourth line copies a modified synchronized_lights.py file to lightshowpi's py directory.

  ```
  cp ../lightshowpiMods/install.sh install.sh
  sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|g' $(git ls-files)
  cp ../lightshowpiMods/overrides.cfg ./config/overrides.cfg
  cp ../lightshowpiMods/synchronized_lights.py ./py/synchronized_lights.py
  ```

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
