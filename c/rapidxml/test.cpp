#include "rapidxml.hpp"
#include "rapidxml_print.hpp"
#include <fstream>
#include <sstream>
#include <iostream>

using namespace rapidxml;
using namespace std;

int main(int argc, char *argv[])
{
	// Write xml file =================================
	xml_document<> doc;
	xml_node<>* decl = doc.allocate_node(node_declaration);
	decl->append_attribute(doc.allocate_attribute("version", "1.0"));
	decl->append_attribute(doc.allocate_attribute("encoding", "utf-8"));
	doc.append_node(decl);

	xml_node<>* root = doc.allocate_node(node_element, "main");
	root->append_attribute(doc.allocate_attribute("version", "1.0"));
	root->append_attribute(doc.allocate_attribute("type", "example"));
	doc.append_node(root);

	xml_node<>* child = doc.allocate_node(node_element, "test_child1");
	child->append_attribute(doc.allocate_attribute("type","testeando"));
    for(int i = 0;i<10;++i)
    {
        xml_node<> *file = doc.allocate_node(node_element, "File");
        root->append_node(file);

        xml_node<> *path = doc.allocate_node(node_element, "Path","File_path");
        file->append_node(path);
        xml_node<> *name = doc.allocate_node(node_element, "Name","File_name");
        file->append_node(name);
    }
	root->append_node(child);

	// Convert doc to string if needed
	std::string xml_as_string;
	rapidxml::print(std::back_inserter(xml_as_string), doc);

	// Save to file
	std::ofstream file_stored("file_stored.xml");
	file_stored << doc;
	file_stored.close();
	doc.clear();

	// Read xml file =================================
	// xml_document<> doc;
	std::ifstream file("file_stored.xml");

	std::stringstream buffer;
	buffer << file.rdbuf();
	std::string content(buffer.str());
	doc.parse<0>(&content[0]);
	std::cout << content << std::endl;
    
    return 0;
}

