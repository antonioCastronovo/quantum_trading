import json
from qiskit import QuantumCircuit
from qiskit.qobj import qobj_to_dict

class QuantumSerializer:
    def serialize_circuit(self, circuit: QuantumCircuit):
        """Serializza circuito quantistico in formato JSON quantistico"""
        qobj = circuit.qobj()
        return json.dumps(qobj_to_dict(qobj), 
            cls=QuantumJSONEncoder)
    
    def deserialize_circuit(self, data):
        """Deserializza da JSON a circuito quantistico"""
        qobj_dict = json.loads(data, cls=QuantumJSONDecoder)
        return QuantumCircuit.from_qobj(qobj_dict)

class QuantumJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {'__complex__': True, 'real': obj.real, 'imag': obj.imag}
        return super().default(obj)

class QuantumJSONDecoder(json.JSONDecoder):
    def decode(self, s):
        return super().decode(s, object_hook=self.quantum_object_hook)
    
    def quantum_object_hook(self, dct):
        if '__complex__' in dct:
            return complex(dct['real'], dct['imag'])
        return dct