# esptool

## install esptool

```
python -m pip install esptool
```

## erase_flash

```
python -m esptool --chip esp32s3 --port COM9 --baud 921600 erase_flash
```

## write_flash

```
python -m esptool --chip esp32s3 --port COM9 --baud 921600 write_flash 0x0 BPI-Leaf-S3_MicroPython_v1.19.1-dirty.bin
```
