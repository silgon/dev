#include <iostream>
#include <boost/graph/graph_utility.hpp>
#include <boost/graph/adjacency_list.hpp>

typedef std::map<std::string, double> gproperties;
// typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::undirectedS, boost::no_property, gproperties> Graph;
typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, boost::no_property, gproperties> Graph;
  
int main(int argc, char *argv[])
{
    Graph g;
    Graph::vertex_descriptor v0 = boost::add_vertex(g);
    Graph::vertex_descriptor v1 = boost::add_vertex(g);

    gproperties gp;
    gp.insert(gproperties::value_type("hello", 5.1));
    boost::add_edge(v0, v1, gp, g);

    const char* name = "ABCDEF";
    std::cout << "vertex set: ";
    boost::print_vertices(g, name);
    std::cout << std::endl;

    std::cout << "edge set: ";
    boost::print_edges(g, name);
    std::cout << std::endl;

    std::cout << "out-edges: " << std::endl;
    boost::print_graph(g, name);
    std::cout << std::endl;

    return 0;
}
