name = "tbb"

authors = ["Intel"]

version = "2020.3"

description = \
    """
    Threading Building Blocks
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
]

tools = [
]

build_command = "bash {root}/rez_build.sh {root}"

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.TBB_ROOT = "{root}"
    env.TBB_LOCATION = "{root}"

    env.TBBROOT = "{root}"
    env.TBB_INSTALL_DIR = "{root}"
    env.TBB_INCLUDE_DIR = "{root}/include"

    env.LD_LIBRARY_PATH.append("{root}/lib")

uuid = "repository.oneTBB"
