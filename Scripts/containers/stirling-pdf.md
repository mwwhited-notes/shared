
## Render PDF to Image Pages

```cmd
curl -X "POST" "http://127.0.0.1:8081/api/v1/convert/pdf/img" ^
    -H "accept: */*" ^
    -H "Content-Type: multipart/form-data" ^
    -F "fileInput=@%fileName%;type=application/pdf" ^
    -F "imageFormat=png" ^
    -F "singleOrMultiple=multiple" ^
    -F "pageNumbers=all" ^
    -F "colorType=greyscale" ^
    -F "dpi=300" ^
    --output "%outfileName%"
```