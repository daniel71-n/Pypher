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

pypher -e -r -n3 -i "somefile"
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
The text above is from 'Hard Times' By CHARLES DICKENS (from Project Gutenberg). Original (read from 'somefile'):
```
‘Bounderby,’ said Mr. Gradgrind, drawing a chair to the fireside, ‘you are always so interested in my young people—particularly in Louisa—that I make no apology for saying to you, I am very much vexed by this discovery.  I have systematically devoted myself (as you know) to the education of the reason of my family.  The reason is (as you know) the only faculty to which education should be addressed.  ‘And yet, Bounderby, it would appear from this unexpected circumstance of to-day, though in itself a trifling one, as if something had crept into Thomas’s and Louisa’s minds which is—or rather, which is not—I don’t know that I can express myself better than by saying—which has never been intended to be developed, and in which their reason has no part.’

‘There certainly is no reason in looking with interest at a parcel of vagabonds,’ returned Bounderby.  ‘When I was a vagabond myself, nobody looked with any interest at me; I know that.’

‘Then comes the question; said the eminently practical father, with his eyes on the fire, ‘in what has this vulgar curiosity its rise?’

‘I’ll tell you in what.  In idle imagination.’

‘I hope not,’ said the eminently practical; ‘I confess, however, that the misgiving has crossed me on my way home.’

```


