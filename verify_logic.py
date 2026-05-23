
import re

def check_file_content():
    with open('src/wqx.js', 'r') as f:
        content = f.read()

    # Check banking fix
    banking_fix = 'var realBank = bank & 0x7F;'
    if banking_fix in content:
        print("✅ Banking fix (bank & 0x7F) found.")
    else:
        print("❌ Banking fix NOT found.")

    # Check LCD buffer update
    lcd_fix = 'this.setLcdStartAddr(((this.ram[io0C_lcd_config] & 0x03) << 12) | (value << 4));'
    if lcd_fix in content:
        print("✅ Dynamic LCD buffer update in write06LCDStartAddr found.")
    else:
        print("❌ Dynamic LCD buffer update NOT found.")

    # Check sleep mode skip
    sleep_skip = 'if (!this.slept) {\n                this.cpu.execute();\n            } else {'
    if sleep_skip in content:
        print("✅ Sleep mode cycle skipping logic found.")
    else:
        print("❌ Sleep mode cycle skipping logic NOT found.")

    # Check reset fix
    reset_fix = 'this.ram.fill(0);\n        this.initIo();\n        this.initMemmap();'
    if reset_fix in content:
        print("✅ Comprehensive reset found.")
    else:
        print("❌ Comprehensive reset NOT found.")

    with open('index.html', 'r') as f:
        html = f.read()

    if 'NC1020 Emulator v3.0' in html:
        print("✅ Version v3.0 found in index.html.")
    else:
        print("❌ Version v3.0 NOT found.")

    if 'PgUp' in html and 'PgDn' in html:
        print("✅ PgUp/PgDn buttons found in index.html.")
    else:
        print("❌ PgUp/PgDn buttons NOT found.")

if __name__ == "__main__":
    check_file_content()
