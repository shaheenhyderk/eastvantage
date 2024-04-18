from geopy.distance import geodesic

from app.schema.address_schema import Address


class DistanceUtil:
    @staticmethod
    def is_within_range(address: Address, coordinate: tuple, km: float) -> bool:
        """
        Determine if the specified address is within a certain distance from a given coordinate.

        Args:
            address (Address): The address object, expected to have 'latitude' and 'longitude' attributes.
            coordinate (tuple): A tuple containing the latitude and longitude as floats.
            km (float): The radius in kilometers within which the address should fall.

        Returns:
            bool: True if the address is within the specified distance, False otherwise.
        """
        address_location = (address.latitude, address.longitude)
        distance = geodesic(coordinate, address_location).kilometers
        return distance <= km
