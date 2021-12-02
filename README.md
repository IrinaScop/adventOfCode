# adventOfCode

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels: https://adventofcode.com/. 

The days folders represent each day of the calendar.
<hr>
<h3> DAY1</h3>

<p><b>ex1.</b>
Count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.)</p>

<p><b>ex2.</b>
Start by comparing the first and second three-measurement windows. Count the number of times the sum of measurements in this sliding window increases from the previous sum.</p>
<hr>
<h3> DAY2</h3>

<p><b>ex1.</b> 
Hundle a series of commands like forward 1, down 2, or up 3:
  
- forward X increases the horizontal position by X units.
- down X increases the depth by X units.
- up X decreases the depth by X units.
  
Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth? </p>

<p><b>ex2.</b>
In addition to horizontal position and depth, you'll also need to track a third value, aim, which starts at 0. The commands also mean something entirely different than you first thought:

- down X increases your aim by X units.
- up X decreases your aim by X units.
- forward X does two things:
    <ul> - It increases your horizontal position by X units.</ul>
    <ul> - It increases your depth by your aim multiplied by X.</ul>  
   
Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?</p>
<hr>
<p><i> (on every puzzle the input is given from the adventofcode randomly to each player)</i></p>
