'''
Calculate the number of games played by a player during a given time interval 
in a video game, with 4 rounds every hour starting at 0, 15, 30, and 45 minutes.
The input parameters of the function are the start and end times in the format 
"hh:mm", where hh is the hour (00 to 23) and mm is the minute (00 to 59).
'''

def solution(start_time, end_time):

    if start_time == end_time:
        return  0
    
    rounds = {0 : 4, 15 : 3, 30 : 2, 45 : 1}

    # Extract hours and minutes from start and end times
    start_h, start_m = map(int, start_time.split(':'))
    end_h, end_m = map(int, end_time.split(':'))

    
    # Check how many hours did the player play 
    if end_h < start_h:
        hours = 24 - start_h + end_h 
    else:
        hours = end_h - start_h
        
        # If player played for almost one day
        if not hours and end_m < start_m:
            hours = 24

    # Calculate number of games played in the first hour
    if start_m in rounds.keys():
        first_hour = rounds[start_m]    
    else:
        first_hour = 3 - start_m // 15

    # Calculate number of games played in the last hour
    if end_m >= 15:
        last_hour = 1 + (end_m - 15)//15
    else:
        last_hour = 0
    
    # If gameplay is above one hour
    if hours:
        games = first_hour + last_hour + 4*(hours-1)
    
    # If gameplay is under an hour
    else:
        games = last_hour - (4 - first_hour)
        if games < 0:
            games = 0

    return games