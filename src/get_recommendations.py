recommendations = {0:1, 2:3}



def get_recommendations(state):

    if state =='initial':
        return random_board
    else:
        return recommendations[state]