#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/reverse_graph.hpp>
#include <boost/graph/iteration_macros.hpp>
#include <boost/graph/graph_utility.hpp>

// using namespace boost;
typedef boost::adjacency_list < boost::vecS, boost::vecS, boost::undirectedS > Graph;


template <typename T> std::set<T> operator-(const std::set<T>& a, const std::set<T>& b)
{
    std::set<T> r;
    std::set_difference(
                        a.begin(), a.end(),
                        b.begin(), b.end(),
                        std::inserter(r, r.end()));

    return r;
}

template <typename T> std::set<T> operator/(const std::set<T>& a, const std::set<T>& b)
{
    std::set<T> r;
    std::set_intersection(
                          a.begin(), a.end(),
                          b.begin(), b.end(),
                          std::inserter(r, r.end()));

    return r;
}


void compare(const Graph& a, const Graph& b)
{
    std::set<Graph::vertex_descriptor > av, bv, samev, extrav, missingv;
    std::set<Graph::edge_descriptor> ae, be, re, samee, extrae, missinge;

    BGL_FORALL_VERTICES_T(v, a, Graph) av.insert(v);
    BGL_FORALL_VERTICES_T(v, b, Graph) bv.insert(v);
    samev    = (av / bv);
    extrav   = (bv - av);
    missingv = (av - bv);


    BGL_FORALL_EDGES_T(e, a, Graph) ae.insert(e);
    BGL_FORALL_EDGES_T(e, b, Graph) be.insert(e);

    samee    = (ae / be);
    extrae   = (be - ae);
    missinge = (ae - be);

    // TODO(silgon): reverse_graph
    // boost::reverse_graph<Graph> r(b);
    // BGL_FORALL_EDGES_T(e, r, Graph) re.insert(e);
    std::cout << "---- Vertices ----\n"
              << "same: " << samev.size() << std::endl
              << "extra: " << extrav.size() << std::endl
              << "missing: " << missingv.size() << std::endl;

    std::cout << "---- Edges ----\n"
              << "same: " << samee.size() << std::endl
              << "extra: " << extrae.size() << std::endl
              << "missing: " << missinge.size() << std::endl;
}

int main()
{
    Graph a;
    {
        boost::graph_traits<Graph>::vertex_descriptor v, u, y;
        u = boost::vertex(1, a);
        v = boost::vertex(2, a);
        y = boost::vertex(3, a);
        boost::add_edge(u, v, a);
    }
    Graph b;
    {
        boost::graph_traits<Graph>::vertex_descriptor v, u, y;
        u = vertex(1, b);
        v = vertex(2, b);
        y = vertex(3, b);
        boost::add_edge(u, v, b);
        boost::add_edge(y, v, b);
    }

    const char* name = "123456";
    std::cout << "---Graph1---" << "\n";
    boost::print_graph(a);
    boost::print_edges(a,name);
    std::cout << "---Graph2---" << "\n";
    boost::print_graph(b);
    boost::print_edges(b,name);

    compare(a,b);
}
