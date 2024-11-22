from glob import glob
import os 

gifs = glob('*.gif')
for gif in gifs:
    if '11586' in gif:
        os.system(f'gifsicle -O3 {gif} --colors 256 -o {gif}')
        # os.system(f'gifsicle --scale 0.5 {gif} -o {gif}')