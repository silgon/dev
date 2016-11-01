NAME = read_yaml.cpp
OUTPUT = read_yaml
compile:
	g++ $(NAME) -o $(OUTPUT) -std=c++11 `pkg-config --cflags yaml-cpp` `pkg-config --libs yaml-cpp`

run: $(OUTPUT)
	./$(OUTPUT)
