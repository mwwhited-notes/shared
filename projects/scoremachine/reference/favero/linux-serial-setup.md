```shell
dmesg | grep ttyUSB
ls /dev/tty*
lsusb

# https://dejanstojanovic.net/aspnet/2018/december/running-net-core-on-raspberry-pi-with-raspbian-stretch/

export SM_WEBHOST=
export SM_NETVHOST=
export SM_E810HOST=
export SM_BUSYLIGHT=
export SM_H4NPORT=/dev/ttyUSB0
export SM_HDMIPORT=/dev/ttyUSB1

# (run this as root)

export SM_WEBHOST=Disabled
export SM_NETVHOST=Disabled
export SM_E810HOST=
export SM_BUSYLIGHT=Disabled
export SM_HDMIPORT=Disabled
export SM_H4NPORT=Disabled
export SM_HDMIPORT=Disabled

export SM_WEBHOST=
export SM_NETVHOST=
export SM_E810HOST=
export SM_BUSYLIGHT=

export SM_H4NPORT=/dev/$(dmesg | grep ttyUSB | grep pl2303 | grep -oE '[^ ]+$' | tail -n 1)
export SM_HDMIPORT=/dev/$(dmesg | grep ttyUSB | grep  ch341-uart | grep -oE '[^ ]+$' | tail -n 1)

cd /home/pi/tfs/oobdev/Sandbox/OoBDev.ScoreMachine/OoBDev.ScoreMachine.Web.Core
dotnet run -v d --no-build OoBDev.ScoreMachine.Web.Core.csproj

cd /home/pi/tfs/oobdev/Sandbox/OoBDev.ScoreMachine/OoBDev.ScoreMachine.Web.Core
dotnet build -v d OoBDev.ScoreMachine.Web.Core.csproj

cd /home/pi/tfs/oobdev/Sandbox/OoBDev.ScoreMachine/OoBDev.ScoreMachine.Web.Core
dotnet build OoBDev.ScoreMachine.Web.Core.csproj

export SM_WEBHOST=Disabled
export SM_NETVHOST=Disabled
export SM_E810HOST=
export SM_BUSYLIGHT=Disabled
export SM_HDMIPORT=Disabled
export SM_H4NPORT=Disabled
export SM_HDMIPORT=Disabled
cd /home/pi/tfs/oobdev/Sandbox/OoBDev.ScoreMachine/OoBDev.ScoreMachine.Web.Core
dotnet run -v d --no-build OoBDev.ScoreMachine.Web.Core.csproj
```
