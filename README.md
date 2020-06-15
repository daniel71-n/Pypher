# Pypher
A Caesar Cipher encoder in Python3


```
usage: 
     pypher [options]
            (-e|-d) (-l|-r) -n=N -i=INPUT [-o=FILE]
            -h,--help

Pypher : a substitution cipher implementation
      Encode (-e) or decode(-d) text by shifting        
      characters a specified number of positions(-n N)  
      in a specified direction(-l|-r)                   

Get help:
  -h, --help            show this help message and exit

Options:
  -e, --encode          encode some text
  -d, --decode          decode some text
  -l, --left            shift characters to the left
  -r, --right           shift characters to the right
  -n N, --number N      shift each character N characters to the left or to the right, as set by the -l or -r switches
  -i INPUT, --input-from INPUT
                        read text to encode/decode from INPUT, which can be either a string or a filename
  -o FILE, --output-to FILE
                        [OPTIONAL] redirect the result to FILE, else to stdout if omitted

```



**Example:**

 python pypher -e -r -n3 -i "somefile"
```
   ........................................
   |ENCODED using a RIGHT shift of ---3---|
   ........................................
       |  ‘Erxqghueb,’ vdlg Pu. Judgjulqg, gudzlqj d fkdlu wr wkh iluhvlgh, ‘brx duh dozdbv vr        |
       |  lqwhuhvwhg lq pb brxqj shrsoh—sduwlfxoduob lq Orxlvd—wkdw L pdnh qr dsrorjb iru vdblqj      |
       |  wr brx, L dp yhub pxfk yhahg eb wklv glvfryhub.  L kdyh vbvwhpdwlfdoob ghyrwhg pbvhoi       |
       |  (dv brx nqrz) wr wkh hgxfdwlrq ri wkh uhdvrq ri pb idplob.  Wkh uhdvrq lv (dv brx nqrz)     |
       |  wkh rqob idfxowb wr zklfk hgxfdwlrq vkrxog eh dgguhvvhg.  ‘Dqg bhw, Erxqghueb, lw zrxog     |
       |  dsshdu iurp wklv xqhashfwhg flufxpvwdqfh ri wr-gdb, wkrxjk lq lwvhoi d wuliolqj rqh, dv     |
       |  li vrphwklqj kdg fuhsw lqwr Wkrpdv’v dqg Orxlvd’v plqgv zklfk lv—ru udwkhu, zklfk lv        |
       |  qrw—L grq’w nqrz wkdw L fdq hasuhvv pbvhoi ehwwhu wkdq eb vdblqj—zklfk kdv qhyhu ehhq       |
       |  lqwhqghg wr eh ghyhorshg, dqg lq zklfk wkhlu uhdvrq kdv qr sduw.’                           |
       |                                                                                              |
       |  ‘Wkhuh fhuwdlqob lv qr uhdvrq lq orrnlqj zlwk lqwhuhvw dw d sdufho ri ydjderqgv,’           |
       |  uhwxuqhg Erxqghueb.  ‘Zkhq L zdv d ydjderqg pbvhoi, qrergb orrnhg zlwk dqb lqwhuhvw dw      |
       |  ph; L nqrz wkdw.’                                                                           |
       |                                                                                              |
       |  ‘Wkhq frphv wkh txhvwlrq; vdlg wkh hplqhqwob sudfwlfdo idwkhu, zlwk klv hbhv rq wkh         |
       |  iluh, ‘lq zkdw kdv wklv yxojdu fxulrvlwb lwv ulvh?’                                         |
       |                                                                                              |
       |  ‘L’oo whoo brx lq zkdw.  Lq lgoh lpdjlqdwlrq.’                                              |
       |                                                                                              |
       |  ‘L krsh qrw,’ vdlg wkh hplqhqwob sudfwlfdo; ‘L frqihvv, krzhyhu, wkdw wkh plvjlylqj kdv     |
       |  furvvhg ph rq pb zdb krph.’                                                                 |
       |                                                                                              |
       |                                                                                              |
       |______________________________________________________________________________________________|
```
The text above is from 'Hard Times' By CHARLES DICKENS (from Project Gutenberg).


