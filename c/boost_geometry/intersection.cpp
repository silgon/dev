#include <iostream>
#include <vector>

#include <boost/geometry.hpp>
#include <boost/geometry/geometries/point_xy.hpp>
#include <boost/geometry/geometries/polygon.hpp>
#include <boost/geometry/io/wkt/wkt.hpp>

#include <boost/foreach.hpp>


int main()
{
    typedef boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double> > polygon;

    polygon green, blue;

    boost::geometry::read_wkt(
        "POLYGON((0 0, 0 2, 2 2, 2 0, 0 0))", green);

    boost::geometry::read_wkt(
        "POLYGON((1.9 1.9, 1.9 3, 3 3, 3 1.9, 1.9 1.9))", blue);
    // boost::geometry::read_wkt(
    //     "POLYGON((2 2, 2 3, 3 3, 3 2, 2 2))", blue);


    std::deque<polygon> output;
    boost::geometry::intersection(green, blue, output);

    std::cout << "intersection: " << output.size() << "\n";

    int i = 0;
    std::cout << "green && blue:" << std::endl;
    BOOST_FOREACH(polygon const& p, output)
    {
        std::cout << i++ << ": " << boost::geometry::area(p) << std::endl;
    }
    
    return 0;
}
