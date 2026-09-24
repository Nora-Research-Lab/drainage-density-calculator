def calculate_drainage_density(watershed_area_km2: float, total_stream_length_km: float) -> dict:
    """Calculate drainage density and classify it.

    Args:
        watershed_area_km2: Area of watershed in square kilometers (positive float).
        total_stream_length_km: Total length of streams in kilometers (positive float).

    Returns:
        Dictionary with keys 'drainage_density' (float) and 'classification' (str).
    
    Raises:
        ValueError: If either argument is non-positive.
    """
    if watershed_area_km2 <= 0 or total_stream_length_km <= 0:
        raise ValueError("Both watershed area and stream length must be positive numbers.")
    dd = total_stream_length_km / watershed_area_km2
    if dd < 1.0:
        classification = "Low drainage density (coarse texture)"
    elif dd <= 3.0:
        classification = "Medium drainage density (moderate texture)"
    else:
        classification = "High drainage density (fine texture)"
    return {"drainage_density": dd, "classification": classification}
