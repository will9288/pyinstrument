from __future__ import print_function
import time, sys

from pyinstrument import Profiler

# Utilities

def recurse(frames):
    if frames == 0:
        time.sleep(0.1)
        return

    recurse(frames - 1)

# Tests

def test_profiler_doesnt_overflow_on_large_call_stacks():
    profiler = Profiler()
    profiler.start()

    # give ourselves 150 frames of leeway to do our work.
    recursion_depth = sys.getrecursionlimit() - 150
    recurse(recursion_depth)

    profiler.stop()
    print(profiler.output_text())
