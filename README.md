# Donkeycar: A Python Self Driving Library
```
   __  ___     _                   __    ______        __             __          _       
  /  |/  /_ __(_)__ _  _____ ___  / /_  /_  __/__ ____/ /  ___  ___  / /__  ___ _(_)__ ___
 / /|_/ / // / / _ \ |/ / -_) _ \/ __/   / / / -_) __/ _ \/ _ \/ _ \/ / _ \/ _ `/ / -_|_-<
/_/  /_/\_, /_/_//_/___/\__/_//_/\__/   /_/  \__/\__/_//_/_//_/\___/_/\___/\_, /_/\__/___/
       /___/                                                              /___/           
ai.iot.cloud.technology.training.trading =================================================

Ts. Mohamad Ariffin Zulkifli
ariffin@myduino.com
```
[Donkeycar](https://github.com/autorope/donkeycar) is minimalist and modular self driving library for Python. It is developed for hobbyists and students with a focus on allowing fast experimentation and easy community contributions.

Big salute and thank you to all Donkeycar [![contributors](https://img.shields.io/github/contributors/autorope/donkeycar)](#contributors-)

You can access Donkeycar updates & examples from their website [http://donkeycar.com](http://donkeycar.com) or [build instructions and software documentation](http://docs.donkeycar.com) as well as [community chat on Discord](https://discord.gg/PN6kFeA).

This repo is a fork from [Donkeycar](https://github.com/autorope/donkeycar) and modified to be use with [Waveshare PiRacer AI Kit](https://www.waveshare.com/piracer-ai-kit.htm) and works with the latest [Raspberry Pi OS Bookworm](https://www.raspberrypi.com/news/bookworm-the-new-version-of-raspberry-pi-os/) 👍

## PiRacer AI Kit

<p align="center"><a href="https://www.waveshare.com/wiki/PiRacer_AI_Kit"><img src="https://www.waveshare.com/w/A6Y79bcq/Kdy80nYY.php?f=PiRacer-AI-Kit-1.jpg&width=800" width="400"></a></p>

PiRacer AI Kit featuring its Expansion Board comes with 3x battery holder of 18650 batteries with on-board lithium battery protection circuit with anti-overcharge, anti-over-discharge, anti-over-current short-circuit protection functions and voltage regulator chip to provide stable 5V to the Raspberry Pi.

The expansion board also comes with 2 units of [PCA9685](https://www.nxp.com/products/power-management/lighting-driver-and-controller-ics/led-controllers/16-channel-12-bit-pwm-fm-plus-ic-bus-led-controller:PCA9685) 16-channel PWM controller interfaced to:
1. [TB6612FNG](https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TB6612FNG-C-8-EL/1730070) 1.2A Dual Motor Driver to control the DC Motors with I2C Address: `0x60`.
2. Servo Motor with I2C Address: `0x40`.

The expansion board also comes with on-board 0.91" 128×32 resolution OLED and [INA219](https://www.ti.com/product/INA219) a bidirectional current/power monitor with I2C Address: `0x41`.

## Hardware Requirements

I recommend to use Raspberry Pi 4 with at least 4GB of RAM and MicroSD card > 64GB.

## Raspberry Pi OS Setup
1. Run the following command to update the package lists:
```bash
sudo apt update --allow-releaseinfo-change
```

2. Upgrade installed packages to the latest versions:
```bash
sudo apt upgrade
```

3. Configure `VNC` and `I2C`. Use the `raspi-config` tool to enable both VNC and I2C. This tool provides an interactive menu for configuring various settings on your Raspberry Pi:
```bash
sudo raspi-config
```

4. Verify if I2C is enabled and detect devices on the I2C bus, by using the following command:
```bash
sudo i2cdetect -y 1
```

## Setup Python Virtual Environment
1. Create a virtual environment named `piracer` with system site packages:
```bash
python -m venv piracer --system-site-packages
```

2. Append the following line to your `.bashrc` file to automatically activate the virtual environment when you open the Terminal:
```bash
echo "source ~/piracer/bin/activate" >> ~/.bashrc
```

3. Apply the changes to your current Terminal session, run:
```bash
source ~/.bashrc
```

## Install Donkeycar Python Code
1. Clone the Donkeycar repository from the provided URL:
```bash
git clone https://github.com/ariffinzulkifli/donkeycar
```

2. Change your current directory to the Donkeycar directory:
```bash
cd donkeycar
```

3. If you want to work with the "main" branch, you can check it out using this command:
```bash
git checkout main
```

4. Use the following command to install Donkeycar's dependencies for the Raspberry Pi:
```bash
pip install -e .[pi]
```

5. Verify the installed TensorFlow version by running the following command:
```bash
python -c "import tensorflow; print(tensorflow.__version__)"
```

## Install OpenCV

1. Install the OpenCV Python package with the following command:
```bash
pip install opencv-python
```

2. You can install the OpenCV-contrib Python package if needed:
```bash
pip install opencv-contrib-python
```

3. Verify the installed OpenCV version by running the following command:
```bash
python -c "import cv2; print(cv2.__version__)"
```

## Create Donkeycar

1. Use the `donkey createcar` command to create a Donkeycar project. Replace `~/mycar` with the desired path for your project:
```bash
donkey createcar --path ~/mycar
```

## Let's Drive Your Car

1. Change your current directory to the Donkeycar project directory:
```bash
cd ~/mycar
```

2. Run the following command to start driving your car using Donkeycar:
```bash
python manage.py drive
```
Optionally add `--js` prefix at the end of the command to control the Donkeycar with joystick.
```bash
python manage.py drive --js
```

3. Control your car from your PC's web browser at the URL:
*Note*: change the car-hostname with your Raspberry Pi hostname or IP address.
```
car-hostname.local:8887
```

For example:
```
http://piracer-10.local:8887
```