class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            elements = email.split('@')
            email_set.add(elements[0].split('+')[0].replace('.', '') + elements[1])
        return len(email_set)
