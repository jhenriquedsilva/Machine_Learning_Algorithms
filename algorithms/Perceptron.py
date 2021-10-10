import numpy as np
"""
As a convention, it's append an underscore (_) to attributes that are not being created
upon the initialization of the object but by calling the object's other methods
"""

class Perceptron(object):
    
    """
    Perceptron classifier.
    
    Parameters
    -----------
    learning_rate: float
        Learning rate (between 0.0 and 1.0)
    passes_over_training_set: int
        Passes over the training data set
    random_state: int
        Random number generator seed for random weight initialization
        
    Attributes
    -----------
    weights_ : 1d-array
        weights_ after fitting.
    errors_ : list
        Number of misclassifications (updates) in each epoch.    
    """
    def __init__(self, learning_rate=0.01, passes_over_training_set=50, random_state=1):
        self.learning_rate = learning_rate
        self.passes_over_training_set = passes_over_training_set
        self.random_state = random_state

    def fit(self, X, y):
        """
        Fit training data
        
        Parameters
        -----------
        X: {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples
            and n_features is the number of features
        y: array-like, shape = [n_samples]
            Target values    
            
        Returns
        -----------
        self : object 
        """
        ramdom_number_generator = np.random.RandomState(self.random_state)
        self.weights_ = ramdom_number_generator.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.passes_over_training_set):
            errors = 0
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights_[1:] += update * xi
                self.weights_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.weights_[1:]) + self.weights_[0]

    def predict(self, X):
        """Return class label after unit step"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)                