class KalmanFilterBase:
    """
    A base class for Kalman Filter implementation.

    Attributes:
        state: The current state of the filter.
        covariance: The current covariance of the filter.
        innovation: The last innovation of the filter.
        innovation_covariance: The last innovation covariance of the filter.

    Methods:
        _get_attribute(attribute):
            A helper method to retrieve the attribute in a list format.

        get_current_state():
            Returns the current state of the filter as a list.

        get_current_covariance():
            Returns the current covariance of the filter as a list.

        get_last_innovation():
            Returns the last innovation of the filter as a list.

        get_last_innovation_covariance():
            Returns the last innovation covariance of the filter as a list.
    """

    
    def __init__(self):
        self.state = None
        self.covariance = None
        self.innovation = None
        self.innovation_covariance = None
    
    def _get_attribute(self, attribute):
        if attribute is not None:
            return attribute.tolist()
        return None
    
    def get_current_state(self):
        return self._get_attribute(self.state)
    
    def get_current_covariance(self):
        return self._get_attribute(self.covariance)
    
    def get_last_innovation(self):
        return self._get_attribute(self.innovation)
    
    def get_last_innovation_covariance(self):
        return self._get_attribute(self.innovation_covariance)