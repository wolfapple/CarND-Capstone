from styx_msgs.msg import TrafficLight

STATE_COUNT_THRESHOLD = 3

class StateFilter(object):
    def __init__(self, enabled = True):
        self.state = TrafficLight.UNKNOWN
        self.last_state = TrafficLight.UNKNOWN
        self.last_wp = -1
        self.state_count = 0
        self.enabled = enabled

    def append(self, state, light_wp):
        '''
        Publish upcoming red lights at camera frequency.
        Each predicted state has to occur `STATE_COUNT_THRESHOLD` number
        of times till we start using it. Otherwise the previous stable state is
        used.
        '''
        if not self.enabled:
            return light_wp

        if self.state != state:
            
            self.state = state
            self.state_count = 1
            return None

        elif self.state_count >= STATE_COUNT_THRESHOLD:
            
            self.last_state = self.state
            light_wp = light_wp if state == TrafficLight.RED or state == TrafficLight.YELLOW else -1
            self.last_wp = light_wp
            self.state_count += 1
            return light_wp

        else:

            self.state_count += 1
            return self.last_wp

