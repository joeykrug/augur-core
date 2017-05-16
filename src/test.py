from ethereum import tester

state = tester.state()
contract = state.abi_contract("""
data cherry[]

def main():
    self.cherry[0] = 1
    self.cherry[1] = 3
    self.cherry[2] = 5
    self.cherry = array(3)
    return(cherry[1])
""")

print(contract.main())
