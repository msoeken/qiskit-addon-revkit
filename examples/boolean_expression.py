from qiskit import BasicAer
from qiskit.aqua.algorithms import Grover
from qiskit_addon_revkit.aqua import BooleanExpression

backend = BasicAer.get_backend('qasm_simulator')
oracle = BooleanExpression("[[abc]<abc>]")
algorithm = Grover(oracle)
result = algorithm.run(backend)
print(result['result'])
