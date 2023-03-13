name = "tbb"

authors = ["Intel"]

version = "2020.3"

description = \
    """
    Threading Building Blocks
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"]
]

tools = [
]

build_command = "bash {root}/rez_build.sh {root}"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.TBB_ROOT = "{root}"
    env.TBB_LOCATION = "{root}"

    env.TBBROOT = "{root}"
    env.TBB_INSTALL_DIR = "{root}"
    env.TBB_INCLUDE_DIR = "{root}/include"

    env.LD_LIBRARY_PATH.append("{root}/lib")

uuid = "repository.oneTBB"
