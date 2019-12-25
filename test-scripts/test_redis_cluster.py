def test_masters_slaves():
    from rediscluster import RedisCluster
    nodes = [{"host": f"hostname",
              "port": "6379"}]
    r = RedisCluster(startup_nodes=nodes, password="xxxxx", skip_full_coverage_check=True, decode_responses=u'utf-8')
    all_keys = r.keys("*")
    print(f"\nKeys are : {all_keys}")
    print(r.get('coccoc-music-api:ALL_SOURCES'))


