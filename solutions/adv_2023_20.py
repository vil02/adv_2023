"""solution of adv_2023_20"""
import collections
import math

Pulse = collections.namedtuple("Pulse", ["source", "target", "type"])

_LOW = "-"
_HIGH = "+"


class FlipFlop:
    """represents a FlipFlop module"""

    _off = "off"
    _on = "on"

    def __init__(self, in_name, in_targets):
        self.name = in_name
        self.targets = in_targets
        self._state = ""
        self.reset()

    def reset(self):
        """sets the module to off"""
        self._state = FlipFlop._off

    def _flip(self, circuit):
        new_pulse_type = {FlipFlop._off: _HIGH, FlipFlop._on: _LOW}[self._state]
        self._state = {_HIGH: FlipFlop._on, _LOW: FlipFlop._off}[new_pulse_type]
        for _ in self.targets:
            circuit.add_pulse(Pulse(self.name, _, new_pulse_type))

    def receive(self, circuit, in_pulse):
        """simulates receiving a pulse"""
        if in_pulse.type == _HIGH:
            return
        assert in_pulse.type == _LOW
        self._flip(circuit)


class Conjunction:
    """repsesents a Conjunction module"""

    def __init__(self, in_name, in_targets):
        self.name = in_name
        self.targets = in_targets
        self._last = {}

    def add_source(self, in_source):
        """adds a source"""
        self._last[in_source] = _LOW

    def reset(self):
        """resets the Conjunction"""
        for _ in self._last:
            self._last[_] = _LOW

    def _send(self, circuit, in_pulse_type):
        for _ in self.targets:
            circuit.add_pulse(Pulse(self.name, _, in_pulse_type))

    def receive(self, circuit, in_pulse):
        """simulates receiving a pulse"""
        self._last[in_pulse.source] = in_pulse.type
        new_pulse_type = _LOW if all(_ == _HIGH for _ in self._last.values()) else _HIGH
        self._send(circuit, new_pulse_type)


class Broadcaster:
    """represents a Broadcaster module"""

    def __init__(self, in_name, in_targets):
        self.name = in_name
        self.targets = in_targets

    def reset(self):
        """resets the Broadcaster"""

    def receive(self, circuit, in_pulse):
        """simulates receiving a pulse"""
        for _ in self.targets:
            circuit.add_pulse(Pulse(self.name, _, in_pulse.type))


class Circuit:
    """represents a circuit of modules"""

    _initial_pulse = Pulse("button", "broadcaster", _LOW)

    def __init__(self, in_modules):
        self._modules = in_modules
        self.reset()

    @property
    def modules(self):
        """getter of _modules"""
        return self._modules

    def reset(self):
        """resets the state of circuit and all of its modules"""
        self._pulses = []
        self.counts = {_LOW: 0, _HIGH: 0}
        for _ in self.modules.values():
            _.reset()

    def add_pulse(self, in_pulse):
        """adds a pulse to the list of active pulses"""
        self._pulses.append(in_pulse)

    def push_button(self):
        """simulates a single push button"""
        self.add_pulse(Circuit._initial_pulse)
        while self._pulses:
            cur_pulse = self._pulses.pop(0)
            self.counts[cur_pulse.type] += 1
            if cur_pulse.target in self.modules:
                self.modules[cur_pulse.target].receive(self, cur_pulse)

    def find_pulse(self, in_pulse):
        """returns the number of button pushes needed to generate a given pulse"""
        count = 1
        cur_pulse = Circuit._initial_pulse
        while cur_pulse != in_pulse:
            if cur_pulse.target in self.modules:
                self.modules[cur_pulse.target].receive(self, cur_pulse)
            if not self._pulses:
                self.add_pulse(Circuit._initial_pulse)
                count += 1
            cur_pulse = self._pulses.pop(0)
        return count


def _parse_single_line(in_str: str):
    source, targets_str = in_str.split(" -> ")
    module_type = source[0]
    module_name = source[1:]
    targets = targets_str.split(", ")
    if module_type == "%":
        return module_name, FlipFlop(module_name, targets)
    if module_type == "&":
        return module_name, Conjunction(module_name, targets)
    assert source == "broadcaster"
    return source, Broadcaster(source, targets)


def _names_of_conjunctions(in_modules):
    return {
        name for name, module in in_modules.items() if isinstance(module, Conjunction)
    }


def _add_sources_to_conjunctions(modules):
    conjunctions = _names_of_conjunctions(modules)
    for name, module in modules.items():
        for target in module.targets:
            if target in conjunctions:
                modules[target].add_source(name)


def _parse_input(in_str: str):
    modules = dict(_parse_single_line(_) for _ in in_str.splitlines())
    _add_sources_to_conjunctions(modules)
    return Circuit(modules)


def solve_a(in_str: str):
    """returns the solution for part_a"""
    circuit = _parse_input(in_str)
    for _ in range(1000):
        circuit.push_button()
    return circuit.counts[_LOW] * circuit.counts[_HIGH]


def _find_sources(in_modules, in_target):
    return [name for name, module in in_modules.items() if in_target in module.targets]


def _find_leading_to_rx(in_modules):
    res = _find_sources(in_modules, "rx")
    assert len(res) == 1
    res = res[0]
    assert isinstance(in_modules[res], Conjunction)
    return res


def solve_b(in_str: str):
    """returns the solution for part_b"""
    circuit = _parse_input(in_str)
    leading_to_rx = _find_leading_to_rx(circuit.modules)
    nums = []
    for source in _find_sources(circuit.modules, leading_to_rx):
        circuit.reset()
        nums.append(circuit.find_pulse(Pulse(source, leading_to_rx, _HIGH)))
    return math.lcm(*nums)
