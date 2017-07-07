import sklearn.ensemble as skens


class PredictionMethod:
    def __init__(self, name, params):
        self.name = name
        self.description = ''
        self.params = params

    def get_name(self):
        return self.name

    def __str__(self):
        s = ""
        if self.name:
            s = "{name} is a ".format(name=self.name)
        s += "PredictionMethod of class {class_name}\n".format(class_name=self.__class__.__name__)

        s += "Description:\n{}".format(self.description)
        if self.params:
            s += "\nUsing parameters:"
            for param, vallue in self.params.items():
                s += "\n\t- {}: {}".format(param, vallue)
        else:
            s += "\nUsing default parameters."
        return s

    def set_description(self, d):
        self.description = d

    def fit(self, X, y):
        print("You should implement the '{method}' method for this PredictionMethod subclass ({class_name})".format(
            method='fit', class_name=self.__class__.__name__))
        return None

    def predict(self, X):
        print("You should implement the '{method}' method for this PredictionMethod subclass ({class_name})".format(
            method='predict', class_name=self.__class__.__name__))
        return None


class RandomForestRegressor(PredictionMethod):
    def __init__(self, name: str = None, params: dict = None):
        PredictionMethod.__init__(self, name, params)
        description = "The basic RandomForestRegressor from the powerful sklearn python package"
        self.set_description(description)

        # initializing parameters
        if self.params:
            self.regressor = skens.RandomForestRegressor(n_estimators=params["n_estimators"])
        else:
            self.regressor = skens.RandomForestRegressor(n_estimators=20)

    def fit(self, X, y):
        self.regressor.fit(X, y)

    def predict(self, X):
        return self.regressor.predict(X)

class GradientBoostingRegressor(PredictionMethod):
    def __init__(self, name: str = None, params: dict = None):
        PredictionMethod.__init__(self, name, params)
        description = "Gradient Boosting for regression from the powerful sklearn python package"
        self.set_description(description)

        # initializing parameters
        if self.params:
            self.regressor = skens.GradientBoostingRegressor(n_estimators=params["n_estimators"])
        else:
            self.regressor = skens.GradientBoostingRegressor(n_estimators=100)

    def fit(self, X, y):
        self.regressor.fit(X, y)

    def predict(self, X):
        return self.regressor.predict(X)

if __name__ == "__main__":
    rfr1 = RandomForestRegressor("Méthode 1", {"n_estimators": 30})
    print(rfr1)
    rfr1.fit([[1, 2], [3, 4]], [1, 2])
    y = rfr1.predict([[0, 1], [2, 3]])
    print(y)

    print()

    rfr2 = RandomForestRegressor()
    print(rfr2)
    rfr2.fit([[1, 2], [3, 4]], [1, 2])
    y = rfr2.predict([[0, 1], [2, 3]])
    print(y)
