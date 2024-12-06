# HID USB Decoding

## Summary

This is a guide on how you can decode existing USB devices and protocols.  

## Wireshark with USBPcap

Wireshark makes it possible to trace and capture raw data from USB Devices

### Useful filters

| Use                    | Filter                  |
| :--------------------- | :-----------------------|
| Vendor ID              | usb.idVendor = 0x04d8   |
| Product ID             | usb.idProduct           |
| Source                 | usb.src == "1.11.1"     |
| Destination            | usb.dst == "1.11.1"     |
| Data Length            | usb.data_len > 0        |
| Source or Destiniation | usb.addr matches "^1.4  |

### Hints

If you find know the Vendor/Product ID you can filter in wiresharp like 

```filter
usb.idVendor = 0x04d8
```

After that filter you can look at the source/destination `ie. 1.10.0` and set your filter similar to below to see the data being exchanged

```filter
usb.addr matches "^1.10" && usb.data_len > 0
```

this will return all traffic with content while exclusing the HID control events.

### Fuzzy matching (regex)

partial match on strings with regular expressions

```filter
usb.src matches "^1.11" || usb.dst matches "^1.11"
```

matching on partial data *00ff000000ffff000000*

```filter
usbhid.data[:3] == 00:ff:00
```

[More examples](https://wiki.wireshark.org/DisplayFilters)

## HidSharp



