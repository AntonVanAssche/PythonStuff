#!/usr/bin/env python3

import random as r
import webbrowser as wb
    
links = [
   'https://youtu.be/dQw4w9WgXcQ',
   'https://youtu.be/Cj8n4MfhjUc',
   'https://youtu.be/Mg02NzsXrJk',
   'https://youtu.be/kK7uljnAmQI',
   'https://youtu.be/vTIIMJ9tUc8',
   'https://youtu.be/o_LrHt4Hhhs',
   'https://youtu.be/EKgGSf-xTMg',
   'https://youtu.be/St32aLCNMmQ',
   'https://youtu.be/0FmzeEcuEos',
   'https://youtu.be/feA64wXhbjo',
   'https://youtu.be/3ejAMB3g_b8',
   'https://youtu.be/e8jR-t9axFI',
   'https://youtu.be/n2bKLqUKb9w',
   'https://youtu.be/7yh9i0PAjck',
   'https://youtu.be/6xUnSVTh8fI',
   'https://youtu.be/VJe6LLoGgR8',
   'https://youtu.be/g3jCAyPai2Y',
   'https://youtu.be/Hy8kmNEo1i8',
   'https://youtu.be/MtN1YnoL46Q',
   'https://youtu.be/iuJDhFRDx9M',
   'https://youtu.be/J-fXTRHApRc',
   'https://youtu.be/3Q8TSrDFG6w',
   'https://youtu.be/G-T3qKl6y-c',
   'https://youtu.be/rR9qUm_WEfg',
   'https://youtu.be/IjOkC-YYNJo',
   'https://youtu.be/kq5chqQfI9I'
   ]

if __name__ == '__main__':
   # Increasing the second number will potentialy open more
   # windows, thus increasing the risk of your pc crashing
   # due to memory issues.
   randInt = r.randint(1,20)
   randLink = r.choice (links)

   for _ in range(randInt):
      wb.open_new(randLink)
