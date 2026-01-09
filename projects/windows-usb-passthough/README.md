
## Notes and References

* [How to install](https://github.com/dorssel/usbipd-win/tree/b0b7589d2dc4481b1af481787d6d773f46d0758a?tab=readme-ov-file#how-to-install)
* [Connect USB devices](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)
* [Pass USB device into a Docker Windows Container](https://stackoverflow.com/questions/46467295/pass-usb-device-into-a-docker-windows-container)



usbipd wsl list

usbipd wsl attach --busid <bus-id>

In the docker compose script I have:

devices:      
  - /dev/ttyUSB0:/dev/ttyUSB0