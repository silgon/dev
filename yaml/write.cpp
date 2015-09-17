#include <iostream>
#include <stdio.h>
#include <yaml-cpp/yaml.h>

int main(int argc, char *argv[])
{
    std::vector <int> squares;
    squares.push_back(1);
    squares.push_back(4);
    squares.push_back(9);
    squares.push_back(16);

    std::map <std::string, int> ages;
    ages["Daniel"] = 26;
    ages["Jesse"] = 24;

    YAML::Emitter out;
    out << YAML::BeginSeq;
    out << YAML::Flow << squares;
    out << ages;
    out << YAML::EndSeq;
    std::cout << "Here's the output YAML:\n" << out.c_str(); // prints "Hello, World!"
    return 0;
}



