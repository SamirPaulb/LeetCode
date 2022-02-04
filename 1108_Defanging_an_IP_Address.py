class Solution:
    def defangIPaddr(self, address: str) -> str:
        # replace
        return address.replace('.', '[.]')
    # def defangIPaddr(self, address: str) -> str:
    #     # split and join
    #     return '[.]'.join(address.split('.'))
    # def defangIPaddr(self, address: str) -> str:
    #     # replace
    #     return re.sub('\.', '[.]', address)
    # def defangIPaddr(self, address: str) -> str:
    #     return ''.join('[.]' if c == '.' else c for c in address)
