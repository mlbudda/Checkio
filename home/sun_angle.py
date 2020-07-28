# Sun Angle
def sun_angle(time):
    """ finds the angle of the sun """
    angle = (((int(time[0:2]) - 6) * 60) + int(time[3:5])) * 0.25

    if angle < 0 or angle > 180:
        return "I don't see the sun!"
    else:
        return angle


print(sun_angle("07:00") == 15)
print(sun_angle("01:23") == "I don't see the sun!")