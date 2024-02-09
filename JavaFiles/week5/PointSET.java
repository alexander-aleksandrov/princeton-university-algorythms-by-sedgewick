import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import java.util.TreeSet;

public class PointSET {
    private TreeSet<Point2D> set;
    public PointSET() {
        set = new TreeSet<Point2D>();
    }            
    public boolean isEmpty() {
        return set.isEmpty();
    }     
    public int size() {
        return set.size();
    }            
    public void insert(Point2D p) {
        set.add(p);
    }
    public boolean contains(Point2D p) {
        return set.contains(p);
    }
    public void draw() {
        for (Point2D p : set) {
            p.draw();
        }
    }
    public Iterable<Point2D> range(RectHV rect) {
        TreeSet<Point2D> rangeSet = new TreeSet<Point2D>();
        for (Point2D p : set) {
            if (rect.contains(p)) {
                rangeSet.add(p);
            }
        }
        return rangeSet;
    }            
    public Point2D nearest(Point2D p) {
        Point2D nearest = null;
        double minDistance = Double.POSITIVE_INFINITY;
        for (Point2D point : set) {
            double distance = p.distanceSquaredTo(point);
            if (distance < minDistance) {
                minDistance = distance;
                nearest = point;
            }
        }
        return nearest;
    }
 

    // unit testing of the methods (optional) 
    public static void main(String[] args) {
        
    } 
 }