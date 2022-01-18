#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 15, 2022
# This program prints different RGB color codes
# to the console using nested loops.

def main():
  # initialize the colors
  red = 0
  green = 0
  blue = 0

  # display opening message
  print("Here are RGB color variations up to 50:")
  print("")

  # determine the different color codes and display the 
  # results to the console
  for blue in range(0,51,1):
    print("RGB ({}, {}, {})".format(red, green, blue))
    if blue == 50:
      print("")
      for green in range(0,51,1):
        blue = 0
        print("RGB ({}, {}, {})".format(red, green, blue))
        if green == 50:
          print("")
          for red in range(1,51,1):
             green = 0
             print("RGB ({}, {}, {})".format(red, green, blue))

    
if __name__ == "__main__":
    main()

