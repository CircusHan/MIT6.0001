#! /usr/bin/python3

# ********************************************************
# CS 200 HW #3  DUE Monday, 10/21/2024 at 11:59 pm
#                via gradescope.
# ********************************************************
# Name:
# Email address:
# ********************************************************

# This file may be opened in python 3
# Lines beginning with hashes are comments.

# If you are asked to write a procedure, please make sure it has
# the specified name, and the specified number and order of arguments.
# The names of the formal arguments need not be the same
# as in the problem specification.

# For each problem, the intended inputs to your procedures
# are specified (for example, "positive integers")
# and your procedures need not do anything reasonable
# for other possible inputs.

# You may write auxiliary procedures in addition to
# the requested one(s) -- for each of your auxiliary
# procedures, please include a comment explaining
# what it does, and giving an example or two.

# You may also use procedures you have written
# elsewhere in this assignment or previous assignments.
# They only need to be defined once somewhere within this file.

# Reading: Learning Python, chapters 26-32
#          Python Cookbook, chapter 8

# ********************************************************
# ** problem 0 ** (1 easy point)
# Replace the number 0 in the definition below to indicate
# the number of hours you spent doing this assignment
# Decimal numbers (eg, 6.237) are fine.  Exclude time
# spent reading.

def hours():
    return 0


'''
#############################################################################
Problem 1.  10 points

 Wires and gates.

A wire is identified by a Python string, for example 'x', 'y0', or 'next'.

A gate is an object with three fields: 
1) a string indicating the type of gate, one of:
   'not', 'and', 'or', 'xor', 'nand', 'nor'
2) a list of the wire identifiers of the inputs
3) the output wire identifier

Below is the (partial) definition of the gate class, followed by
several examples.

Some of the methods are undefined, as designated "pass".  Provide
those definitions.

One of the methods is good_gate, which returns True if it is a
well-formed gate, and False otherwise.

To be a well-formed gate, the value must be a gate object whose three
fields satisfy the following conditions:

(1) the type field is one of the gate strings: 'not', 'and', 'or',
     'xor', 'nand', 'nor',

(2) the inputs field is a list of wire identifiers

(3) the output field is a single wire identifier

In addition, the number of inputs should be correct for each gate
type.  A gate of type 'not' has 1 input(unary operator), while gates of types 'and',
'or', 'xor', 'nand', 'nor' have 2 inputs(binary operators).


'''


class gate:

    def __init__(self, type, inputs, output):
        self.type = type.lower()  ## make all gate types lowercase.
        self.inputs = inputs
        self.output = output

    def __repr__(self):
        return f"gate({self.type!r}, {self.inputs!r}, {self.output!a})"

    def good_gate(self):
        if self.type not in ['and','or', 'xor', 'nand', 'nor','not']:
            return False
        else:
            if self.type == 'not':
                if len(self.inputs) == 1:
                    if type(self.inputs[0]) == str:
                        return True
                    else: 
                        return False
                else:
                    return False
            else:
                if len(self.inputs) == 2:
                    if type(self.inputs[0]) == str and type(self.inputs[1]) == str:
                        return True
                    else: 
                        return False
                else:
                    return False
                
            

    ## the overloaded == operator for gates.
    def __eq__(self, other):
        return (type(self) == type(other) and
                self.type == other.type and
                set(self.inputs) == set(other.inputs) and
                self.output == other.output)


gate1 = gate('and', ['x', 'y'], 'z')
gate2 = gate('or', ['x', 'v'], 'v')
gate3 = gate('not', ['s'], 'v')
gate4 = gate('nand', ['x', 'v'], 'v')
gate5 = gate('nand', ['v', 'x'], 'v')
gate6 = gate('and', ['v', 'x'], 'v')

gateb1 = gate('bad', ['x', 'v'], 'v')
gateb2 = gate('not', [1], 'v')
gateb3 = gate('not', ["x", "y"], 'v')
gateb4 = gate('and', ["x", "y", "z"], 'v')
gates = [gate1, gate2, gate3, gate4, gate5, gate6, gateb1, gateb2, gateb3, gateb4]
for gate in gates:
    print(gate.good_gate())
    

'''
########################################################################
Problem 2. 10 points

Circuits.

 A circuit is an object with three fields
 (1) a list of input wire identifiers
 (2) a list of output wire identifiers
 (3) a list of gates

Below is the (partial) definition of the circuit class, followed by
several examples.

Some of the methods are undefined, as designated "pass".  Provide
those definitions.

One of the methods is good_circuit, which returns True if it is a
well-formed circuit, and False otherwise.

To be a well-formed circuit, it must be a circuit object and its
inputs field must be a list of wires, its outputs field must be a list
of wires, and its gates field must be a list of gates that are
well-formed according to the good_gate method.

In addition, the circuit must satisfy the following conditions:

 (1) no input of the circuit is the output of a gate, #output 선이 input으로 들어감.

 (2) every input of a gate is either an input of the circuit or the #게이트의 인풋이 회로의 인풋이거나 게이트의 아웃풋
 output of a gate, 

 (3) no wire is the output of two or more gates,  #어떤 wire도 두 개 이상의 게이트의 아웃풋일 수 없다.

 (4) every output of the circuit is either an input of the circuit or
 the output of a gate.
'''


class circuit:

    def __init__(self, inputs, outputs, gates):
        self.inputs = inputs
        self.outputs = outputs
        self.gates = gates

    def __repr__(self):
        return f"circuit({self.inputs!r}, {self.outputs!r}, {self.gates!r})"

    def good_circuit(self):
        for input in self.inputs:
            for output in self.outputs:
                if input == output:
                    return False
                else:
                    return True
        

    ## See problem 3 below
    def all_wires(self):
        pass

    ## See problem 3 below
    def find_gate(self, wire):
        pass

    ## See problem xx below.  You do not have to write this one.
    def next_value(self, wire, config):
        if wire in self.inputs:
            return config[wire]
        wgate = self.find_gate(wire)
        wtype = wgate.type
        winputs = wgate.inputs
        input_values = list(map(lambda x: config[x], winputs))
        if wtype == 'not':
            return 1 - input_values[0]
        if wtype == 'and':
            if input_values[0] == 0:
                return 0
            else:
                return input_values[1]
        if wtype == 'or':
            if input_values[0] == 1:
                return 1
            else:
                return input_values[1]
        if wtype == 'xor':
            if input_values[0] == input_values[1]:
                return 0
            else:
                return 1
        if wtype == 'nand':
            if input_values[0] == 0:
                return 1
            else:
                return 1 - input_values[1]
        if wtype == 'nor':
            if input_values[0] == 0:
                return 0
            else:
                return 1 - input_values[1]

    ## See problem 5 below
    def next_config(self, config):
        pass

    ## See problem 6 below
    def stable(self, config):
        pass

    ## See problem 6 below
    def all_stable_configs(self):
        pass

    ## See problem 6 below
    def output_values(self, config):
        pass

    ## See problem 6 below
    def init_config(self, input_values):
        pass

    ## See problem 7 below
    def simulate(self, config, n):
        pass

    ## See problem 8 below
    def final_config(self, config):
        pass


### use in all_stable_configs above
## similar to power_set() in hw1
def all_configs(wires):
    lst = all_configs_aux(wires)
    r = []
    for x in lst:
        r.append({z[0]: z[1] for z in x})
    return r


def all_configs_aux(wires):
    if not wires:
        return [[]]
    ac = all_configs_aux(wires[1:])
    left = [[[wires[0], 0]] + x for x in ac]
    right = [[[wires[0], 1]] + x for x in ac]
    return left + right


## We provide the flatten() function which may be useful in defining the circuit methods.

def flatten(tree):
    result = []
    if not isinstance(tree, list):
        return [tree]
    else:
        for x in tree:
            result.extend(flatten(x))
    return result


###########################################################################
###  Example circuits  (see lecture notes)
###########################################################################

'''
The eq1_ckt is interpreted as follows:
- the inputs of the circuit are the wires x and y,
- the outputs of the circuit consist of just the wire z,
- there are five gates specified as follows:
- wire cx is the output of a NOT gate with input x,
- wire cy is the output of a NOT gate with input y,
- wire t1 is the output of an AND gate with inputs x and y,
- wire t2 is the output of an AND gate with inputs cx and cy,
- wire z is the output of an OR gate with inputs t1 and t2.

'''

eq1_ckt = circuit(["x", 'y'], ['z'],
                  [gate('not', ['x'], 'cx'),
                   gate('not', ['y'], 'cy'),
                   gate('and', ['x', 'y'], 't1'),
                   gate('and', ['cx', 'cy'], 't2'),
                   gate('or', ['t1', 't2'], 'z')])

nullckt = circuit([], [], [])
badckt1 = circuit([1], [2], [3])
badckt2 = circuit([], [], [gateb1])

'''
Below is eq2_ckt,  another implementation of comparing two bits for equality.
- This uses the implementation as the NOT of (x XOR y).
- This is also a combinational circuit.
- The inputs and output of this circuit are named as in eq1_ckt.
'''

eq2_ckt = circuit(["x", 'y'], ['z'],
                  [gate('xor', ['x', 'y'], 'w'),
                   gate('not', ['w'], 'z')])

'''Here is a two-bit selector whose Boolean expressions are as follows.

z1 = x1 * s' + y1 * s
z0 = x0 * s' + y0 * s

For this circuit, z1 and z0 are equal to x1 and x0 if s = 0, and z1
and z0 are equal to y1 and y0 if s = 1.

This is a combinational circuit.

'''
sel_ckt = circuit(["x1", 'x0', 'y1', 'y0', 's'],
                  ['z1', 'z0'],
                  [gate('not', ['s'], 'sc'),
                   gate('and', ['x1', 'sc'], 'u1'),
                   gate('and', ['y1', 's'], 'v1'),
                   gate('or', ['u1', 'v1'], 'z1'),
                   gate('and', ['x0', 'sc'], 'u0'),
                   gate('and', ['y0', 's'], 'v0'),
                   gate('or', ['u0', 'v0'], 'z0')])

'''
Below is a NAND latch, used to store one bit.  It is a sequential (not
combinational) circuit, because it has a loop from a wire to itself
through other wires and gates.
'''
latch_ckt = circuit(["x", 'y'],
                    ['q', 'u'],
                    [gate('nand', ['x', 'u'], 'q'),
                     gate('nand', ['y', 'q'], 'u')])

'''
The following is also a sequential circuit, with an OR gate one of
whose inputs is its output.  (The "Garden of Eden" circuit.)
'''
seq_or_ckt = circuit(["x"],
                     ['z'],
                     [gate('or', ['x', 'z'], 'z'), ])

'''
The next is also a sequential circuit.  It could serve as a clock.
Note that this circuit has *no* inputs, but does have an output.

'''

clock_ckt = circuit([],
                    ['z'],
                    [gate('not', ['z'], 'z'), ])
'''########################################################################
; ** problem 3 ** (10 points)

Write the two circuit methods (modify the circuit class definition above)

ckt.all_wires() returns the list of all the wire names that appear in
      the circuit, as circuit inputs, circuit outputs, gate inputs or
      gate outputs, in that order, with duplicates removed.


ckt.find_gate(wire) returns the gate in the circuit with the given
      output wire, or #f if there is no such gate.

You may assume that circuit is a well-formed circuit; in particular,
a wire is the output of *at most one* gate.

Examples:

eq1_ckt.all_wires() => ['cx', 'cy', 't1', 't2', 'x', 'y', 'z']
sel_ckt.all_wires() =>  ['s', 'sc', 'u0', 'u1', 'v0', 'v1', 'vo', 'x0', 'x1', 'y0', 'y1', 'z0', 'z01', 'z1']

eq1_ckt.find_gate('t2') => gate('and', ['cx', 'cy'], 't2')
eq2_ckt.find_gate('w') => gate('xor', ['x', 'y'], 'w')
sel_ckt.find_gate('y') => False

################################################################################
## Problem 4 ** (10 points)

Define circuits for a half-adder and a full-adder in the
representation described above. Note these are defined in the lecture
notes.  Also, the staff solution does NOT include these circuits. Tant
pis.

Your half-adder should be called ha_ckt and should have input wires: x
and y and output wires: z and co, where z is the exclusive or of x and
y, and co is 1 if both x and y are 1.

Your full-adder should be called fa_ckt and should have input wires:
x, y, and ci and output wires: z and co, where the value of z is 1 if
the sum of x, y, and ci is odd, and the value of co is 1 if and only
if at least two of x, y, and ci are 1.

The order and names of the circuit input and output wires should be as
specified above, but the number and names of internal wires (wires
that are neither circuit inputs nor circuit outputs) are up to you.

Examples

ha_ckt.good_circuit() => True
ha_ckt.inputs =>['x', 'y']
ha_ckt.outputs => ['z', 'c0']

fa_ckt.good_circuit() => True
fa_ckt.inputs => ['x', 'y', 'ci']
fa_ckt.outputs => ['z', 'c0']

'''
ha_ckt = circuit([], [], [])
fa_ckt = circuit([], [], [])

'''
############################################################################
### Configurations

A configuration of a circuit is a dict giving a value (0 or 1) for
each wire in the circuit.  The dict key is the wire string and the dict
value is a binary digit, either 0 or 1.

Examples

Two configurations of the wires of the eq1_ckt Note that the order of
wires in the configuration is that returned by eq1_ckt.all-wires()

'''

eq1_config1 = {'x': 0, 'y': 1, 'z': 0, 'cx': 0, 'cy': 0, 't1': 0, 't2': 0}

eq1_config2 = {'x': 0, 'y': 0, 'z': 0, 'cx': 1, 'cy': 1, 't1': 0, 't2': 0}

# Two configurations of the wires of the sel-ckt

sel_config1 = {'x1': 0, 'x0': 1, 'y1': 1, 'y0': 0, 's': 1, 'z1': 0,
               'z0': 0, 'sc': 0, 'u1': 0, 'v1': 0, 'u0': 0, 'v0': 0}

sel_config2 = {'x1': 1, 'x0': 1, 'y1': 0, 'y0': 0, 's': 0, 'z1': 0,
               'z0': 0, 'sc': 1, 'u1': 0, 'v1': 0, 'u0': 0, 'v0': 0}

# Two configurations of the wires of the latch-ckt

latch_config1 = {'x': 0, 'y': 0, 'q': 0, 'u': 0}

latch_config2 = {'x': 0, 'y': 1, 'q': 1, 'u': 0}

'''############################################################################
## Problem XX (not graded.  I give you the code).

Write the circuit method next_value(wire, config) (modify the circuit
class definition above)

that returns the value on the given wire of the given circuit, *after
one gate delay* starting with the given configuration config of the
circuit.

You may assume that

 (1) circuit is a well-formed circuit, according to the specifications
 in problem 2,

 (2) the given wire is one of the wires of circuit, and

 (3) the given configuration config specifies a value for every wire
 in the circuit.

If the given wire is an input wire of the circuit, its next value is
just its value in the configuration config.

If the given wire is the output wire of a gate, its next value is
obtained by finding the gate of circuit for which it is the output
wire, looking up the values of the input wires of the gate in the
configuration config, and applying the appropriate function of the
gate to the input values.

Note that this doesn't compute the *eventual* value (if any) of the
wire, just the *next* value of the wire, after one gate delay.

Note that to look up the value of a wire in the current configutation,
you merely write config[wire] which retrieves the value from the
configuration dictionary.

; Examples

eq1_ckt.next_value('cx', eq1_config1) => 1
eq1_ckt.next_value('t2', eq1_config1) => 0
eq1_ckt.next_value('z', eq1_config2) => 0
sel_ckt.next_value('x0', sel_config1) => 1
sel_ckt.next_value('v1', sel_config1) => 1
sel_ckt.next_value('v0', sel_config2) => 0

############################################################################
## Problem 5 (10 points)

Write the circuit method next_config() (modify the circuit class
definition above) that takes a circuit and a current configuration
config and returns the "next" configuration of the circuit, after *one
gate delay* has elapsed.

In the "next" configuration of the circuit the value of each wire is
the result of applying the next-value procedure to the wire, circuit
and the configuration config.  Note that only the values of wires in
config are used for inputs, not the new values.

Thus, values on the input wires do not change, and each wire that is
the output of a gate has the value determined by its gate function
applied the values of its input wires in the configuration config.

This is a rather simplified model of the time-varying behavior of
wires and gates.

; Examples

eq1_ckt.next_config(eq1_config1) => {'x': 0, 'y': 1, 'z': 0, 'cx': 1, 'cy': 0, 't1': 0, 't2': 0}
eq1_ckt.next_config(eq1_config2) => {'x': 0, 'y': 0, 'z': 0, 'cx': 1, 'cy': 1, 't1': 0, 't2': 1}
sel_ckt.next_config(sel_config1) => {'x1': 0, 'x0': 1, 'y1': 1, 'y0': 0, 's': 1, 'z1': 0, 'z0': 0, 'sc': 0, 'u1': 0, 'v1': 1, 'u0': 0, 'v0': 0}


**********************************************************
## problem 6 ** (20 points)
Write four methods (modify the circuit class above)

stable(config)
all_stable_configs()
output_values(config)
init_config(input-values)

stable(config)
returns True if the next configuration of the circuit after the
configuration config is the same as config, ie, this configuration is
stable for the circuit.

all_stable_configs()
returns a list of all the stable configurations of the circuit.  The
wires in the configurations should be listed in the same order as
all_wires(), and the values in the configurations list should be in
increasing order, considered as binary numbers.

output_values(config)
returns a list giving the Boolean values of each of the output wires
of the circuit in the configuration config.  The order is the same as
the list of output wires of the circuit.

init_config(input-values)
takes a circuit and a list input-values of Boolean values
which has the same length as the number of inputs of the circuit
and returns a configuration in which the circuit input wires have the values 
specified (in order) by the list inputs, and all other wires have the value 0.

Examples

eq1_ckt.stable({"x": 0, "y": 0, "z": 1, "cx": 1, "cy": 1, 't1': 0, 't2': 1}) => True
eq1_ckt.stable({"x": 0, "y": 0, "z": 0, "cx": 1, "cy": 0, 't1': 0, 't2': 0}) => False

eq2_ckt.all_stable_configs() => [{'w': 0, 'x': 0, 'y': 0, 'z': 1}, {'w': 0, 'x': 1, 'y': 1, 'z': 1}, {'w': 1, 'x': 0, 'y': 1, 'z': 0}, {'w': 1, 'x': 1, 'y': 0, 'z': 0}]
seq_or_ckt.all_stable_configs() => [{'x': 0, 'z': 0}, {'x': 0, 'z': 1}, {'x': 1, 'z': 1}]

eq1_ckt.output_values(eq1_config1) => [0])
latch_ckt.output_values(latch_config2) => [1,0]

eq1_ckt.init_config([1,0]) => {'x': 1, 'y': 0, 'cx': 0, 'cy': 0, 't1': 0, 't2': 0, 'z': 0} 
clock_ckt.init_config([]) => {'z': 0}


############################################################################
## Problem 7 (15 points)

 Write a method simulate(self, config, n) (modify the circuit class above)

which simulates the given circuit from the given configuration by
repeatedly calling next-config until either the configuration reached
is stable, or next-config has been called n times, whichever occurs
first.

Examples

clock_ckt.simulate({"z": 0}, 4) => [{'z': 0}, {'z': 0}, {'z': 1}, {'z': 0}, {'z': 1}]
eq1_ckt.simulate(eq1_config1, 5) => [{'x': 0, 'y': 1, 'z': 0, 'cx': 0, 'cy': 0, 't1': 0, 't2': 0}, {'x': 0, 'y': 1, 'z': 0, 'cx': 0, 'cy': 0, 't1': 0, 't2': 0}]

sel_ckt.simulate(sel_config1, 5) => [{'x1': 0, 'x0': 1, 'y1': 1, 'y0': 0, 's': 1, 'z1': 0, 'z0': 0, 'sc': 0, 'u1': 0, 'v1': 0, 'u0': 0, 'v0': 0}, {'x1': 0, 'x0': 1, 'y1': 1, 'y0': 0, 's': 1, 'z1': 0, 'z0': 0, 'sc': 0, 'u1': 0, 'v1': 0, 'u0': 0, 'v0': 0}, {'x1': 0, 'x0': 1, 'y1': 1, 'y0': 0, 's': 1, 'z1': 0, 'z0': 0, 'sc': 0, 'u1': 0, 'v1': 1, 'u0': 0, 'v0': 0}]

ERROR.  See below.  latch_ckt.simulate(latch_config2, 3) => [{'x': 0, 'y': 1, 'q': 1, 'u': 0}]

latch_ckt.simulate(latch_config2, 3) => []
eq2_ckt.simulate(eq2_ckt.init_config([0,1]), 5) => [{'x': 0, 'y': 1, 'w': 0, 'z': 0}, {'x': 0, 'y': 1, 'w': 0, 'z': 0}, {'x': 0, 'y': 1, 'w': 1, 'z': 1}]


**********************************************************
** problem 8 ** (15 points)

Write a method final_config(self, config) (modify the circuit class
above)

that takes a circuit and a configuration config for the circuit.  If
the circuit would eventually reach a stable configuration from config,
then (final-config circuit config) returns the stable configuration of
the circuit that would be reached.

Otherwise, final_config(config) returns the string "none"

Examples

clock_ckt.final_config({'z': 0}) => 'none'

eq1_ckt.final_config({'x': 1, 'y': 1, 'z': 0, 'cx': 0, 'cy': 0, 't1': 0, 't2': 0}) => {'x': 1, 'y': 1, 'z': 1, 'cx': 0, 'cy': 0, 't1': 1, 't2': 0}

sel_ckt.final_config({'x1': 0, 'x0': 0, 'y1': 1, 'y0': 0, 's': 0, 'z1': 1, 'z0': 1, 'sc': 0, 'u1': 1, 'v1': 1, 'u0': 0, 'v0': 1}) =>
       {'x1': 0, 'x0': 0, 'y1': 1, 'y0': 0, 's': 0, 'z1': 0, 'z0': 0, 'sc': 1, 'u1': 0, 'v1': 0, 'u0': 0, 'v0': 0}

latch_ckt.final_config({'x': 1, 'y': 1, 'q': 0, 'u': 0}) => 'none'

latch_ckt.final_config({'x': 1, 'y': 1, 'q': 0, 'u': 1}) => {'x': 1, 'y': 1, 'q': 0, 'u': 1}

# ********************************************************

'''


### test function from google python course
### =======================================
# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if (hasattr(expected, '__call__')):
        OK = expected(got)
    else:
        OK = (got == expected)
    if OK:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('hours')
    print('# is it greater than 0?')
    test(hours(), lambda x: x > 0)

    print('gates')
    test(gate1.good_gate(), True)
    test(gate2.good_gate(), True)
    test(gate3.good_gate(), True)
    test(gate4.good_gate(), True)
    test(gate5.good_gate(), True)
    test(gate6.good_gate(), True)

    test(gate4 == gate5, True)
    test(gate5 == gate6, False)

    test(gateb1.good_gate(), False)
    test(gateb2.good_gate(), False)
    test(gateb3.good_gate(), False)
    test(gateb4.good_gate(), False)

    print('circuits')
    test(eq1_ckt.good_circuit(), True)
    test(nullckt.good_circuit(), True)
    test(badckt1.good_circuit(), False)
    test(badckt2.good_circuit(), False)

    print('all_wires')

    test(eq1_ckt.all_wires(), ['cx', 'cy', 't1', 't2', 'x', 'y', 'z'])
    test(sel_ckt.all_wires(), ['s', 'sc', 'u0', 'u1', 'v0', 'v1', 'x0', 'x1', 'y0', 'y1', 'z0', 'z1'])

    print('find_gate')
    test(eq1_ckt.find_gate('t2'), gate('and', ['cx', 'cy'], 't2'))
    test(eq2_ckt.find_gate('w'), gate('xor', ['x', 'y'], 'w'))
    test(sel_ckt.find_gate('y'), False)

    print('ha_ckt')
    test(ha_ckt.good_circuit(), True)
    test(ha_ckt.inputs, ['x', 'y'])
    test(ha_ckt.outputs, ['z', 'c0'])

    print('fa_ckt')
    test(fa_ckt.good_circuit(), True)
    test(fa_ckt.inputs, ['x', 'y', 'ci'])
    test(fa_ckt.outputs, ['z', 'c0'])

    print('next_value')
    test(eq1_ckt.next_value('cx', eq1_config1), 1)
    test(eq1_ckt.next_value('t2', eq1_config1), 0)
    test(eq1_ckt.next_value('z', eq1_config2), 0)
    test(sel_ckt.next_value('x0', sel_config1), 1)
    test(sel_ckt.next_value('v1', sel_config1), 1)
    test(sel_ckt.next_value('v0', sel_config2), 0)

    print('next_config')

    test(eq1_ckt.next_config(eq1_config1), {'x': 0, 'y': 1, 'z': 0, 'cx': 1, 'cy': 0, 't1': 0, 't2': 0})
    test(eq1_ckt.next_config(eq1_config2), {'x': 0, 'y': 0, 'z': 0, 'cx': 1, 'cy': 1, 't1': 0, 't2': 1})
    test(sel_ckt.next_config(sel_config1),
         {'x1': 0, 'x0': 1, 'y1': 1, 'y0': 0, 's': 1, 'z1': 0, 'z0': 0, 'sc': 0, 'u1': 0, 'v1': 1, 'u0': 0, 'v0': 0})
    test(sel_ckt.next_config(sel_ckt.next_config(sel_config1)),
         {'x1': 0, 'x0': 1, 'y1': 1, 'y0': 0, 's': 1, 'z1': 1, 'z0': 0, 'sc': 0, 'u1': 0, 'v1': 1, 'u0': 0, 'v0': 0})
    test(latch_ckt.next_config(latch_config1), {'x': 0, 'y': 0, 'q': 1, 'u': 1})
    test(latch_ckt.next_config(latch_config2), {'x': 0, 'y': 1, 'q': 1, 'u': 0})

    print('stable')

    test(eq1_ckt.stable({"x": 0, "y": 0, "z": 1, "cx": 1, "cy": 1, 't1': 0, 't2': 1}), True)
    test(eq1_ckt.stable({"x": 0, "y": 0, "z": 0, "cx": 1, "cy": 0, 't1': 0, 't2': 0}), False)

    print('all_stable_configs')

    test(eq2_ckt.all_stable_configs(),
         [{'w': 0, 'x': 0, 'y': 0, 'z': 1}, {'w': 0, 'x': 1, 'y': 1, 'z': 1}, {'w': 1, 'x': 0, 'y': 1, 'z': 0},
          {'w': 1, 'x': 1, 'y': 0, 'z': 0}])
    test(seq_or_ckt.all_stable_configs(), [{'x': 0, 'z': 0}, {'x': 0, 'z': 1}, {'x': 1, 'z': 1}])

    print('output_values')

    test(eq1_ckt.output_values(eq1_config1), [0])
    test(latch_ckt.output_values(latch_config2), [1, 0])

    print('init_config')

    test(eq1_ckt.init_config([1, 0]), {'x': 1, 'y': 0, 'cx': 0, 'cy': 0, 't1': 0, 't2': 0, 'z': 0})
    test(clock_ckt.init_config([]), {'z': 0})

    print('simulate')

    test(clock_ckt.simulate({"z": 0}, 4), [{'z': 0}, {'z': 1}, {'z': 0}, {'z': 1}])
    test(eq1_ckt.simulate(eq1_config1, 5), [{'x': 0, 'y': 1, 'z': 0, 'cx': 0, 'cy': 0, 't1': 0, 't2': 0}])

    test(sel_ckt.simulate(sel_config1, 5),
         [{'x1': 0, 'x0': 1, 'y1': 1, 'y0': 0, 's': 1, 'z1': 0, 'z0': 0, 'sc': 0, 'u1': 0, 'v1': 0, 'u0': 0, 'v0': 0},
          {'x1': 0, 'x0': 1, 'y1': 1, 'y0': 0, 's': 1, 'z1': 0, 'z0': 0, 'sc': 0, 'u1': 0, 'v1': 1, 'u0': 0, 'v0': 0}])
    test(latch_ckt.simulate(latch_config2, 3), [])

    test(eq2_ckt.simulate(eq2_ckt.init_config([0, 1]), 5),
         [{'x': 0, 'y': 1, 'w': 0, 'z': 0}, {'x': 0, 'y': 1, 'w': 1, 'z': 1}])

    print('final_config')

    test(clock_ckt.final_config({'z': 0}), 'none')

    test(eq1_ckt.final_config({'x': 1, 'y': 1, 'z': 0, 'cx': 0, 'cy': 0, 't1': 0, 't2': 0}),
         {'x': 1, 'y': 1, 'z': 1, 'cx': 0, 'cy': 0, 't1': 1, 't2': 0})
    test(sel_ckt.final_config(
        {'x1': 0, 'x0': 0, 'y1': 1, 'y0': 0, 's': 0, 'z1': 1, 'z0': 1, 'sc': 0, 'u1': 1, 'v1': 1, 'u0': 0, 'v0': 1}),
         {'x1': 0, 'x0': 0, 'y1': 1, 'y0': 0, 's': 0, 'z1': 0, 'z0': 0, 'sc': 1, 'u1': 0, 'v1': 0, 'u0': 0, 'v0': 0})

    test(latch_ckt.final_config({'x': 1, 'y': 1, 'q': 0, 'u': 0}), 'none')

    test(latch_ckt.final_config({'x': 1, 'y': 1, 'q': 0, 'u': 1}), {'x': 1, 'y': 1, 'q': 0, 'u': 1})


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
