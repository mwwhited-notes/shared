
```shell
curl -T DM3058-User-Guide.pdf http://127.0.0.1:9999/tika --header "X-Tika-PDFOcrStrategy: ocr_only" > DM3058-User-Guide.txt
```

```shell
curl -T text-and-images.pdf http://127.0.0.1:9999/tika --header "X-Tika-PDFOcrStrategy: ocr_only" --header "X-Tika-OCROutputType: hocr" > text-and-images.xml
```

curl -v -X PUT \
     --data-binary @file.pdf \
     -H "Content-Type: application/pdf" \
     -H "X-Tika-PDFOcrStrategy: ocr_only" \
     -H "X-Tika-OCROutputType: hocr" \
     "http://tika-server:8081/tika"


- https://cwiki.apache.org/confluence/display/TIKA/TikaServer#TikaServer-UnpackResource
  
```
curl -T text-and-images.pdf http://localhost:9999/unpack  --header "X-Tika-PDFExtractInlineImages: true" > test.zip
```

curl -T text-and-images.pdf http://127.0.0.1:9999/tika --header "X-Tika-PDFOcrStrategy: ocr_only" --header "X-Tika-OCROutputType: hocr" --header "X-Extract-Embedded: true" > text-and-images.xml