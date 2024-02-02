import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdOut;

public class Deque<Item> implements Iterable<Item> {
    private Node<Item> first;
    private Node<Item> last;
    private int size;

    private static class Node<Item> {
        Item item;
        Node<Item> next;
        Node<Item> prev;

        public Node(Item item) {
            this.item = item;
            this.next = null;
            this.prev = null;
        }
    }

    public Deque() {
        first = null;
        last = null;
        size = 0;
    }

    public boolean isEmpty() {
        return first == null;
    }

    public int size() {
        return size;
    }

    public void addFirst(Item item) {
        if (item == null) throw new IllegalArgumentException("Item is null");
        size++;

        if (isEmpty()) {
            first = new Node<>(item);
            last = first;
        }
        else {
            Node<Item> oldFirst = first;
            first = new Node<>(item);
            oldFirst.prev = first;
            first.next = oldFirst;
        }
        
    }

    public void addLast(Item item) {
        if (item == null) throw new IllegalArgumentException("Item is null");
        size++;

        if (isEmpty()) {
            last = new Node<>(item);
            first = last;
        }
        else {
            Node<Item> oldLast = last;
            last = new Node<>(item);
            last.prev = oldLast;
            oldLast.next = last;
        }
        
    }

    public Item removeFirst() {
        if (isEmpty()) throw new NoSuchElementException("Deque is empty");
        size--;
        Item item = first.item;
              
        if (first.next == null) {
            first = null;
            last = null;
        }
        else {
            first = first.next;
            first.prev = null;
        }
        return item;
    }

    public Item removeLast() {
        if (isEmpty()) throw new NoSuchElementException("Deque is empty");
        size--;
        Item item = last.item;
        
        if (last.prev == null) {

            first = null;
            last = null;
        }
        else {
            last = last.prev;
            last.next = null;
        } 
        return item;
    }

    @Override
    public Iterator<Item> iterator() {
        return new DequeIterator(first);
    }

    private class DequeIterator implements Iterator<Item> {
        private Node<Item> current;

        public DequeIterator(Node<Item> first) {
            current = first;
        }

        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public Item next() {
            if (current == null) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    public static void main(String[] args) {
        Deque<Integer> deque = new Deque<>();
        deque.addFirst(1);
        deque.addLast(2);
        deque.addLast(3);
        deque.addFirst(4);
        for (int item : deque) {
            StdOut.println(item);
        }
        StdOut.println(deque.removeFirst());
        deque.removeLast();
        StdOut.println(deque.isEmpty());
        StdOut.println(deque.size());
    }
}
