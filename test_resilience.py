import json
import base64

def create_mock_state():
    # Create a minimal valid-looking state
    ram = bytearray(0x10000)
    nor = bytearray(0x8000 * 32)
    state = {
        "ram": base64.b64encode(ram).decode('ascii'),
        "nor": base64.b64encode(nor).decode('ascii'),
        "ramRomBank1": base64.b64encode(bytearray(0x2000)).decode('ascii'),
        "zp40cache": base64.b64encode(bytearray(0x40)).decode('ascii'),
        "clockRecords": base64.b64encode(bytearray(80)).decode('ascii'),
        "keypadmatrix": base64.b64encode(bytearray(8)).decode('ascii'),
        "cpu": {
            "reg_a": 0, "reg_x": 0, "reg_y": 0, "reg_pc": 0, "reg_sp": 0, "cycles": 0,
            "flag_c": 0, "flag_z": 0, "flag_i": 0, "flag_d": 0, "flag_b": 0, "flag_u": 0, "flag_v": 0, "flag_n": 0
        },
        "lcdbuffaddr": 0x0C00
    }
    return state

def verify_js_logic():
    with open('src/wqx.js', 'r') as f:
        content = f.read()

    # Check if loadState handles missing keypadmatrix gracefully (it uses if(state.keypadmatrix))
    if "if (state.keypadmatrix) this.keypadmatrix.set(base64ToUint8Array(state.keypadmatrix));" in content:
        print("PASSED: loadState checks for keypadmatrix existence")
    else:
        print("FAILED: loadState might crash if keypadmatrix is missing in old state")

    # Check if loadState restores realBank correctly (masked)
    if "var realBank = bank & 0x7F;" in content:
        print("PASSED: loadState masks high bank")
    else:
        print("FAILED: loadState might use unmasked bank index")

verify_js_logic()
