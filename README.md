# ABCR
A queue-based esoteric language.

# What is this language?

ABCR is a Turing tarpit that operates on queues and registers.  It has three queues (hereafter referred to as A, B, and C, not to be confused with the commands of the same name) and one register R which stores the result of the last operation.

There is no "active queue", so each of the three queues have their own versions of most commands.  For example, `a` is the dequeue operation for A, while `c` is the dequeue operation for C; `4` is the while loop that examines the front of A for truthiness and `5` is the while loop that examines the front of B for truthiness, with `6` for C.  At any given point, therefore, it is unambiguous which queue you are working with.

That is not to say, however, that all queues are created equal.  The three queues default to different values when they're popped (or peeked):

#### A defaults to `0` for both popping and peeking.

#### B defaults to `1` for both popping and peeking.

#### C defaults to grabbing the character code of the next input character (the rest of which, of course, are queued if more than one input character is given) if popped, or to the current register value if peeked.



#Full command list

(Disclaimer: I have very little clue how to use Markdown formatting.)

    A-Variant | B-Variant | C-Variant | R-Variant | Name      | Function
    ----------|-----------|-----------|-----------|-----------|---------------
    a         | b         | c         |           | Dequeue   | Dequeues a single value into R. (dequeuing R into R is effectively a no-op.)
    A         | B         | C         |           | Enqueue   | Pushes R to the queue.  (pushing R to R is effectively a no-op.)
    o         | p         | q         |           | Numprint  | Prints the front of the queue as a number. Does not dequeue.
    O         | P         | Q         |           | Charprint | Prints the front of the queue as a character. Does not dequeue.
    1         | 2         | 3         |           | Peek      | Looks at the front of the queue. (Looking at R is a no-op.)
    !         | @         | #         |           | Length    | Gets the length of the queue.
    *         | +         | ,         |           | Add       | Adds the front of the queue to the register value.  Dequeues.
    -         | .         | /         |           | Subtract  | Subtracts the front of the queue from the register value. Dequeues.
    4         | 5         | 6         | 7         | While     | Begins a loop that continues while the front of the queue is truthy.
    x         | x         | x         | x         | Mark      | Ends a single while loop.
              |           |           | )         | Increment | Increments register value.
              |           |           | (         | Decrement | Decrements register value.
              |           |           | i         | Input     | Grabs a positive or negative integer from the input stream.
