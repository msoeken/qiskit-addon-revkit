venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	test -d lib || mkdir -p lib
	test -d lib/qiskit-aqua || git clone https://github.com/Qiskit/qiskit-aqua lib/qiskit-aqua
	venv/bin/pip install cython pybind11
	venv/bin/pip install git+https://github.com/msoeken/revkit@develop
	venv/bin/pip install git+https://github.com/Qiskit/qiskit-terra
	venv/bin/pip install -e lib/qiskit-aqua
	venv/bin/pip install -r requirements.txt
	touch venv/bin/activate

devbuild: venv
	venv/bin/python setup.py install
