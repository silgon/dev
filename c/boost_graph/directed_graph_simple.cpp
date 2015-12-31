#include <iostream>
#include <boost/graph/graph_utility.hpp>
#include <boost/graph/adjacency_list.hpp>
  
int main(int,char*[])
{
    // Make convenient labels for the vertices
    enum { A, B, C, D, E, F, N };
    const char* name = "ABCDEF";

    // with matrix
    // typedef boost::adjacency_matrix<boost::directedS> Graph;
    // with list
    typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS> Graph;
    Graph g(N);
    boost::add_edge(B, C, g);
    boost::add_edge(B, F, g);
    boost::add_edge(C, A, g);
    boost::add_edge(C, C, g);
    boost::add_edge(D, E, g);
    boost::add_edge(E, D, g);
    boost::add_edge(F, A, g);

    std::cout << "vertex set: ";
    boost::print_vertices(g, name);
    std::cout << std::endl;

    std::cout << "edge set: ";
    boost::print_edges(g, name);
    std::cout << std::endl;

    std::cout << "out-edges: " << std::endl;
    boost::print_graph(g, name);
    std::cout << std::endl;
}
