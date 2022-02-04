class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_count = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            sub_domain = domain.split('.')
            for i in range(len(sub_domain)):
                curr = '.'.join(sub_domain[i:])
                domain_count[curr] = domain_count.get(curr, 0) + int(count)
        return [str(v) + ' ' + k for k, v in domain_count.items()]


    # def subdomainVisits(self, cpdomains):
    #     # https://leetcode.com/problems/subdomain-visit-count/discuss/121770/Python-short-and-understandable-solution-68-ms
    #     counter = collections.Counter()
    #     for cpdomain in cpdomains:
    #         count, *domains = cpdomain.replace(" ",".").split(".")
    #         for i in range(len(domains)):
    #             counter[".".join(domains[i:])] += int(count)
    #     return [" ".join((str(v), k)) for k, v in counter.items()]
