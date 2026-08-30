class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            res_x = find(x)
            res_y = find(y)

            if res_x != res_y:
                parent[res_y] = res_x
        
        #Init and union
        for account in accounts:
            name = account[0]
            first_email = account[1]

            if first_email not in parent:
                parent[first_email] = first_email
            email_to_name[first_email] = name

            for email in account[2:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name

                union(first_email, email)
        
        #create result
        groups = defaultdict(list)
        for email in parent:
            real_boss = find(email)
            groups[real_boss].append(email)

        merged = []
        for boss,emails in groups.items():
            name = email_to_name[boss]
            merged.append([name] + sorted(emails))
        
        return merged
