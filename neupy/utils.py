import sys


__all__ = ('format_data',)


def format_data(input_data, column1d=False):
    if input_data is None:
        return

    # Valid number of features for one or two dimentions
    n_features = input_data.shape[-1]
    if 'pandas' in sys.modules:
        pandas = sys.modules['pandas']

        if isinstance(input_data, (pandas.Series, pandas.DataFrame)):
            input_data = input_data.values

    if input_data.ndim == 1:
        data_shape = (n_features, 1) if column1d else (1, n_features)
        input_data = input_data.reshape(data_shape)

    return input_data
