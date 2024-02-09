import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import java.util.ArrayList;
import java.util.List;

public class KdTree {
    private int size;
    private Node root;
    


    private class Node {
        private Point2D p;      
        private RectHV rect;    
        private Node lb;        
        private Node rt;        
    }

    public KdTree() {
        size = 0;
        root = null;
    }


    public boolean isEmpty() {
        return size == 0;
    }     

    public int size() {
        return size;
    }            

    public void insert(Point2D p) {
        if (p == null) {
            throw new IllegalArgumentException("calls insert() with a null point");
        }
        if (isEmpty()) {
            root = new Node();
            root.p = p;
            root.rect = new RectHV(0, 0, 1, 1);
            size++;
        }
        else {
            insert(root, p, true);
        }
    }
    private void insert(Node root2, Point2D p, boolean b) {
        if (root2 == null) {
            return;
        }
        if (b) {
            if (p.x() < root2.p.x()) {
                if (root2.lb == null) {
                    Node newNode = new Node();
                    newNode.p = p;
                    newNode.rect = new RectHV(root2.rect.xmin(), root2.rect.ymin(), root2.p.x(), root2.rect.ymax());
                    root2.lb = newNode;
                    size++;
                }
                else {
                    insert(root2.lb, p, false);
                }
            }
            else {
                if (root2.rt == null) {
                    Node newNode = new Node();
                    newNode.p = p;
                    newNode.rect = new RectHV(root2.p.x(), root2.rect.ymin(), root2.rect.xmax(), root2.rect.ymax());
                    root2.rt = newNode;
                    size++;
                }
                else {
                    insert(root2.rt, p, false);
                }
            }
        }
        else {
            if (p.y() < root2.p.y()) {
                if (root2.lb == null) {
                    Node newNode = new Node();
                    newNode.p = p;
                    newNode.rect = new RectHV(root2.rect.xmin(), root2.rect.ymin(), root2.rect.xmax(), root2.p.y());
                    root2.lb = newNode;
                    size++;
                }
                else {
                    insert(root2.lb, p, true);
                }
            }
            else {
                if (root2.rt == null) {
                    Node newNode = new Node();
                    newNode.p = p;
                    newNode.rect = new RectHV(root2.rect.xmin(), root2.p.y(), root2.rect.xmax(), root2.rect.ymax());
                    root2.rt = newNode;
                    size++;
                }
                else {
                    insert(root2.rt, p, true);
                }
            }
        }
        
    }


    public boolean contains(Point2D p) {
        if (p == null) {
            throw new IllegalArgumentException("calls contains() with a null point");
        }
        return contains(root, p, true);
    }
    private boolean contains(Node root2, Point2D p, boolean b) {
        if (root2 == null) {
            return false;
        }
        if (root2.p.equals(p)) {
            return true;
        }
        if (b) {
            if (p.x() < root2.p.x()) {
                return contains(root2.lb, p, false);
            }
            else {
                return contains(root2.rt, p, false);
            }
        }
        else {
            if (p.y() < root2.p.y()) {
                return contains(root2.lb, p, true);
            }
            else {
                return contains(root2.rt, p, true);
            }
        }
        
    }


    public void draw() {
        draw(root, true);
    }
    private void draw(Node root2, boolean b) {
        if (root2 == null) {
            return;
        }
        if (b) {
            draw(root2.lb, false);
            root2.p.draw();
            draw(root2.rt, false);
        }
        else {
            draw(root2.lb, true);
            root2.p.draw();
            draw(root2.rt, true);
        }
    }


    public Iterable<Point2D> range(RectHV rect) {
        if (rect == null) {
            throw new IllegalArgumentException("calls range() with a null rectangle");
        }
        List<Point2D> rangeList = new ArrayList<>();
        range(root, rect, rangeList);
        return rangeList;
    }

    private void range(Node root2, RectHV rect, List<Point2D> rangeList) {
        if (root2 == null) {
            return;
        }
        if (rect.contains(root2.p)) {
            rangeList.add(root2.p);
        }
        if (root2.lb != null && rect.intersects(root2.lb.rect)) {
            range(root2.lb, rect, rangeList);
        }
        if (root2.rt != null && rect.intersects(root2.rt.rect)) {
            range(root2.rt, rect, rangeList);
        }
    }

    public Point2D nearest(Point2D p) {
        if (p == null) {
            throw new IllegalArgumentException("calls nearest() with a null point");
        }
        if (isEmpty()) {
            return null;
        }
        return nearest(root, p, root.p, true);        
    }


    private Point2D nearest(Node root2, Point2D p, Point2D p2, boolean b) {
        if (root2 == null) {
            return p2;
        }
        if (p.distanceSquaredTo(root2.p) < p.distanceSquaredTo(p2)) {
            p2 = root2.p;
        }
        if (b) {
            if (p.x() < root2.p.x()) {
                p2 = nearest(root2.lb, p, p2, false);
                p2 = nearest(root2.rt, p, p2, false);
            }
            else {
                p2 = nearest(root2.rt, p, p2, false);
                p2 = nearest(root2.lb, p, p2, false);
            }
        }
        else {
            if (p.y() < root2.p.y()) {
                p2 = nearest(root2.lb, p, p2, true);
                p2 = nearest(root2.rt, p, p2, true);
            }
            else {
                p2 = nearest(root2.rt, p, p2, true);
                p2 = nearest(root2.lb, p, p2, true);
            }
        }
        return p2;
    }  
}
