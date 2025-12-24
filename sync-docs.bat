pushd .\AnalogComputers\analog-computing-repository
call sync-docs.bat
popd

pushd "Expansion Boards"
call sync-docs.bat
popd

pushd "Programmable Devices"
call sync-docs.bat
popd