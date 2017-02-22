// Code extracted from http://stackoverflow.com/a/19966714/2237916

using System;
using QuickGraph;
using System.Collections.Generic;
using QuickGraph.Algorithms;
using QuickGraph.Algorithms.ShortestPath;
using QuickGraph.Algorithms.Observers;


namespace Graph
{
    class MainClass
    {
        public static void Main (string[] args)
        {

            AdjacencyGraph<string, Edge<string>> graph = new AdjacencyGraph<string, Edge<string>>(true);

            // Add some vertices to the graph
            graph.AddVertex("A");
            graph.AddVertex("B");
            graph.AddVertex("C");
            graph.AddVertex("D");
            graph.AddVertex("E");
            graph.AddVertex("F");
            graph.AddVertex("G");
            graph.AddVertex("H");
            graph.AddVertex("I");
            graph.AddVertex("J");

            // Create the edges
            Edge<string> a_b = new Edge<string>("A", "B");
            Edge<string> a_d = new Edge<string>("A", "D");
            Edge<string> b_a = new Edge<string>("B", "A");
            Edge<string> b_c = new Edge<string>("B", "C");
            Edge<string> b_e = new Edge<string>("B", "E");
            Edge<string> c_b = new Edge<string>("C", "B");
            Edge<string> c_f = new Edge<string>("C", "F");
            Edge<string> c_j = new Edge<string>("C", "J");
            Edge<string> d_e = new Edge<string>("D", "E");
            Edge<string> d_g = new Edge<string>("D", "G");
            Edge<string> e_d = new Edge<string>("E", "D");
            Edge<string> e_f = new Edge<string>("E", "F");
            Edge<string> e_h = new Edge<string>("E", "H");
            Edge<string> f_i = new Edge<string>("F", "I");
            Edge<string> f_j = new Edge<string>("F", "J");
            Edge<string> g_d = new Edge<string>("G", "D");
            Edge<string> g_h = new Edge<string>("G", "H");
            Edge<string> h_g = new Edge<string>("H", "G");
            Edge<string> h_i = new Edge<string>("H", "I");
            Edge<string> i_f = new Edge<string>("I", "F");
            Edge<string> i_j = new Edge<string>("I", "J");
            Edge<string> i_h = new Edge<string>("I", "H");
            Edge<string> j_f = new Edge<string>("J", "F");

            // Add the edges
            graph.AddEdge(a_b);
            graph.AddEdge(a_d);
            graph.AddEdge(b_a);
            graph.AddEdge(b_c);
            graph.AddEdge(b_e);
            graph.AddEdge(c_b);
            graph.AddEdge(c_f);
            graph.AddEdge(c_j);
            graph.AddEdge(d_e);
            graph.AddEdge(d_g);
            graph.AddEdge(e_d);
            graph.AddEdge(e_f);
            graph.AddEdge(e_h);
            graph.AddEdge(f_i);
            graph.AddEdge(f_j);
            graph.AddEdge(g_d);
            graph.AddEdge(g_h);
            graph.AddEdge(h_g);
            graph.AddEdge(h_i);
            graph.AddEdge(i_f);
            graph.AddEdge(i_h);
            graph.AddEdge(i_j);
            graph.AddEdge(j_f);

            // Define some weights to the edges
            Dictionary<Edge<string>, double> edgeCost = new Dictionary<Edge<string>, double>(graph.EdgeCount)
                {
                    {a_b, 4},
                    {a_d, 1},
                    {b_a, 74},
                    {b_c, 2},
                    {b_e, 12},
                    {c_b, 12},
                    {c_f, 74},
                    {c_j, 12},
                    {d_e, 32},
                    {d_g, 22},
                    {e_d, 66},
                    {e_f, 76},
                    {e_h, 33},
                    {f_i, 11},
                    {f_j, 21},
                    {g_d, 12},
                    {g_h, 10},
                    {h_g, 2},
                    {h_i, 72},
                    {i_f, 31},
                    {i_h, 18},
                    {i_j, 7},
                    {j_f, 8}
                };

            Func<Edge<string>, double> getWeight = edge => edgeCost[edge];

            // We want to use Dijkstra on this graph
            DijkstraShortestPathAlgorithm<string, Edge<string>> dijkstra = new DijkstraShortestPathAlgorithm<string, Edge<string>>(graph, getWeight);

            //// attach a distance observer to give us the shortest path distances
            VertexDistanceRecorderObserver<string, Edge<string>> distObserver = new VertexDistanceRecorderObserver<string, Edge<string>>(getWeight);

            using (distObserver.Attach(dijkstra))
            {

                //// Attach a Vertex Predecessor Recorder Observer to give us the paths
                VertexPredecessorRecorderObserver<string, Edge<string>> predecessorObserver = new VertexPredecessorRecorderObserver<string, Edge<string>>();
                using (predecessorObserver.Attach(dijkstra))
                {
                    //// Run the algorithm with A set to be the source
                    dijkstra.Compute("A");

                    foreach (KeyValuePair<string, double> kvp in distObserver.Distances)
                        Console.WriteLine("Distance from root to node {0} is {1}", kvp.Key, kvp.Value);

                    foreach (KeyValuePair<string, Edge<string>> kvp in predecessorObserver.VertexPredecessors)
                        Console.WriteLine("If you want to get to {0} you have to enter through the in edge {1}", kvp.Key, kvp.Value);

                }
            }
        }
    }
}
