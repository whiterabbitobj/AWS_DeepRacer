def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    #params['x'] (FLOAT)
    #params['y'] (FLOAT)
    #params['all_wheels_on_track'] (BOOL)
    #params['distance_from_center'] (FLOAT)
    #params['is_left_of_center'] (BOOL) (true if left, false if right)
    #params['heading'] (FLOAT) [-180,180]
    #params['progress'] (FLOAT) [0-100]
    #params['steps'] (INT) (number of steps completed, one step is a full SARS` tuple)
    #params['speed'] (FLOAT) [0.0 - 8.0]
    #params['steering_angle'] (FLOAT) [-30, 30]
    #params['track_width'] (FLOAT)
    #params['waypoints'] (list of FLOAT,FLOAT)
    #params['closest_waypoints'] (int, int)

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)
