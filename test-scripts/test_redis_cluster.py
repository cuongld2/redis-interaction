def test_masters_slaves():
    from rediscluster import RedisCluster
    nodes = [{"host": "redis-cluster-coccoc-music-0.browser-dev.svc.cluster.local",
              "port": "6379"}]
    r = RedisCluster(startup_nodes=nodes, password="dga4DD26V", skip_full_coverage_check=True)
    all_keys = r.keys("*")
    for each_key in all_keys:
        print(str(r.type(each_key)).split('b')[1])
        if 'string' in (str(r.type(each_key)).split('b')[1]):
            print(r.get(each_key))
        else:
            print(r.smembers(each_key))
