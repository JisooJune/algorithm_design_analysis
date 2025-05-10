def f(houses):
    if not houses:
        return 0, []

    n = len(houses)
    stations = []
    i = 0

    while i < n:
        station_pos = houses[i]
        stations.append(station_pos)
        while i < n and houses[i] <= station_pos + 4:
            i += 1
    return len(stations), stations



# 示例
houses = [1, 5, 12, 33, 34, 35]
num_stations, station_positions = f(houses)
print("基站数目为", num_stations, "，基站位置为", station_positions)