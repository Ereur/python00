def ft_filter(function, iterable):
    """Replicates the behavior of the built-in filter function.

    Args:
        function: A function that returns True/False, or None.
        iterable: An iterable to filter.

    Returns:
        An iterator of elements for which function returns True.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
