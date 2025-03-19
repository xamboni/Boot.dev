def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    energy_needed = ((distance_one_way*2) / meters_per_energy)
    if energy_needed <= energy_available:
        return True
    return False