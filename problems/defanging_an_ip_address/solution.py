class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = str(address)
        address = address.replace(".","[.]")
        return address


        