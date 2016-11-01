#include <yaml-cpp/yaml.h>
#include <stdio.h>
#include <vector>

int main(int argc, char *argv[])
{
    YAML::Node config = YAML::LoadFile("config.yaml");    
    const std::string username = config["username"].as<std::string>();
    const int testvalue = config["testvalue"].as<int>();
    std::vector<int> testarray = config["testarray"].as<std::vector<int>>();

    std::cout << "The username is:" << username << "\n";
    std::cout << "The testvalue is: " << testvalue << "\n";
    std::cout << "-------------" << "\n";
    std::cout << "The values of the array are: " << "\n";
    for(auto &val: testarray)
        std::cout << val << ",";
    std::cout << std::endl;
    std::cout << "-------------" << "\n";
    std::cout << "Printing all the values" << "\n";
    std::cout << config << "\n";
    return 0;

}

