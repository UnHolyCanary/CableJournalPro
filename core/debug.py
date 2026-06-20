def dump_project(project):
    print("=" * 60)
    print("PROJECT DEBUG")
    print("=" * 60)
    print("Layers:", len(project.layer_info))
    print("Blocks:", len(project.block_info))