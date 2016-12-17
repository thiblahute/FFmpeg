#!/usr/bin/env python3

import os
import subprocess
import shutil
import sys

print(' '.join(sys.argv))
subprocess.check_call(['make', '-C', sys.argv[1]])
for i, f in enumerate(['libavformat/libavformat.a', 'libavcodec/libavcodec.a',
            'libavfilter/libavfilter.a', 'libswresample/libswresample.a',
          'libavutil/libavutil.a']):
    shutil.copy(os.path.join(sys.argv[1], f), os.path.join(sys.argv[i + 2]))
