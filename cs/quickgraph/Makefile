NAME=01_example
download_dependencies:
	nuget install quickgraph
build:
	mcs ${NAME}.cs -r:QuickGraph.3.6.61119.7/lib/net4/QuickGraph.dll
run:
	MONO_PATH=${PWD}/QuickGraph.3.6.61119.7/lib/net4/ mono ${NAME}.exe
