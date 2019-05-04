# Avatar Generator
- Generates random pixelated avatar images for you
- Inspired by [this article](https://medium.freecodecamp.org/how-to-create-generative-art-in-less-than-100-lines-of-code-d37f379859f)

![img1](img_1556964797.png)
![img2](img_1556964802.png)

## Usage
Compatible for python3
- Install requirements: `pip install Pillow`
- Run in your command line: `python run.py`

Additional arguments:
```
python3 run.py -w 100 -p 10 -c 3 -cc '(255,0,0)' '(0,255,0)'
```
```
optional arguments:
-h, --help                show help 
-c, --num_colors          number of colors in avatar 
                          to generate (excluding 
                          corporate color if any)
-w,  --width              width of avatar to generate
-p, --num_pixels          number of pixels of avatar
-cc, --corporate_colors   color(s) to be included (in rgb tuple)
```

## Run Test
```
python test.py
```

### Todo
- [ ] Create simple api for this? 
- [ ] Create circular avatars