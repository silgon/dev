#include "rapidxml.hpp"
#include "rapidxml_print.hpp"
#include <fstream>
#include <sstream>
#include <iostream>

using namespace rapidxml;
using namespace std;

int main(int argc, char *argv[])
{
	// filename
	const char * fname="stored.xml";
	// Write xml file =================================
	// create document type
	xml_document<> doc;
	// create node and add attributes for the declaration of the xml file
	xml_node<>* decl = doc.allocate_node(node_declaration);
	decl->append_attribute(doc.allocate_attribute("version", "1.0"));
	decl->append_attribute(doc.allocate_attribute("encoding", "utf-8"));
	doc.append_node(decl);
	// create main node
	xml_node<>* root = doc.allocate_node(node_element, "main");
	root->append_attribute(doc.allocate_attribute("version", "1.0"));
	root->append_attribute(doc.allocate_attribute("type", "example"));
	doc.append_node(root);
	// create a child of the root document
	// xml_node<>* child = doc.allocate_node(node_element, "test_child1");
	// child->append_attribute(doc.allocate_attribute("type","testeando"));
	// root->append_node(child);

	// creating many children of root
    for(int i = 0;i<10;++i)
    {
        xml_node<> *file = doc.allocate_node(node_element, "File");
        root->append_node(file);

        xml_node<> *path = doc.allocate_node(node_element, "Path","File_path");
        file->append_node(path);
        xml_node<> *name = doc.allocate_node(node_element, "Name","File_name");
        file->append_node(name);
    }

	// Convert doc to string if needed
	std::string xml_as_string;
	rapidxml::print(std::back_inserter(xml_as_string), doc);

	// Save to file
	std::ofstream file_stored(fname);
	file_stored << doc;
	file_stored.close();
	doc.clear();

	// Read xml file =================================
	// xml_document<> doc; // use this line if doc is not declared
	// reading file
	std::ifstream file(fname);
	// buffer type
	std::stringstream buffer;
	// insert all the file in buffer
	buffer << file.rdbuf();
	// put all the content in a string
	std::string content(buffer.str());
	// parsing the string
	doc.parse<0>(&content[0]);
	root = doc.first_node("main");
	for(xml_node<> * node_name = root->first_node("File"); node_name; node_name = node_name->next_sibling()){
		// printf("On %s, I tried their %s which is a %s. ",
		// 	   node_name->first_attribute("dateSampled")->value(),
		// 	   node_name->first_attribute("name")->value(),
		// 	   node_name->first_attribute("description")->value());
		printf("Value: %s\n", node_name->first_node("Path")->value());
	}

	// for (xml_attribute<> *attr = node->first_attribute(); attr; attr = attr->next_attribute()){
	// 	cout << "Node foobar has attribute " << attr->name() << " ";
	// 	cout << "with value " << attr->value() << "\n";
	// }

	// std::cout << content << std::endl;
    
    return 0;
}

