### Only modify my_nsl and my_ol functions
### Only use bitwise and, or and not operations
### Bitwise not operation of x is (~x)&0xb1
### Bitwise or operaiton is |
### Bitwise and operation is &

def n(a):
    return (~a&0b1)

def my_nsl(ps,inputs):
    
    q0, q1 = ps & 0b1, (ps >> 1) & 0b1          
    i0, i1, i2 = inputs & 0b1, (inputs >> 1) & 0b1, (inputs >> 2) & 0b1            
            
    d0 = n(q0) & n(q1)
    d1 = q0
    
    
    ns = (d1 << 1) | d0
    return (ns)

def my_ol(ps):
    
    q0, q1 = ps & 0b1, (ps >> 1) & 0b1

    y0 = q0
    y1 = q1
    
    
    outputs = (y1 << 1) | y0
    return (outputs)

def my_input_schedule():
    
    # Define an array of tuples (absolute_time, input_value)
    # Example: [(5.5, 0b001), (10.5, 0b000), (15.5, 0b001)]
    input_schedule = [
        # User-defined schedule
        # (absolute_time, input_value)
        (5.5, 0b001), (15.5, 0b000), (17.5, 0b001)
    ]
    
    return(input_schedule)
    
    