import sys

def check_file_content(filepath, patterns):
    with open(filepath, 'r') as f:
        content = f.read()
    for pattern in patterns:
        if pattern not in content:
            print(f"FAILED: Pattern '{pattern}' not found in {filepath}")
            return False
    print(f"PASSED: All patterns found in {filepath}")
    return True

patterns_index = [
    "function run() {",
    "wqx.startFrame();",
    "_origUpdateLCD(addr, value);",
    "drawIndicator(row - 64, active);",
    "name: 'PgUp'",
    "name: 'PgDn'"
]

patterns_wqx = [
    "clockRecords: uint8ArrayToBase64(this.clockRecords),",
    "keypadmatrix: uint8ArrayToBase64(this.keypadmatrix),",
    "if (state.clockRecords) this.clockRecords.set(base64ToUint8Array(state.clockRecords));",
    "vol === 1",
    "vol === 3",
    "return this.read05StartTimer0();"
]

patterns_keyinput = [
    "'A': 0x28,"
]

success = True
success &= check_file_content('index.html', patterns_index)
success &= check_file_content('src/wqx.js', patterns_wqx)
success &= check_file_content('src/keyinput.js', patterns_keyinput)

if not success:
    sys.exit(1)
