def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    #params['x'] (FLOAT)
    #params['y'] (FLOAT)
    #params['all_wheels_on_track'] (BOOL)
    #params['distance_from_center'] (FLOAT) [0 - track_width/2]
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
    steering = abs(params['steering_angle'])
    speed = params['speed']

    #USER SET PARAMS
    std_dev = .25
    mean = 0
    MAX_SPEED = 8.0
    STEERING_THRESHOLD = 30

    #NORMAL DISTRIBUTION PARAMS
    e = 2.71828
    pi = 3.14159
    sqrt_2pi = 2.50663
    first_term = 1 / (std_dev * sqrt_2pi)

    ##############################################################

    #POSITIONING REWARD
    # give a higher reward for being closer to the center of the
    # track
    x = distance_from_center / (track_width / 2)
    pos_exp_denom = 2 * (std_dev**1.5)
    pos_reward = first_term * (e**-( ((x-mean)**4) / pos_exp_denom) / 1.6)

    #STEERING SMOOTHNESS REWARD
    # give a higher reward for less extreme steering
    x = steering / STEERING_THRESHOLD
    steering_exp_denom = 2 * (std_dev**1.75)
    steering_reward = first_term * (e**-(((abs(x)-mean)**3) / steering_exp_denom) / 1.6)

    #SPEED REWARD
    # give a higher reward if the speed is higher
    x = speed / MAX_SPEED
    speed_exp_denom = 2 * (std_dev**1.5)
    speed_reward = -first_term * (e**-(((x-mean)**2) / speed_exp_denom) / 1.6) + 1

    ##############################################################

    #CALCULATE OVERALL REWARD
    # overall reward is the weighted average of the speed, positioning, and
    # steering correcting reward values
    pos_weight = 0.2
    steering_weight = 0.3
    speed_weight = 0.5
    reward = (pos_weight * pos_reward) + (steering_weight * steering_reward) + (speed_weight * speed_reward)

    return float(reward)
