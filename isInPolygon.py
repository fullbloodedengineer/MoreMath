'''
public bool IsPointInPolygon( Point p, Point[] polygon )
{
    double minX = polygon[ 0 ].X;
    double maxX = polygon[ 0 ].X;
    double minY = polygon[ 0 ].Y;
    double maxY = polygon[ 0 ].Y;
    //bounding box check, this can be preprocessed
    for ( int i = 1 ; i < polygon.Length ; i++ )
    {
        Point q = polygon[ i ];
        minX = Math.Min( q.X, minX );
        maxX = Math.Max( q.X, maxX );
        minY = Math.Min( q.Y, minY );
        maxY = Math.Max( q.Y, maxY );
    }

    if ( p.X < minX || p.X > maxX || p.Y < minY || p.Y > maxY )
    {
        return false;
    }

    // http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html
    bool inside = false;
    for ( int i = 0, j = polygon.Length - 1 ; i < polygon.Length ; j = i++ )
    {
        if ( ( polygon[ i ].Y > p.Y ) != ( polygon[ j ].Y > p.Y ) &&
             p.X < ( polygon[ j ].X - polygon[ i ].X ) * ( p.Y - polygon[ i ].Y ) / ( polygon[ j ].Y - polygon[ i ].Y ) + polygon[ i ].X )
        {
            inside = !inside;
        }
    }

    return inside;
}
'''
