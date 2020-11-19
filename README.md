# Using This repository

First of all, *watch* and *star* this repository for all important releases. You can find those at the very top right of this page

## If you are familiar with Github:
Clone this repository as you regularly would and pull when updates are pushed to this repository to keep everything up to date.

## If you are unfamiliar with Github:
Simply click the green "code" at the top right of the file list and download as a zip file.

Extract the zip to a location of your choosing. Upon updates, the .hex file will need to be replaced with the latest manually to avoid uploading an old version

# Binaries

Firmware for the 3rd Wave Labs Controllino controller comes in the form of a .hex binary file.

## Uploading the binary HEX file

Included within this repository is Xloader which is a third party program that is is used to upload binary HEX files to the controller.

Below are the steps to using Xloader:

### Using XLoader
Xloader has 4 main input fields: Hex file, Device, COM port, and Baud rate

![](https://i.imgur.com/C8yEg6S.jpeg)

Plug in the controller to the computer using the usb port on the controller.

Open the *XLoader.exe* within the XLoader folder

1. Set the *Hex file* feild to the location of the provided **.hex** binary
2. Set the *Device* to: **Mega(ATMEGA2560)**
3. Set the *COM port* to the appropriate device. Should be listed in the drop down menu as COM followed by a number. 
4. Set the *Baud Rate* field to: **115200**
5. Click upload

# Data Logging

## Using serial plot

Under the [Serial Plot](https://github.com/wcschroe/Prismatic_4x_Binaries/tree/master/Serial%20Plot) folder you will find everything you need to install and use serial plot.

### Installation

Install serial plot using the [serialplot-0.11.0-win32.exe](https://github.com/wcschroe/Prismatic_4x_Binaries/blob/master/Serial%20Plot/serialplot-0.11.0-win32.exe)

### Setup and Use

After installing Serial Plot, load the proper settings from [Prismatic_logging_config.ini](https://github.com/wcschroe/Prismatic_4x_Binaries/blob/master/Serial%20Plot/Prismatic_logging_config.ini)

![](https://i.imgur.com/WZUkBJS.png)

![](https://i.imgur.com/QX3nE9o.png)

After loading the settings file, you should see the correctly labeled fields under the plot tab at the bottom and at the bottom right of the plot window.

Connect your pc to the USB port on the front of the control box and from the HMI enable serial streaming

Select the listing with the name containing **arduino** and click *open*
If you don't see it listed, click the refresh button next to open.

![](https://i.imgur.com/wPrhj6v.png)

Upon connecting, you will hear the controller restart. This is normal behavior. After a few seconds the data will start showing in the plot window.

# RS485 USB Dongle Driver (CH340)

### [Driver](https://github.com/wcschroe/Prismatic_4x_Binaries/tree/master/CH340)

Install this driver to be able to interface with our controller using the [minimalmobus](https://pypi.org/project/minimalmodbus/) python library.

### [Example Python Interface Script](https://github.com/wcschroe/Prismatic_4x_Binaries/tree/master/Python/external.py)