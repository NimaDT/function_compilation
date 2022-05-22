def NPV_real_estate(operating_net, required_rate_of_return, inflation):
    """Takes operating net, required rate of return and inflation as inputs to calculate Net Present Value of a real estate investment.
    Parameters:
    operating_net (int or float): The net operating income of a property
    required_rate_of_return (float): The required rate of return as a decimal number. Ex: 2% -> 0.02
    inflation (float): The expected rate of inflation as a decimal number. Ex:: 3.5% -> 0.035

    Returns:
    NPV (float): The Net Present Value, i.e. the appropiate investment for a property given the parameters.
        """
    NPV = operation_net * ((1 + inflation) / ((1 + required_rate_of_return) - (1 + inflation)))
    return NPV
