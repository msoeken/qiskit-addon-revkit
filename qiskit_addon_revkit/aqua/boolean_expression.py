from qiskit import QuantumCircuit, QuantumRegister
from qiskit.aqua.components.oracles import Oracle
from revkit import oracle_synth, truth_table
import revkit.export.qiskit

class BooleanExpression(Oracle):
  """
  Oracle for Boolean expressions
  """

  CONFIGURATION = {
    'name': 'BooleanExpression',
    'description': 'Boolean expression oracle',
    'input_schema': {
      '$schema': 'http://json-schema.org/schema#',
      'id': 'boolean_expression_oracle_schema',
      'type': 'object',
      'properties': {
        'expr': {
          'type': 'string'
        },
        'strategy': {
          'type': 'integer',
          'default': 1
        }
      },
      'additionalProperties': False
    }
  }

  def __init__(self, expr, strategy=1):
    self.validate(locals())

    # Create truth table from expression
    self.tt = truth_table.from_expression(expr)

    # Perform synthesis
    netlist = oracle_synth(self.tt)
    self.var_regs = QuantumRegister(self.tt.num_vars, "qv")
    self.out_regs = QuantumRegister(1, "qo")
    self.circuit = QuantumCircuit(self.var_regs, self.out_regs)
    self.circuit = netlist.to_qiskit(circuit=self.circuit)

  @property
  def variable_register(self):
    return self.var_regs

  @property
  def ancillary_register(self):
    return None

  @property
  def outcome_register(self):
    return self.out_regs

  def construct_circuit(self):
    return self.circuit

  def evaluate_classically(self, assignment):
    return sum(2**i if a else 0 for i, a in enumerate(assignment))

  def interpret_measurement(self, top_measurement=None):
    return [bool(int(tf)) for tf in top_measurement[::-1]]
