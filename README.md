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

This repo is a fork from [Donkeycar](https://github.com/autorope/donkeycar) and modified to be use with [Waveshare PiRacer](https://www.waveshare.com/piracer-ai-kit.htm). PiRacer is using 2 PCA9685 to:
1. Control servo for steering wheel. I2C Address: `0x40`
2. Control TB6612FNG Motor Driver for motor throttle. I2C Address: `0x60`