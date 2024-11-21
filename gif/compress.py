from glob import glob
import os 

gifs = glob('*.gif')
for gif in gifs:
    os.system(f'gifsicle -O3 {gif} --colors 256 -o {gif}')