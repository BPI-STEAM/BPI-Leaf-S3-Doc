# How to flash

## install esptool

```
python -m pip install esptool
```

## erase_flash

```
python -m esptool --chip esp32s3 --port COM1 --baud 460800 erase_flash
```

## write_flash

```
python -m esptool --chip esp32s3 --port COM1 --baud 460800 --before=usb_reset --after=no_reset write_flash 0x0 BPI-Leaf-S3_MicroPython_v1.20.0_3229791.bin
```
