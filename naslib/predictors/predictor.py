class Predictor:
    
    def __init__(self, ss_type=None, encoding_type=None):
        self.ss_type = ss_type
        self.encoding_type = encoding_type
        
    def set_ss_type(self, ss_type):
        self.ss_type = ss_type
        
    def pre_process(self):
        """
        This is called at the start of the NAS algorithm,
        before any architectures have been queried
        """
        pass
    
    def pre_compute(self, xtrain, xtest):
        """
        This method is used to make batch predictions
        more efficient. Perform a computation on the train/test
        set once (e.g., calculate the Jacobian covariance)
        and then use it for all train_sizes.
        """
        pass
    
    def fit(self, xtrain, ytrain, info=None):
        """
        This can be called any number of times during the NAS algorithm.
        input: list of architectures, list of architecture accuracies
        output: none
        """
        pass
    
    def query(self, xtest, info):
        """
        This can be called any number of times during the NAS algorithm.
        inputs: list of architectures, 
                info about the architectures (e.g., training data up to 20 epochs)
        output: predictions for the architectures
        """
        pass
    
    def get_data_reqs(self):
        """
        Returns a dictionary with info about whether the predictor needs
        extra info to train/query, such as a partial learning curve,
        or hyperparameters of the architecture
        """
        reqs = {'requires_partial_lc':False, 
                'metric':None, 
                'requires_hyperparameters':False, 
                'hyperparams':{}}
        return reqs