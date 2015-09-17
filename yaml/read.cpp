#include <fstream>
#include <yaml-cpp/yaml.h>

int main()
{
    YAML::Node config = YAML::LoadFile("test.yaml");
    std::vector<std::vector <float> > matrix;
    std::cout << config["array"] << std::endl;
    return 0;
}
