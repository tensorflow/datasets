Files in this directory have been created manually.
They exhibit the following properties seen on original dataset:

 - a: notch
   1. none
   2. triangle
   3. round
   4. rectangle
 - b: contrast
   1. high
   2. low
 - c: crop
   1. larger than retina circle
   2. just around the retina circle
   3. smaller than retina circle

Common properties:

 - notch is always on the top right side
 - retina (circle) is about centered on the picture

So we have the following mix of images:
 - a1, b1, c1: 1_left.jpeg  -> sample
 - a1, b1, c2: 1_right.jpeg -> sample
 - a1, b1, c3: 2_left.jpeg
 - a1, b2, c1: 2_right.jpeg
 - a1, b2, c2: 3_left.jpeg
 - a1, b2, c3: 3_right.jpeg

 - a2, b1, c1: 4_left.jpeg
 - a2, b1, c2: 4_right.jpeg
 - a2, b1, c3: 5_left.jpeg -> sample
 - a2, b2, c1: 5_right.jpeg -> sample
 - a2, b2, c2: 6_left.jpeg
 - a2, b2, c3: 6_right.jpeg

 - a3, b1, c1: 7_left.jpeg
 - a3, b1, c2: 7_right.jpeg
 - a3, b1, c3: 8_left.jpeg
 - a3, b2, c1: 8_right.jpeg
 - a3, b2, c2: 9_left.jpeg
 - a3, b2, c3: 9_right.jpeg

 - a4, b1, c1: 10_left.jpeg
 - a4, b1, c2: 10_right.jpeg
 - a4, b1, c3: 11_left.jpeg
 - a4, b2, c1: 11_right.jpeg
 - a4, b2, c2: 12_left.jpeg
 - a4, b2, c3: 12_right.jpeg

There are 4 pictures in `sample` split (marked above).
Pictures with an even ID are in the `train` split, those with ID {1, 3, 5} are
in the `validation` split, and those with ID {7, 9, 11} are in the `test` split.
