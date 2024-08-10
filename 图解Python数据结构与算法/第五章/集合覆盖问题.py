def greedy_set_cover(states_needed, stations):
    final_stations = set()
    
    while states_needed:
        best_station = None
        states_covered = set()
        
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
                
        if best_station:
            final_stations.add(best_station)
            states_needed -= states_covered
            
    return final_stations

states_needed = {'北京', '上海', '天津', '广州', '深圳', '成都', '杭州', '大连'}
stations = {
    '广播台1': {'北京', '上海', '天津', '广州'},
    '广播台2': {'北京', '深圳', '杭州'},
    '广播台3': {'成都', '上海', '杭州'},
    '广播台4': {'上海', '天津', '大连'}
}

# 调用贪心算法求解
selected_stations = greedy_set_cover(states_needed, stations)
print("最终选择的广播台:", selected_stations)
