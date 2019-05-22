#!/usr/bin/env python3.7

import imageflasher
import configparser

import argparse

def main(config, device, chip=""):
    # First parse the config
    images = configparser.get_images(config.read())
    flasher = imageflasher.ImageFlasher(chip))
    if device != False: # We have to check not False rather than just True, because None evaluates to False, and None should be passed intact
        flasher.connect_device(device)
    for addr, fil in images:
        flasher.download_from_disk(os.path.join(os.path.join(os.path.dirname(config.path), fil.replace("/", os.path.sep)), addr)
    print("Flash successful!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(epilog="""Copyright 2019 Penn Mackintosh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.""")
    parser.add_argument("--norun", "-n", action="store_false", dest="run")
    parser.add_argument("--device", "-d")
    parser.add_argument("config", type=argparse.FileType("rb"))
    args = parser.parse_args()
    main(args.config.read(), main.device if main.run else False)