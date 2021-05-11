#!/usr/bin/bash

root_dir=$1

# build
echo "----------------------------------------------------------------------"
echo "Running command... make -f ${root_dir}/Makefile -j1 tbb_root=${root_dir} tbb_build_dir=${root_dir}/_rez_build"
echo "----------------------------------------------------------------------"

make -f ${root_dir}/Makefile -j1 tbb_root=${root_dir} tbb_build_dir=${root_dir}/_rez_build

echo "----------------------------------------------------------------------"
echo "Copying the files to REZ location"
echo "----------------------------------------------------------------------"
mkdir ${REZ_BUILD_INSTALL_PATH}/lib
mkdir ${REZ_BUILD_INSTALL_PATH}/include

cp -a ${root_dir}/_rez_build/*_release/libtbb*.* ${REZ_BUILD_INSTALL_PATH}/lib
cp -a ${root_dir}/_rez_build/*_debug/libtbb*.* ${REZ_BUILD_INSTALL_PATH}/lib
cp -a ${root_dir}/include/serial ${REZ_BUILD_INSTALL_PATH}/include/serial
cp -a ${root_dir}/include/tbb ${REZ_BUILD_INSTALL_PATH}/include/tbb
