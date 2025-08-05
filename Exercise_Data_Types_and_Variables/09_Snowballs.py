number_of_balls = int(input())
ball_n = 0
biggest_ball_score = 0
while ball_n < number_of_balls:
    ball_n += 1
    weight = int(input())
    time = int(input())
    quality = int(input())
    ball_score = (weight / time) ** quality
    if biggest_ball_score < ball_score:
        biggest_weight = weight
        biggest_time = time
        biggest_quality = quality
        biggest_ball_score = ball_score
print(f"{biggest_weight} : {biggest_time} = {int(biggest_ball_score)} ({biggest_quality})")
