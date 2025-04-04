Favero
    
    To read the serial data from the Full-Arm-05 is a bit complicated as the FA-05 uses a "20mA current loop" port and you will need an interface fron current loop to Rs232 or Rs422, to be able to read it from a PC. Furthermore you will need to develop a software to read the protocol. 
    
    Below, in blue color, is the protocol that the FA-05 uses. 
    
    If you are an electronic technician, please see also the attached draft, where you can see the output circuit of the FA-05. 
    
    Best Regards,   Gino Favero
    FAVERO ELECTRONIC DESIGN 
    via R.Lombardi 64 - 31030 Arcade TV - ITALY 
    Tel.+39 0422 874140   fax +39 0422 874141 
    www.favero.com   SkypeName: favero_electronic 
    
    
    Here are the information regarding the serial data of our Full-Arm-05 apparatus.
     Serial type: 2400-N-8-1
    
     The apparatuses send out continuously a string of 10 bytes.  The string is
    repeated every about 42msec.
     Here is what every byte of the string contains:
    
     1° byte: FFh  = Start string
              The FFh value identifies the beginning of the string.
    
     2° byte: XXh  = Right score
              Ex.: if =06h , the right score is 6
    
     3° byte: XXh  = Left score
              Ex.: if =12h, the left score is 12
    
     4° byte: XXh  = Seconds of the time (units and tens)
              Ex.: if =56h , the seconds of the time = 56.
    
     5° byte: 0Xh  = Minutes of the time (only units)
              Ex.: if =02h , the minutes of the time = 2.
    
     6° byte: XXh  = Define the state of the lamps (red, green, whites and
    yellows).  Every bit defines the state of a lamp (zero=OFF, 1=ON).
     Following is the correspondence of the 8 bits:
              Bit D0 = Left white lamp
              Bit D1 = Right white lamp
              Bit D2 = RED lamp (left)
              Bit D3 = GREEN lamp (right)
              Bit D4 = Right yellow lamp
              Bit D5 = Left yellow lamp
              Bit D6 = 0   not used
              Bit D7 = 0   not used
           Example: if byte 6° = 14h , we have D2=1 (red light=on) and D4=1
    (right yellow light=on)
    
     7° byte: 0Xh  = Number of matches and Priorite signals.
           The D0 e D1 bits define the number of matches (from 0 to 3):
              D1=0 D0=0  Num.Matchs = 0
              D1=0 D0=1  Num.Matchs = 1
              D1=1 D0=0  Num.Matchs = 2
              D1=1 D0=1  Num.Matchs = 3
           The D2 e D3 bits define the signals of Priorite:
              D2 = Right Priorite (if=1 is ON)
              D3 = Left Priorite (if=1 is ON)
         Example: if byte 7° =0Ah (D0=0, D1=1, D2=0 D3=1) , the number of
    Matchs is =2 and the Left Priorite lamp is ON.
    
     8° byte: XXh  This byte is only for our use. Do not consider this byte.
    Its value is always different from FFh.
    
     9° byte:  Red and Yellow penalty cards.
           The 4 bits D0, D1, D2, e D3 are used on the following way:
              D0 = Right RED penalty card
              D1 = Left RED penalty card
              D2 = Right YELLOW penalty card
              D3 = Left YELLOW penalty card
           Do not consider the bit D4 and D5 which can be at zero or 1, instead
    the bit D6 and D7 are always =0.
          Example: if byte 8° = 38h , we have D3=1 and so the left yellow
    penalty card is ON.
    
     10° byte:  CRC , it is the sum without carry of the 9 previous bytes.
    
     As example, the string could be:
     FFh, 06h, 12h, 56h, 02h, 14h, 0Ah, 00h, 38h, 56h
     which will display:
     Right score = 6
     Left score = 12
     Time = 2:56
     The Lamps ON are: Red, Yellow right, Left priorite.
     Number of Matchs = 2
     Left yellow penalty lamp = ON. 
