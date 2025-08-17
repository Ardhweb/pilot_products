import warnings

# Suppress NumPy's longdouble compatibility warning
warnings.filterwarnings(
    "ignore",
    message=r"Signature .* for <class 'numpy\.longdouble'> does not match any known type.*",
    category=UserWarning,
    module='numpy'
)
