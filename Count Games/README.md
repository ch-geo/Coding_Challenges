# Count Games
Calculate the number of games played by a player during a given time interval 
in a video game, with 4 rounds every hour starting at 0, 15, 30, and 45 minutes.

## Parameters
This function takes two parameters:
- `start_time` : A string representing the start time in the "hh:mm" format.
- `end_time` : A string representing the end time in the "hh:mm" format.

## Return Value
The function returns an integer representing the number of games played during the given time interval.

## Notes
This function assumes that the video game has 4 rounds every hour starting at 0, 15, 30, and 45 minutes, and that a game takes exactly 15 minutes to play. If the start and end times are the same, the function returns 0.