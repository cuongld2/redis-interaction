def test_masters_slaves():
    from rediscluster import RedisCluster
    # for node in [0, 1, 2, 3, 4, 5]:
    nodes = [{"host": f"redis-cluster-coccoc-music-0.browser-dev.svc.cluster.local",
              "port": "6379"}]
    r = RedisCluster(startup_nodes=nodes, password="dga4DD26V", skip_full_coverage_check=True, decode_responses=u'utf-8')
    # all_keys = r.keys("*")
    # if 'b"coccoc-music-api:ALL_SOURCES"' in all_keys:
    #     r.get('b"coccoc-music-api:ALL_SOURCES"')
    # for each_key in all_keys:
    #     if 'string' in (str(r.type(each_key)).split('b')[1]):
    #         if "coccoc-music-api:ALL_SOURCES" in str(each_key):
    #             print(r.get(each_key))
    # print(f"\nKeys are : {all_keys}")
    print(r.get('coccoc-music-api:ALL_CATEGORIES'))


