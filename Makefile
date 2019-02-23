venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	test -d lib || mkdir -p lib
	test -d lib/qiskit-aqua || git clone https://github.com/Qiskit/qiskit-aqua lib/qiskit-aqua
	git -C lib/qiskit-aqua checkout aaa2d55b5f570ad40934bedc6d2d4a5bbbefa446
	venv/bin/pip install cython pybind11
	venv/bin/pip install git+https://github.com/msoeken/revkit
	venv/bin/pip install git+https://github.com/Qiskit/qiskit-terra@ab72d9e8f10ba0f4d6a6a49dae9fe782607811b7
	venv/bin/pip install -e lib/qiskit-aqua
	venv/bin/pip install -r requirements.txt
	touch venv/bin/activate

devbuild: venv
	venv/bin/python setup.py install
