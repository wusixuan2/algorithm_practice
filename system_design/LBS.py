class GeoHash:
    # @param {double} latitude, longitude a location coordinate pair
    # @param {int} precision an integer between 1 to 12
    # @return {string} a base32 string
    def encode(self, latitude, longitude, precision):
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        lat_bin = self.get_bin(latitude, -90, 90)
        lng_bin = self.get_bin(longitude, -180, 180)

        hash_code, b = '', ''
        for i in xrange(30):
            b += lng_bin[i] + lat_bin[i]

        for i in xrange(0, 60, 5):
            hash_code += _base32[int(b[i:i + 5], 2)]

        return hash_code[:precision]

    def get_bin(self, value, left, right):
        b = ''
        for i in xrange(30):
            mid = (left + right) / 2.0
            if value > mid:
                left = mid
                b += '1'
            else:
                right = mid
                b += '0'
        return b
class GeoHashII:
    # @param {string} geohash a base32 string
    # @return {double[]} latitude and longitude a location coordinate pair
    def decode(self, geohash):
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        b = ""
        for c in geohash:
            b += self.i2b(_base32.find(c))

        odd = ''.join([b[i] for i in xrange(0, len(b), 2)])
        even = ''.join([b[i] for i in xrange(1, len(b), 2)])

        location = []
        location.append(self.get_location(-90.0, 90.0, even))
        location.append(self.get_location(-180.0, 180.0, odd))
        return location

    def i2b(self, val):
        b = ""
        for i in xrange(5):
            if val % 2:
                b = '1' + b
            else:
                b = '0' + b
            val /= 2
        return b

    def get_location(self, start, end, string):
        for c in string:
            mid = (start + end) / 2.0
            if c == '1':
                start = mid
            else:
                end = mid
        return (start + end) / 2.0

# report(dirver_id, lat, lng)
# 如果在 dirver_id -> trip 的映射中查找到对应的trip, 直接返回
# 没有查找到trip, 更新 dirver_id -> location 中的位置信息
# request(rider_id, lat, lng)
# 遍历 driver_id -> location , 选择距离最近的司机
# 建立 trip 并添加至 driver_id -> trip
# 将该司机从 dirver_id -> location 中删除
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)

class Location:

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

class MiniUber:

    def __init__(self):
        # initialize your data structure here.
        self.driver2Location = {}
        self.driver2Trip = {}


    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        # Write your code here
        if driver_id in self.driver2Trip:
            return self.driver2Trip[driver_id]

        if driver_id in self.driver2Location:
            self.driver2Location[driver_id].lat = lat
            self.driver2Location[driver_id].lng = lng
        else:
            self.driver2Location[driver_id] = Location(lat, lng)

        return None

    # @param rider_id an integer
    # @param lat, lng driver's location
    # return a trip
    def request(self, rider_id, lat, lng):
        # Write your code here
        trip = Trip(rider_id, lat, lng)
        distance, driver_id = -1, -1

        for key, value in self.driver2Location.items():
            dis = Helper.get_distance(value.lat, value.lng, lat, lng);
            if distance < 0 or distance > dis:
                driver_id = key
                distance = dis

        if driver_id != -1:
            del self.driver2Location[driver_id]

        trip.driver_id = driver_id;
        self.driver2Trip[driver_id] = trip

        return trip

'''
Definition of Location:
class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        # This will create a new location object

Definition of Restaurant:
class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        # This will create a new restaurant object,
        # and auto fill id

Definition of Helper
class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        # return calculate the distance between two location

Definition of GeoHash
class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethom
    def encode(cls, location):
        # return convert location to a geohash string

    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        # return convert a geohash string to location
'''
import bisect
from YelpHelper import Location, Restaurant, GeoHash, Helper

class MiniYelp:

    def __init__(self):
        # initialize your data structure here.
        self.restaurants = {}
        self.ids = {}
        self.geo_value  = []

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        restaurant = Restaurant.create(name, location)
        hashcode = "%s.%s" % (GeoHash.encode(location), restaurant.id)
        bisect.insort(self.geo_value, hashcode)
        self.restaurants[hashcode] = restaurant
        self.ids[restaurant.id] = hashcode
        return restaurant.id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        hashcode = self.ids[restaurant_id]
        index = bisect.bisect_left(self.geo_value, hashcode)
        self.geo_value.pop(index)
        del self.restaurants[hashcode]
        del self.ids[restaurant_id]

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        length = self.get_length(k)
        hashcode = GeoHash.encode(location)[0:length]
        left = bisect.bisect_left(self.geo_value, hashcode)
        right = bisect.bisect_right(self.geo_value, hashcode + '{')

        results = []
        # print left, right, hashcode
        for index in range(left, right):
            hashcode = self.geo_value[index]
            restaurant = self.restaurants[hashcode]
            distance = Helper.get_distance(location, restaurant.location)
            if  distance <= k:
                results.append((distance, restaurant))

        results = sorted(results, key=lambda obj: obj[0])
        return [rt[1].name for rt in results]

    def get_length(self, k):
        ERROR = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.01911, 0.00478, 0.0005971, 0.0001492, 0.0000186]
        for i, error in enumerate(ERROR):
            if k  > error:
                return i

        return len(ERROR)
